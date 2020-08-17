#  This runs the basic default_richards test case.
#  This run, as written in this input file, should take
#  3 nonlinear iterations.

#
# Import the ParFlow TCL package
#
from parflow import Run
default_richards_with_silopmpio = Run("default_richards_with_silopmpio", __file__)

# Examples of compression options for SILO
# Note compression only works for HDF5
#pfset SILO.Filetype "HDF5"
#pfset SILO.CompressionOptions "METHOD=GZIP"
#pfset SILO.CompressionOptions "METHOD=SZIP"
#pfset SILO.CompressionOptions "METHOD=FPZIP"
#pfset SILO.CompressionOptions "ERRMODE=FALLBACK METHOD=GZIP"

default_richards_with_silopmpio.FileVersion = 4

default_richards_with_silopmpio.Process.Topology.P = 1
default_richards_with_silopmpio.Process.Topology.Q = 1
default_richards_with_silopmpio.Process.Topology.R = 2

#---------------------------------------------------------
# Computational Grid
#---------------------------------------------------------
default_richards_with_silopmpio.ComputationalGrid.Lower.X = -10.0
default_richards_with_silopmpio.ComputationalGrid.Lower.Y = 10.0
default_richards_with_silopmpio.ComputationalGrid.Lower.Z = 1.0

default_richards_with_silopmpio.ComputationalGrid.DX = 8.8888888888888893
default_richards_with_silopmpio.ComputationalGrid.DY = 10.666666666666666
default_richards_with_silopmpio.ComputationalGrid.DZ = 1.0

default_richards_with_silopmpio.ComputationalGrid.NX = 10
default_richards_with_silopmpio.ComputationalGrid.NY = 10
default_richards_with_silopmpio.ComputationalGrid.NZ = 8

#---------------------------------------------------------
# The Names of the GeomInputs
#---------------------------------------------------------
default_richards_with_silopmpio.GeomInput.Names = 'domain_input background_input source_region_input \'
# 		       concen_region_input"


#---------------------------------------------------------
# Domain Geometry Input
#---------------------------------------------------------
default_richards_with_silopmpio.GeomInput.domain_input.InputType = 'Box'
default_richards_with_silopmpio.GeomInput.domain_input.GeomName = 'domain'

#---------------------------------------------------------
# Domain Geometry
#---------------------------------------------------------
default_richards_with_silopmpio.Geom.domain.Lower.X = -10.0
default_richards_with_silopmpio.Geom.domain.Lower.Y = 10.0
default_richards_with_silopmpio.Geom.domain.Lower.Z = 1.0

default_richards_with_silopmpio.Geom.domain.Upper.X = 150.0
default_richards_with_silopmpio.Geom.domain.Upper.Y = 170.0
default_richards_with_silopmpio.Geom.domain.Upper.Z = 9.0

default_richards_with_silopmpio.Geom.domain.Patches = 'left right front back bottom top'

#---------------------------------------------------------
# Background Geometry Input
#---------------------------------------------------------
default_richards_with_silopmpio.GeomInput.background_input.InputType = 'Box'
default_richards_with_silopmpio.GeomInput.background_input.GeomName = 'background'

#---------------------------------------------------------
# Background Geometry
#---------------------------------------------------------
default_richards_with_silopmpio.Geom.background.Lower.X = -99999999.0
default_richards_with_silopmpio.Geom.background.Lower.Y = -99999999.0
default_richards_with_silopmpio.Geom.background.Lower.Z = -99999999.0

default_richards_with_silopmpio.Geom.background.Upper.X = 99999999.0
default_richards_with_silopmpio.Geom.background.Upper.Y = 99999999.0
default_richards_with_silopmpio.Geom.background.Upper.Z = 99999999.0


#---------------------------------------------------------
# Source_Region Geometry Input
#---------------------------------------------------------
default_richards_with_silopmpio.GeomInput.source_region_input.InputType = 'Box'
default_richards_with_silopmpio.GeomInput.source_region_input.GeomName = 'source_region'

#---------------------------------------------------------
# Source_Region Geometry
#---------------------------------------------------------
default_richards_with_silopmpio.Geom.source_region.Lower.X = 65.56
default_richards_with_silopmpio.Geom.source_region.Lower.Y = 79.34
default_richards_with_silopmpio.Geom.source_region.Lower.Z = 4.5

default_richards_with_silopmpio.Geom.source_region.Upper.X = 74.44
default_richards_with_silopmpio.Geom.source_region.Upper.Y = 89.99
default_richards_with_silopmpio.Geom.source_region.Upper.Z = 5.5


#---------------------------------------------------------
# Concen_Region Geometry Input
#---------------------------------------------------------
default_richards_with_silopmpio.GeomInput.concen_region_input.InputType = 'Box'
default_richards_with_silopmpio.GeomInput.concen_region_input.GeomName = 'concen_region'

#---------------------------------------------------------
# Concen_Region Geometry
#---------------------------------------------------------
default_richards_with_silopmpio.Geom.concen_region.Lower.X = 60.0
default_richards_with_silopmpio.Geom.concen_region.Lower.Y = 80.0
default_richards_with_silopmpio.Geom.concen_region.Lower.Z = 4.0

default_richards_with_silopmpio.Geom.concen_region.Upper.X = 80.0
default_richards_with_silopmpio.Geom.concen_region.Upper.Y = 100.0
default_richards_with_silopmpio.Geom.concen_region.Upper.Z = 6.0

#-----------------------------------------------------------------------------
# Perm
#-----------------------------------------------------------------------------
default_richards_with_silopmpio.Geom.Perm.Names = 'background'

default_richards_with_silopmpio.Geom.background.Perm.Type = 'Constant'
default_richards_with_silopmpio.Geom.background.Perm.Value = 4.0

default_richards_with_silopmpio.Perm.TensorType = 'TensorByGeom'

default_richards_with_silopmpio.Geom.Perm.TensorByGeom.Names = 'background'

default_richards_with_silopmpio.Geom.background.Perm.TensorValX = 1.0
default_richards_with_silopmpio.Geom.background.Perm.TensorValY = 1.0
default_richards_with_silopmpio.Geom.background.Perm.TensorValZ = 1.0

#-----------------------------------------------------------------------------
# Specific Storage
#-----------------------------------------------------------------------------

default_richards_with_silopmpio.SpecificStorage.Type = 'Constant'
default_richards_with_silopmpio.SpecificStorage.GeomNames = 'domain'
default_richards_with_silopmpio.Geom.domain.SpecificStorage.Value = 1.0e-4

#-----------------------------------------------------------------------------
# Phases
#-----------------------------------------------------------------------------

default_richards_with_silopmpio.Phase.Names = 'water'

default_richards_with_silopmpio.Phase.water.Density.Type = 'Constant'
default_richards_with_silopmpio.Phase.water.Density.Value = 1.0

default_richards_with_silopmpio.Phase.water.Viscosity.Type = 'Constant'
default_richards_with_silopmpio.Phase.water.Viscosity.Value = 1.0

#-----------------------------------------------------------------------------
# Contaminants
#-----------------------------------------------------------------------------
default_richards_with_silopmpio.Contaminants.Names = ''

#-----------------------------------------------------------------------------
# Retardation
#-----------------------------------------------------------------------------
default_richards_with_silopmpio.Geom.Retardation.GeomNames = ''

#-----------------------------------------------------------------------------
# Gravity
#-----------------------------------------------------------------------------

default_richards_with_silopmpio.Gravity = 1.0

#-----------------------------------------------------------------------------
# Setup timing info
#-----------------------------------------------------------------------------

default_richards_with_silopmpio.TimingInfo.BaseUnit = 1.0
default_richards_with_silopmpio.TimingInfo.StartCount = 0
default_richards_with_silopmpio.TimingInfo.StartTime = 0.0
default_richards_with_silopmpio.TimingInfo.StopTime = 0.010
default_richards_with_silopmpio.TimingInfo.DumpInterval = -1
default_richards_with_silopmpio.TimeStep.Type = 'Constant'
default_richards_with_silopmpio.TimeStep.Value = 0.001

#-----------------------------------------------------------------------------
# Porosity
#-----------------------------------------------------------------------------

default_richards_with_silopmpio.Geom.Porosity.GeomNames = 'background'

default_richards_with_silopmpio.Geom.background.Porosity.Type = 'Constant'
default_richards_with_silopmpio.Geom.background.Porosity.Value = 1.0

#-----------------------------------------------------------------------------
# Domain
#-----------------------------------------------------------------------------
default_richards_with_silopmpio.Domain.GeomName = 'domain'

#-----------------------------------------------------------------------------
# Relative Permeability
#-----------------------------------------------------------------------------

default_richards_with_silopmpio.Phase.RelPerm.Type = 'VanGenuchten'
default_richards_with_silopmpio.Phase.RelPerm.GeomNames = 'domain'
default_richards_with_silopmpio.Geom.domain.RelPerm.Alpha = 0.005
default_richards_with_silopmpio.Geom.domain.RelPerm.N = 2.0

#---------------------------------------------------------
# Saturation
#---------------------------------------------------------

default_richards_with_silopmpio.Phase.Saturation.Type = 'VanGenuchten'
default_richards_with_silopmpio.Phase.Saturation.GeomNames = 'domain'
default_richards_with_silopmpio.Geom.domain.Saturation.Alpha = 0.005
default_richards_with_silopmpio.Geom.domain.Saturation.N = 2.0
default_richards_with_silopmpio.Geom.domain.Saturation.SRes = 0.2
default_richards_with_silopmpio.Geom.domain.Saturation.SSat = 0.99

#-----------------------------------------------------------------------------
# Wells
#-----------------------------------------------------------------------------
default_richards_with_silopmpio.Wells.Names = ''

#-----------------------------------------------------------------------------
# Time Cycles
#-----------------------------------------------------------------------------
default_richards_with_silopmpio.Cycle.Names = 'constant'
default_richards_with_silopmpio.Cycle.constant.Names = 'alltime'
default_richards_with_silopmpio.Cycle.constant.alltime.Length = 1
default_richards_with_silopmpio.Cycle.constant.Repeat = -1

#-----------------------------------------------------------------------------
# Boundary Conditions: Pressure
#-----------------------------------------------------------------------------
default_richards_with_silopmpio.BCPressure.PatchNames = 'left right front back bottom top'

default_richards_with_silopmpio.Patch.left.BCPressure.Type = 'DirEquilRefPatch'
default_richards_with_silopmpio.Patch.left.BCPressure.Cycle = 'constant'
default_richards_with_silopmpio.Patch.left.BCPressure.RefGeom = 'domain'
default_richards_with_silopmpio.Patch.left.BCPressure.RefPatch = 'bottom'
default_richards_with_silopmpio.Patch.left.BCPressure.alltime.Value = 5.0

default_richards_with_silopmpio.Patch.right.BCPressure.Type = 'DirEquilRefPatch'
default_richards_with_silopmpio.Patch.right.BCPressure.Cycle = 'constant'
default_richards_with_silopmpio.Patch.right.BCPressure.RefGeom = 'domain'
default_richards_with_silopmpio.Patch.right.BCPressure.RefPatch = 'bottom'
default_richards_with_silopmpio.Patch.right.BCPressure.alltime.Value = 3.0

default_richards_with_silopmpio.Patch.front.BCPressure.Type = 'FluxConst'
default_richards_with_silopmpio.Patch.front.BCPressure.Cycle = 'constant'
default_richards_with_silopmpio.Patch.front.BCPressure.alltime.Value = 0.0

default_richards_with_silopmpio.Patch.back.BCPressure.Type = 'FluxConst'
default_richards_with_silopmpio.Patch.back.BCPressure.Cycle = 'constant'
default_richards_with_silopmpio.Patch.back.BCPressure.alltime.Value = 0.0

default_richards_with_silopmpio.Patch.bottom.BCPressure.Type = 'FluxConst'
default_richards_with_silopmpio.Patch.bottom.BCPressure.Cycle = 'constant'
default_richards_with_silopmpio.Patch.bottom.BCPressure.alltime.Value = 0.0

default_richards_with_silopmpio.Patch.top.BCPressure.Type = 'FluxConst'
default_richards_with_silopmpio.Patch.top.BCPressure.Cycle = 'constant'
default_richards_with_silopmpio.Patch.top.BCPressure.alltime.Value = 0.0

#---------------------------------------------------------
# Topo slopes in x-direction
#---------------------------------------------------------

default_richards_with_silopmpio.TopoSlopesX.Type = 'Constant'
default_richards_with_silopmpio.TopoSlopesX.GeomNames = ''

default_richards_with_silopmpio.TopoSlopesX.Geom.domain.Value = 0.0

#---------------------------------------------------------
# Topo slopes in y-direction
#---------------------------------------------------------

default_richards_with_silopmpio.TopoSlopesY.Type = 'Constant'
default_richards_with_silopmpio.TopoSlopesY.GeomNames = ''

default_richards_with_silopmpio.TopoSlopesY.Geom.domain.Value = 0.0

#---------------------------------------------------------
# Mannings coefficient 
#---------------------------------------------------------

default_richards_with_silopmpio.Mannings.Type = 'Constant'
default_richards_with_silopmpio.Mannings.GeomNames = ''
default_richards_with_silopmpio.Mannings.Geom.domain.Value = 0.

#---------------------------------------------------------
# Initial conditions: water pressure
#---------------------------------------------------------

default_richards_with_silopmpio.ICPressure.Type = 'HydroStaticPatch'
default_richards_with_silopmpio.ICPressure.GeomNames = 'domain'
default_richards_with_silopmpio.Geom.domain.ICPressure.Value = 3.0
default_richards_with_silopmpio.Geom.domain.ICPressure.RefGeom = 'domain'
default_richards_with_silopmpio.Geom.domain.ICPressure.RefPatch = 'bottom'

#-----------------------------------------------------------------------------
# Phase sources:
#-----------------------------------------------------------------------------

default_richards_with_silopmpio.PhaseSources.water.Type = 'Constant'
default_richards_with_silopmpio.PhaseSources.water.GeomNames = 'background'
default_richards_with_silopmpio.PhaseSources.water.Geom.background.Value = 0.0


#-----------------------------------------------------------------------------
# Exact solution specification for error calculations
#-----------------------------------------------------------------------------

default_richards_with_silopmpio.KnownSolution = 'NoKnownSolution'


#-----------------------------------------------------------------------------
# Set solver parameters
#-----------------------------------------------------------------------------
default_richards_with_silopmpio.Solver = 'Richards'
default_richards_with_silopmpio.Solver.MaxIter = 5

default_richards_with_silopmpio.Solver.Nonlinear.MaxIter = 10
default_richards_with_silopmpio.Solver.Nonlinear.ResidualTol = 1e-9
default_richards_with_silopmpio.Solver.Nonlinear.EtaChoice = 'EtaConstant'
default_richards_with_silopmpio.Solver.Nonlinear.EtaValue = 1e-5
default_richards_with_silopmpio.Solver.Nonlinear.UseJacobian = True
default_richards_with_silopmpio.Solver.Nonlinear.DerivativeEpsilon = 1e-2

default_richards_with_silopmpio.Solver.Linear.KrylovDimension = 10

default_richards_with_silopmpio.Solver.Linear.Preconditioner = 'PFMGOctree'
default_richards_with_silopmpio.Solver.Linear.Preconditioner.MGSemi.MaxIter = 1
default_richards_with_silopmpio.Solver.Linear.Preconditioner.MGSemi.MaxLevels = 100


default_richards_with_silopmpio.Solver.WriteSiloSubsurfData = True
default_richards_with_silopmpio.Solver.WriteSiloPMPIOSubsurfData = True
default_richards_with_silopmpio.Solver.WriteSiloPressure = True
default_richards_with_silopmpio.Solver.WriteSiloSaturation = True
default_richards_with_silopmpio.Solver.WriteSiloConcentration = True
default_richards_with_silopmpio.Solver.WriteSiloPMPIOPressure = True
default_richards_with_silopmpio.SILO.pmpio.NumFiles = 1

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


#
# Check if silopmpio output matches pfb output
#
pfb = [pfload -silo default_richards.out.press.00001.silo]
silo = [pfload -silo default_richards.out.pmpio.press.00001.silo]
diff = [pfmdiff $silo $pfb 10]
# if {[string length $diff] != 0 } {
#     puts "FAILED : Silo output does not match siloPMPIO output"
#     puts $diff
#     set passed 0
# } 

silo = [pfload default_richards.out.pmpio.porosity.silo]
pfb = [pfload default_richards.out.porosity.pfb]
diff = [pfmdiff $silo $pfb 10]
# if {[string length $diff] != 0 } {
#     puts "FAILED : SiloPMPIO output does not match PFB output"
#     puts $diff
#     set passed 0
# } 

# pfsave $silo -silo "single_block.silo"
silo_single_block = [pfload "single_block.silo"]
diff = [pfmdiff $silo $silo_single_block 10]
# if {[string length $diff] != 0 } {
#     puts "FAILED : Silo MP format does not match Silo single block format"
#     puts $diff
#     set passed 0
# } 

#set silo [pfload -silo default_richards.out.pmpio.press.00001.silo]
# pfsave $silo -sa "single_block.sa"
diff = [pfmdiff $silo_single_block $pfb 8]
# if {[string length $diff] != 0 } {
#     puts "FAILED : Silo Single Block format does not match PFB format"
#     puts $diff
#     set passed 0
# } 


# if $passed {
#     puts "default_richards_with_siloPMPIO : PASSED"
# } {
#     puts "default_richards_with_siloPMPIO : FAILED"
# }

default_richards_with_silopmpio.run()
