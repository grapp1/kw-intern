# tcl-python

Collection of scripts and notes for converting ParFlow tcl scripts to Python

## examples

Examples of existing tcl scripts with the associated Python conversions.

#### sandtank

Converting the sandtank run.tcl (and config.tcl) script to Python. This includes multiple ideas of ways to interface with ParFlow, including converting the TCL file to a YAML file, setting the key/value pairs in Python itself, and some combination of the two.

#### washita

Converting the Little Washita LW_Test.tcl  script to Python. This includes multiple ideas of ways to interface with ParFlow, including converting the TCL file to a YAML file, setting the key/value pairs in Python itself, and some combination of the two.

This also includes two scripts:
  1) yaml-to-pfidb.py: convert a YAML file to a .pfidb file
  2) read a csv file of geologic parameters and convert it to a series of nested dictionaries mimicking the ParFlow key/value pairs
  
## schemas

This includes several scripts showing ways to develop the schemas and structure of ParFlow input files in Python. Several examples include:

- schema_v1.py: ParFlow class definition that builds schema using DotMap
- schema_v2.py: ParFlow class that imports yaml file with defined dictionary structure, with class (PFDict) that enables autocomplete
- schema_v3.py: ParFlow class that defines each key in ParFlow as a separate class. This enables autocompletion in the terminal and the script editor (PyCharm).
- implementation.py: This includes examples implementing all three example schemas.
