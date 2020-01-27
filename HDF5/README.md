# README

[**HDF5**](https://www.hdfgroup.org/solutions/hdf5/) (Hierarchical Data Format) 由美国**伊利诺伊大学厄巴纳-香槟分校** [**UIUC**](http://www.illinois.edu) (University of Illinois at Urbana-Champaign) 开发，是一种常见的跨平台数据储存文件，可以存储不同类型的图像和数码数据，并且可以在不同类型的机器上传输，同时还有统一处理这种文件格式的函数库。


## **HDF5 结构**

**HDF5** 文件一般以 **.h5** 或者 **.hdf5** 作为后缀名，需要专门的软件才能打开预览文件的内容。**HDF5** 文件结构中有 **2 primary objects:** **Groups** 和 **Datasets**。

- **Groups** 就类似于文件夹，每个 **HDF5** 文件其实就是**根目录** (root) **group** `'/'`。
- **Datasets** 类似于 [**NumPy**](https://numpy.org) 中的数组 array 。

每个 dataset 可以分成两部分: **原始数据 (raw) data values** 和 **元数据 metadata** (a set of data that describes and gives information about other data => raw data)。

``` cpp
+-- Dataset
|   +-- (Raw) Data Values (eg: a 4 x 5 x 6 matrix)
|   +-- Metadata
|   |   +-- Dataspace (eg: Rank = 3, Dimensions = {4, 5, 6})
|   |   +-- Datatype (eg: Integer)
|   |   +-- Properties (eg: Chuncked, Compressed)
|   |   +-- Attributes (eg: attr1 = 32.4, attr2 = "hello", ...)
|
```


从上面的结构中可以看出：

* **Dataspace** 给出原始数据的**秩** (Rank) 和**维度** (dimension)
* **Datatype** 给出数据类型
* **Properties** 说明该 dataset 的**分块储存**以及**压缩**情况 
	+ **Chunked**: Better access time for subsets; extendible
	+ **Chunked & Compressed**: Improves storage efficiency, transmission speed
* **Attributes** 为该 dataset 的其他自定义属性
 
整个 **HDF5** 文件的结构如下所示：
 
``` cpp
+-- /
|   +-- group_1
|   |   +-- dataset_1_1
|   |   |   +-- attribute_1_1_1
|   |   |   +-- attribute_1_1_2
|   |   |   +-- ...
|   |   |
|   |   +-- dataset_1_2
|   |   |   +-- attribute_1_2_1
|   |   |   +-- attribute_1_2_2
|   |   |   +-- ...
|   |   |
|   |   +-- ...
|   |
|   +-- group_2
|   |   +-- dataset_2_1
|   |   |   +-- attribute_2_1_1
|   |   |   +-- attribute_2_1_2
|   |   |   +-- ...
|   |   |
|   |   +-- dataset_2_2
|   |   |   +-- attribute_2_2_1
|   |   |   +-- attribute_2_2_2
|   |   |   +-- ...
|   |   |
|   |   +-- ...
|   |
|   +-- ...
|
```


## **HDF5 下载与安装**

下载安装 **HDF5** 的方法有多种，Mac 下可以直接 `brew install hdf5`，其他 Linux 系统也可以使用对应**安装包管理工具**下载就行了。当然也可以去官网 <https://portal.hdfgroup.org/display/support/Downloads> 下载对应操作系统的压缩包。

下载安装完成后可以在终端使用 `h5dump` 命令查看 **HDF5** 文件的内容。官网同时提供一个 **JAVA** 开发的 **HDF5** 数据可视化工具 [**HDFView**](https://portal.hdfgroup.org/display/support/Download+HDFView)，支持全平台查看数据, 但是注意打开文件的路径中不要包含中文。

* **注意:** 当为 **python** 安装 **HDF5** 的 [**h5py**]( http://www.h5py.org) 库时，使用 `conda install h5py` 或者 `pip install h5py` 后也会安装部分二进制文件 (如 `h5dump`, `h5cc/h5c++`,  `h5fc` 等) 和库文件，但是可能不完整，导致 **HDF5** 的 C/C++ 编译器 `h5cc/h5c++` 和 Fortran 编译器 `h5fc` 无法正常工作。

* **解决办法:** 若 `h5c++` 无法正常编译 C++ 文件，终端输入 `which h5c++`, 若显示该二进制文件在 **python** 的二进制 (binary) 文件夹 **bin** 内，则只需找到 `brew` 或者其他**安装包管理工具**下载的 `h5c++` (一般在 `/usr/local/bin` 内) 或者官网下载解压后的 `h5c++`，在根目录 (~) 下的 .bashrc 文件 (或者其他 shell, 如 zsh 的配置文件 .zshrc) 内添加 `alias h5c++ = /usr/local/bin/h5c++` 就可以了。
<br><br>
若是想用 `clang++` 或者 `g++` 而非 `h5c++` 编译, 其中只要添加一些**头文件** (-I) 和**库文件** (-L) 的 **flags** 就行了。首先确认 `h5c++` 可以正常编译后，在终端输入 `h5c++ -show`, 会显示 
`CXX_COMPILER` + `CXX_FLAGS`, 例如: `g++ -I/usr/local/opt/szip/include -L/usr/local/Cellar/hdf5/1.10.6/lib /usr/local/Cellar/hdf5/1.10.6/lib/libhdf5_hl_cpp.a /usr/local/Cellar/hdf5/1.10.6/lib/libhdf5_cpp.a /usr/local/Cellar/hdf5/1.10.6/lib/libhdf5_hl.a /usr/local/Cellar/hdf5/1.10.6/lib/libhdf5.a -L/usr/local/opt/szip/lib -lsz -lz -ldl -lm`
, 故我们可以使用 `CXX_COMPILER` + `XXX.cpp` + `CXX_FLAGS` 来编译 C++ 文件 (因为编译依赖关系，`CXX_FLAGS` 通常放在最后，`XXX.cpp` 放在 `CXX_FLAGS` 之前，否则可能会无法成功编译) 。


## **Python 读写 HDF5 文件**

**HDF5** 的 **python** 库 [**h5py**]( http://www.h5py.org) 调用起来比较简单，我在这给出一个简单的例子：

[`/HDF5/h5py_example.py`](/HDF5/h5py_example.py)


## **C++ 读写 HDF5 文件**

**C++** 读写 **HDF5** 文件比较复杂，参考官网给出的 Examples，下面给出一个创建 **HDF5** 文件的例子和一个读写 **HDF5** 文件的例子:

1. [`/HDF5/CPP/h5cpp_creating.cpp`](/HDF5/CPP/h5cpp_creating.cpp)
2. [`/HDF5/CPP/h5cpp_reading.cpp`](/HDF5/CPP/h5cpp_reading.cpp)


## **总结**

更多高级 **API** (Application Program Interface) 的调用，如 **Subset**, **Hyperslab**, **Chunk** , **Compress**, **Single-Writer/Multiple-Reader** (SWMR), **Parallel HDF5** (即 **HDF5 MPI - Message Passing Interface** 并行读写) 以及 **Virtual Dataset** (VDS) 等，可以查阅官网的 [**Documentation**](https://portal.hdfgroup.org/display/HDF5/HDF5)。

除了储存数码数据，**HDF5** 文件还可以用于存储图像、PDF文件，甚至 Excel 文件，但是鉴于我目前的科研需求，还是 .tsv 和 .txt 更适合我，毕竟查看起来更简单，跨平台跨语言读写也很方便。对我来说，.csv 文件都已经算是比较高级的数据储存格式了😆。 🎉 🎉 🎉 












