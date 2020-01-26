/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
 * Copyright © 2020 Wei Wang.						       *
 * Created by WW on 2020/01/26.	                                               *
 * All rights reserved.							       *
 *	                                                                       *
 * This example illustrates how to create a dataset that is a 4 x 6 array.     *
 * Reference: HDF5 Tutorial (https://portal.hdfgroup.org/display/HDF5/HDF5)    *
 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */

//
// h5cpp_creating.cpp
// CPP
//

#include <iostream>
#include <string>
#include "H5Cpp.h"

#ifndef _H5_NO_NAMESPACE_
using namespace H5;
#ifndef _H5_NO_STD_
    using std::cout;
    using std::endl;
#endif /* _H5_NO_STD_ */        
#endif /* _H5_NO_NAMESPACE_ */

#define PI 3.1415926535

/* 
 *  Define the names of HDF5 file, groups, datasets, and attributes.
 *  Use H5::H5std_string for name strings.
 */
const H5std_string FILE_NAME("h5cpp_example.hdf5");
const H5std_string GROUP_NAME("group1");
const H5std_string DATASET_NAME("dset");
const H5std_string ATTR_NAME1("myAttr1");
const H5std_string ATTR_NAME2("myAttr2");

const int DIM0 = 4;       // dataset dimensions
const int DIM1 = 6;
const int RANK = 2;

int main (int argc, char **argv)
{
    // Try block to detect exceptions raised by any of the calls inside it.
    try
    {
    	/* 
         * Turn off the auto-printing when failure occurs so that we can
    	 * handle the errors appropriately.
         */
    	Exception::dontPrint();

        /* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */

        double data[DIM0][DIM1];	    // buffer for data to write

        for (int i = 0; i < DIM0; i++)
    		for (int j = 0; j < DIM1; j++)
    	 		data[i][j] = (i + 1) * PI + j;
    	
    	
    	// Create a new file using the default property lists.
        // H5::H5F_ACC_TRUNC : create a new file or overwrite an existing file.
    	H5File file(FILE_NAME, H5F_ACC_TRUNC);

        // Create a group under root '/'.
    	Group group(file.createGroup(GROUP_NAME));
    	
        
        // Use H5::hsize_t (similar to int) for dimensions.
    	hsize_t dims[RANK];               // dataset dimensions
    	dims[0] = DIM0;
    	dims[1] = DIM1;
    	
        // Create the dataspace for a dataset first.
    	DataSpace dataspace(RANK, dims);
    	
    	// Create the dataset under group with specified dataspace.      
    	DataSet dataset = group.createDataSet(DATASET_NAME, PredType::NATIVE_DOUBLE, dataspace);

        // Write data in buffer to dataset.
    	dataset.write(data, PredType::NATIVE_DOUBLE);

        /* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */ 

        int attr1_data[2] = {100, 200};          // buffer for attribute data to wirte

        hsize_t attr1_dims[1] = {2};             // attribute dimension, rank = 1
        
        // Create the dataspace for an attribute first.
        DataSpace attr1_dataspace(1, attr1_dims);         // rank = 1

        // Create the attribute of dataset with specified dataspace.
        Attribute attribute1 = dataset.createAttribute(ATTR_NAME1, PredType::STD_I32BE, attr1_dataspace);
        
        // Write data in buffer to attribute.
        attribute1.write(PredType::NATIVE_INT, attr1_data);

        /* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */ 

        /* String Data */

        char attr2_data[30];    // buffer for attribute data to wirte 
    	sprintf(attr2_data, "hello, world!\nAuthor: Wei Wang");

        hsize_t attr2_dims[1] = {30};       // attribute dimension, rank = 1

        // Create the dataspace for an attribute first.
        DataSpace attr2_dataspace(1, attr2_dims);       // rank = 1

        // Create the attribute of dataset with specified dataspace.
        Attribute attribute2 = dataset.createAttribute(ATTR_NAME2, PredType::NATIVE_CHAR, attr2_dataspace);
        
        // Write data in buffer to attribute.
        attribute2.write(PredType::NATIVE_CHAR, attr2_data);

        /* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */ 

        // Save and exit the group.
    	group.close();
        // Save and exit the file.
    	file.close();

        /* h5cpp_example.hdf5 file structure
         * +-- '/'
         * |   +-- group 'group1'
         * |   |   +-- dataset 'dset'
         * |   |   |   +-- attribute 'myAttr1'
         * |   |   |   +-- attribute 'myAttr2'
         * |   |   |
         * |   |
         * |
         */

    }  // end of try block

    
    // Catch failure caused by the H5File operations.
    catch(FileIException error)
    {
    	error.printErrorStack();
    	return -1;
    }

    // Catch failure caused by the DataSet operations.
    catch(DataSetIException error)
    {
    	error.printErrorStack();
    	return -1;
    }

    // Catch failure caused by the DataSpace operations.
    catch(DataSpaceIException error)
    {
    	error.printErrorStack();
    	return -1;
    }
	
    return 0;  // successfully terminated
    
}
