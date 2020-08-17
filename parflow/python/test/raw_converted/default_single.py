#
# Import the ParFlow TCL package
#
from parflow import Run
default_single = Run("default_single", __file__)


#-----------------------------------------------------------------------------
# File input version number
#-----------------------------------------------------------------------------
default_single.FileVersion = 4

#-----------------------------------------------------------------------------
# Process Topology
#-----------------------------------------------------------------------------

default_single.Process.Topology.P = [lindex $argv 0]
default_single.Process.Topology.Q = [lindex $argv 1]
default_single.Process.Topology.R = [lindex $argv 2]

#-----------------------------------------------------------------------------
# Computational Grid
#-----------------------------------------------------------------------------
default_single.ComputationalGrid.Lower.X = -10.0
default_single.ComputationalGrid.Lower.Y = 10.0
default_single.ComputationalGrid.Lower.Z = 1.0

default_single.ComputationalGrid.DX = 8.8888888888888893
default_single.ComputationalGrid.DY = 10.666666666666666
default_single.ComputationalGrid.DZ = 1.0

default_single.ComputationalGrid.NX = 18
default_single.ComputationalGrid.NY = 15
default_single.ComputationalGrid.NZ = 8

#-----------------------------------------------------------------------------
# The Names of the GeomInputs
#-----------------------------------------------------------------------------
default_single.GeomInput.Names = 'domain_input background_input source_region_input concen_region_input'


#-----------------------------------------------------------------------------
# Domain Geometry Input
#-----------------------------------------------------------------------------
default_single.GeomInput.domain_input.InputType = 'Box'
default_single.GeomInput.domain_input.GeomName = 'domain'

#-----------------------------------------------------------------------------
# Domain Geometry
#-----------------------------------------------------------------------------
default_single.Geom.domain.Lower.X = -10.0
default_single.Geom.domain.Lower.Y = 10.0
default_single.Geom.domain.Lower.Z = 1.0

default_single.Geom.domain.Upper.X = 150.0
default_single.Geom.domain.Upper.Y = 170.0
default_single.Geom.domain.Upper.Z = 9.0

default_single.Geom.domain.Patches = 'left right front back bottom top'

#-----------------------------------------------------------------------------
# Background Geometry Input
#-----------------------------------------------------------------------------
default_single.GeomInput.background_input.InputType = 'Box'
default_single.GeomInput.background_input.GeomName = 'background'

#-----------------------------------------------------------------------------
# Background Geometry
#-----------------------------------------------------------------------------
default_single.Geom.background.Lower.X = -99999999.0
default_single.Geom.background.Lower.Y = -99999999.0
default_single.Geom.background.Lower.Z = -99999999.0

default_single.Geom.background.Upper.X = 99999999.0
default_single.Geom.background.Upper.Y = 99999999.0
default_single.Geom.background.Upper.Z = 99999999.0


#-----------------------------------------------------------------------------
# Source_Region Geometry Input
#-----------------------------------------------------------------------------
default_single.GeomInput.source_region_input.InputType = 'Box'
default_single.GeomInput.source_region_input.GeomName = 'source_region'

#-----------------------------------------------------------------------------
# Source_Region Geometry
#-----------------------------------------------------------------------------
default_single.Geom.source_region.Lower.X = 65.56
default_single.Geom.source_region.Lower.Y = 79.34
default_single.Geom.source_region.Lower.Z = 4.5

default_single.Geom.source_region.Upper.X = 74.44
default_single.Geom.source_region.Upper.Y = 89.99
default_single.Geom.source_region.Upper.Z = 5.5


#-----------------------------------------------------------------------------
# Concen_Region Geometry Input
#-----------------------------------------------------------------------------
default_single.GeomInput.concen_region_input.InputType = 'Box'
default_single.GeomInput.concen_region_input.GeomName = 'concen_region'

#-----------------------------------------------------------------------------
# Concen_Region Geometry
#-----------------------------------------------------------------------------
default_single.Geom.concen_region.Lower.X = 60.0
default_single.Geom.concen_region.Lower.Y = 80.0
default_single.Geom.concen_region.Lower.Z = 4.0

default_single.Geom.concen_region.Upper.X = 80.0
default_single.Geom.concen_region.Upper.Y = 100.0
default_single.Geom.concen_region.Upper.Z = 6.0

#-----------------------------------------------------------------------------
# Perm
#-----------------------------------------------------------------------------
default_single.Geom.Perm.Names = 'background'

default_single.Geom.background.Perm.Type = 'Constant'
default_single.Geom.background.Perm.Value = 4.0

default_single.Perm.TensorType = 'TensorByGeom'

default_single.Geom.Perm.TensorByGeom.Names = 'background'

default_single.Geom.background.Perm.TensorValX = 1.0
default_single.Geom.background.Perm.TensorValY = 1.0
default_single.Geom.background.Perm.TensorValZ = 1.0

#-----------------------------------------------------------------------------
# Specific Storage
#-----------------------------------------------------------------------------
# specific storage does not figure into the impes (fully sat) case but we still
# need a key for it

default_single.SpecificStorage.Type = 'Constant'
default_single.SpecificStorage.GeomNames = ''
default_single.Geom.domain.SpecificStorage.Value = 1.0e-4

#-----------------------------------------------------------------------------
# Phases
#-----------------------------------------------------------------------------

default_single.Phase.Names = 'water'

default_single.Phase.water.Density.Type = 'Constant'
default_single.Phase.water.Density.Value = 1.0

default_single.Phase.water.Viscosity.Type = 'Constant'
default_single.Phase.water.Viscosity.Value = 1.0

#-----------------------------------------------------------------------------
# Contaminants
#-----------------------------------------------------------------------------
default_single.Contaminants.Names = 'tce'
default_single.Contaminants.tce.Degradation.Value = 0.0

#-----------------------------------------------------------------------------
# Gravity
#-----------------------------------------------------------------------------

default_single.Gravity = 1.0

#-----------------------------------------------------------------------------
# Setup timing info
#-----------------------------------------------------------------------------

default_single.TimingInfo.BaseUnit = 1.0
default_single.TimingInfo.StartCount = 0
default_single.TimingInfo.StartTime = 0.0
default_single.TimingInfo.StopTime = 1000.0
default_single.TimingInfo.DumpInterval = -1

#-----------------------------------------------------------------------------
# Porosity
#-----------------------------------------------------------------------------

default_single.Geom.Porosity.GeomNames = 'background'

default_single.Geom.background.Porosity.Type = 'Constant'
default_single.Geom.background.Porosity.Value = 1.0

#-----------------------------------------------------------------------------
# Domain
#-----------------------------------------------------------------------------
default_single.Domain.GeomName = 'domain'

#-----------------------------------------------------------------------------
# Mobility
#-----------------------------------------------------------------------------
default_single.Phase.water.Mobility.Type = 'Constant'
default_single.Phase.water.Mobility.Value = 1.0

#-----------------------------------------------------------------------------
# Retardation
#-----------------------------------------------------------------------------
default_single.Geom.Retardation.GeomNames = 'background'
default_single.Geom.background.tce.Retardation.Type = 'Linear'
default_single.Geom.background.tce.Retardation.Rate = 0.0

#-----------------------------------------------------------------------------
# Wells
#-----------------------------------------------------------------------------
default_single.Wells.Names = 'snoopy'

default_single.Wells.snoopy.InputType = 'Recirc'

default_single.Wells.snoopy.Cycle = 'constant'

default_single.Wells.snoopy.ExtractionType = 'Flux'
default_single.Wells.snoopy.InjectionType = 'Flux'

default_single.Wells.snoopy.X = 71.0
default_single.Wells.snoopy.Y = 90.0
default_single.Wells.snoopy.ExtractionZLower = 5.0
default_single.Wells.snoopy.ExtractionZUpper = 5.0
default_single.Wells.snoopy.InjectionZLower = 2.0
default_single.Wells.snoopy.InjectionZUpper = 2.0

default_single.Wells.snoopy.ExtractionMethod = 'Standard'
default_single.Wells.snoopy.InjectionMethod = 'Standard'

default_single.Wells.snoopy.alltime.Extraction.Flux.water.Value = 5.0
default_single.Wells.snoopy.alltime.Injection.Flux.water.Value = 7.5
default_single.Wells.snoopy.alltime.Injection.Concentration.water.tce.Fraction = 0.1

#-----------------------------------------------------------------------------
# Time Cycles
#-----------------------------------------------------------------------------
default_single.Cycle.Names = 'constant'
default_single.Cycle.constant.Names = 'alltime'
default_single.Cycle.constant.alltime.Length = 1
default_single.Cycle.constant.Repeat = -1

#-----------------------------------------------------------------------------
# Boundary Conditions: Pressure
#-----------------------------------------------------------------------------
default_single.BCPressure.PatchNames = 'left right front back bottom top'

default_single.Patch.left.BCPressure.Type = 'DirEquilRefPatch'
default_single.Patch.left.BCPressure.Cycle = 'constant'
default_single.Patch.left.BCPressure.RefGeom = 'domain'
default_single.Patch.left.BCPressure.RefPatch = 'bottom'
default_single.Patch.left.BCPressure.alltime.Value = 14.0

default_single.Patch.right.BCPressure.Type = 'DirEquilRefPatch'
default_single.Patch.right.BCPressure.Cycle = 'constant'
default_single.Patch.right.BCPressure.RefGeom = 'domain'
default_single.Patch.right.BCPressure.RefPatch = 'bottom'
default_single.Patch.right.BCPressure.alltime.Value = 9.0

default_single.Patch.front.BCPressure.Type = 'FluxConst'
default_single.Patch.front.BCPressure.Cycle = 'constant'
default_single.Patch.front.BCPressure.alltime.Value = 0.0

default_single.Patch.back.BCPressure.Type = 'FluxConst'
default_single.Patch.back.BCPressure.Cycle = 'constant'
default_single.Patch.back.BCPressure.alltime.Value = 0.0

default_single.Patch.bottom.BCPressure.Type = 'FluxConst'
default_single.Patch.bottom.BCPressure.Cycle = 'constant'
default_single.Patch.bottom.BCPressure.alltime.Value = 0.0

default_single.Patch.top.BCPressure.Type = 'FluxConst'
default_single.Patch.top.BCPressure.Cycle = 'constant'
default_single.Patch.top.BCPressure.alltime.Value = 0.0


#---------------------------------------------------------
# Topo slopes in x-direction
#---------------------------------------------------------
# topo slopes do not figure into the impes (fully sat) case but we still
# need keys for them

default_single.TopoSlopesX.Type = 'Constant'
default_single.TopoSlopesX.GeomNames = ''

default_single.TopoSlopesX.Geom.domain.Value = 0.0

#---------------------------------------------------------
# Topo slopes in y-direction
#---------------------------------------------------------

default_single.TopoSlopesY.Type = 'Constant'
default_single.TopoSlopesY.GeomNames = ''

default_single.TopoSlopesY.Geom.domain.Value = 0.0

#---------------------------------------------------------
# Mannings coefficient 
#---------------------------------------------------------
# mannings roughnesses do not figure into the impes (fully sat) case but we still
# need a key for them

default_single.Mannings.Type = 'Constant'
default_single.Mannings.GeomNames = ''
default_single.Mannings.Geom.domain.Value = 0.

#-----------------------------------------------------------------------------
# Phase sources:
#-----------------------------------------------------------------------------

default_single.PhaseSources.water.Type = 'Constant'
default_single.PhaseSources.water.GeomNames = 'background'
default_single.PhaseSources.water.Geom.background.Value = 0.0

default_single.PhaseConcen.water.tce.Type = 'Constant'
default_single.PhaseConcen.water.tce.GeomNames = 'concen_region'
default_single.PhaseConcen.water.tce.Geom.concen_region.Value = 0.8


default_single.Solver.WriteSiloSubsurfData = True
default_single.Solver.WriteSiloPressure = True
default_single.Solver.WriteSiloSaturation = True
default_single.Solver.WriteSiloConcentration = True


#-----------------------------------------------------------------------------
# The Solver Impes MaxIter default value changed so to get previous
# results we need to set it back to what it was
#-----------------------------------------------------------------------------
default_single.Solver.MaxIter = 5

#-----------------------------------------------------------------------------
# Run and Unload the ParFlow output files
#-----------------------------------------------------------------------------
# pfrun default_single
# pfundist default_single

# To run with debugging
# pfrun default_single -g {0 1}
# will debug process 0 and 1

#
# Tests 
#
# source pftest.tcl

sig_digits = 4

passed = 1

# if ![pftestFile default_single.out.press.00000.pfb "Max difference in Pressure" $sig_digits] {
#     set passed 0
# }

# if ![pftestFile default_single.out.perm_x.pfb "Max difference in perm_x" $sig_digits] {
#     set passed 0
# }
# if ![pftestFile default_single.out.perm_y.pfb "Max difference in perm_y" $sig_digits] {
#     set passed 0
# }
# if ![pftestFile default_single.out.perm_z.pfb "Max difference in perm_z" $sig_digits] {
#     set passed 0
# }

# foreach i "00000 00001 00002 00003 00004 00005" {
#     if ![pftestFile default_single.out.concen.0.00.$i.pfsb "Max difference in concen timestep $i" $sig_digits] {
#     set passed 0
#     }
# }

# if $passed {
#     puts "default_single : PASSED"
# } {
#     puts "default_single : FAILED"
# }
default_single.run()
