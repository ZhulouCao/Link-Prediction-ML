import sys
import operator
import math
import random as r

f = open('9606.protein.200.txt', 'r')

neighbours={}

sample=[]
weights = {}
i = 0
for line in f:
	sample = line.split()
	
	if sample[0] in neighbours:
		neighbours[sample[0]].append(sample[1])
	else:
		neighbours[sample[0]]=[]
		neighbours[sample[0]].append(sample[1])
		
	weights[sample[0] + ' ' + sample[1]] = int(sample[2])
	
	i = i+1
f.close()

number_of_test = int(i * 0.1)
number_of_training = i - number_of_test * 2
print len(weights)
neighbours_test = {}
for i in range(0, number_of_test):
	rnd = r.randint(0, len(neighbours) - 1)
	protein1 = neighbours.keys()[rnd]
	rnd = r.randint(0, len(neighbours[protein1]) - 1)
	protein2 = neighbours[protein1][rnd]
	
	neighbours[protein1].remove(protein2)
	neighbours[protein2].remove(protein1)
	
	if protein1 in neighbours_test:
		neighbours_test[protein1].append(protein2)
	else:
		neighbours_test[protein1] = []
		neighbours_test[protein1].append(protein2)
	if protein2 in neighbours_test:
		neighbours_test[protein2].append(protein1)
	else:
		neighbours_test[protein2] = []
		neighbours_test[protein2].append(protein1)

file = open('samples\\200protein_fold5\\training_data.txt','w')
for protein1 in neighbours:
	for protein2 in neighbours[protein1]:
		file.write(protein1 + ' ' + protein2 + ' ' + str(weights[protein1 + ' ' + protein2]) + '\n')
file.close()

file = open('samples\\200protein_fold5\\test_data.txt','w')
for protein1 in neighbours_test:
	for protein2 in neighbours_test[protein1]:
		file.write(protein1 + ' ' + protein2 + ' ' + str(weights[protein1 + ' ' + protein2]) + '\n')
file.close()
