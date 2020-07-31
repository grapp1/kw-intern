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

  p = pv.Plotter()
  p.add_mesh(grid, show_edges=True, color='white')
  # Now plot the grid!
  # grid.plot(show_edges=True, show_axes=True, text=plot_text)
  p.show()


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

# # testing different configurations
#
# nx = 10
# ny = 10
# nz = 5
# lower_x = 0.0
# lower_y = 0.0
# lower_z = 0.0
# dx = 2
# dy = 2
# dz = 1
#
#
# values = np.linspace(0, 10, nx * ny * nz).reshape((nx, ny, nz))
# values.shape
#
# grid = pv.UniformGrid()
# grid.dimensions = np.array(values.shape) + 1
# grid.origin = (lower_x, lower_y, lower_z)
# grid.spacing = (dx, dy, dz)
# grid.cell_arrays["values"] = 1
#
# sub_nx = 5
# sub_ny = 5
# sub_nz = 5
# sub_values = np.linspace(0, 10, sub_nx * sub_ny * sub_nz).reshape((sub_nx, sub_ny, sub_nz))
# sub_values.shape
#
# # Create the spatial reference
# subgrid = pv.UniformGrid()
#
# # Set the grid dimensions: shape + 1 because we want to inject our values on
# #   the CELL data
# subgrid.dimensions = np.array(sub_values.shape) + 1
#
# # Edit the spatial reference
# subgrid.origin = (lower_x, lower_y, lower_z)  # The bottom left corner of the data set
# subgrid.spacing = (dx, dy, dz)  # These are the cell sizes along each axis
#
# # Add the data values to the cell data
# # grid.cell_arrays["values"] = values.flatten(order="F")  # Flatten the array!
# subgrid.cell_arrays["values"] = 1
# print(subgrid.cell_arrays["values"].shape)
#
# p = pv.Plotter()
# p.add_mesh(grid, style='wireframe', show_edges=True, color='black')
# p.add_mesh(subgrid, show_edges=True, color='red')
# # Now plot the grid!
# # grid.plot(show_edges=True, show_axes=True, text=plot_text)
# p.show()