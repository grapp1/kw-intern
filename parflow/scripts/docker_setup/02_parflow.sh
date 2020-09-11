BASE_PATH=$PWD

export CMAKE=$BASE_PATH/parflow/dependencies/cmake/bin/cmake
export CTEST=$BASE_PATH/parflow/dependencies/cmake/bin/ctest

export HDF5_DIR=$BASE_PATH/opt/hdf5

export NETCDF_DIR=$BASE_PATH/opt/netcdf

export SILO_DIR=$BASE_PATH/opt/silo

export HYPRE_DIR=$BASE_PATH/opt/hypre

# -----------------------------------------------------------------------------
# Fail on error
# -----------------------------------------------------------------------------

set -e

# -----------------------------------------------------------------------------
# Setup Parflow
# -----------------------------------------------------------------------------

PARFLOW_VERSION=py-pftools
PARFLOW_GIT_URL=git@github.com:grapp1/parflow.git
git clone                             \
  --recursive --single-branch          \
  --branch $PARFLOW_VERSION             \
  $PARFLOW_GIT_URL                       \
  $BASE_PATH/parflow/src

$CMAKE                         \
    -S $BASE_PATH/parflow/src   \
    -B $BASE_PATH/parflow/build  \
    -D CMAKE_BUILD_TYPE=Release   \
    -D HDF5_ROOT=$HDF5_DIR         \
    -D PARFLOW_ENABLE_HDF5=TRUE     \
    -D HYPRE_ROOT=$HYPRE_DIR         \
    -D PARFLOW_ENABLE_HYPRE=TRUE      \
    -D PARFLOW_ENABLE_SILO=TRUE        \
    -D SILO_ROOT=$SILO_DIR              \
    -D PARFLOW_HAVE_CLM=TRUE             \
    -D PARFLOW_ENABLE_PYTHON=TRUE         \
    -D PARFLOW_ENABLE_TIMING=TRUE          \
    -D PARFLOW_AMPS_LAYER=mpi1              \
    -D PARFLOW_AMPS_SEQUENTIAL_IO=TRUE       \
    -D PARFLOW_ENABLE_NETCDF=TRUE             \
    -D NETCDF_DIR=$NETCDF_DIR                  \
    -D CURL_LIBRARY=/usr/lib/x86_64-linux-gnu/libcurl.so.4

$CMAKE --build $BASE_PATH/parflow/build
$CMAKE --install $BASE_PATH/parflow/build --prefix $BASE_PATH/opt/parflow

export PARFLOW_DIR=$BASE_PATH/opt/parflow/
