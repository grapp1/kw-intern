BASE_PATH=$PWD

# -----------------------------------------------------------------------------
# Fail on error
# -----------------------------------------------------------------------------

set -e

# -----------------------------------------------------------------------------
# Setup CMake 3.18.2
# -----------------------------------------------------------------------------

CMAKE_URL=https://cmake.org/files/v3.18/cmake-3.18.2-Linux-x86_64.tar.gz

mkdir -p $BASE_PATH/parflow/dependencies/cmake
cd $BASE_PATH/parflow/dependencies/cmake
curl -L $CMAKE_URL | tar --strip-components=1 -xzv

export CMAKE=$BASE_PATH/parflow/dependencies/cmake/bin/cmake
export CTEST=$BASE_PATH/parflow/dependencies/cmake/bin/ctest

# -----------------------------------------------------------------------------
# Install HDF5
# -----------------------------------------------------------------------------

HDF5_URL=https://support.hdfgroup.org/ftp/HDF5/releases/hdf5-1.12/hdf5-1.12.0/src/hdf5-1.12.0.tar.gz

export HDF5_DIR=$BASE_PATH/opt/hdf5

mkdir -p $BASE_PATH/parflow/dependencies/hdf5-src
cd $BASE_PATH/parflow/dependencies/hdf5-src
curl -L $HDF5_URL | tar --strip-components=1 -xzv
CC=mpicc ./configure --prefix=$HDF5_DIR --enable-parallel
make -j32
make install

# -----------------------------------------------------------------------------
# Install NetCDF
# -----------------------------------------------------------------------------

NETCDF_URL=https://github.com/Unidata/netcdf-c/archive/v4.7.4.tar.gz

export NETCDF_DIR=$BASE_PATH/opt/netcdf

mkdir -p $BASE_PATH/parflow/dependencies/netcdf-src
cd $BASE_PATH/parflow/dependencies/netcdf-src
curl -L $NETCDF_URL | tar --strip-components=1 -xzv
CC=mpicc CPPFLAGS=-I$HDF5_DIR/include LDFLAGS=-L$HDF5_DIR/lib ./configure --disable-shared --disable-dap --prefix=${NETCDF_DIR}
make -j32
make install

# -----------------------------------------------------------------------------
# Install SILO
# -----------------------------------------------------------------------------

SILO_URL=https://wci.llnl.gov/content/assets/docs/simulation/computer-codes/silo/silo-4.10.2/silo-4.10.2.tar.gz

export SILO_DIR=$BASE_PATH/opt/silo

mkdir -p $BASE_PATH/parflow/dependencies/silo-src
cd $BASE_PATH/parflow/dependencies/silo-src
curl -L $SILO_URL | tar --strip-components=1 -xzv
./configure  --prefix=$SILO_DIR --disable-silex --disable-hzip --disable-fpzip
make -j32
make install

# -----------------------------------------------------------------------------
# Install Hypre
# -----------------------------------------------------------------------------

HYPRE_VERSION=v2.19.0

export HYPRE_DIR=$BASE_PATH/opt/hypre

mkdir -p $BASE_PATH/parflow/dependencies/hypre-src
cd $BASE_PATH/parflow/dependencies/hypre-src
git clone https://github.com/hypre-space/hypre.git --single-branch --branch $HYPRE_VERSION

cd $BASE_PATH/parflow/dependencies/hypre-src/hypre/src
./configure --prefix=$HYPRE_DIR --with-MPI
make -j32
make install
