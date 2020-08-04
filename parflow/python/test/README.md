# ParFlow/python/test

This directory contains tools for testing Python scripts and examples of the ParFlow
test files converted to Python.

## Files:

 - batch_test.py: batch testing Python files.
 - clear.py: clearing output files from example directories.
 - pfidbToYaml: converting pfidb files to a more readable yaml file for debugging
 - tclToPython: converting the TCL format to Python format. The conversion does a
    pretty good job, but you'll have to manually edit parts of the resulting Python scripts.
 - writePfidbForComparison.py: Takes two input .pfidb files and writes them to sorted yaml files
    so their keys and values can be compared.

## Folders:

### comparison

This

### examples

Python scripts and yaml files to build the structure to load and generate the Python library of ParFlow keys.

### jupyter_notebook

Jupyter notebook testing of Python scripts.

### tcl_original

Copies of the original ParFlow test files in TCL format (from ParFlow v3.6.0)