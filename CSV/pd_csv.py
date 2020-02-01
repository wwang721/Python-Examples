#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
# Created by WW on Jan. 26, 2020
# All rights reserved.
#

import numpy as np
import pandas as pd 

def main():
	#=====================================================================
	# Create a pandas.DataFrame.
	df = pd.DataFrame(np.arange(16).reshape(4, 4), 
	    index = ['row1', 'row2', 'row3', 'row4'], 
	    columns = ['col1', 'col2', 'col3', 'col4'])
	'''
	:param index: line index
	:param columns: column index
	'''

	print(df, '\n')

	# Save pd.DataFrame as .csv file.
	df.to_csv("pd_test.csv", header = True, index = True, sep = ',')
	'''
	:param header: Bool, default = True (column index saved in CSV file)
	:param index: Bool, default = False (line index not saved in CSV file)
	'''

	#=====================================================================
	# Use pandas to read .csv file.
	data = pd.read_csv('pd_test.csv', header = 0, index_col = 0, names=['a', 'b', 'c',' d'])
	'''
	:param header: {0, None}, default = 0 (read first line as column index)
	:param index_col: {0, None}, default = False (read first column not as line index)
	:param names: List, change column index (no matter header = 0 or None) to names
	'''

	X = data.columns	# get column index
	Y = data.index 		# get line index
	print(X)
	print(Y)
	'''
	Notice: 
		X.dtype = 'object', and Y.dtype = 'object' ('object' is similar to 'string')
		if you need to convert string to numbers:
		X = X.astype(np.float64), Y = Y.astype(np.float64)
	'''

	print(data, '\n')

	# Convert the values (exclude line and column index) of pd.DataFrame -> np.array .
	print(data.values) 

if __name__ == "__main__":
    main()




