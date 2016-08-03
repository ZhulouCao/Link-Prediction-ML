import sys
import operator
import math
import random

neighbours={}
topmatrix={}
weights = {}

f = open('9606.protein.links.v10.txt', 'r')

i = 0
for line in f:
	sample = line.split(' ')
	if sample[0] not in topmatrix:
		topmatrix[sample[0]]=1
	else:
		topmatrix[sample[0]]+=1
	
	if sample[0] in neighbours:
		neighbours[line.split()[0]].append(sample[1])
	else:
		neighbours[sample[0]]=[]
		neighbours[sample[0]].append(sample[1])
	
	weights[sample[0] + ' ' + sample[1]] = int(sample[2])
	if i%10000 == 0:
		print i
	i += 1

idmatrix={}
print 'Siralaniyor'
sortedList = sorted(topmatrix.items(),key=operator.itemgetter(1),reverse=True)
print 'siralandi'
#en yuksek sayida komsulugu olan 200 node
newList=[]
counter=0
for i in range(0,200):
	newList.append(sortedList[i][0])

print newList

file = open('9606.protein.200.txt','w')
for protein1 in newList:
	for protein2 in newList:
		if protein1 + ' ' + protein2 in weights:
			file.write(protein1 + ' ' + protein2 + ' ' + str(weights[protein1 + ' ' + protein2]) + '\n')
file.close()		
																																																																																																																																																																																																																																																																																																																																																																																																																																																									
