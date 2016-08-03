import pylab as pl
import numpy as np
import matplotlib.pyplot as plt
import sys
import operator
import math
import random



f = open('9606.protein.50.txt', 'r')


fw =  open('adjacency50.txt', 'w') 
fww =  open('target50.txt', 'w') 

idmatrix={}
counter=0

cnt=0
for line in f:
	if line.split()[0] not in idmatrix:
		idmatrix[line.split()[0]]=counter
		counter+=1
	if line.split()[1] not in idmatrix:
		idmatrix[line.split()[1]]=counter
		counter+=1
	cnt+=1
print counter

f = open('9606.protein.50.txt', 'r')
cnt=0
print "len",len(idmatrix)
for line in f:

	if cnt%1000==0:
		print cnt
	sample=[0]*len(idmatrix)
	sample[idmatrix[line.split()[0]]]=1
	sample[idmatrix[line.split()[1]]]=1
	for i in range(len(sample)-1):
		fw.write(str(sample[i])+',')
	fw.write(str(sample[len(sample)-1])+'\n')
	fww.write(line.split()[2]+'\n')
	cnt+=1




