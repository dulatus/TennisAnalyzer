#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import urllib
from glob import glob
import random
import csv
import operator
from sklearn.cross_validation import train_test_split
from sklearn import preprocessing
selected_features = [2,7,11,12,14,15,16,17,18,24,25,28,29,30,32,33,34,35,36]
def reorderColumn(input_name):
	# example
	try:
		input_file_handle = open(input_name,'rb')
		output_file_handle = open(input_name[:19]+"_reordered"+input_name[-4:],'wb')
		reader = csv.reader(input_file_handle,delimiter = ',')
		writer = csv.writer(output_file_handle,delimiter = ',')
		# don't forget to open both files in binary mode (2.x)
		# or with `newline=''` (3.x)
		readnames = reader.next()
		selected_features = [2,7,11,12,14,15,16,17,18,24,25,28,29,30,32,33,34,35,36]
		writeindices = [2,24,25,28,29,30,32,33,34,35,36,7,11,12,14,15,16,17,18]
		oldoderfunc = operator.itemgetter(*selected_features)
		reorderfunc = operator.itemgetter(*writeindices)
		rownum = 0
		for row in reader:

			if rownum == 0:
				newrow = oldoderfunc(row) + ('label',)
				writer.writerow(newrow)
			else:
				if(random.randint(0,1)==0):
					newrow = oldoderfunc(row) + ('0',)
					writer.writerow(newrow)
				elif(random.randint(0,1)==1):
					newrow = reorderfunc(row) + ('1',)
					writer.writerow(newrow)
			rownum = rownum + 1
	finally:
		input_file_handle.close()
		output_file_handle.close()

input_fnames = glob('tennis_atp-master/*.csv')#18
new_input_fnames = glob('tennis_atp-master/*_reordered.csv')
arrays = [reorderColumn(f) for f in input_fnames]
# Когда я писал этот код, лишь бог и я знали что этот метод делает,
# остался только бог
#arrays  = [ for f in input_fnames]
#arrays = [ read for f in fnames]
f = "tennis_atp-master/atp_matches_2016_reordered.csv"

#arrays = [np.genfromtxt(f,delimiter = ',',usecols = selected_features) for f in fnames]
reorderColumn()
dataset = np.genfromtxt(f,delimiter = ',')
le = preprocessing.LabelEncoder()

for i in range(len(dataset)):
	dataset[i] = le.fit_transform(dataset[i])

dataset = preprocessing.normalize(dataset,axis = 0)

#dataset = numpy.concatenate((dataset,dataset), axis=0)
X = dataset[:,:-1]
y = dataset[:,-1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)


#print (" X_train: " + X_train.shape+" Train_label: "+ y_train.shape +
#" X_test: "+ x_test.shape +" Y_test: "+y_test.shape)
#for data in dataset:
#	print(data.shape)
"""
def reoderColumns(input_file_handle,output_file_handle):
	writenames = "surface,winner_id,winner,".split(",") # example
	reader = csv.reader(input_file_handle)
	writer = csv.writer(output_file_handle)
	# don't forget to open both files in binary mode (2.x)
	# or with `newline=''` (3.x)
	readnames = reader.next()
	name2index = dict((name, index) for index, name in enumerate(readnames))
	writeindices = [name2index[name] for name in writenames]
	reorderfunc = operator.itemgetter(*writeindices)
	writer.writerow(writenames)
	for row in reader:
		writer.writerow(reorderfunc(row))
"""
