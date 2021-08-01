#include <iostream>
#include <mpi.h>
#include <hdf5.h>

#define fileName "ph5_demo_data.h5"
#define dsetName "ph5_demo_dset"
#define NY 5

int main(int argc, char ** argv)
{
    MPI_Comm comm = MPI_COMM_WORLD;
    MPI_Info info = MPI_INFO_NULL;

    // initialize MPI
    MPI_Init(&argc, &argv);

    // get the rank of the current process, and the total number of processes.
    int rank, size;
    MPI_Comm_rank(comm, &rank);
    MPI_Comm_size(comm, &size);

    // handlers for HDF5 objects
    hid_t fa_plist_id, dx_plist_id, file_id, dspace_id, dset_id, memspace;
    herr_t status;

    /*
    * Set up File Access Property list for MPI-IO access
    */
    fa_plist_id = H5Pcreate(H5P_FILE_ACCESS);
    H5Pset_fapl_mpio(fa_plist_id, comm, info);

    // open the file collectively
    file_id = H5Fopen(fileName, H5F_ACC_RDWR, fa_plist_id);

    hsize_t start[2], count[2];
    
    // open the dataset collectively with default properties
    dset_id = H5Dopen(file_id, dsetName, H5P_DEFAULT);
    // get the dataspace for this dataset
    dspace_id = H5Dget_space(dset_id);

    /*
    * Set up Data transfer(X) Property list for MPI-IO access
    */
    dx_plist_id = H5Pcreate(H5P_DATASET_XFER);
    H5Pset_dxpl_mpio(dx_plist_id, H5FD_MPIO_COLLECTIVE); // collective or independent

    /*
    * create memory space for current process
    */
    start[0] = rank;
    start[1] = 0;

    count[0] = 1;
    count[1] = NY;
    memspace = H5Screate_simple(2, count, NULL);
    // select the hyperslab for current process
    H5Sselect_hyperslab(dspace_id, H5S_SELECT_SET, start, NULL, count, NULL);
    // dspace_id has been modified and points to the selected portion of the original dataspace

    // prepare the data for current process
    int data[NY];

    // read data from the file
    status = H5Dread(dset_id, H5T_NATIVE_INT, memspace, dspace_id, dx_plist_id, data);
    /*
    * memspace: dataspace specifying the size of the memory that needs to be read
    * dspace_id: dataspace sepcifying the portion of the dataset that needs to be read
    */
    
    std::cout<<"Proc"<<rank<<" return "<<status<<"| Read: ";
    for(int i=0; i<NY; i++)
        std::cout<<data[i]<<", ";
    std::cout<<std::endl;

    // close the file
    H5Dclose(dset_id);
    H5Fclose(file_id);

    // finalize MPI
    MPI_Finalize();

    return 0;
}