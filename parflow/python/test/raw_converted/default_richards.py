#  This runs the basic default_richards test case.
#  This run, as written in this input file, should take
#  3 nonlinear iterations.

#
# Import the ParFlow TCL package
#
from parflow import Run
default_richards = Run("default_richards", __file__)

default_richards.FileVersion = 4

default_richards.Process.Topology.P = [lindex $argv 0]
default_richards.Process.Topology.Q = [lindex $argv 1]
default_richards.Process.Topology.R = [lindex $argv 2]

#---------------------------------------------------------
# Computational Grid
#---------------------------------------------------------
default_richards.ComputationalGrid.Lower.X = -10.0
default_richards.ComputationalGrid.Lower.Y = 10.0
default_richards.ComputationalGrid.Lower.Z = 1.0

default_richards.ComputationalGrid.DX = 8.8888888888888893
default_richards.ComputationalGrid.DY = 10.666666666666666
default_richards.ComputationalGrid.DZ = 1.0

default_richards.ComputationalGrid.NX = 10
default_richards.ComputationalGrid.NY = 10
default_richards.ComputationalGrid.NZ = 8

#---------------------------------------------------------
# The Names of the GeomInputs
#---------------------------------------------------------
default_richards.GeomInput.Names = 'domain_input background_input source_region_input \'
# 		       concen_region_input"


#---------------------------------------------------------
# Domain Geometry Input
#---------------------------------------------------------
default_richards.GeomInput.domain_input.InputType = 'Box'
default_richards.GeomInput.domain_input.GeomName = 'domain'

#---------------------------------------------------------
# Domain Geometry
#---------------------------------------------------------
default_richards.Geom.domain.Lower.X = -10.0
default_richards.Geom.domain.Lower.Y = 10.0
default_richards.Geom.domain.Lower.Z = 1.0

default_richards.Geom.domain.Upper.X = 150.0
default_richards.Geom.domain.Upper.Y = 170.0
default_richards.Geom.domain.Upper.Z = 9.0

default_richards.Geom.domain.Patches = 'left right front back bottom top'

#---------------------------------------------------------
# Background Geometry Input
#---------------------------------------------------------
default_richards.GeomInput.background_input.InputType = 'Box'
default_richards.GeomInput.background_input.GeomName = 'background'

#---------------------------------------------------------
# Background Geometry
#---------------------------------------------------------
default_richards.Geom.background.Lower.X = -99999999.0
default_richards.Geom.background.Lower.Y = -99999999.0
default_richards.Geom.background.Lower.Z = -99999999.0

default_richards.Geom.background.Upper.X = 99999999.0
default_richards.Geom.background.Upper.Y = 99999999.0
default_richards.Geom.background.Upper.Z = 99999999.0


#---------------------------------------------------------
# Source_Region Geometry Input
#---------------------------------------------------------
default_richards.GeomInput.source_region_input.InputType = 'Box'
default_richards.GeomInput.source_region_input.GeomName = 'source_region'

#---------------------------------------------------------
# Source_Region Geometry
#---------------------------------------------------------
default_richards.Geom.source_region.Lower.X = 65.56
default_richards.Geom.source_region.Lower.Y = 79.34
default_richards.Geom.source_region.Lower.Z = 4.5

default_richards.Geom.source_region.Upper.X = 74.44
default_richards.Geom.source_region.Upper.Y = 89.99
default_richards.Geom.source_region.Upper.Z = 5.5


#---------------------------------------------------------
# Concen_Region Geometry Input
#---------------------------------------------------------
default_richards.GeomInput.concen_region_input.InputType = 'Box'
default_richards.GeomInput.concen_region_input.GeomName = 'concen_region'

#---------------------------------------------------------
# Concen_Region Geometry
#---------------------------------------------------------
default_richards.Geom.concen_region.Lower.X = 60.0
default_richards.Geom.concen_region.Lower.Y = 80.0
default_richards.Geom.concen_region.Lower.Z = 4.0

default_richards.Geom.concen_region.Upper.X = 80.0
default_richards.Geom.concen_region.Upper.Y = 100.0
default_richards.Geom.concen_region.Upper.Z = 6.0

#-----------------------------------------------------------------------------
# Perm
#-----------------------------------------------------------------------------
default_richards.Geom.Perm.Names = 'background'

default_richards.Geom.background.Perm.Type = 'Constant'
default_richards.Geom.background.Perm.Value = 4.0

default_richards.Perm.TensorType = 'TensorByGeom'

default_richards.Geom.Perm.TensorByGeom.Names = 'background'

default_richards.Geom.background.Perm.TensorValX = 1.0
default_richards.Geom.background.Perm.TensorValY = 1.0
default_richards.Geom.background.Perm.TensorValZ = 1.0

#-----------------------------------------------------------------------------
# Specific Storage
#-----------------------------------------------------------------------------

default_richards.SpecificStorage.Type = 'Constant'
default_richards.SpecificStorage.GeomNames = 'domain'
default_richards.Geom.domain.SpecificStorage.Value = 1.0e-4

#-----------------------------------------------------------------------------
# Phases
#-----------------------------------------------------------------------------

default_richards.Phase.Names = 'water'

default_richards.Phase.water.Density.Type = 'Constant'
default_richards.Phase.water.Density.Value = 1.0

default_richards.Phase.water.Viscosity.Type = 'Constant'
default_richards.Phase.water.Viscosity.Value = 1.0

#-----------------------------------------------------------------------------
# Contaminants
#-----------------------------------------------------------------------------
default_richards.Contaminants.Names = ''

#-----------------------------------------------------------------------------
# Retardation
#-----------------------------------------------------------------------------
default_richards.Geom.Retardation.GeomNames = ''

#-----------------------------------------------------------------------------
# Gravity
#-----------------------------------------------------------------------------

default_richards.Gravity = 1.0

#-----------------------------------------------------------------------------
# Setup timing info
#-----------------------------------------------------------------------------

default_richards.TimingInfo.BaseUnit = 1.0
default_richards.TimingInfo.StartCount = 0
default_richards.TimingInfo.StartTime = 0.0
default_richards.TimingInfo.StopTime = 0.010
default_richards.TimingInfo.DumpInterval = -1
default_richards.TimeStep.Type = 'Constant'
default_richards.TimeStep.Value = 0.001

#-----------------------------------------------------------------------------
# Porosity
#-----------------------------------------------------------------------------

default_richards.Geom.Porosity.GeomNames = 'background'

default_richards.Geom.background.Porosity.Type = 'Constant'
default_richards.Geom.background.Porosity.Value = 1.0

#-----------------------------------------------------------------------------
# Domain
#-----------------------------------------------------------------------------
default_richards.Domain.GeomName = 'domain'

#-----------------------------------------------------------------------------
# Relative Permeability
#-----------------------------------------------------------------------------

default_richards.Phase.RelPerm.Type = 'VanGenuchten'
default_richards.Phase.RelPerm.GeomNames = 'domain'
default_richards.Geom.domain.RelPerm.Alpha = 0.005
default_richards.Geom.domain.RelPerm.N = 2.0

#---------------------------------------------------------
# Saturation
#---------------------------------------------------------

default_richards.Phase.Saturation.Type = 'VanGenuchten'
default_richards.Phase.Saturation.GeomNames = 'domain'
default_richards.Geom.domain.Saturation.Alpha = 0.005
default_richards.Geom.domain.Saturation.N = 2.0
default_richards.Geom.domain.Saturation.SRes = 0.2
default_richards.Geom.domain.Saturation.SSat = 0.99

#-----------------------------------------------------------------------------
# Wells
#-----------------------------------------------------------------------------
default_richards.Wells.Names = ''

#-----------------------------------------------------------------------------
# Time Cycles
#-----------------------------------------------------------------------------
default_richards.Cycle.Names = 'constant'
default_richards.Cycle.constant.Names = 'alltime'
default_richards.Cycle.constant.alltime.Length = 1
default_richards.Cycle.constant.Repeat = -1

#-----------------------------------------------------------------------------
# Boundary Conditions: Pressure
#-----------------------------------------------------------------------------
default_richards.BCPressure.PatchNames = 'left right front back bottom top'

default_richards.Patch.left.BCPressure.Type = 'DirEquilRefPatch'
default_richards.Patch.left.BCPressure.Cycle = 'constant'
default_richards.Patch.left.BCPressure.RefGeom = 'domain'
default_richards.Patch.left.BCPressure.RefPatch = 'bottom'
default_richards.Patch.left.BCPressure.alltime.Value = 5.0

default_richards.Patch.right.BCPressure.Type = 'DirEquilRefPatch'
default_richards.Patch.right.BCPressure.Cycle = 'constant'
default_richards.Patch.right.BCPressure.RefGeom = 'domain'
default_richards.Patch.right.BCPressure.RefPatch = 'bottom'
default_richards.Patch.right.BCPressure.alltime.Value = 3.0

default_richards.Patch.front.BCPressure.Type = 'FluxConst'
default_richards.Patch.front.BCPressure.Cycle = 'constant'
default_richards.Patch.front.BCPressure.alltime.Value = 0.0

default_richards.Patch.back.BCPressure.Type = 'FluxConst'
default_richards.Patch.back.BCPressure.Cycle = 'constant'
default_richards.Patch.back.BCPressure.alltime.Value = 0.0

default_richards.Patch.bottom.BCPressure.Type = 'FluxConst'
default_richards.Patch.bottom.BCPressure.Cycle = 'constant'
default_richards.Patch.bottom.BCPressure.alltime.Value = 0.0

default_richards.Patch.top.BCPressure.Type = 'FluxConst'
default_richards.Patch.top.BCPressure.Cycle = 'constant'
default_richards.Patch.top.BCPressure.alltime.Value = 0.0

#---------------------------------------------------------
# Topo slopes in x-direction
#---------------------------------------------------------

default_richards.TopoSlopesX.Type = 'Constant'
default_richards.TopoSlopesX.GeomNames = ''

default_richards.TopoSlopesX.Geom.domain.Value = 0.0

#---------------------------------------------------------
# Topo slopes in y-direction
#---------------------------------------------------------

default_richards.TopoSlopesY.Type = 'Constant'
default_richards.TopoSlopesY.GeomNames = ''

default_richards.TopoSlopesY.Geom.domain.Value = 0.0

#---------------------------------------------------------
# Mannings coefficient 
#---------------------------------------------------------

default_richards.Mannings.Type = 'Constant'
default_richards.Mannings.GeomNames = ''
default_richards.Mannings.Geom.domain.Value = 0.

#---------------------------------------------------------
# Initial conditions: water pressure
#---------------------------------------------------------

default_richards.ICPressure.Type = 'HydroStaticPatch'
default_richards.ICPressure.GeomNames = 'domain'
default_richards.Geom.domain.ICPressure.Value = 3.0
default_richards.Geom.domain.ICPressure.RefGeom = 'domain'
default_richards.Geom.domain.ICPressure.RefPatch = 'bottom'

#-----------------------------------------------------------------------------
# Phase sources:
#-----------------------------------------------------------------------------

default_richards.PhaseSources.water.Type = 'Constant'
default_richards.PhaseSources.water.GeomNames = 'background'
default_richards.PhaseSources.water.Geom.background.Value = 0.0


#-----------------------------------------------------------------------------
# Exact solution specification for error calculations
#-----------------------------------------------------------------------------

default_richards.KnownSolution = 'NoKnownSolution'


#-----------------------------------------------------------------------------
# Set solver parameters
#-----------------------------------------------------------------------------
default_richards.Solver = 'Richards'
default_richards.Solver.MaxIter = 5

default_richards.Solver.Nonlinear.MaxIter = 10
default_richards.Solver.Nonlinear.ResidualTol = 1e-9
default_richards.Solver.Nonlinear.EtaChoice = 'EtaConstant'
default_richards.Solver.Nonlinear.EtaValue = 1e-5
default_richards.Solver.Nonlinear.UseJacobian = True
default_richards.Solver.Nonlinear.DerivativeEpsilon = 1e-2

default_richards.Solver.Linear.KrylovDimension = 10

default_richards.Solver.Linear.Preconditioner = 'PFMG'
default_richards.Solver.Linear.Preconditioner.MGSemi.MaxIter = 1
default_richards.Solver.Linear.Preconditioner.MGSemi.MaxLevels = 100

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


# if $passed {
#     puts "default_richards : PASSED"
# } {
#     puts "default_richards : FAILED"
# }
default_richards.run()
