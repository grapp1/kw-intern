Notes on potential ParFlow input improvements

1. Increasing the information provided in error messages
  - have Python read input file to make sure that no keys are missing, point output
    unused keys, make sure that it will run, and maybe help debug outputs
  - Adapt this to commonly coupled models (CLM, EcoSLIM, NetCDF) to make sure that
    ParFlow outputs are suited for use in another model
    - For example: you need outputs of velocity, pressure, saturation, and ET for
      EcoSLIM.

2. Making it easier to input lists of data (e.g. geologic properties, multiple wells)
  - Make it possible to read in a file that has all geologic data for the layers
    (perhaps tab-delimited text file) and will automatically generate the key/value pairs
  - Potential formatting for headers:

    Indicator   Perm  Porosity  RelPerm_Alpha RelPerm_N Sat_Alpha Sat_N Sat_SRes  Sat_SSat
    domain      0.2   0.4       3.5           2.0       3.5       2.0   0.2       1.0
    1           0.269 0.375     3.548         4.162     3.548     4.162 0.000001  1.0

  - This would only work well for constant properties since turning bands have many more
    parameters that would not be conducive to this approach.
  - See LW_Test.tcl lines 110 through 150 - it would be more efficient to
    be able to specify "Constant" for all the layers and be able to more easily
    copy/paste the values.
  - Still need to maintain flexibility, so inputting data in this way should be optional

3. Have a small existing database for common geologic properties that could be referenced
  in the input file. Perhaps we pull from some standard text (e.g. Freeze and Cherry) to
  populate it. This would help those modeling in regions that lack data or are developing
  models that may be less sensitive to these properties.
  - The same idea could apply to the CLM parameters (e.g. field capacity, wilting point)

4. Group VariableDz information with domain Geometry

5. Instead of running ParFlow using "pfrun," we could use "pfwritedb"
  - Still need to better understand how this works.
  - .pfidb format:
    > line 1: number of key/value pairs in the ParFlow run
    > line 2: length of first key
    > line 3: first key
    > line 4: length of first key value
    > line 5: first key value
    > lines 2 through 5 repeated for all key/value pairs

6. Develop straightforward way to generate and run ensemble of models
  - Could have file with series of run names and parameters you want to change
  - Immediately show chart with input variables for all runs

7. Build some tools to suit frequently implemented workflows (e.g. spinup)
  - Example: set parameters to evaluate water table convergence, leveraging pftools

8. Would there be a way to assist the building of runs that are implemented on
  HPCs? Such as running brief tests to find the most efficient topology or find
  bottlenecks in the run?

9. Have the option of specifying "water" to populate the default values for the
  Phase keys. It's rare that users will want to deviate from the defaults here,
  at least in my experience.

10. Have default sets of solver parameters based on different types of runs? E.g.
  spinning up a model will likely require a different set of solver parameters than
  a more precisely calibrated run. This could assist users who are less familiar
  with the solver parameters.
