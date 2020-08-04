#!/bin/bash
# -----------------------------------------------------------------------------
# Setting up ParFlow and Python environment in docker
# -----------------------------------------------------------------------------

source ~/parflow/env.sh

export LC_ALL=C.UTF-8
export PYTHONPATH=~/kw-intern/parflow/python/

pip3 install -r ~/kw-intern/parflow/python/requirements.txt
