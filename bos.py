import pylab as pl
import numpy as np
import matplotlib.pyplot as plt
import sys
import operator
import math
import copy
from sklearn import tree
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.learning_curve import learning_curve
from sklearn import cross_validation
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import KFold

with open('sample.data', 'r') as f:
    data = [i.split(",") for i in f.read().split()]
target=[]
samples=[]
for row in data:
    target.append(float(row[0]))
    sample=[]
    for i in range(1,len(row)):
        sample.append(float(row[i]))
    samples.append(sample)



def graph(model, X, y, cv=None, train_sizes=np.linspace(.1, 1.0, 10)):
    plt.figure()   
    train_sizes, train_scores, test_scores = learning_curve(model, X, y, cv=cv, train_sizes=train_sizes)
    train_error_mean = 1-np.mean(train_scores, axis=1)
    test_error_mean = 1-np.mean(test_scores, axis=1)
    plt.grid()
    plt.plot(train_sizes, train_error_mean, 'o-', color="b",label="Training Error")
    plt.plot(train_sizes, test_error_mean, 'o-', color="r",label="Cross-validation Error")
    return plt

print samples[0]
print target[0]
#istenilen model icin gerekli yorum satiri acilarak kod kullanilabilir. 

#logistic Regression with no bagging
#model = LogisticRegression()

#logistic Regression with bagging
model = BaggingClassifier(LogisticRegression())

#Decision Tree classifier with no bagging 
#model = tree.DecisionTreeClassifier(criterion='gini') 

#Decision Tree classifier with bagging 
#model = BaggingClassifier(tree.DecisionTreeClassifier(criterion='gini'))

#Decision Tree classifier with random forest max features is the square root of 36
#model = RandomForestClassifier(n_estimators=10,max_features=6)


mean_r=[]
std_r=[]
targetstd_deviation=0.0
targetmean=0.0
def std_deviationtarget(X):
	global targetstd_deviation
	X_norm = copy.deepcopy(X)
	tempsum=float(0)
	for columnIndex in range(len(X)):
		tempsum=tempsum + (X[columnIndex]-targetmean)**2
	targetstd_deviation=(tempsum / len(X_norm)) ** 0.5
	print "TARGET STD DEVIATION "  , targetstd_deviation


def feature_normalizetarget(X):
	X_norm = copy.deepcopy(X)
	
	for columnIndex in range(len(X)):
		X[columnIndex]=(X[columnIndex]-targetmean)/targetstd_deviation
	return X_norm



def std_deviation(X,ind):
	X_norm = copy.deepcopy(X)
	tempsum=float(0)
	for columnIndex in range(0,ind):
		for sample in X_norm:
			tempsum=tempsum + (sample[columnIndex]-mean_r[columnIndex])**2
		std_r.append((tempsum / len(X_norm)) ** 0.5)


def feature_normalize(X,ind):
	X_norm = copy.deepcopy(X)
	tempsum=0
	for columnIndex in range(0,ind):	

		for sample in X_norm:
			tempsum=tempsum+sample[columnIndex]
		mean_r.append(tempsum/len(X_norm))
		tempsum=0
	std_deviation(X,ind)
	for columnIndex in range(0,ind):

		for sample in X_norm:
			if std_r[columnIndex]>0:
				sample[columnIndex]=(sample[columnIndex]-mean_r[columnIndex])/std_r[columnIndex]
			else:
				sample[columnIndex]=(sample[columnIndex]-mean_r[columnIndex])
			
	return X_norm

print "anan"
print samples[3]
samples = feature_normalize(samples,7)
toplam = 0
for i in range(len(target)):
	toplam+= target[i]
targetmean=toplam/len(target)
std_deviationtarget(target)
target = feature_normalizetarget(target)

print samples[0]
print target[0]

X = np.array(samples).astype('float')
Y = np.array(target)
graph(model, X, Y, cv=cross_validation.KFold(n=200, n_folds=10, shuffle=False,random_state=None))
plt.show()    

