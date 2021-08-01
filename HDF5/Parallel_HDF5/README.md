# Parrallel HDF5

首先要安装 MPI，这一部分网上有很多资料，既然要做并行计算，我相信应该对 MPI 或多或少都有一定程度的了解了。

其次要检查一下电脑上已安装的 HDF5 支不支持并行，简单的用 `h5cc -showconfig` 测试一下, 如果 Features 里显示 `Parallel HDF5: yes` 就可以了； 如果是 no 就得重新配置安装一遍 HDF5, 安装时加上支持并行的选项:

``` shell
$ ./configure --enable-parallel --enable-shared
```

## Python: h5py

这一部分比较简单，而且 h5py 的文档里已经给出demo了： https://docs.h5py.org/en/stable/mpi.html 所以我就不详加叙述。

## C/C++

需要用到 mpi.h 库来实现并行，参见我写的读写的两个 demo，输出一个 $\text{nProc}\times5$ 按顺序递增的二维数组，每个进程输出一行，读取时也是每个进程读取一行。
