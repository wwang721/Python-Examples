/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
 * Copyright © 2020 Wei Wang.                                                  *
 * Created by WW on 2020/01/26.                                                *
 * All rights reserved.                                                        *
 *                                                                             *
 * This example illustrates how to read and edit an existing dataset.              *
 * Reference: HDF5 Tutorial (https://portal.hdfgroup.org/display/HDF5/HDF5)    *
 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */

//
// h5cpp_reading.cpp
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

/* 
 *  Define the names of HDF5 file, groups, datasets, and attributes.
 *  Use H5::H5std_string for name strings.
 */
const H5std_string FILE_NAME("h5cpp_example.hdf5");
const H5std_string GROUP_NAME("group1");
const H5std_string DATASET_NAME("dset");
const H5std_string ATTR_NAME("myAttr2");

int main (int argc, char **argv)
{
    
    // Try block to detect exceptions raised by any of the calls inside it.
    try
    {
        /*
    	 * Turn off the auto-printing when failure occurs so that we can
    	 * handle the errors appropriately
         */
    	Exception::dontPrint();

        /* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */ 

        /* HOW TO DELETING A DATASET! */

        /*

        // Open an existing file.
        // H5::H5F_ACC_RDWR : read or edit an existing file.
        H5File file_d(FILE_NAME, H5F_ACC_RDWR);
        
        // Open an existing group.
        Group group_d = file_d.openGroup(GROUP_NAME);

        // Use H5::H5Ldelete to delete an existing dataset.
        int result = H5Ldelete(group_d.getId(), DATASET_NAME.c_str(), H5P_DEFAULT);
        // String.c_str() convert "string" to "const char *".

        cout << result << endl;     
        // Non-negtive: successfully delete; 
        // Otherwise: fail.

        // Save and exit the group.
        group_d.close();
        // Save and exit the file.
        file_d.close();
        // Important! The two close()s above can't be omitted! 
        // Otherwise, the deleting behavior won't be saved to file.

        */

        /* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */ 

        // Open an existing file.
        // H5::H5F_ACC_RDWR : read or edit an existing file.
        H5File file(FILE_NAME, H5F_ACC_RDWR);
        
        // Open an existing group of the file.
        Group group = file.openGroup(GROUP_NAME);

        // Open an existing dataset of the group.
        DataSet dataset = group.openDataSet(DATASET_NAME);

        // Get the dataspace of the dataset.
    	DataSpace filespace = dataset.getSpace();

        // Get the rank of the dataset.
        int rank = filespace.getSimpleExtentNdims();

        // Use H5::hsize_t (similar to int) for dimensions
        hsize_t dims[rank];        // dataset dimensions

        // Get the dimensions of the dataset.
        rank = filespace.getSimpleExtentDims(dims);

        cout << DATASET_NAME << " rank = " << rank << ", dimensions "
                 << dims[0] << " x "
                 << dims[1] << endl;

        // Dataspace for data read from file.
        DataSpace myspace(rank, dims);

        double data_out[dims[0]][dims[1]];      // buffer for data read from file

        // Read data from file to buffer.
        dataset.read(data_out, PredType::NATIVE_DOUBLE, myspace, filespace);

        for (int i = 0; i < dims[0]; i++)
        {
            for (int j = 0; j < dims[1]; j++)
                cout << data_out[i][j] << " ";
            cout << endl;
        }

        /* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */ 
        // Read the attribute of the dataset.
        cout << endl;

        // Open an existing attribute of the dataset.
        Attribute attr = dataset.openAttribute(ATTR_NAME);

        // Get the dataspace of the attribute.
        DataSpace attr_space = attr.getSpace();

        // Get the rank of the attribute.
        int attr_rank = attr_space.getSimpleExtentNdims();

        // Use H5::hsize_t (similar to int) for dimensions.
        hsize_t attr_dims[attr_rank];       // attribute dimensions

        // Get the dimension of the attribute.
        attr_rank = attr_space.getSimpleExtentDims(attr_dims);

        cout << ATTR_NAME << " rank = " << attr_rank << ", dimensions " << attr_dims[0] << endl;

        char attr_data_out[attr_dims[0]];   // buffer for attribute data read from file

        // Read attribute data from file to buffer.  
        attr.read(PredType::NATIVE_CHAR, attr_data_out);

        cout << attr_data_out << endl;

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