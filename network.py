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
