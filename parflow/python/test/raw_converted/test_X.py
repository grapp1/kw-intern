#  This test problem runs the Richards' equation solvers
#  on the eqn:  - div (p grad p) = f where p = x and f
#  is choosen to guarantee the correct solution.
#  For 64 unknowns, the following line should be printed on
#  the screen:
#
#  l2-error in pressure:       5.84881366e-05

#
# Import the ParFlow TCL package
#
from parflow import Run
test_X = Run("test_X", __file__)

test_X.FileVersion = 4

#---------------------------------------------------------
# Academic test problem name
#---------------------------------------------------------
TestName = 'X'

test_X.Process.Topology.P = 1
test_X.Process.Topology.Q = 1
test_X.Process.Topology.R = 1

#---------------------------------------------------------
# Computational Grid
#---------------------------------------------------------
test_X.ComputationalGrid.Lower.X = 0.0
test_X.ComputationalGrid.Lower.Y = 0.0
test_X.ComputationalGrid.Lower.Z = 0.0

test_X.ComputationalGrid.DX = 0.015625
test_X.ComputationalGrid.DY = 1.0
test_X.ComputationalGrid.DZ = 1.0

test_X.ComputationalGrid.NX = 64
test_X.ComputationalGrid.NY = 1
test_X.ComputationalGrid.NZ = 1

#---------------------------------------------------------
# The Names of the GeomInputs
#---------------------------------------------------------
test_X.GeomInput.Names = 'domain_input background_input'


#---------------------------------------------------------
# Domain Geometry Input
#---------------------------------------------------------
test_X.GeomInput.domain_input.InputType = 'Box'
test_X.GeomInput.domain_input.GeomName = 'domain'

#---------------------------------------------------------
# Domain Geometry
#---------------------------------------------------------
test_X.Geom.domain.Lower.X = 0.0
test_X.Geom.domain.Lower.Y = 0.0
test_X.Geom.domain.Lower.Z = 0.0

test_X.Geom.domain.Upper.X = 1.0
test_X.Geom.domain.Upper.Y = 1.0
test_X.Geom.domain.Upper.Z = 1.0

test_X.Geom.domain.Patches = 'left right front back bottom top'

#---------------------------------------------------------
# Background Geometry Input
#---------------------------------------------------------
test_X.GeomInput.background_input.InputType = 'Box'
test_X.GeomInput.background_input.GeomName = 'background'

#---------------------------------------------------------
# Background Geometry
#---------------------------------------------------------
test_X.Geom.background.Lower.X = -99999999.0
test_X.Geom.background.Lower.Y = -99999999.0
test_X.Geom.background.Lower.Z = -99999999.0

test_X.Geom.background.Upper.X = 99999999.0
test_X.Geom.background.Upper.Y = 99999999.0
test_X.Geom.background.Upper.Z = 99999999.0

#-----------------------------------------------------------------------------
# Perm
#-----------------------------------------------------------------------------
test_X.Geom.Perm.Names = 'background'

test_X.Geom.background.Perm.Type = 'Constant'
test_X.Geom.background.Perm.Value = 1.0

test_X.Perm.TensorType = 'TensorByGeom'

test_X.Geom.Perm.TensorByGeom.Names = 'background'

test_X.Geom.background.Perm.TensorValX = 1.0
test_X.Geom.background.Perm.TensorValY = 1.0
test_X.Geom.background.Perm.TensorValZ = 1.0

#-----------------------------------------------------------------------------
# Phases
#-----------------------------------------------------------------------------

test_X.Phase.Names = 'water'

test_X.Phase.water.Density.Type = 'Constant'
test_X.Phase.water.Density.Value = 1.0

test_X.Phase.water.Viscosity.Type = 'Constant'
test_X.Phase.water.Viscosity.Value = 1.0

#-----------------------------------------------------------------------------
# Contaminants
#-----------------------------------------------------------------------------
test_X.Contaminants.Names = 'tce'
test_X.Contaminants.tce.Degradation.Value = 0.0

test_X.PhaseConcen.water.tce.Type = 'Constant'
test_X.PhaseConcen.water.tce.GeomNames = 'domain'
test_X.PhaseConcen.water.tce.Geom.domain.Value = 0.0

#-----------------------------------------------------------------------------
# Retardation
#-----------------------------------------------------------------------------
test_X.Geom.Retardation.GeomNames = 'background'
test_X.Geom.background.tce.Retardation.Type = 'Linear'
test_X.Geom.background.tce.Retardation.Rate = 0.0

#-----------------------------------------------------------------------------
# Gravity
#-----------------------------------------------------------------------------

test_X.Gravity = 0.0

#-----------------------------------------------------------------------------
# Setup timing info
#-----------------------------------------------------------------------------

test_X.TimingInfo.BaseUnit = 1.0
test_X.TimingInfo.StartCount = 0
test_X.TimingInfo.StartTime = 0.0
test_X.TimingInfo.StopTime = 1.0
test_X.TimingInfo.DumpInterval = -1
test_X.TimeStep.Type = 'Constant'
test_X.TimeStep.Value = 1.0

#-----------------------------------------------------------------------------
# Porosity
#-----------------------------------------------------------------------------

test_X.Geom.Porosity.GeomNames = 'background'

test_X.Geom.background.Porosity.Type = 'Constant'
test_X.Geom.background.Porosity.Value = 1.0

#-----------------------------------------------------------------------------
# Domain
#-----------------------------------------------------------------------------
test_X.Domain.GeomName = 'domain'

#-----------------------------------------------------------------------------
# Relative Permeability
#-----------------------------------------------------------------------------

test_X.Phase.RelPerm.Type = 'Polynomial'
test_X.Phase.RelPerm.GeomNames = 'domain'
test_X.Geom.domain.RelPerm.Degree = 1
test_X.Geom.domain.RelPerm.Coeff.0 = 0.0
test_X.Geom.domain.RelPerm.Coeff.1 = 1.0

#---------------------------------------------------------
# Saturation
#---------------------------------------------------------

test_X.Phase.Saturation.Type = 'Constant'
test_X.Phase.Saturation.GeomNames = 'domain'
test_X.Geom.domain.Saturation.Value = 0.0

#-------------------------------------------------------
# Thermal Conductivity
#-------------------------------------------------------
#  
test_X.Phase.ThermalConductivity.Type = 'Constant'
test_X.Phase.ThermalConductivity.GeomNames = 'domain'
test_X.Geom.domain.ThermalConductivity.Value = 2.0
test_X.Geom.domain.ThermalConductivity.KDry = 1.8
test_X.Geom.domain.ThermalConductivity.KWet = 2.2

#-----------------------------------------------------------------------------
# Wells
#-----------------------------------------------------------------------------
test_X.Wells.Names = ''

#-----------------------------------------------------------------------------
# Time Cycles
#-----------------------------------------------------------------------------
test_X.Cycle.Names = 'constant'
test_X.Cycle.constant.Names = 'alltime'
test_X.Cycle.constant.alltime.Length = 1
test_X.Cycle.constant.Repeat = -1

#-----------------------------------------------------------------------------
# Boundary Conditions: Pressure
#-----------------------------------------------------------------------------
test_X.BCPressure.PatchNames = 'left right front back bottom top'

test_X.Patch.left.BCPressure.Type = 'ExactSolution'
test_X.Patch.left.BCPressure.Cycle = 'constant'
test_X.Patch.left.BCPressure.alltime.PredefinedFunction = TestName

test_X.Patch.right.BCPressure.Type = 'ExactSolution'
test_X.Patch.right.BCPressure.Cycle = 'constant'
test_X.Patch.right.BCPressure.alltime.PredefinedFunction = TestName

test_X.Patch.front.BCPressure.Type = 'FluxConst'
test_X.Patch.front.BCPressure.Cycle = 'constant'
test_X.Patch.front.BCPressure.alltime.Value = 0.0

test_X.Patch.back.BCPressure.Type = 'FluxConst'
test_X.Patch.back.BCPressure.Cycle = 'constant'
test_X.Patch.back.BCPressure.alltime.Value = 0.0

test_X.Patch.bottom.BCPressure.Type = 'FluxConst'
test_X.Patch.bottom.BCPressure.Cycle = 'constant'
test_X.Patch.bottom.BCPressure.alltime.Value = 0.0

test_X.Patch.top.BCPressure.Type = 'FluxConst'
test_X.Patch.top.BCPressure.Cycle = 'constant'
test_X.Patch.top.BCPressure.alltime.Value = 0.0


#---------------------------------------------------------
# Initial conditions: water pressure
#---------------------------------------------------------

test_X.ICPressure.Type = 'Constant'
test_X.ICPressure.GeomNames = 'domain'
test_X.Geom.domain.ICPressure.Value = 1.0

#-----------------------------------------------------------------------------
# Boundary Conditions: Temperature 
#-----------------------------------------------------------------------------
test_X.BCTemperature.PatchNames = 'left right front back bottom top'
#  
test_X.Patch.left.BCTemperature.Type = 'FluxConst'
test_X.Patch.left.BCTemperature.Cycle = 'constant'
test_X.Patch.left.BCTemperature.alltime.Value = 0.0
#  
test_X.Patch.right.BCTemperature.Type = 'FluxConst'
test_X.Patch.right.BCTemperature.Cycle = 'constant'
test_X.Patch.right.BCTemperature.alltime.Value = 0.0
#  
test_X.Patch.front.BCTemperature.Type = 'FluxConst'
test_X.Patch.front.BCTemperature.Cycle = 'constant'
test_X.Patch.front.BCTemperature.alltime.Value = 0.0
#  
test_X.Patch.back.BCTemperature.Type = 'FluxConst'
test_X.Patch.back.BCTemperature.Cycle = 'constant'
test_X.Patch.back.BCTemperature.alltime.Value = 0.0
#  
test_X.Patch.bottom.BCTemperature.Type = 'FluxConst'
test_X.Patch.bottom.BCTemperature.Cycle = 'constant'
test_X.Patch.bottom.BCTemperature.alltime.Value = 0.0
#  
test_X.Patch.top.BCTemperature.Type = 'FluxConst'
test_X.Patch.top.BCTemperature.Cycle = 'constant'
test_X.Patch.top.BCTemperature.alltime.Value = 0.0
#  
#---------------------------------------------------------
# Initial conditions: water temperature
#---------------------------------------------------------
test_X.ICTemperature.Type = 'Constant'
test_X.ICTemperature.GeomNames = 'domain'
test_X.Geom.domain.ICTemperature.Value = 288.15
#  
test_X.Geom.domain.ICTemperature.RefGeom = 'domain'
test_X.Geom.domain.ICTemperature.RefPatch = 'bottom'

#-----------------------------------------------------------------------------
# Phase sources:
#-----------------------------------------------------------------------------

test_X.PhaseSources.water.Type = 'PredefinedFunction'
test_X.PhaseSources.water.PredefinedFunction = TestName

#-----------------------------------------------------------------------------
# Temperature sources:
#-----------------------------------------------------------------------------
test_X.TempSources.Type = 'Constant'
test_X.TempSources.GeomNames = 'background'
test_X.TempSources.Geom.background.Value = 0.0

#-----------------------------------------------------------------------------
# Heat Capacity 
#-----------------------------------------------------------------------------
#  
test_X.Phase.water.HeatCapacity.Type = 'Constant'
test_X.Phase.water.HeatCapacity.GeomNames = 'background'
test_X.Phase.water.Geom.background.HeatCapacity.Value = 4000.

#-----------------------------------------------------------------------------
# Exact solution specification for error calculations
#-----------------------------------------------------------------------------

test_X.KnownSolution = TestName


#-----------------------------------------------------------------------------
# Set solver parameters
#-----------------------------------------------------------------------------
test_X.Solver = 'Richards'
test_X.Solver.MaxIter = 5

test_X.Solver.Nonlinear.MaxIter = 15
test_X.Solver.Nonlinear.ResidualTol = 1e-9
test_X.Solver.Nonlinear.EtaValue = 1e-2
test_X.Solver.Nonlinear.UseJacobian = True
test_X.Solver.Nonlinear.DerivativeEpsilon = 1e-8

test_X.Solver.Linear.KrylovDimension = 10
test_X.Solver.Linear.Preconditioner = 'MGSemi'

test_X.Solver.Linear.Preconditioner.SymmetricMat = 'Symmetric'
test_X.Solver.Linear.Preconditioner.MGSemi.MaxIter = 1
test_X.Solver.Linear.Preconditioner.MGSemi.MaxLevels = 100

#---------------------------------------------------------
# Topo slopes in x-direction
#---------------------------------------------------------
#  
test_X.TopoSlopesX.Type = 'Constant'
test_X.TopoSlopesX.GeomNames = 'domain'
test_X.TopoSlopesX.Geom.domain.Value = 0.0005
#  
#---------------------------------------------------------
# Topo slopes in y-direction
#---------------------------------------------------------
#  
test_X.TopoSlopesY.Type = 'Constant'
test_X.TopoSlopesY.GeomNames = 'domain'
test_X.TopoSlopesY.Geom.domain.Value = 0.0005
#  
#---------------------------------------------------------
# Mannings coefficient
#---------------------------------------------------------
#  
test_X.Mannings.Type = 'Constant'
test_X.Mannings.GeomNames = 'domain'
test_X.Mannings.Geom.domain.Value = 2.3e-7
#  
#-----------------------------------------------------------------------------
# Specific Storage
#-----------------------------------------------------------------------------
#  
test_X.SpecificStorage.Type = 'Constant'
test_X.SpecificStorage.GeomNames = 'domain'
test_X.Geom.domain.SpecificStorage.Value = 1.0e-4

#-----------------------------------------------------------------------------
# Run and Unload the ParFlow output files
#-----------------------------------------------------------------------------
# pfrun test_X
# pfrun test_X -g {0}
# pfundist test_X

#-----------------------------------------------------------------------------
# Tests
#-----------------------------------------------------------------------------
# source pftest.tcl


# Expects setting of pressure_l2_error(1) is in output
# pftestParseAndEvaluateOutputForTCL test_X.out.txt

passed = 1

# if ![pftestIsEqual $pressure_l2_error(1) 5.84881366e-05 "Pressure l2_error is not corrrect" ] {
#     set passed 0
# }

# if $passed {
#     puts "test_X : PASSED"
# } {
#     puts "test_X : FAILED"
# }
test_X.run()
