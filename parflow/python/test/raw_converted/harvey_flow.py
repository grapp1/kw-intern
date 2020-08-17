# this runs the Cape Cod site flow case for the Harvey and Garabedian bacterial 
# injection experiment from Maxwell, et al, 2007.

#
# Import the ParFlow TCL package
#
from parflow import Run
harvey.flow = Run("harvey.flow", __file__)


#-----------------------------------------------------------------------------
# File input version number
#-----------------------------------------------------------------------------
harvey.flow.FileVersion = 4

#-----------------------------------------------------------------------------
# Process Topology
#-----------------------------------------------------------------------------

harvey.flow.Process.Topology.P = 1
harvey.flow.Process.Topology.Q = 1
harvey.flow.Process.Topology.R = 1

#-----------------------------------------------------------------------------
# Computational Grid
#-----------------------------------------------------------------------------
harvey.flow.ComputationalGrid.Lower.X = 0.0
harvey.flow.ComputationalGrid.Lower.Y = 0.0
harvey.flow.ComputationalGrid.Lower.Z = 0.0

harvey.flow.ComputationalGrid.DX = 0.34
harvey.flow.ComputationalGrid.DY = 0.34
harvey.flow.ComputationalGrid.DZ = 0.038

harvey.flow.ComputationalGrid.NX = 50
harvey.flow.ComputationalGrid.NY = 30
harvey.flow.ComputationalGrid.NZ = 100

#-----------------------------------------------------------------------------
# The Names of the GeomInputs
#-----------------------------------------------------------------------------
harvey.flow.GeomInput.Names = 'domain_input upper_aquifer_input lower_aquifer_input'


#-----------------------------------------------------------------------------
# Domain Geometry Input
#-----------------------------------------------------------------------------
harvey.flow.GeomInput.domain_input.InputType = 'Box'
harvey.flow.GeomInput.domain_input.GeomName = 'domain'

#-----------------------------------------------------------------------------
# Domain Geometry
#-----------------------------------------------------------------------------
harvey.flow.Geom.domain.Lower.X = 0.0
harvey.flow.Geom.domain.Lower.Y = 0.0
harvey.flow.Geom.domain.Lower.Z = 0.0

harvey.flow.Geom.domain.Upper.X = 17.0
harvey.flow.Geom.domain.Upper.Y = 10.2
harvey.flow.Geom.domain.Upper.Z = 3.8

harvey.flow.Geom.domain.Patches = 'left right front back bottom top'

#-----------------------------------------------------------------------------
# Upper Aquifer Geometry Input
#-----------------------------------------------------------------------------
harvey.flow.GeomInput.upper_aquifer_input.InputType = 'Box'
harvey.flow.GeomInput.upper_aquifer_input.GeomName = 'upper_aquifer'

#-----------------------------------------------------------------------------
# Upper Aquifer Geometry
#-----------------------------------------------------------------------------
harvey.flow.Geom.upper_aquifer.Lower.X = 0.0
harvey.flow.Geom.upper_aquifer.Lower.Y = 0.0
harvey.flow.Geom.upper_aquifer.Lower.Z = 1.5
#pfset Geom.upper_aquifer.Lower.Z                        0.0

harvey.flow.Geom.upper_aquifer.Upper.X = 17.0
harvey.flow.Geom.upper_aquifer.Upper.Y = 10.2
harvey.flow.Geom.upper_aquifer.Upper.Z = 3.8

#-----------------------------------------------------------------------------
# Lower Aquifer Geometry Input
#-----------------------------------------------------------------------------
harvey.flow.GeomInput.lower_aquifer_input.InputType = 'Box'
harvey.flow.GeomInput.lower_aquifer_input.GeomName = 'lower_aquifer'

#-----------------------------------------------------------------------------
# Lower Aquifer Geometry
#-----------------------------------------------------------------------------
harvey.flow.Geom.lower_aquifer.Lower.X = 0.0
harvey.flow.Geom.lower_aquifer.Lower.Y = 0.0
harvey.flow.Geom.lower_aquifer.Lower.Z = 0.0

harvey.flow.Geom.lower_aquifer.Upper.X = 17.0
harvey.flow.Geom.lower_aquifer.Upper.Y = 10.2
harvey.flow.Geom.lower_aquifer.Upper.Z = 1.5


#-----------------------------------------------------------------------------
# Perm
#-----------------------------------------------------------------------------
harvey.flow.Geom.Perm.Names = 'upper_aquifer lower_aquifer'
# we open a file, in this case from PEST to set upper and lower kg and sigma
#
fileId = [open stats4.txt r 0600]
kgu = [gets $fileId]
varu = [gets $fileId]
kgl = [gets $fileId]
varl = [gets $fileId]
# close $fileId


## we use the parallel turning bands formulation in ParFlow to simulate
## GRF for upper and lower aquifer
##

harvey.flow.Geom.upper_aquifer.Perm.Type = 'TurnBands'
harvey.flow.Geom.upper_aquifer.Perm.LambdaX = 3.60
harvey.flow.Geom.upper_aquifer.Perm.LambdaY = 3.60
harvey.flow.Geom.upper_aquifer.Perm.LambdaZ = 0.19
harvey.flow.Geom.upper_aquifer.Perm.GeomMean = 112.00

harvey.flow.Geom.upper_aquifer.Perm.Sigma = 1.0
harvey.flow.Geom.upper_aquifer.Perm.Sigma = 0.48989794
harvey.flow.Geom.upper_aquifer.Perm.NumLines = 150
harvey.flow.Geom.upper_aquifer.Perm.RZeta = 5.0
harvey.flow.Geom.upper_aquifer.Perm.KMax = 100.0000001
harvey.flow.Geom.upper_aquifer.Perm.DelK = 0.2
harvey.flow.Geom.upper_aquifer.Perm.Seed = 33333
harvey.flow.Geom.upper_aquifer.Perm.LogNormal = 'Log'
harvey.flow.Geom.upper_aquifer.Perm.StratType = 'Bottom'
harvey.flow.Geom.lower_aquifer.Perm.Type = 'TurnBands'
harvey.flow.Geom.lower_aquifer.Perm.LambdaX = 3.60
harvey.flow.Geom.lower_aquifer.Perm.LambdaY = 3.60
harvey.flow.Geom.lower_aquifer.Perm.LambdaZ = 0.19

harvey.flow.Geom.lower_aquifer.Perm.GeomMean = 77.0
harvey.flow.Geom.lower_aquifer.Perm.Sigma = 1.0
harvey.flow.Geom.lower_aquifer.Perm.Sigma = 0.48989794
harvey.flow.Geom.lower_aquifer.Perm.NumLines = 150
harvey.flow.Geom.lower_aquifer.Perm.RZeta = 5.0
harvey.flow.Geom.lower_aquifer.Perm.KMax = 100.0000001
harvey.flow.Geom.lower_aquifer.Perm.DelK = 0.2
harvey.flow.Geom.lower_aquifer.Perm.Seed = 33333
harvey.flow.Geom.lower_aquifer.Perm.LogNormal = 'Log'
harvey.flow.Geom.lower_aquifer.Perm.StratType = 'Bottom'

# uncomment the lines below to run parallel gaussian instead
# of parallel turning bands

#pfset Geom.upper_aquifer.Perm.Type "ParGauss"

#pfset Geom.upper_aquifer.Perm.Seed 1
#pfset Geom.upper_aquifer.Perm.MaxNPts 70.0
#pfset Geom.upper_aquifer.Perm.MaxCpts 20


#pfset Geom.lower_aquifer.Perm.Type "ParGauss"

#pfset Geom.lower_aquifer.Perm.Seed 1
#pfset Geom.lower_aquifer.Perm.MaxNPts 70.0
#pfset Geom.lower_aquifer.Perm.MaxCpts 20

#pfset lower aqu and upper aq stats to pest/read in values

harvey.flow.Geom.upper_aquifer.Perm.GeomMean = kgu
harvey.flow.Geom.upper_aquifer.Perm.Sigma = varu

harvey.flow.Geom.lower_aquifer.Perm.GeomMean = kgl
harvey.flow.Geom.lower_aquifer.Perm.Sigma = varl


harvey.flow.Perm.TensorType = 'TensorByGeom'

harvey.flow.Geom.Perm.TensorByGeom.Names = 'domain'

harvey.flow.Geom.domain.Perm.TensorValX = 1.0
harvey.flow.Geom.domain.Perm.TensorValY = 1.0
harvey.flow.Geom.domain.Perm.TensorValZ = 1.0

#-----------------------------------------------------------------------------
# Specific Storage
#-----------------------------------------------------------------------------
# specific storage does not figure into the impes (fully sat) case but we still
# need a key for it

harvey.flow.SpecificStorage.Type = 'Constant'
harvey.flow.SpecificStorage.GeomNames = ''
harvey.flow.Geom.domain.SpecificStorage.Value = 1.0e-4

#-----------------------------------------------------------------------------
# Phases
#-----------------------------------------------------------------------------

harvey.flow.Phase.Names = 'water'

harvey.flow.Phase.water.Density.Type = 'Constant'
harvey.flow.Phase.water.Density.Value = 1.0

harvey.flow.Phase.water.Viscosity.Type = 'Constant'
harvey.flow.Phase.water.Viscosity.Value = 1.0

#-----------------------------------------------------------------------------
# Contaminants
#-----------------------------------------------------------------------------
harvey.flow.Contaminants.Names = ''


#-----------------------------------------------------------------------------
# Gravity
#-----------------------------------------------------------------------------

harvey.flow.Gravity = 1.0

#-----------------------------------------------------------------------------
# Setup timing info
#-----------------------------------------------------------------------------

harvey.flow.TimingInfo.BaseUnit = 1.0
harvey.flow.TimingInfo.StartCount = -1
harvey.flow.TimingInfo.StartTime = 0.0
harvey.flow.TimingInfo.StopTime = 0.0
harvey.flow.TimingInfo.DumpInterval = -1

#-----------------------------------------------------------------------------
# Porosity
#-----------------------------------------------------------------------------

harvey.flow.Geom.Porosity.GeomNames = 'domain'

harvey.flow.Geom.domain.Porosity.Type = 'Constant'
harvey.flow.Geom.domain.Porosity.Value = 0.390

#-----------------------------------------------------------------------------
# Domain
#-----------------------------------------------------------------------------
harvey.flow.Domain.GeomName = 'domain'

#-----------------------------------------------------------------------------
# Mobility
#-----------------------------------------------------------------------------
harvey.flow.Phase.water.Mobility.Type = 'Constant'
harvey.flow.Phase.water.Mobility.Value = 1.0


#-----------------------------------------------------------------------------
# Wells
#-----------------------------------------------------------------------------
harvey.flow.Wells.Names = ''


#-----------------------------------------------------------------------------
# Time Cycles
#-----------------------------------------------------------------------------
harvey.flow.Cycle.Names = 'constant'
harvey.flow.Cycle.constant.Names = 'alltime'
harvey.flow.Cycle.constant.alltime.Length = 1
harvey.flow.Cycle.constant.Repeat = -1

#-----------------------------------------------------------------------------
# Boundary Conditions: Pressure
#-----------------------------------------------------------------------------
harvey.flow.BCPressure.PatchNames = 'left right front back bottom top'

harvey.flow.Patch.left.BCPressure.Type = 'DirEquilRefPatch'
harvey.flow.Patch.left.BCPressure.Cycle = 'constant'
harvey.flow.Patch.left.BCPressure.RefGeom = 'domain'
harvey.flow.Patch.left.BCPressure.RefPatch = 'bottom'
harvey.flow.Patch.left.BCPressure.alltime.Value = 10.0

harvey.flow.Patch.right.BCPressure.Type = 'DirEquilRefPatch'
harvey.flow.Patch.right.BCPressure.Cycle = 'constant'
harvey.flow.Patch.right.BCPressure.RefGeom = 'domain'
harvey.flow.Patch.right.BCPressure.RefPatch = 'bottom'
harvey.flow.Patch.right.BCPressure.alltime.Value = 9.97501

harvey.flow.Patch.front.BCPressure.Type = 'FluxConst'
harvey.flow.Patch.front.BCPressure.Cycle = 'constant'
harvey.flow.Patch.front.BCPressure.alltime.Value = 0.0

harvey.flow.Patch.back.BCPressure.Type = 'FluxConst'
harvey.flow.Patch.back.BCPressure.Cycle = 'constant'
harvey.flow.Patch.back.BCPressure.alltime.Value = 0.0

harvey.flow.Patch.bottom.BCPressure.Type = 'FluxConst'
harvey.flow.Patch.bottom.BCPressure.Cycle = 'constant'
harvey.flow.Patch.bottom.BCPressure.alltime.Value = 0.0

harvey.flow.Patch.top.BCPressure.Type = 'FluxConst'
harvey.flow.Patch.top.BCPressure.Cycle = 'constant'
harvey.flow.Patch.top.BCPressure.alltime.Value = 0.0

#---------------------------------------------------------
# Topo slopes in x-direction
#---------------------------------------------------------
# topo slopes do not figure into the impes (fully sat) case but we still
# need keys for them

harvey.flow.TopoSlopesX.Type = 'Constant'
harvey.flow.TopoSlopesX.GeomNames = ''

harvey.flow.TopoSlopesX.Geom.domain.Value = 0.0

#---------------------------------------------------------
# Topo slopes in y-direction
#---------------------------------------------------------

harvey.flow.TopoSlopesY.Type = 'Constant'
harvey.flow.TopoSlopesY.GeomNames = ''

harvey.flow.TopoSlopesY.Geom.domain.Value = 0.0

#---------------------------------------------------------
# Mannings coefficient 
#---------------------------------------------------------
# mannings roughnesses do not figure into the impes (fully sat) case but we still
# need a key for them

harvey.flow.Mannings.Type = 'Constant'
harvey.flow.Mannings.GeomNames = ''
harvey.flow.Mannings.Geom.domain.Value = 0.

#-----------------------------------------------------------------------------
# Phase sources:
#-----------------------------------------------------------------------------

harvey.flow.PhaseSources.water.Type = 'Constant'
harvey.flow.PhaseSources.water.GeomNames = 'domain'
harvey.flow.PhaseSources.water.Geom.domain.Value = 0.0

#-----------------------------------------------------------------------------
#  Solver Impes  
#-----------------------------------------------------------------------------
harvey.flow.Solver.MaxIter = 50
harvey.flow.Solver.AbsTol = 1E-10
harvey.flow.Solver.Drop = 1E-15

#-----------------------------------------------------------------------------
# Run and Unload the ParFlow output files
#-----------------------------------------------------------------------------

# this script is setup to run 100 realizations, for testing we just run one
###set n_runs 100
n_runs = 1

#
#  Loop through runs
#
# for {set k 1} {$k <= $n_runs} {incr k 1} {
#
# set the random seed to be different for every run
#
harvey.flow.Geom.upper_aquifer.Perm.Seed = [ expr 33333+2*$k ]
harvey.flow.Geom.lower_aquifer.Perm.Seed = [ expr 31313+2*$k ]



# pfrun harvey_flow.$k
# pfundist harvey_flow.$k

# we use pf tools to convert from pressure to head
# we could do a number of other things here like copy files to different format
press = [pfload harvey_flow.$k.out.press.pfb]
head = [pfhhead $press]
# pfsave $head -pfb harvey_flow.$k.head.pfb
# }

# this could run other tcl scripts now an example is below
#puts stdout "running SLIM"
#source bromide_trans.sm.tcl

#
# Tests 
#
# source pftest.tcl

passed = 1

# if ![pftestFile harvey_flow.1.out.press.pfb "Max difference in Pressure" $sig_digits] {
#     set passed 0
# }

# if ![pftestFile harvey_flow.1.out.porosity.pfb "Max difference in Porosity" $sig_digits] {
#     set passed 0
# }

# if ![pftestFile harvey_flow.1.head.pfb "Max difference in Head" $sig_digits] {
#     set passed 0
# }

# if ![pftestFile harvey_flow.1.out.perm_x.pfb "Max difference in perm_x" $sig_digits] {
#     set passed 0
# }
# if ![pftestFile harvey_flow.1.out.perm_y.pfb "Max difference in perm_y" $sig_digits] {
#     set passed 0
# }
# if ![pftestFile harvey_flow.1.out.perm_z.pfb "Max difference in perm_z" $sig_digits] {
#     set passed 0
# }

# if $passed {
#     puts "harvey_flow.1 : PASSED"
# } {
#     puts "harvey_flow.1 : FAILED"
# }
harvey.flow.run()
