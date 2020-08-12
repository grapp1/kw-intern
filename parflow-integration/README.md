# kw-intern/parflow-integration

Setting up directories to eventually merge into the main ParFlow repo.

## doc

RST documentation set up through Sphinx, connected to readthedocs. 

## pf-keys

Includes the yaml files that contain the definitions of all the keys and the Python generator scripts that generate the 
Python library of ParFlow keys and the documentation. 

## pf-python

Includes the tools that make the Python-ParFlow interface work. These tools convert between Python script and the PF 
database (.pfidb) file, including a call to run ParFlow with the .pfidb file. 

## test

Includes scripts to test our Python-ParFlow interface. These consist of many of the tests from the main ParFlow test 
directory. 
