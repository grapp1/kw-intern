# Landlab: model for earth system processes

http://landlab.github.io/#/

Landlab components = pftools

## Input deck
Working through various tutorial jupyter notebooks in
https://github.com/landlab/landlab/tree/master/notebooks/tutorials

Just a few that I went through:
- landlab-fault-scarp.ipynb
- boundary_conds/set_BCs_on_raster_perimeter.ipynb
- component_tutorial/component_tutorial.ipynb
- gradient_and_divergence/gradient_and_divergence.ipynb

### What is nice
- Helpful tutorials in the form of jupyter notebooks.
- Standard interface for components. This makes it easier to work with different
components.
- Allows for loading parameters with a YAML file
- Fully contained within python
- Can work with irregular grids

### What is not nice
- Not as "standardized" as ParFlow, i.e. every version of the model looks very
different.
- Less readable than ParFlow's tcl scripts
- Boundary condition specification is a little confusing. However, it is more
straightforward than developing a solid file.
- Manual mapping of data (slopes)
