#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
# Created by WW on Jan. 26, 2020
# All rights reserved.
#

import h5py
import numpy as np

def main():
	#=======================================================================================
	# Create a HDF5 file.
	f = h5py.File("h5py_example.hdf5", "w") 	# mode = {'w', 'r', 'a'}

	# Create two groups under root '/'.
	g1 = f.create_group("bar1")
	g2 = f.create_group("bar2")

	# Create a dataset under root '/'.
	d = f.create_dataset("dset", data=np.arange(16).reshape([4, 4]))

	# Add two attributes to dataset 'dset'
	d.attrs["myAttr1"] = [100, 200]
	d.attrs["myAttr2"] = "Hello, world!"

	# Create a group and a dataset under group "bar1".
	c1 = g1.create_group("car1")
	d1 = g1.create_dataset("dset1", data=np.arange(10))

	# Create a group and a dataset under group "bar2".
	c2 = g2.create_group("car2")
	d2 = g2.create_dataset("dset2", data=np.arange(10))

	# Save and exit the file.
	f.close()

	''' h5py_example.hdf5 file structure
	+-- '/'
	|   +--	group "bar1"
	|   |   +-- group "car1"
	|   |   |   +-- None
	|   |   |   
	|   |   +-- dataset "dset1"
	|   |
	|   +-- group "bar2"
	|   |   +-- group "car2"
	|   |   |   +-- None
	|   |   |
	|   |   +-- dataset "dset2"
	|   |   
	|   +-- dataset "dset"
	|   |   +-- attribute "myAttr1"
	|   |   +-- attribute "myAttr2"
	|   |   
	|   
	'''

	#=======================================================================================
	# Read HDF5 file.
	f = h5py.File("h5py_example.hdf5", "r") 	# mode = {'w', 'r', 'a'}

	# Print the keys of groups and datasets under '/'.
	print(f.filename, ":")
	print([key for key in f.keys()], "\n")  

	#===================================================
	# Read dataset 'dset' under '/'.
	d = f["dset"]

	# Print the data of 'dset'.
	print(d.name, ":")
	print(d[:])

	# Print the attributes of dataset 'dset'.
	for key in d.attrs.keys():
		print(key, ":", d.attrs[key])

	print()

	#===================================================
	# Read group 'bar1'.
	g = f["bar1"]

	# Print the keys of groups and datasets under group 'bar1'.
	print([key for key in g.keys()])

	# Three methods to print the data of 'dset1'.
	print(f["/bar1/dset1"][:])		# 1. absolute path

	print(f["bar1"]["dset1"][:])	# 2. relative path: file[][]

	print(g['dset1'][:])		# 3. relative path: group[]



	# Delete a database.
	# Notice: the mode should be 'a' when you read a file.
	'''
	del g["dset1"]
	'''

	# Save and exit the file
	f.close()

if __name__ == "__main__":
    main()



