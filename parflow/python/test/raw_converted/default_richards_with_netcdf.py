#  This runs the basic default_richards test case.
#  This run, as written in this input file, should take
#  3 nonlinear iterations.

#
# Import the ParFlow TCL package
#
from parflow import Run
default_richards_with_netcdf = Run("default_richards_with_netcdf", __file__)

# Examples of compression options for SILO
# Note compression only works for HDF5
#pfset SILO.Filetype "HDF5"
#pfset SILO.CompressionOptions "METHOD=GZIP"
#pfset SILO.CompressionOptions "METHOD=SZIP"
#pfset SILO.CompressionOptions "METHOD=FPZIP"
#pfset SILO.CompressionOptions "ERRMODE=FALLBACK METHOD=GZIP"

default_richards_with_netcdf.FileVersion = 4

default_richards_with_netcdf.Process.Topology.P = 1
default_richards_with_netcdf.Process.Topology.Q = 1
default_richards_with_netcdf.Process.Topology.R = 1

#---------------------------------------------------------
# Computational Grid
#---------------------------------------------------------
default_richards_with_netcdf.ComputationalGrid.Lower.X = -10.0
default_richards_with_netcdf.ComputationalGrid.Lower.Y = 10.0
default_richards_with_netcdf.ComputationalGrid.Lower.Z = 1.0

default_richards_with_netcdf.ComputationalGrid.DX = 8.8888888888888893
default_richards_with_netcdf.ComputationalGrid.DY = 10.666666666666666
default_richards_with_netcdf.ComputationalGrid.DZ = 1.0

default_richards_with_netcdf.ComputationalGrid.NX = 10
default_richards_with_netcdf.ComputationalGrid.NY = 10
default_richards_with_netcdf.ComputationalGrid.NZ = 8

#---------------------------------------------------------
# The Names of the GeomInputs
#---------------------------------------------------------
default_richards_with_netcdf.GeomInput.Names = 'domain_input background_input source_region_input \'
# 		       concen_region_input"


#---------------------------------------------------------
# Domain Geometry Input
#---------------------------------------------------------
default_richards_with_netcdf.GeomInput.domain_input.InputType = 'Box'
default_richards_with_netcdf.GeomInput.domain_input.GeomName = 'domain'

#---------------------------------------------------------
# Domain Geometry
#---------------------------------------------------------
default_richards_with_netcdf.Geom.domain.Lower.X = -10.0
default_richards_with_netcdf.Geom.domain.Lower.Y = 10.0
default_richards_with_netcdf.Geom.domain.Lower.Z = 1.0

default_richards_with_netcdf.Geom.domain.Upper.X = 150.0
default_richards_with_netcdf.Geom.domain.Upper.Y = 170.0
default_richards_with_netcdf.Geom.domain.Upper.Z = 9.0

default_richards_with_netcdf.Geom.domain.Patches = 'left right front back bottom top'

#---------------------------------------------------------
# Background Geometry Input
#---------------------------------------------------------
default_richards_with_netcdf.GeomInput.background_input.InputType = 'Box'
default_richards_with_netcdf.GeomInput.background_input.GeomName = 'background'

#---------------------------------------------------------
# Background Geometry
#---------------------------------------------------------
default_richards_with_netcdf.Geom.background.Lower.X = -99999999.0
default_richards_with_netcdf.Geom.background.Lower.Y = -99999999.0
default_richards_with_netcdf.Geom.background.Lower.Z = -99999999.0

default_richards_with_netcdf.Geom.background.Upper.X = 99999999.0
default_richards_with_netcdf.Geom.background.Upper.Y = 99999999.0
default_richards_with_netcdf.Geom.background.Upper.Z = 99999999.0


#---------------------------------------------------------
# Source_Region Geometry Input
#---------------------------------------------------------
default_richards_with_netcdf.GeomInput.source_region_input.InputType = 'Box'
default_richards_with_netcdf.GeomInput.source_region_input.GeomName = 'source_region'

#---------------------------------------------------------
# Source_Region Geometry
#---------------------------------------------------------
default_richards_with_netcdf.Geom.source_region.Lower.X = 65.56
default_richards_with_netcdf.Geom.source_region.Lower.Y = 79.34
default_richards_with_netcdf.Geom.source_region.Lower.Z = 4.5

default_richards_with_netcdf.Geom.source_region.Upper.X = 74.44
default_richards_with_netcdf.Geom.source_region.Upper.Y = 89.99
default_richards_with_netcdf.Geom.source_region.Upper.Z = 5.5


#---------------------------------------------------------
# Concen_Region Geometry Input
#---------------------------------------------------------
default_richards_with_netcdf.GeomInput.concen_region_input.InputType = 'Box'
default_richards_with_netcdf.GeomInput.concen_region_input.GeomName = 'concen_region'

#---------------------------------------------------------
# Concen_Region Geometry
#---------------------------------------------------------
default_richards_with_netcdf.Geom.concen_region.Lower.X = 60.0
default_richards_with_netcdf.Geom.concen_region.Lower.Y = 80.0
default_richards_with_netcdf.Geom.concen_region.Lower.Z = 4.0

default_richards_with_netcdf.Geom.concen_region.Upper.X = 80.0
default_richards_with_netcdf.Geom.concen_region.Upper.Y = 100.0
default_richards_with_netcdf.Geom.concen_region.Upper.Z = 6.0

#-----------------------------------------------------------------------------
# Perm
#-----------------------------------------------------------------------------
default_richards_with_netcdf.Geom.Perm.Names = 'background'

default_richards_with_netcdf.Geom.background.Perm.Type = 'Constant'
default_richards_with_netcdf.Geom.background.Perm.Value = 4.0

default_richards_with_netcdf.Perm.TensorType = 'TensorByGeom'

default_richards_with_netcdf.Geom.Perm.TensorByGeom.Names = 'background'

default_richards_with_netcdf.Geom.background.Perm.TensorValX = 1.0
default_richards_with_netcdf.Geom.background.Perm.TensorValY = 1.0
default_richards_with_netcdf.Geom.background.Perm.TensorValZ = 1.0

#-----------------------------------------------------------------------------
# Specific Storage
#-----------------------------------------------------------------------------

default_richards_with_netcdf.SpecificStorage.Type = 'Constant'
default_richards_with_netcdf.SpecificStorage.GeomNames = 'domain'
default_richards_with_netcdf.Geom.domain.SpecificStorage.Value = 1.0e-4

#-----------------------------------------------------------------------------
# Phases
#-----------------------------------------------------------------------------

default_richards_with_netcdf.Phase.Names = 'water'

default_richards_with_netcdf.Phase.water.Density.Type = 'Constant'
default_richards_with_netcdf.Phase.water.Density.Value = 1.0

default_richards_with_netcdf.Phase.water.Viscosity.Type = 'Constant'
default_richards_with_netcdf.Phase.water.Viscosity.Value = 1.0

#-----------------------------------------------------------------------------
# Contaminants
#-----------------------------------------------------------------------------
default_richards_with_netcdf.Contaminants.Names = ''

#-----------------------------------------------------------------------------
# Retardation
#-----------------------------------------------------------------------------
default_richards_with_netcdf.Geom.Retardation.GeomNames = ''

#-----------------------------------------------------------------------------
# Gravity
#-----------------------------------------------------------------------------

default_richards_with_netcdf.Gravity = 1.0

#-----------------------------------------------------------------------------
# Setup timing info
#-----------------------------------------------------------------------------

default_richards_with_netcdf.TimingInfo.BaseUnit = 1.0
default_richards_with_netcdf.TimingInfo.StartCount = 0
default_richards_with_netcdf.TimingInfo.StartTime = 0.0
default_richards_with_netcdf.TimingInfo.StopTime = 0.010
default_richards_with_netcdf.TimingInfo.DumpInterval = -1
default_richards_with_netcdf.TimeStep.Type = 'Constant'
default_richards_with_netcdf.TimeStep.Value = 0.001

#-----------------------------------------------------------------------------
# Porosity
#-----------------------------------------------------------------------------

default_richards_with_netcdf.Geom.Porosity.GeomNames = 'background'

default_richards_with_netcdf.Geom.background.Porosity.Type = 'Constant'
default_richards_with_netcdf.Geom.background.Porosity.Value = 1.0

#-----------------------------------------------------------------------------
# Domain
#-----------------------------------------------------------------------------
default_richards_with_netcdf.Domain.GeomName = 'domain'

#-----------------------------------------------------------------------------
# Relative Permeability
#-----------------------------------------------------------------------------

default_richards_with_netcdf.Phase.RelPerm.Type = 'VanGenuchten'
default_richards_with_netcdf.Phase.RelPerm.GeomNames = 'domain'
default_richards_with_netcdf.Geom.domain.RelPerm.Alpha = 0.005
default_richards_with_netcdf.Geom.domain.RelPerm.N = 2.0

#---------------------------------------------------------
# Saturation
#---------------------------------------------------------

default_richards_with_netcdf.Phase.Saturation.Type = 'VanGenuchten'
default_richards_with_netcdf.Phase.Saturation.GeomNames = 'domain'
default_richards_with_netcdf.Geom.domain.Saturation.Alpha = 0.005
default_richards_with_netcdf.Geom.domain.Saturation.N = 2.0
default_richards_with_netcdf.Geom.domain.Saturation.SRes = 0.2
default_richards_with_netcdf.Geom.domain.Saturation.SSat = 0.99

#-----------------------------------------------------------------------------
# Wells
#-----------------------------------------------------------------------------
default_richards_with_netcdf.Wells.Names = ''

#-----------------------------------------------------------------------------
# Time Cycles
#-----------------------------------------------------------------------------
default_richards_with_netcdf.Cycle.Names = 'constant'
default_richards_with_netcdf.Cycle.constant.Names = 'alltime'
default_richards_with_netcdf.Cycle.constant.alltime.Length = 1
default_richards_with_netcdf.Cycle.constant.Repeat = -1

#-----------------------------------------------------------------------------
# Boundary Conditions: Pressure
#-----------------------------------------------------------------------------
default_richards_with_netcdf.BCPressure.PatchNames = 'left right front back bottom top'

default_richards_with_netcdf.Patch.left.BCPressure.Type = 'DirEquilRefPatch'
default_richards_with_netcdf.Patch.left.BCPressure.Cycle = 'constant'
default_richards_with_netcdf.Patch.left.BCPressure.RefGeom = 'domain'
default_richards_with_netcdf.Patch.left.BCPressure.RefPatch = 'bottom'
default_richards_with_netcdf.Patch.left.BCPressure.alltime.Value = 5.0

default_richards_with_netcdf.Patch.right.BCPressure.Type = 'DirEquilRefPatch'
default_richards_with_netcdf.Patch.right.BCPressure.Cycle = 'constant'
default_richards_with_netcdf.Patch.right.BCPressure.RefGeom = 'domain'
default_richards_with_netcdf.Patch.right.BCPressure.RefPatch = 'bottom'
default_richards_with_netcdf.Patch.right.BCPressure.alltime.Value = 3.0

default_richards_with_netcdf.Patch.front.BCPressure.Type = 'FluxConst'
default_richards_with_netcdf.Patch.front.BCPressure.Cycle = 'constant'
default_richards_with_netcdf.Patch.front.BCPressure.alltime.Value = 0.0

default_richards_with_netcdf.Patch.back.BCPressure.Type = 'FluxConst'
default_richards_with_netcdf.Patch.back.BCPressure.Cycle = 'constant'
default_richards_with_netcdf.Patch.back.BCPressure.alltime.Value = 0.0

default_richards_with_netcdf.Patch.bottom.BCPressure.Type = 'FluxConst'
default_richards_with_netcdf.Patch.bottom.BCPressure.Cycle = 'constant'
default_richards_with_netcdf.Patch.bottom.BCPressure.alltime.Value = 0.0

default_richards_with_netcdf.Patch.top.BCPressure.Type = 'FluxConst'
default_richards_with_netcdf.Patch.top.BCPressure.Cycle = 'constant'
default_richards_with_netcdf.Patch.top.BCPressure.alltime.Value = 0.0

#---------------------------------------------------------
# Topo slopes in x-direction
#---------------------------------------------------------

default_richards_with_netcdf.TopoSlopesX.Type = 'Constant'
default_richards_with_netcdf.TopoSlopesX.GeomNames = ''

default_richards_with_netcdf.TopoSlopesX.Geom.domain.Value = 0.0

#---------------------------------------------------------
# Topo slopes in y-direction
#---------------------------------------------------------

default_richards_with_netcdf.TopoSlopesY.Type = 'Constant'
default_richards_with_netcdf.TopoSlopesY.GeomNames = ''

default_richards_with_netcdf.TopoSlopesY.Geom.domain.Value = 0.0

#---------------------------------------------------------
# Mannings coefficient 
#---------------------------------------------------------

default_richards_with_netcdf.Mannings.Type = 'Constant'
default_richards_with_netcdf.Mannings.GeomNames = ''
default_richards_with_netcdf.Mannings.Geom.domain.Value = 0.

#---------------------------------------------------------
# Initial conditions: water pressure
#---------------------------------------------------------

default_richards_with_netcdf.ICPressure.Type = 'HydroStaticPatch'
default_richards_with_netcdf.ICPressure.GeomNames = 'domain'
default_richards_with_netcdf.Geom.domain.ICPressure.Value = 3.0
default_richards_with_netcdf.Geom.domain.ICPressure.RefGeom = 'domain'
default_richards_with_netcdf.Geom.domain.ICPressure.RefPatch = 'bottom'

#-----------------------------------------------------------------------------
# Phase sources:
#-----------------------------------------------------------------------------

default_richards_with_netcdf.PhaseSources.water.Type = 'Constant'
default_richards_with_netcdf.PhaseSources.water.GeomNames = 'background'
default_richards_with_netcdf.PhaseSources.water.Geom.background.Value = 0.0


#-----------------------------------------------------------------------------
# Exact solution specification for error calculations
#-----------------------------------------------------------------------------

default_richards_with_netcdf.KnownSolution = 'NoKnownSolution'


#-----------------------------------------------------------------------------
# Set solver parameters
#-----------------------------------------------------------------------------
default_richards_with_netcdf.Solver = 'Richards'
default_richards_with_netcdf.Solver.MaxIter = 5

default_richards_with_netcdf.Solver.Nonlinear.MaxIter = 10
default_richards_with_netcdf.Solver.Nonlinear.ResidualTol = 1e-9
default_richards_with_netcdf.Solver.Nonlinear.EtaChoice = 'EtaConstant'
default_richards_with_netcdf.Solver.Nonlinear.EtaValue = 1e-5
default_richards_with_netcdf.Solver.Nonlinear.UseJacobian = True
default_richards_with_netcdf.Solver.Nonlinear.DerivativeEpsilon = 1e-2

default_richards_with_netcdf.Solver.Linear.KrylovDimension = 10

default_richards_with_netcdf.Solver.Linear.Preconditioner = 'PFMGOctree'
default_richards_with_netcdf.Solver.Linear.Preconditioner.MGSemi.MaxIter = 1
default_richards_with_netcdf.Solver.Linear.Preconditioner.MGSemi.MaxLevels = 100

default_richards_with_netcdf.NetCDF.NumStepsPerFile = 5
default_richards_with_netcdf.NetCDF.WritePressure = True
default_richards_with_netcdf.NetCDF.WriteSaturation = True

#-----------------------------------------------------------------------------
# Run and Unload the ParFlow output files
#-----------------------------------------------------------------------------
# pfrun default_richards
# pfundist default_richards

#
# Tests 
#
# source pftest.tcl
passed = 1

# if ![pftestFile default_richards.out.perm_x.pfb "Max difference in perm_x" $sig_digits] {
#     set passed 0
# }
# if ![pftestFile default_richards.out.perm_y.pfb "Max difference in perm_y" $sig_digits] {
#     set passed 0
# }
# if ![pftestFile default_richards.out.perm_z.pfb "Max difference in perm_z" $sig_digits] {
#     set passed 0
# }

# foreach i "00000 00001 00002 00003 00004 00005" {
#     if ![pftestFile default_richards.out.press.$i.pfb "Max difference in Pressure for timestep $i" $sig_digits] {
#     set passed 0
# }
#     if ![pftestFile default_richards.out.satur.$i.pfb "Max difference in Saturation for timestep $i" $sig_digits] {
#     set passed 0
# }
# }

#
# PFTOOLS doesn't support netcdf yet so just see if file was created.
#

# if ![file exists default_richards.out.00000.nc] {
#     puts "NetCDF file was not created"
#     set passed 0
# }

# if ![file exists default_richards.out.00001.nc] {
#     puts "NetCDF file was not created"
#     set passed 0
# }

# if $passed {
#     puts "default_richards_with_netcdf : PASSED"
# } {
#     puts "default_richards_with_netcdf : FAILED"
# }

default_richards_with_netcdf.run()
