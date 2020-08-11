#!/bin/bash
# -----------------------------------------------------------------------------
# Setting up ParFlow and Python environment in docker
# -----------------------------------------------------------------------------

export PARFLOW_DIR=~/parflow/install
export LC_ALL=C.UTF-8
export PYTHONPATH=~/kw-intern/parflow/python/

pip3 install -r ~/kw-intern/parflow/python/requirements.txt
