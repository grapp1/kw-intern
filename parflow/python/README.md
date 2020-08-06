# ParFlow/python

This directory includes our work to develop python tools to assist input file
creation, file validation, and running models in ParFlow.

## Steps to build, validate, and run ParFlow input script

1. Set up your environment. This sets $PYTHONPATH, installs the necessary Python
dependencies, and sources the ParFlow environment file 
(see ~/kw-intern/parflow/scripts/02_parflow.sh).
```
. ./run_setup.sh
```

2. Run the generator to load and generate the ParFlow
database structure as Python classes so IDE and runtime environment can
be used to query the help and constraints associated to each keys.
```
./run_generator.sh
```
3. Build a Python script and run ParFlow. You can build a Python script as an
input deck for your ParFlow run and run it from the terminal as a Python script:
```
python3 /path/to/file/runname.py
```
As a default, this will write any outputs in the directory with the Python script.

## Folders:

### test

This folder includes useful files for testing the Python scripts and contains the ParFlow testing files converted
to Python. 

### parflow

Python scripts and yaml files to build the structure to load and generate the Python library of ParFlow keys. This
folder includes documentation on how to add a key to the Python ParFlow library.
