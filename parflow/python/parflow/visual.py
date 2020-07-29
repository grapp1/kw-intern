# adding visualization features

import numpy as np
import pyvista as pv
from .database.generated import BaseRun, PFDBObj
from .core import Run

def plotUniformGrid(lower_x, lower_y, lower_z, dx, dy, dz, nx, ny, nz, plot_text):
  values = np.linspace(0, 10, nx * ny * nz).reshape((nx, ny, nz))
  values.shape

  # Create the spatial reference
  grid = pv.UniformGrid()

  # Set the grid dimensions: shape + 1 because we want to inject our values on
  #   the CELL data
  grid.dimensions = np.array(values.shape) + 1

  # Edit the spatial reference
  grid.origin = (lower_x, lower_y, lower_z)  # The bottom left corner of the data set
  grid.spacing = (dx, dy, dz)  # These are the cell sizes along each axis

  # Add the data values to the cell data
  # grid.cell_arrays["values"] = values.flatten(order="F")  # Flatten the array!
  grid.cell_arrays["values"] = 1
  print(grid.cell_arrays["values"].shape)

  # Now plot the grid!
  grid.plot(show_edges=True, show_axes=True, text=plot_text)


class Visual(BaseRun):
  def __init__(self, name):
    super().__init__(None)
    self._name = name

  def plotCompGrid(self):
    keyDict = self.getKeyDict()

    lower_x = keyDict['ComputationalGrid.Lower.X']
    lower_y = keyDict['ComputationalGrid.Lower.Y']
    lower_z = keyDict['ComputationalGrid.Lower.Z']

    dx = keyDict['ComputationalGrid.DX']
    dy = keyDict['ComputationalGrid.DY']
    dz = keyDict['ComputationalGrid.DZ']

    nx = keyDict['ComputationalGrid.NX']
    ny = keyDict['ComputationalGrid.NY']
    nz = keyDict['ComputationalGrid.NZ']

    plotUniformGrid(lower_x, lower_y, lower_z, dx, dy, dz, nx, ny, nz, 'Computational Grid')

  def plotDomGrid(self, domain='domain'):
    keyDict = self.getKeyDict()

    lower_x = keyDict['Geom.' + domain + '.Lower.X']
    lower_y = keyDict['Geom.' + domain + '.Lower.Y']
    lower_z = keyDict['Geom.' + domain + '.Lower.Z']

    dx = keyDict['ComputationalGrid.DX']
    dy = keyDict['ComputationalGrid.DY']
    dz = keyDict['ComputationalGrid.DZ']

    upper_x = keyDict['Geom.' + domain + '.Upper.X']
    upper_y = keyDict['Geom.' + domain + '.Upper.Y']
    upper_z = keyDict['Geom.' + domain + '.Upper.Z']

    nx = int(upper_x / dx)
    ny = int(upper_y / dy)
    nz = int(upper_z / dz)

    plotUniformGrid(lower_x, lower_y, lower_z, dx, dy, dz, nx, ny, nz, domain)