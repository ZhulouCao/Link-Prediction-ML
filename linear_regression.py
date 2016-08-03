import math

#x: ornekler. Iki boyutlu matris alir 
#y: orneklerin aldigi degerler. Integer dizisidir.
#alpha: Ogrenme orani
#converged_error: Ogrenmeyi tamamlamak icin gerekli maksimum hata
#cost_function: Hatayi hesaplamak icin kullandigi cost fonksiyonu. 0: mse, 1(diger durumlar): mae
#iteration: converged_error degerini saglamazsa maksimum iterasyon sayisi
def batch_gradient_descent(x, y, alpha = 0.000009, converged_error = 0.01, iteration = 1000):
	number_of_katsayi = len(x[0]) + 1
	number_of_samples = len(y)
	print str(number_of_samples)
	
	katsayilar = []
	yeniKatsayilar = []
	tahmini_y = []

	for i in range(0,number_of_katsayi):
		katsayilar.append(0)
		yeniKatsayilar.append(0)
	
	for i in range(0, number_of_samples):
		tahmini_y.append(0)
	
	last_error = mse(katsayilar, x, y)
			
	for i in range(0,iteration):
		print 'i: ' + str(i)
		
		for sample in range(0, number_of_samples):
			tahmini_y[sample] = fonksiyon(katsayilar, x[sample])
		
		j = sum((y[sample] - tahmini_y[sample]) for sample in range(0, number_of_samples))
		yeniKatsayilar[0] = katsayilar[0] + alpha * j
		
		for feature in range(1, number_of_katsayi):
			j = sum((y[sample] - tahmini_y[sample]) * x[sample][feature - 1] for sample in range(0, number_of_samples))
			yeniKatsayilar[feature] = katsayilar[feature] + alpha * j
			
		for index in range(0,number_of_katsayi):
			katsayilar[index] = yeniKatsayilar[index]
		
		error = mse(katsayilar, x, y)
			
		if abs(last_error - error) < converged_error:
			print abs(last_error - error)
			print 'Converged: ' + str(i)
			break
		
		print abs(last_error - error)
		last_error = error
		
	return katsayilar

#Verilen katsayi ve sample'a gore f=b0 + b1x1 + b2x2 + ... + bnxn seklindeki fonksiyonu sonucunu dondurur.	
def fonksiyon(katsayi,sample):
	number_of_katsayi = len(katsayi)
	result = katsayi[0] + sum(katsayi[i] * sample[i-1] for i in range(1, number_of_katsayi))
	return result

#Verilen katsayi ve orneklere gore mean squared error degerini dondurur.	
def mse(katsayi, samples, y):
	number_of_samples = len(y)
	mse = sum(math.pow((y[i] - fonksiyon(katsayi, samples[i])), 2) for i in range(0, number_of_samples))
	mse = mse / number_of_samples
	return math.sqrt(mse)
	
url = 'samples\\200protein_fold2\\'
data_file = open(url + "training.data.txt", "r")
next(data_file)
test_data = []
training_data = []
test_y = []
training_y = []

print 'Training Data Aliniyor...'
for i in data_file:
	sample = []
	i = i.replace('\n','')
	sample_str = i.split(',')
	training_y.append(int(sample_str[0]))
	for j in range(1,len(sample_str)):
		sample.append(float(sample_str[j]))
	training_data.append(sample)
data_file.close()
print len(training_data)

data_file = open(url + "test.data.txt", "r")
next(data_file)
print 'Test Data Aliniyor...'
for i in data_file:
	sample = []
	i = i.replace('\n','')
	sample_str = i.split(',')
	test_y.append(int(sample_str[0]))
	for j in range(1,len(sample_str)):
		sample.append(float(sample_str[j]))
	test_data.append(sample)
data_file.close()
print len(test_data)

alpha = 0.000000000001
converged_error = 0.00001

katsayilar = batch_gradient_descent(training_data, training_y, alpha, converged_error, 5000)
mean_error = mse(katsayilar, test_data, test_y)

print 'Root Mean Square Error: ' + str(mean_error)
print ''

print '\a'