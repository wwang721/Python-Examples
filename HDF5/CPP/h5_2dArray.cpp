/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
 * Copyright © 2021 Wei Wang.						                           *
 * Created by WW on 2020/01/26.	                                               *
 * All rights reserved.							                               *
 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */

#include <iostream>
#include <string>
#include "H5Cpp.h"
using namespace H5;
/* 
 *  Define the names of HDF5 file, groups, datasets, and attributes.
 *  Use H5::H5std_string for name strings.
 */
const H5std_string FILE_NAME("2dArray.h5");
const H5std_string GROUP_NAME("group");
const H5std_string DATASET_NAME1("static_array");
const H5std_string DATASET_NAME2("dynamic_array(pointer)");
const H5std_string DATASET_NAME3("pointer_hyperslab");

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

        /*
         * The HDF5 library expects to a contiguous array of elements, 
         * not pointers to elements in lower dimensions
         */
        double static_data[DIM0][DIM1];	    // contiguous array

        double **dynamic_data = new double * [DIM0];    // incontiguous array
            
        int index = 0;
        for (int i = 0; i < DIM0; i++)
        {
            dynamic_data[i] = new double [DIM1];
    		for (int j = 0; j < DIM1; j++)
            {   
                static_data[i][j] = index;
    	 		dynamic_data[i][j] = index;
                index ++;
            }
    	}
    	
    	// Create a new file using the default property lists.
        // H5::H5F_ACC_TRUNC : create a new file or overwrite an existing file.
    	H5File file(FILE_NAME, H5F_ACC_TRUNC);

        // Create a group under root '/'.
    	Group group(file.createGroup(GROUP_NAME));
    	
        // Use H5::hsize_t (similar to int) for dimensions.
    	hsize_t dims[RANK], start[RANK], count[RANK];               // dataset dimensions
    	dims[0] = DIM0;
    	dims[1] = DIM1;

        /* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */ 
        // For static array.
        // Create the dataspace for a dataset first.
        DataSpace dataspace1(RANK, dims);
        
        // Create the dataset under group with specified dataspace.      
        DataSet dataset1 = group.createDataSet(DATASET_NAME1, PredType::NATIVE_DOUBLE, dataspace1);

        // Write data in buffer to dataset.
        dataset1.write(static_data, PredType::NATIVE_DOUBLE);

        dataspace1.close();
        dataset1.close();

        /* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */ 
        // For dynamic array.
        // Create the dataspace for a dataset first.
        DataSpace dataspace2(RANK, dims);
        
        // Create the dataset under group with specified dataspace.      
        DataSet dataset2 = group.createDataSet(DATASET_NAME2, PredType::NATIVE_DOUBLE, dataspace2);

        // Write data in buffer to dataset.
        dataset2.write(dynamic_data, PredType::NATIVE_DOUBLE);

        dataspace2.close();
        dataset2.close();

        /* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */ 
        // Using hyperslab method
        count[0] = 1;
        count[1] = DIM1;

        start[1] = 0;

        // Create the dataspace for a dataset first.
    	DataSpace dataspace3(RANK, dims);

        // Create memory space for one line
        DataSpace memspace(RANK, count);

        // Create the dataset under group with specified dataspace.      
        DataSet dataset3 = group.createDataSet(DATASET_NAME3, PredType::NATIVE_DOUBLE, dataspace3);
        
        for(int k=0; k<DIM0; k++)
        {
            start[0] = k;

            // select the hyperslab for one line
            dataspace3.selectHyperslab(H5S_SELECT_SET, count, start, NULL, NULL);
            // Write data in buffer to dataset.
        	dataset3.write(dynamic_data[k], PredType::NATIVE_DOUBLE, memspace, dataspace3);
            /*
            * memspace: dataspace specifying the size of the memory that needs to be written
            * dataspace: dataspace sepcifying the portion of the dataset that needs to be written
            */

            // Reset the selection for the dataspace.
            dataspace3.selectNone();
        }

        dataspace3.close();
        memspace.close();
        dataset3.close();
        
        /* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */ 

        // Save and exit the group.
    	group.close();
        // Save and exit the file.
    	file.close();

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
