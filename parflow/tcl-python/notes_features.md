## notes on potential ParFlow improvements


1. Increasing the information provided in error messages
  - have Python read input file to make sure that no keys are missing, point output
    unused keys, make sure that it will run, and maybe help debug outputs
  - Adapt this to commonly coupled models (CLM, EcoSLIM, NetCDF) to make sure that
    ParFlow outputs are suited for use in another model

2. Making it easier to input lists of data (e.g. permeability properties for multiple areas)
  - Example: see LW_Test.tcl lines 110 through 150. It would be more efficient to
    be able to specify "Constant" for all the layers and be able to more easily
    copy/paste the values.
  - Still need to maintain flexibility

3. Group VariableDz information with domain Geometry

4. Instead of running ParFlow using "pfrun," we could use "pfwritedb"
  - Still need to better understand how this works.
  - .pfidb format:
    > line 1: number of key/value pairs in the ParFlow run
    > line 2: length of first key
    > line 3: first key
    > line 4: length of first key value
    > line 5: first key value
    > lines 2 through 5 repeated for all key/value pairs
