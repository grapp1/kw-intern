# 20201028 documentation on CLM working

Tools to interface with CLM files in a script using Python-PFTools

## Reading files

### ``read_clm(file_name, type='clmin')`` (Located in io.py)

This reads any of the three CLM input files:

1. ``type='clmin'``: reads the main CLM input file (drv_clmin.dat) and returns a dictionary 
with all the CLM variables as keys and their values.

2. ``type='vegm'``: reads the CLM vegetation mapping file (drv_vegm.dat) and returns a 3D
array where the x/y dimensions are the dimensions of the domain grid, and the z dimension
corresponds to the amount of parameters in the file (=23 for the default 18 land use types).

3. ``type='vegp'``: reads the CLM vegetation parameter file (drv_vegp.dat) and returns a dictionary 
with all the vegetation parameter variables as keys and a list of the parameter values corresponding
to each land cover type.

### ``set_clm_keys(clm_key_dict)`` (Located in database/core.py)

This will set the corresponding ParFlow keys from the dictionary of CLM variables and values. This 
filters out variables that are deprecated or missing from the ParFlow key database.

### ``VegParamBuilder`` class (Located in builders.py)

This class allows for setting vegetation parameters from a table, similar to the 
``SubsurfacePropertiesBuilder``. The ``load_default_properties()`` method currently
loads the default IGBP vegetation parameter data.

### ``CLMExporter`` class (Located in export.py)

This class will export data or keys to any of the three main CLM input files.

1. ``.export_drv_clmin(working_directory='.')``: writes out the main CLM input file (drv_clmin.dat)
from the corresponding key/value pairs set to the ``Run`` object.

2. ``.export_drv_vegm(from_keys=True, vegm_array=None,
                        out_file='drv_vegm.dat', working_directory='.', dec_round=3)``: writes out
   the CLM vegetation mapping file (drv_vegm.dat) from either a 3D array (``vegm_array`` argument)
   or from key/value pairs on the ``Run`` object (``from_keys=True``). This is still a work in progress
   given how many combinations of keys we need to accommodate.
   
3. ``.export_drv_vegp(vegp_data, working_directory='.')``: writes the CLM vegetation parameter file 
(drv_vegp.dat) from a dictionary ``vegp_data``. I have not updated this to generate the file without
the reference file as a guide. 

### Usage examples

Two tests show the range of usage of these new classes and methods (in test/python/new_features/):

[clm_file_handling.py](https://github.com/grapp1/parflow/blob/py_metadata/test/python/new_features/clm_file_handling.py)

[clm_veg_mapping.py](https://github.com/grapp1/parflow/blob/py_metadata/test/python/new_features/clm_veg_mapping.py)