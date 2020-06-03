#!/bin/bash
## ParFlow install script for Ubuntu (Part 2 of 2)
## installing ParFlow as non-root user

set -e
export ROOT=$PWD

mkdir -p $ROOT/parflow/build $ROOT/parflow/dependencies/cmake  $ROOT/parflow/dependencies/hypre-src

git clone --single-branch --branch v3.6.0 --recursive https://github.com/parflow/parflow.git $ROOT/parflow/src

echo HYPRE_DIR=$ROOT/parflow/dependencies/hypre >> $ROOT/parflow/env.sh
echo export PARFLOW_DIR=$ROOT/parflow/install >> $ROOT/parflow/env.sh
echo CMAKE=$ROOT/parflow/dependencies/cmake/bin/cmake >> $ROOT/parflow/env.sh
echo CTEST=$ROOT/parflow/dependencies/cmake/bin/ctest >> $ROOT/parflow/env.sh

source $ROOT/parflow/env.sh

cd $ROOT/parflow/dependencies/cmake
curl -L https://cmake.org/files/v3.17/cmake-3.17.2-Linux-x86_64.tar.gz | tar --strip-components=1 -xzv

cd $ROOT/parflow/dependencies/hypre-src
curl -L https://github.com/hypre-space/hypre/archive/v2.17.0.tar.gz | tar --strip-components=1 -xzv
cd src
./configure --prefix=$HYPRE_DIR --with-MPI
make install


$CMAKE \
   -S $ROOT/parflow/src \
   -B $ROOT/parflow/build \
   -D PARFLOW_AMPS_LAYER=mpi1 \
   -D PARFLOW_AMPS_SEQUENTIAL_IO=TRUE \
   -D HYPRE_ROOT=$HYPRE_DIR \
   -D PARFLOW_ENABLE_TIMING=TRUE \
   -D PARFLOW_HAVE_CLM=TRUE

$CMAKE --build $ROOT/parflow/build
$CMAKE --install $ROOT/parflow/build --prefix $ROOT/parflow/install
cd $ROOT/parflow/build/
##$CTEST -VV
