import pylab as pl
import numpy as np
import matplotlib.pyplot as plt
import sys
import operator
f = open('9606.protein.links.v10.txt', 'r')
#ismi key olanin kac baglantisi var
number_of_connections={}

#isim keyi icin id valuesi var
name_of_nodes={}

#isim key olanin weight toplami kac
sum_of_weights={}

#isim key olanin weight ortalamasi kac
mean_of_weights={}
cnt=0
next(f)
for line in f:
	
	if line.split()[0] in number_of_connections:
		number_of_connections[line.split()[0]]=number_of_connections[line.split()[0]]+1
	else:
		number_of_connections[line.split()[0]]=1
	
	if line.split()[0] in sum_of_weights:
		sum_of_weights[line.split()[0]]+=float(line.split()[2])
	else:
		sum_of_weights[line.split()[0]]=float(line.split()[2])
	cnt+=1
		
for key in sum_of_weights:
	mean_of_weights[key]=float(sum_of_weights[key]/number_of_connections[key])

#for key in mean_of_weights:
 #  print "key: %s , value: %s" % (key, mean_of_weights[key])

sortedList = sorted(mean_of_weights.items(),key=operator.itemgetter(1),reverse=True)
sortedList2 = sorted(number_of_connections.items(),key=operator.itemgetter(1),reverse=True)
for i in range(50):
	print sortedList[i][0] , "  " , mean_of_weights[sortedList[i][0]] ,  "       " , number_of_connections[sortedList[i][0]]

for i in range(50):
	print sortedList2[i][0] , "  " , number_of_connections[sortedList2[i][0]] 
'''
sortedList = sorted(number_of_connections.items(),key=operator.itemgetter(1),reverse=True)

for i in range(50):
	print sortedList[i][0] , "  " , number_of_connections[sortedList[i][0]]


print len(number_of_connections)
'''
x=[]
y=[]
for key in sum_of_weights:
	y.append(mean_of_weights[key])
	x.append(number_of_connections[key])
npx=np.array(x)
npy=np.array(y)
plt.grid()
plt.plot(npx,npy,'ro')
plt.show() 

	
