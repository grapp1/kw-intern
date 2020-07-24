# ParFlow/python

This directory includes our work to develop python tools to assist input file
creation, file validation, and running models in ParFlow.

## Steps to build, validate, and run ParFlow input script

1. Run the generator to load and generate the ParFlow
database structure as Python classes so IDE and runtime environment can
be used to query the help and constraints associated to each keys.
```
./run_generator.sh
```
2. Run the test on a demo file to test the validation tools
```
./run_test.sh default_richards.py
```
3. If the validation does not return any errors, ParFlow can be run with the following command:
```
./run_parflow.sh ./output/default_richards
```
Where './output/default_richards' is the name and location of the pfidb file. This assumes that the user's ParFlow
directory is set to $PARFLOW_DIR. 

## Folders:

### test

ParFlow input files written in Python used for testing the validation code. This folder also has the scripts that can be
used to change the format of files (e.g. pfidb -> yaml, tcl -> Python)

### parflow

Python scripts and yaml files to build the structure to load and generate the Python library of ParFlow keys.

### output

Outputs that are written from the Python ParFlow scripts. These include the yaml, json, and pfidb files.
