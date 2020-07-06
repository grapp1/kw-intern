# ParFlow/python

This directory includes our work to develop python tools to assist input file
creation and validation in ParFlow.

## Steps to run validation test on ParFlow input script

1. Run the generator to load and generate the ParFlow
database structure as Python classes so IDE and runtime environment can
be used to query the help and constraints associated to each keys.
```
./run_generator.sh
```
2. Run the test on a demo file to test the validation tools
```
./run_test.sh demo1.py
```

## Folders:

### test

ParFlow input files written in python used for testing the validation code

### parflow

Python scripts and yaml files to build the structure to load and generate ParFlow

### output

For now, just a .gitignore file.
