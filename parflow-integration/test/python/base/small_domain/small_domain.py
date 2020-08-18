size = 1
name = "small_domain"
#  This is a 2D sloped problem w/ time varying input and topography
#  it is used as a test of active/inactive efficiency
#
#    Reed Maxwell, 11/08
#      

#
# Import the ParFlow TCL package
#
from parflow import Run
small_domain = Run("small_domain", __file__)

small_domain.FileVersion = 4

small_domain.Process.Topology.P = 1
small_domain.Process.Topology.Q = 1
small_domain.Process.Topology.R = 1

#---------------------------------------------------------
# Computational Grid
#---------------------------------------------------------
small_domain.ComputationalGrid.Lower.X = 0.0
small_domain.ComputationalGrid.Lower.Y = 0.0
small_domain.ComputationalGrid.Lower.Z = 0.0

small_domain.ComputationalGrid.NX = [expr 100*$size]
small_domain.ComputationalGrid.NY = 1
small_domain.ComputationalGrid.NZ = [expr 100*$size]

UpperX = [expr 400*$size]
UpperY = 1.0
UpperZ = [expr 200*$size]

LowerX = [pfget ComputationalGrid.Lower.X]
LowerY = [pfget ComputationalGrid.Lower.Y]
LowerZ = [pfget ComputationalGrid.Lower.Z]

NX = [pfget ComputationalGrid.NX]
NY = [pfget ComputationalGrid.NY]
NZ = [pfget ComputationalGrid.NZ]

small_domain.ComputationalGrid.DX = [expr ($UpperX - $LowerX) / $NX]
small_domain.ComputationalGrid.DY = [expr ($UpperY - $LowerY) / $NY]
small_domain.ComputationalGrid.DZ = [expr ($UpperZ - $LowerZ) / $NZ]

#---------------------------------------------------------
# The Names of the GeomInputs
#---------------------------------------------------------

small_domain.GeomInput.Names = 'solidinput background'

small_domain.GeomInput.solidinput.InputType = 'SolidFile'
small_domain.GeomInput.solidinput.GeomNames = 'domain'
small_domain.GeomInput.solidinput.FileName = 'crater2D.pfsol'


small_domain.GeomInput.background.InputType = 'Box'
small_domain.GeomInput.background.GeomName = 'background'

small_domain.Geom.background.Lower.X = -99999999.0
small_domain.Geom.background.Lower.Y = -99999999.0
small_domain.Geom.background.Lower.Z = -99999999.0
small_domain.Geom.background.Upper.X = 99999999.0
small_domain.Geom.background.Upper.Y = 99999999.0
small_domain.Geom.background.Upper.Z = 99999999.0

small_domain.Geom.domain.Patches = 'infiltration z_upper x_lower y_lower \'
#                                       x-upper y-upper z-lower"


#-----------------------------------------------------------------------------
# Perm
#-----------------------------------------------------------------------------
small_domain.Geom.Perm.Names = 'domain'



small_domain.Geom.domain.Perm.Type = 'Constant'
small_domain.Geom.domain.Perm.Value = 1.0

small_domain.Perm.TensorType = 'TensorByGeom'

small_domain.Geom.Perm.TensorByGeom.Names = 'background'

small_domain.Geom.background.Perm.TensorValX = 1.0
small_domain.Geom.background.Perm.TensorValY = 1.0
small_domain.Geom.background.Perm.TensorValZ = 1.0

#-----------------------------------------------------------------------------
# Specific Storage
#-----------------------------------------------------------------------------

small_domain.SpecificStorage.Type = 'Constant'
small_domain.SpecificStorage.GeomNames = 'domain'
small_domain.Geom.domain.SpecificStorage.Value = 1.0e-4

#-----------------------------------------------------------------------------
# Phases
#-----------------------------------------------------------------------------

small_domain.Phase.Names = 'water'

small_domain.Phase.water.Density.Type = 'Constant'
small_domain.Phase.water.Density.Value = 1.0

small_domain.Phase.water.Viscosity.Type = 'Constant'
small_domain.Phase.water.Viscosity.Value = 1.0

#-----------------------------------------------------------------------------
# Contaminants
#-----------------------------------------------------------------------------

small_domain.Contaminants.Names = ''


#-----------------------------------------------------------------------------
# Retardation
#-----------------------------------------------------------------------------

small_domain.Geom.Retardation.GeomNames = ''


#-----------------------------------------------------------------------------
# Gravity
#-----------------------------------------------------------------------------

small_domain.Gravity = 1.0

#-----------------------------------------------------------------------------
# Setup timing info
#-----------------------------------------------------------------------------

small_domain.TimingInfo.BaseUnit = 1.0
small_domain.TimingInfo.StartCount = 0
small_domain.TimingInfo.StartTime = 0.0
small_domain.TimingInfo.StopTime = [expr 30.0*1]
small_domain.TimingInfo.DumpInterval = 10
small_domain.TimeStep.Type = 'Constant'
small_domain.TimeStep.Value = 10.0
small_domain.TimingInfo.DumpAtEnd = True

#-----------------------------------------------------------------------------
# Porosity
#-----------------------------------------------------------------------------

small_domain.Geom.Porosity.GeomNames = 'domain'

small_domain.Geom.domain.Porosity.Type = 'Constant'
small_domain.Geom.domain.Porosity.Value = 0.3680

#-----------------------------------------------------------------------------
# Domain
#-----------------------------------------------------------------------------

small_domain.Domain.GeomName = 'domain'

#-----------------------------------------------------------------------------
# Relative Permeability
#-----------------------------------------------------------------------------

small_domain.Phase.RelPerm.Type = 'VanGenuchten'
small_domain.Phase.RelPerm.GeomNames = 'domain'

small_domain.Geom.domain.RelPerm.Alpha = 3.34
small_domain.Geom.domain.RelPerm.N = 1.982

#---------------------------------------------------------
# Saturation
#---------------------------------------------------------

small_domain.Phase.Saturation.Type = 'VanGenuchten'
small_domain.Phase.Saturation.GeomNames = 'domain'

small_domain.Geom.domain.Saturation.Alpha = 3.34
small_domain.Geom.domain.Saturation.N = 1.982
small_domain.Geom.domain.Saturation.SRes = 0.2771
small_domain.Geom.domain.Saturation.SSat = 1.0

#-----------------------------------------------------------------------------
# Wells
#-----------------------------------------------------------------------------
small_domain.Wells.Names = ''

#-----------------------------------------------------------------------------
# Time Cycles
#-----------------------------------------------------------------------------
small_domain.Cycle.Names = 'constant onoff'
small_domain.Cycle.constant.Names = 'alltime'
small_domain.Cycle.constant.alltime.Length = 1
small_domain.Cycle.constant.Repeat = -1

small_domain.Cycle.onoff.Names = 'on off'
small_domain.Cycle.onoff.on.Length = 10
small_domain.Cycle.onoff.off.Length = 90
small_domain.Cycle.onoff.Repeat = -1

#-----------------------------------------------------------------------------
# Boundary Conditions: Pressure
#-----------------------------------------------------------------------------
small_domain.BCPressure.PatchNames = [pfget Geom.domain.Patches]

small_domain.Patch.infiltration.BCPressure.Type = 'FluxConst'
small_domain.Patch.infiltration.BCPressure.Cycle = 'constant'
small_domain.Patch.infiltration.BCPressure.alltime.Value = -0.10
small_domain.Patch.infiltration.BCPressure.off.Value = 0.0

small_domain.Patch.x_lower.BCPressure.Type = 'FluxConst'
small_domain.Patch.x_lower.BCPressure.Cycle = 'constant'
small_domain.Patch.x_lower.BCPressure.alltime.Value = 0.0

small_domain.Patch.y_lower.BCPressure.Type = 'FluxConst'
small_domain.Patch.y_lower.BCPressure.Cycle = 'constant'
small_domain.Patch.y_lower.BCPressure.alltime.Value = 0.0

small_domain.Patch.z_lower.BCPressure.Type = 'FluxConst'
small_domain.Patch.z_lower.BCPressure.Cycle = 'constant'
small_domain.Patch.z_lower.BCPressure.alltime.Value = 0.0

small_domain.Patch.x_upper.BCPressure.Type = 'FluxConst'
small_domain.Patch.x_upper.BCPressure.Cycle = 'constant'
small_domain.Patch.x_upper.BCPressure.alltime.Value = 0.0

small_domain.Patch.y_upper.BCPressure.Type = 'FluxConst'
small_domain.Patch.y_upper.BCPressure.Cycle = 'constant'
small_domain.Patch.y_upper.BCPressure.alltime.Value = 0.0

small_domain.Patch.z_upper.BCPressure.Type = 'FluxConst'
small_domain.Patch.z_upper.BCPressure.Cycle = 'constant'
small_domain.Patch.z_upper.BCPressure.alltime.Value = 0.0

#---------------------------------------------------------
# Topo slopes in x-direction
#---------------------------------------------------------

small_domain.TopoSlopesX.Type = 'Constant'
small_domain.TopoSlopesX.GeomNames = ''

small_domain.TopoSlopesX.Geom.domain.Value = 0.0

#---------------------------------------------------------
# Topo slopes in y-direction
#---------------------------------------------------------

small_domain.TopoSlopesY.Type = 'Constant'
small_domain.TopoSlopesY.GeomNames = ''

small_domain.TopoSlopesY.Geom.domain.Value = 0.0

#---------------------------------------------------------
# Mannings coefficient 
#---------------------------------------------------------

small_domain.Mannings.Type = 'Constant'
small_domain.Mannings.GeomNames = ''
small_domain.Mannings.Geom.domain.Value = 0.

#---------------------------------------------------------
# Initial conditions: water pressure
#---------------------------------------------------------

small_domain.ICPressure.Type = 'HydroStaticPatch'
small_domain.ICPressure.GeomNames = 'domain'

small_domain.Geom.domain.ICPressure.Value = 1.0
small_domain.Geom.domain.ICPressure.RefPatch = 'z_lower'
small_domain.Geom.domain.ICPressure.RefGeom = 'domain'

small_domain.Geom.infiltration.ICPressure.Value = 10.0
small_domain.Geom.infiltration.ICPressure.RefPatch = 'infiltration'
small_domain.Geom.infiltration.ICPressure.RefGeom = 'domain'

#-----------------------------------------------------------------------------
# Phase sources:
#-----------------------------------------------------------------------------

small_domain.PhaseSources.water.Type = 'Constant'
small_domain.PhaseSources.water.GeomNames = 'background'
small_domain.PhaseSources.water.Geom.background.Value = 0.0


#-----------------------------------------------------------------------------
# Exact solution specification for error calculations
#-----------------------------------------------------------------------------

small_domain.KnownSolution = 'NoKnownSolution'

#-----------------------------------------------------------------------------
# Set solver parameters
#-----------------------------------------------------------------------------
small_domain.Solver = 'Richards'
small_domain.Solver.MaxIter = 10000

small_domain.Solver.Nonlinear.MaxIter = 15
small_domain.Solver.Nonlinear.ResidualTol = 1e-9
small_domain.Solver.Nonlinear.StepTol = 1e-9
small_domain.Solver.Nonlinear.EtaValue = 1e-5
small_domain.Solver.Nonlinear.UseJacobian = True
small_domain.Solver.Nonlinear.DerivativeEpsilon = 1e-7

small_domain.Solver.Linear.KrylovDimension = 25
small_domain.Solver.Linear.MaxRestarts = 2

small_domain.Solver.Linear.Preconditioner = 'MGSemi'
small_domain.Solver.Linear.Preconditioner.MGSemi.MaxIter = 1
small_domain.Solver.Linear.Preconditioner.MGSemi.MaxLevels = 100

#-----------------------------------------------------------------------------
# Run and Unload the ParFlow output files
#-----------------------------------------------------------------------------
# pfrun $name
# pfundist $name

#
# Tests 
#
# source pftest.tcl
passed = 1

# if ![pftestFile small_domain.out.perm_x.pfb "Max difference in perm_x" $sig_digits] {
#     set passed 0
# }
# if ![pftestFile small_domain.out.perm_y.pfb "Max difference in perm_y" $sig_digits] {
#     set passed 0
# }
# if ![pftestFile small_domain.out.perm_z.pfb "Max difference in perm_z" $sig_digits] {
#     set passed 0
# }
# if ![pftestFile small_domain.out.porosity.pfb "Max difference in porosity" $sig_digits] {
#     set passed 0
# }

# foreach i "00000 00001 00002 00003 00004" {
#     if ![pftestFile small_domain.out.press.$i.pfb "Max difference in Pressure for timestep $i" $sig_digits] {
# 	set passed 0
#     }
#     if ![pftestFile small_domain.out.satur.$i.pfb "Max difference in Saturation for timestep $i" $sig_digits] {
# 	set passed 0
#     }
# }


# if $passed {
#     puts "small_domain : PASSED"
# } {
#     puts "small_domain : FAILED"
# }
small_domain.run()
