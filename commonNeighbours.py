import sys
import operator
import math
import networkx as nx
import numpy as np






idmatrix={}
f = open('9606.protein.100.fold5.txt', 'r')
index=0
for line in f:
	sample = line.split()
	if sample[0] not in idmatrix:
		idmatrix[sample[0]]=index
		index+=1

fw =  open('sample.fold5.data', 'w') 

fl = open('9606.protein.100.fold5.txt', 'r')
f = open('9606.protein.100.fold5.txt', 'r')
x=[]
y=[]
p=0
neighbours={}
number_of_connections={}
target=[]
samples=[]
sample=[]
second_level_neighbours={}
#isim key olanin weight toplami kac
sum_of_weights={}
weights = {}
#isim key olanin weight ortalamasi kac
mean_of_weights={}
i = 0
for line in f:
	sample = line.split()
	if sample[0] in number_of_connections:
		number_of_connections[sample[0]]=number_of_connections[sample[0]]+1
	else:
		number_of_connections[sample[0]]=1
	
	if sample[0] in neighbours:
		neighbours[sample[0]].append(sample[1])
	else:
		neighbours[sample[0]]=[]
		neighbours[sample[0]].append(sample[1])

	if sample[0] in sum_of_weights:
		sum_of_weights[sample[0]]+=float(sample[2])
	else:
		sum_of_weights[sample[0]]=float(sample[2])
	weights[sample[0] + ' ' + sample[1]] = int(sample[2])
	
	i = i+1
		
for key in sum_of_weights:
	mean_of_weights[key]=float(sum_of_weights[key]/number_of_connections[key])
f.close()
p=0		
for line in fl:
	ornek = line.split()
	print p
	sample=[]
	#target value
	sample.append(int(ornek[2]))
	#feature 1 ve feature 2
	#ortak komsu sayilari
	#ortak komsu sayilari / ikisinin toplam komsulari
	ortakKomsu = 0
	komsularinToplamAgirliklari = 0
	ilkProteinOrtakKomsularinToplamAgirliklari = 0
	ikinciProteinOrtakKomsularinToplamAgirliklari = 0
	for val in neighbours[ornek[0]]:
		if val in neighbours[ornek[1]]:
			ortakKomsu+=1
			ilkProteinOrtakKomsularinToplamAgirliklari += weights[ornek[0] + ' ' + val]
			ikinciProteinOrtakKomsularinToplamAgirliklari += weights[ornek[1] + ' ' + val]
	sample.append(ortakKomsu)
	sample.append(float(ortakKomsu)/(number_of_connections[ornek[0]]+number_of_connections[ornek[1]] - ortakKomsu))
	#feature 3 ilkinin komsu sayisi
	sample.append(number_of_connections[ornek[0]])
	#feature 4 ikincisinin komsu sayisi
	sample.append(number_of_connections[ornek[1]])
	#feature 5  komsularimin  ortak komsulari toplami / komsu sayilarimizin carpimi
	ucuncuSeviyeKomsu = {}
	third_level_neighbours = {}
	ikinciSeviyeKomsu = {}
	for val in neighbours[ornek[0]]:
		if val not in neighbours[ornek[1]]:
			for val1 in neighbours[val]:
				third_level_neighbours[val1]=1
	for val in neighbours[ornek[1]]:
		if val not in neighbours[ornek[0]]:
			for val1 in neighbours[val]:
				if val1 in third_level_neighbours:
					ucuncuSeviyeKomsu[val1] = 1
	sample.append(float(len(ucuncuSeviyeKomsu))/(number_of_connections[ornek[0]]*number_of_connections[ornek[1]]))			
	
	#feature 6 : 1. proteinin agirlik ortalamasi	
	sample.append(mean_of_weights[ornek[0]])
	#feature 7: 2. proteinin agirlik ortalamasi
	sample.append(mean_of_weights[ornek[1]])
	#feature 8: 2 proteinin toplam agirliklari ortalamasi
	sample.append((sum_of_weights[ornek[0]] + sum_of_weights[ornek[1]])/(number_of_connections[ornek[0]] + number_of_connections[ornek[1]]))
	samples.append(sample)
	#feature 9
	sample.append((sum_of_weights[ornek[0]]/number_of_connections[ornek[0]])/(sum_of_weights[ornek[1]]/number_of_connections[ornek[1]]))

	p+=1
	for i in range(len(sample)-1):
		fw.write(str(sample[i])+',')
	fw.write(str(sample[len(sample)-1])+'\n')
