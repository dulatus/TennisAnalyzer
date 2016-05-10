#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import math
from sklearn import svm
import urllib
from glob import glob
import random
import csv
import operator
from sklearn.cross_validation import train_test_split
from sklearn import preprocessing
from sklearn.grid_search import GridSearchCV
from sklearn import svm
from sklearn.metrics import accuracy_score
def reorderColumn():
	# example
	try:
		input_file_handle = open("tennis_atp-master/all/atp_matches_all.csv",'rb')
		output_file_handle = open("tennis_atp-master/all/atp_matches_all_reordered.csv",'wb')
		writer = csv.writer(output_file_handle,delimiter = ',')
		reader = csv.reader(input_file_handle,delimiter = ',')
		# don't forget to open both files in binary mode (2.x)
		# or with `newline=''` (3.x)
		readnames = reader.next()
		selected_features = [2,7,11,12,14,15,16,17,18,24,25,28,29,30,32,33,34,35,36]
		writeindices = [2,24,25,28,29,30,32,33,34,35,36,7,11,12,14,15,16,17,18]
		oldoderfunc = operator.itemgetter(*selected_features)
		reorderfunc = operator.itemgetter(*writeindices)
		rownum = 0
		for row in reader:
			if(random.randint(0,1)==0):
				newrow = oldoderfunc(row) + ('0',)
				writer.writerow(newrow)
			elif(random.randint(0,1)==1):
				newrow = reorderfunc(row) + ('1',)
				writer.writerow(newrow)
				rownum +=1
	finally:
		input_file_handle.close()
		output_file_handle.close()
# Когда я писал этот код лишь богкодинга и я знали что этот метод делает,
# остался только бог
#arrays  = [ for f in input_fnames]
#arrays = [ read for f in fnames]
#arrays = [np.genfromtxt(f,delimiter = ',',usecols = selected_features) for f in fnames]
def machiner():
	selected_features = [2,7,11,12,14,15,16,17,18,24,25,28,29,30,32,33,34,35,36]
	f = "tennis_atp-master/all/atp_matches_all_reordered.csv"
	dataset = np.genfromtxt(f,delimiter = ',')
	X = dataset[:,:-1]
	y = dataset[:,-1]
	for i in range(len(X)):
		if math.isnan(X[i,0]):
			X[i,0]=0.
	# coding=utf-8
	le = preprocessing.LabelEncoder()
	for i in range(len(X)):
		X[i] = le.fit_transform(X[i])
	X = preprocessing.normalize(X,axis = 0)
	#dataset = numpy.concatenate((dataset,dataset), axis=0)
	X = dataset[:,:-1]
	y = dataset[:,-1]
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=42)
	parameters = [{'kernel': ['rbf'], 'gamma': [1e-2, 1e-3, 1e-4],
	'C': [1, 10, 100, 1000, 10000]},
	{'kernel': ['linear'], 'C': [1, 10, 100, 1000, 10000]}]
	svr = svm.SVC()
	clf = GridSearchCV(svr, parameters, cv=5)
	clf = clf.fit(X_train, y_train)
	print(clf.best_estimator_)
	predicted=clf.predict(X_test)


	acc = accuracy_score(predicted,y_test)
	print("Accuracy: ",acc)
	for i in range(len(predicted)):
		print (predicted[i],":",y_test[i])


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
