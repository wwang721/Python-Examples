#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
# Created by WW on Jan. 23, 2020
# All rights reserved.
#

import numpy as np 

def main():
	#=============================================================
	''' load plain text file (.txt) as np.array '''
	data = np.loadtxt(r"lambda.txt")

	#print(data)

	x = data[:,0] # get the first column of data
	y = data[:,1] # get the second column of data

	#print(x)
	#print(y)

	#=============================================================
	''' load .csv (comma separated values) file as np.array '''
	np.savetxt("lambda.csv", data, fmt="%g", delimiter=',')

	data1 = np.loadtxt(r"lambda.csv", delimiter=',')
	#print(data1)

	#=============================================================
	''' load .tsv (tab separated values) file as np.array '''
	np.savetxt("lambda.tsv", data, fmt="%g", delimiter='\t')

	data2 = np.loadtxt(r"lambda.tsv", delimiter='\t')
	#print(data2)

if __name__ == "__main__":
    main()
