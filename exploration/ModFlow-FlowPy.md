# Notes on MODFLOW and Flopy implementation, and thoughts on application of features to ParFlow

Links to references:

https://github.com/groundwater-modeling-Spring2020/Course_Materials
https://www.hatarilabs.com/ih-en/regional-groundwater-modeling-with-modflow-and-flopy-tutorial

## Input deck
- Worked through several of the HW problems from course materials above, read
through Hatari tutorial.

### What is nice
- Requires fewer lines than ParFlow to build and run a model
- Better integration with visualization
- Better integration with ModPath (we could apply the same idea to EcoSLIM)
- Solver choice has fewer components (and thus, simpler and less customizable)
- Calling the MODFLOW packages individually helps with identifying errors
- Easier than ParFlow to build ensembles

### What is not nice
- Having to call different MODFLOW packages individually makes the code messier
- Overall, code is generally less readable
