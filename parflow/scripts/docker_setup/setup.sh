BASE_PATH=$PWD

export CMAKE=$BASE_PATH/parflow/dependencies/cmake/bin/cmake
export CTEST=$BASE_PATH/parflow/dependencies/cmake/bin/ctest

export HDF5_DIR=$BASE_PATH/opt/hdf5

export NETCDF_DIR=$BASE_PATH/opt/netcdf

export SILO_DIR=$BASE_PATH/opt/silo

export HYPRE_DIR=$BASE_PATH/opt/hypre

export PYTHONPATH=$BASE_PATH/parflow/build/pftools/python

export PARFLOW_DIR=$BASE_PATH/opt/parflow/
export PARFLOW_BUILD=$BASE_PATH/parflow/build
export PARFLOW_SRC=$BASE_PATH/parflow/src

source $BASE_PATH/py-env/bin/activate
