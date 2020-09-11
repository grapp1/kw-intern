BASE_PATH=$PWD

export CMAKE=$BASE_PATH/parflow/dependencies/cmake/bin/cmake
export CTEST=$BASE_PATH/parflow/dependencies/cmake/bin/ctest

export HDF5_DIR=$BASE_PATH/opt/hdf5

export NETCDF_DIR=$BASE_PATH/opt/netcdf

export SILO_DIR=$BASE_PATH/opt/silo

export HYPRE_DIR=$BASE_PATH/opt/hypre

export PARFLOW_DIR=$BASE_PATH/opt/parflow/

# -----------------------------------------------------------------------------
# Fail on error
# -----------------------------------------------------------------------------

set -e

# -----------------------------------------------------------------------------
# Setup python
# -----------------------------------------------------------------------------

python3 -m venv py-env

$BASE_PATH/py-env/bin/pip3 install -r $BASE_PATH/opt/parflow/python/requirements.txt

export PYTHONPATH=$BASE_PATH/parflow/build/pftools/python
