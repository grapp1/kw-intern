# Test case submitted by:
# Joshua B. Kollat, Ph.D. 
# Research Associate
# Penn State University

#
# Tests running solver impes with no advection.
#

#
# Import the ParFlow TCL package
#
from parflow import Run
uvm_flow = Run("uvm_flow", __file__)

# set runname uvm.flow

#set PARFLOW_DIR {/home/juk124/parflow/parflow}
INPUT_DIR = {.}
OUTPUT_DIR = {.}

#Base Units:
# Mass - g
# Length - m
# Time - days

#-----------------------------------------------------------------------------
# File input version number
#-----------------------------------------------------------------------------
uvm_flow.FileVersion = 4

#-----------------------------------------------------------------------------
# Process Topology
#-----------------------------------------------------------------------------
uvm_flow.Process.Topology.P = [lindex $argv 0]
uvm_flow.Process.Topology.Q = [lindex $argv 1]
uvm_flow.Process.Topology.R = [lindex $argv 2]

#-----------------------------------------------------------------------------
# Computational Grid
#-----------------------------------------------------------------------------

#These are based on Donna's formulation using MODFLOW/MT3DMS
uvm_flow.ComputationalGrid.Lower.X = 0.0
uvm_flow.ComputationalGrid.Lower.Y = 0.0
uvm_flow.ComputationalGrid.Lower.Z = 0.0

#These are based on Donna's formulation using MODFLOW/MT3DMS
uvm_flow.ComputationalGrid.NX = 45
uvm_flow.ComputationalGrid.NY = 63
uvm_flow.ComputationalGrid.NZ = 33
#These are the UVM model resolutions
#pfset ComputationalGrid.NX                35
#pfset ComputationalGrid.NY                50
#pfset ComputationalGrid.NZ                33

#These are based on Donna's formulation using MODFLOW/MT3DMS
UpperX = 2.7
UpperY = 3.8
UpperZ = 2.0
#These are the UVM model limits:
#set   UpperX                              2.74295
#set   UpperY                              3.937
#set   UpperZ                              2.0066
#These are the true UVM tank dimensions
#set   UpperX                              2.540
#set   UpperY                              3.560
#set   UpperZ                              2.030

LowerX = [pfget ComputationalGrid.Lower.X]
LowerY = [pfget ComputationalGrid.Lower.Y]
LowerZ = [pfget ComputationalGrid.Lower.Z]

NX = [pfget ComputationalGrid.NX]
NY = [pfget ComputationalGrid.NY]
NZ = [pfget ComputationalGrid.NZ]

uvm_flow.ComputationalGrid.DX = [expr ($UpperX - $LowerX) / $NX]
uvm_flow.ComputationalGrid.DY = [expr ($UpperY - $LowerY) / $NY]
uvm_flow.ComputationalGrid.DZ = [expr ($UpperZ - $LowerZ) / $NZ]

#-----------------------------------------------------------------------------
# The Names of the GeomInputs
#-----------------------------------------------------------------------------
uvm_flow.GeomInput.Names = 'domain layer1 layer2 layer3 layer4 layer5 lens'

#-----------------------------------------------------------------------------
# Entire domain
#-----------------------------------------------------------------------------
uvm_flow.GeomInput.domain.InputType = 'Box'
uvm_flow.GeomInput.domain.GeomName = 'domain'

uvm_flow.Geom.domain.Lower.X = 0.0
uvm_flow.Geom.domain.Lower.Y = 0.0
uvm_flow.Geom.domain.Lower.Z = 0.0
uvm_flow.Geom.domain.Upper.X = UpperX
uvm_flow.Geom.domain.Upper.Y = UpperY
uvm_flow.Geom.domain.Upper.Z = UpperZ

uvm_flow.Geom.domain.Patches = 'left right front back bottom top'

#-----------------------------------------------------------------------------
# Layer 1 - coarse sand
#-----------------------------------------------------------------------------
uvm_flow.GeomInput.layer1.InputType = 'Box'
uvm_flow.GeomInput.layer1.GeomName = 'layer1'

uvm_flow.Geom.layer1.Lower.X = 0.0
uvm_flow.Geom.layer1.Lower.Y = 0.0
uvm_flow.Geom.layer1.Lower.Z = 0.0
uvm_flow.Geom.layer1.Upper.X = UpperX
uvm_flow.Geom.layer1.Upper.Y = UpperY
uvm_flow.Geom.layer1.Upper.Z = 0.51

uvm_flow.Geom.layer1.Patches = 'left right front back bottom top'

#-----------------------------------------------------------------------------
# Layer 2 - silt
#-----------------------------------------------------------------------------
uvm_flow.GeomInput.layer2.InputType = 'Box'
uvm_flow.GeomInput.layer2.GeomName = 'layer2'

uvm_flow.Geom.layer2.Lower.X = 0.0
uvm_flow.Geom.layer2.Lower.Y = 0.0
uvm_flow.Geom.layer2.Lower.Z = 0.51
uvm_flow.Geom.layer2.Upper.X = UpperX
uvm_flow.Geom.layer2.Upper.Y = UpperY
uvm_flow.Geom.layer2.Upper.Z = 0.69

uvm_flow.Geom.layer2.Patches = 'left right front back bottom top'

#-----------------------------------------------------------------------------
# Layer 3 - medium sand
#-----------------------------------------------------------------------------
uvm_flow.GeomInput.layer3.InputType = 'Box'
uvm_flow.GeomInput.layer3.GeomName = 'layer3'

uvm_flow.Geom.layer3.Lower.X = 0.0
uvm_flow.Geom.layer3.Lower.Y = 0.0
uvm_flow.Geom.layer3.Lower.Z = 0.69
uvm_flow.Geom.layer3.Upper.X = UpperX
uvm_flow.Geom.layer3.Upper.Y = UpperY
uvm_flow.Geom.layer3.Upper.Z = 1.14

uvm_flow.Geom.layer3.Patches = 'left right front back bottom top'

#-----------------------------------------------------------------------------
# Layer4 - medium sand
#-----------------------------------------------------------------------------
uvm_flow.GeomInput.layer4.InputType = 'Box'
uvm_flow.GeomInput.layer4.GeomName = 'layer4'

uvm_flow.Geom.layer4.Lower.X = 0.0
uvm_flow.Geom.layer4.Lower.Y = 0.0
uvm_flow.Geom.layer4.Lower.Z = 1.14
uvm_flow.Geom.layer4.Upper.X = UpperX
uvm_flow.Geom.layer4.Upper.Y = UpperY
uvm_flow.Geom.layer4.Upper.Z = 1.60

uvm_flow.Geom.layer4.Patches = 'left right front back bottom top'

#-----------------------------------------------------------------------------
# Layer 5 - medium sand
#-----------------------------------------------------------------------------
uvm_flow.GeomInput.layer5.InputType = 'Box'
uvm_flow.GeomInput.layer5.GeomName = 'layer5'

uvm_flow.Geom.layer5.Lower.X = 0.0
uvm_flow.Geom.layer5.Lower.Y = 0.0
uvm_flow.Geom.layer5.Lower.Z = 1.60
uvm_flow.Geom.layer5.Upper.X = UpperX
uvm_flow.Geom.layer5.Upper.Y = UpperY
uvm_flow.Geom.layer5.Upper.Z = UpperZ

uvm_flow.Geom.layer5.Patches = 'left right front back bottom top'

#-----------------------------------------------------------------------------
# Fine lens block - specify after layers to replace layer section
#-----------------------------------------------------------------------------
uvm_flow.GeomInput.lens.InputType = 'Box'
uvm_flow.GeomInput.lens.GeomName = 'lens'

uvm_flow.Geom.lens.Lower.X = 0.86
uvm_flow.Geom.lens.Lower.Y = 1.34
uvm_flow.Geom.lens.Lower.Z = 1.14
uvm_flow.Geom.lens.Upper.X = 2.11
uvm_flow.Geom.lens.Upper.Y = 2.68
uvm_flow.Geom.lens.Upper.Z = 1.60

uvm_flow.Geom.lens.Patches = 'left right front back bottom top'

#-----------------------------------------------------------------------------
# Perm
#-----------------------------------------------------------------------------
#pfset Geom.Perm.Names "domain"
uvm_flow.Geom.Perm.Names = 'layer1 layer2 layer3 layer4 layer5 lens'

#Note: Since gravity, viscosity, and density have been normalized to 1, we are
#dealing with hydraulic conductivity rather than permiability.  The value below
#have been specified as such.

#Note: Parflow.exe is running form the debug folder
uvm_flow.Perm.Conditioning.FileName = INPUT_DIR/uvm.flow.KConditioningPts.txt

#Gravel Layer
uvm_flow.Geom.layer1.Perm.Type = 'TurnBands'
uvm_flow.Geom.layer1.Perm.LambdaX = 0.30
uvm_flow.Geom.layer1.Perm.LambdaY = 0.30
uvm_flow.Geom.layer1.Perm.LambdaZ = 0.30
uvm_flow.Geom.layer1.Perm.GeomMean = 134.0
uvm_flow.Geom.layer1.Perm.Sigma = 21.4344
uvm_flow.Geom.layer1.Perm.NumLines = 100
uvm_flow.Geom.layer1.Perm.RZeta = 5.0
uvm_flow.Geom.layer1.Perm.KMax = 100.0
uvm_flow.Geom.layer1.Perm.DelK = 0.2
uvm_flow.Geom.layer1.Perm.MaxNPts = 100
uvm_flow.Geom.layer1.Perm.MaxCpts = 8
uvm_flow.Geom.layer1.Perm.LogNormal = 'Normal'
uvm_flow.Geom.layer1.Perm.StratType = 'Bottom'

#Silt Layer
uvm_flow.Geom.layer2.Perm.Type = 'Constant'
#Note: You cannot specify a K value of 0, it just needs to be really small
uvm_flow.Geom.layer2.Perm.Value = 0.00001

#Medium Sand Layer 3
uvm_flow.Geom.layer3.Perm.Type = 'TurnBands'
uvm_flow.Geom.layer3.Perm.LambdaX = 0.30
uvm_flow.Geom.layer3.Perm.LambdaY = 0.30
uvm_flow.Geom.layer3.Perm.LambdaZ = 0.30
uvm_flow.Geom.layer3.Perm.GeomMean = 17.3542
uvm_flow.Geom.layer3.Perm.Sigma = 1.6632
uvm_flow.Geom.layer3.Perm.NumLines = 100
uvm_flow.Geom.layer3.Perm.RZeta = 5.0
uvm_flow.Geom.layer3.Perm.KMax = 100.0
uvm_flow.Geom.layer3.Perm.DelK = 0.2
uvm_flow.Geom.layer3.Perm.MaxNPts = 100
uvm_flow.Geom.layer3.Perm.MaxCpts = 8
uvm_flow.Geom.layer3.Perm.LogNormal = 'Normal'
uvm_flow.Geom.layer3.Perm.StratType = 'Bottom'

#Medium Sand Layer 4
uvm_flow.Geom.layer4.Perm.Type = 'TurnBands'
uvm_flow.Geom.layer4.Perm.LambdaX = 0.30
uvm_flow.Geom.layer4.Perm.LambdaY = 0.30
uvm_flow.Geom.layer4.Perm.LambdaZ = 0.30
uvm_flow.Geom.layer4.Perm.GeomMean = 18.1849
uvm_flow.Geom.layer4.Perm.Sigma = 1.0392
uvm_flow.Geom.layer4.Perm.NumLines = 100
uvm_flow.Geom.layer4.Perm.RZeta = 5.0
uvm_flow.Geom.layer4.Perm.KMax = 100.0
uvm_flow.Geom.layer4.Perm.DelK = 0.2
uvm_flow.Geom.layer4.Perm.MaxNPts = 100
uvm_flow.Geom.layer4.Perm.MaxCpts = 8
uvm_flow.Geom.layer4.Perm.LogNormal = 'Normal'
uvm_flow.Geom.layer4.Perm.StratType = 'Bottom'

#Fine Sand Lens
uvm_flow.Geom.lens.Perm.Type = 'TurnBands'
uvm_flow.Geom.lens.Perm.LambdaX = 0.30
uvm_flow.Geom.lens.Perm.LambdaY = 0.30
uvm_flow.Geom.lens.Perm.LambdaZ = 0.30
uvm_flow.Geom.lens.Perm.GeomMean = 10.89139
uvm_flow.Geom.lens.Perm.Sigma = 2.0664
uvm_flow.Geom.lens.Perm.NumLines = 100
uvm_flow.Geom.lens.Perm.RZeta = 5.0
uvm_flow.Geom.lens.Perm.KMax = 100.0
uvm_flow.Geom.lens.Perm.DelK = 0.2
uvm_flow.Geom.lens.Perm.MaxNPts = 100
uvm_flow.Geom.lens.Perm.MaxCpts = 8
uvm_flow.Geom.lens.Perm.LogNormal = 'Normal'
uvm_flow.Geom.lens.Perm.StratType = 'Bottom'

#Medium Sand Layer 5
uvm_flow.Geom.layer5.Perm.Type = 'TurnBands'
uvm_flow.Geom.layer5.Perm.LambdaX = 0.30
uvm_flow.Geom.layer5.Perm.LambdaY = 0.30
uvm_flow.Geom.layer5.Perm.LambdaZ = 0.30
uvm_flow.Geom.layer5.Perm.GeomMean = 14.142552
uvm_flow.Geom.layer5.Perm.Sigma = 1.4112
uvm_flow.Geom.layer5.Perm.NumLines = 100
uvm_flow.Geom.layer5.Perm.RZeta = 5.0
uvm_flow.Geom.layer5.Perm.KMax = 100.0
uvm_flow.Geom.layer5.Perm.DelK = 0.2
uvm_flow.Geom.layer5.Perm.MaxNPts = 100
uvm_flow.Geom.layer5.Perm.MaxCpts = 8
uvm_flow.Geom.layer5.Perm.LogNormal = 'Normal'
uvm_flow.Geom.layer5.Perm.StratType = 'Bottom'

#K tensor is specified over the whole domain
uvm_flow.Perm.TensorType = 'TensorByGeom'

uvm_flow.Geom.Perm.TensorByGeom.Names = 'domain'

uvm_flow.Geom.domain.Perm.TensorValX = 1.0
uvm_flow.Geom.domain.Perm.TensorValY = 1.0
uvm_flow.Geom.domain.Perm.TensorValZ = 1.0

#-----------------------------------------------------------------------------
# Specific Storage
#-----------------------------------------------------------------------------
# specific storage does not figure into the impes (fully sat) case but we still
# need a key for it
uvm_flow.SpecificStorage.Type = 'Constant'
uvm_flow.SpecificStorage.GeomNames = ''
uvm_flow.Geom.domain.SpecificStorage.Value = 1.0e-4

#-----------------------------------------------------------------------------
# Phases
#-----------------------------------------------------------------------------
uvm_flow.Phase.Names = 'water'

uvm_flow.Phase.water.Density.Type = 'Constant'
uvm_flow.Phase.water.Density.Value = 1.0

uvm_flow.Phase.water.Viscosity.Type = 'Constant'
uvm_flow.Phase.water.Viscosity.Value = 1.0

#-----------------------------------------------------------------------------
# Gravity
#-----------------------------------------------------------------------------
uvm_flow.Gravity = 1.0

#-----------------------------------------------------------------------------
# Contaminants - only needed is advecting
#-----------------------------------------------------------------------------
#This key is needed no matter what
uvm_flow.Contaminants.Names = ''

#-----------------------------------------------------------------------------
# Setup timing info
#-----------------------------------------------------------------------------

#This sets up the stress periods - i.e., the injection well is on for 360 
#steps and off the remaining 120.  Note: PF is smart about this.  It only dumps 
#output for step 360 when the well is turned off, regardless of the values
#entered below.
uvm_flow.TimingInfo.BaseUnit = 1.0
uvm_flow.TimingInfo.StartCount = 0
uvm_flow.TimingInfo.StartTime = 0.0
uvm_flow.TimingInfo.StopTime = 20.0
uvm_flow.TimingInfo.DumpInterval = 1.0

#-----------------------------------------------------------------------------
# Porosity - set similar to MODFLOW/MT3DMS
#-----------------------------------------------------------------------------

uvm_flow.Geom.Porosity.GeomNames = 'domain layer1 layer2'

#Define a porosity of 0.3 throughout the entire domain
uvm_flow.Geom.domain.Porosity.Type = 'Constant'
uvm_flow.Geom.domain.Porosity.Value = 0.300

#Replace layer 1 (gravel) with...
uvm_flow.Geom.layer1.Porosity.Type = 'Constant'
uvm_flow.Geom.layer1.Porosity.Value = 0.600

#Replace layer 2 (silt) with...
uvm_flow.Geom.layer2.Porosity.Type = 'Constant'
uvm_flow.Geom.layer2.Porosity.Value = 0.320

#-----------------------------------------------------------------------------
# Domain - specifies which geometry is the problem domain
#-----------------------------------------------------------------------------
uvm_flow.Domain.GeomName = 'domain'

#-----------------------------------------------------------------------------
# Relative Permeability
#-----------------------------------------------------------------------------

uvm_flow.Phase.RelPerm.Type = 'VanGenuchten'
uvm_flow.Phase.RelPerm.GeomNames = 'domain'
uvm_flow.Geom.domain.RelPerm.Alpha = 0.005
uvm_flow.Geom.domain.RelPerm.N = 2.0

#---------------------------------------------------------
# Saturation
#---------------------------------------------------------

uvm_flow.Phase.Saturation.Type = 'VanGenuchten'
uvm_flow.Phase.Saturation.GeomNames = 'domain'
uvm_flow.Geom.domain.Saturation.Alpha = 0.005
uvm_flow.Geom.domain.Saturation.N = 2.0
uvm_flow.Geom.domain.Saturation.SRes = 0.2
uvm_flow.Geom.domain.Saturation.SSat = 0.99

#-----------------------------------------------------------------------------
# Mobility
#-----------------------------------------------------------------------------
uvm_flow.Phase.water.Mobility.Type = 'Constant'
uvm_flow.Phase.water.Mobility.Value = 1.0

#-----------------------------------------------------------------------------
# Wells - tracer source well
#-----------------------------------------------------------------------------

#This key is needed no matter what
#pfset Wells.Names ""

#Here we define the source well for the tracer - confirmed location on 9-25-08

uvm_flow.Wells.Names = 'B4'
uvm_flow.Wells.B4.InputType = 'Vertical'
uvm_flow.Wells.B4.Action = 'Injection'
uvm_flow.Wells.B4.Type = 'Flux'
uvm_flow.Wells.B4.X = 1.326
uvm_flow.Wells.B4.Y = 0.495
#Just assuming one cell for source
uvm_flow.Wells.B4.ZUpper = 1.35
uvm_flow.Wells.B4.ZLower = 1.25
uvm_flow.Wells.B4.Method = 'Standard'
uvm_flow.Wells.B4.Cycle = 'onoff'
# 
#Source on
# 1500 cm^3/hr or 1.5 L/hr or 0.036 m^3/day
uvm_flow.Wells.B4.on.Flux.water.Value = 0.036
uvm_flow.Wells.B4.on.Saturation.water.Value = 1.0
#Source off
uvm_flow.Wells.B4.off.Flux.water.Value = 0.0
uvm_flow.Wells.B4.off.Saturation.water.Value = 1.0
# 
#-----------------------------------------------------------------------------
# Time Cycles
#-----------------------------------------------------------------------------
uvm_flow.Cycle.Names = 'constant onoff'

uvm_flow.Cycle.constant.Names = 'alltime'
uvm_flow.Cycle.constant.alltime.Length = 1
uvm_flow.Cycle.constant.Repeat = -1

uvm_flow.Cycle.onoff.Names = 'on off'
uvm_flow.Cycle.onoff.on.Length = 15
#Use this for getting the output
CycleOffOutputFileNum = "00015"
uvm_flow.Cycle.onoff.off.Length = 5
uvm_flow.Cycle.onoff.Repeat = -1

#-----------------------------------------------------------------------------
# Boundary Conditions: Pressure
#-----------------------------------------------------------------------------
uvm_flow.BCPressure.PatchNames = 'left right front back bottom top'

#Front boundary - constant head reservoir
uvm_flow.Patch.front.BCPressure.Type = 'DirEquilRefPatch'
uvm_flow.Patch.front.BCPressure.Cycle = 'constant'
uvm_flow.Patch.front.BCPressure.RefGeom = 'domain'
uvm_flow.Patch.front.BCPressure.RefPatch = 'bottom'
uvm_flow.Patch.front.BCPressure.alltime.Value = 2.032

#Back boundary - constant head reservoir
uvm_flow.Patch.back.BCPressure.Type = 'DirEquilRefPatch'
uvm_flow.Patch.back.BCPressure.Cycle = 'constant'
uvm_flow.Patch.back.BCPressure.RefGeom = 'domain'
uvm_flow.Patch.back.BCPressure.RefPatch = 'bottom'
uvm_flow.Patch.back.BCPressure.alltime.Value = 2.007

#Left boundary - no flow
uvm_flow.Patch.left.BCPressure.Type = 'FluxConst'
uvm_flow.Patch.left.BCPressure.Cycle = 'constant'
uvm_flow.Patch.left.BCPressure.alltime.Value = 0.0

#Right boundary - no flow
uvm_flow.Patch.right.BCPressure.Type = 'FluxConst'
uvm_flow.Patch.right.BCPressure.Cycle = 'constant'
uvm_flow.Patch.right.BCPressure.alltime.Value = 0.0

#Bottom boundary - no flow
uvm_flow.Patch.bottom.BCPressure.Type = 'FluxConst'
uvm_flow.Patch.bottom.BCPressure.Cycle = 'constant'
uvm_flow.Patch.bottom.BCPressure.alltime.Value = 0.0

#Top boundary - no flow
uvm_flow.Patch.top.BCPressure.Type = 'FluxConst'
uvm_flow.Patch.top.BCPressure.Cycle = 'constant'
uvm_flow.Patch.top.BCPressure.alltime.Value = 0.0

#---------------------------------------------------------
# Topo slopes in x-direction
#---------------------------------------------------------
# topo slopes do not figure into the impes (fully sat) case but we still
# need keys for them

uvm_flow.TopoSlopesX.Type = 'Constant'
uvm_flow.TopoSlopesX.GeomNames = ''
uvm_flow.TopoSlopesX.Geom.domain.Value = 0.0

#---------------------------------------------------------
# Topo slopes in y-direction
#---------------------------------------------------------

uvm_flow.TopoSlopesY.Type = 'Constant'
uvm_flow.TopoSlopesY.GeomNames = ''
uvm_flow.TopoSlopesY.Geom.domain.Value = 0.0

#---------------------------------------------------------
# Mannings coefficient 
#---------------------------------------------------------
# mannings roughnesses do not figure into the impes (fully sat) case but we still
# need a key for them

uvm_flow.Mannings.Type = 'Constant'
uvm_flow.Mannings.GeomNames = ''
uvm_flow.Mannings.Geom.domain.Value = 0.0

#-----------------------------------------------------------------------------
# Phase sources:
#-----------------------------------------------------------------------------

uvm_flow.PhaseSources.water.Type = 'Constant'
uvm_flow.PhaseSources.water.GeomNames = 'domain'
uvm_flow.PhaseSources.water.Geom.domain.Value = 0.0

#-----------------------------------------------------------------------------
#  Solver Impes  
#-----------------------------------------------------------------------------

uvm_flow.Solver.AbsTol = 1E-20

uvm_flow.Solver.PrintSubsurf = True
uvm_flow.Solver.PrintPressure = True
uvm_flow.Solver.PrintVelocities = True
uvm_flow.Solver.PrintSaturation = True

#-----------------------------------------------------------------------------
# Run and Unload the ParFlow output files
#-----------------------------------------------------------------------------

#Loop through runs
k = 1

##########################
# Seeds
##########################

#Set the random seed to be different for every run
uvm_flow.Geom.layer1.Perm.Seed = [ expr 23586+2*$k ]
uvm_flow.Geom.layer2.Perm.Seed = [ expr 71649+2*$k ]
uvm_flow.Geom.layer3.Perm.Seed = [ expr 46382+2*$k ]
uvm_flow.Geom.layer4.Perm.Seed = [ expr 54987+2*$k ]
uvm_flow.Geom.layer5.Perm.Seed = [ expr 93216+2*$k ]
uvm_flow.Geom.lens.Perm.Seed = [ expr 61329+2*$k ]

##########################
# Run
##########################
# pfrun    $runname
# pfundist $runname

#
# Tests 
#
# source pftest.tcl
passed = 1

# This test is not as stable as some of the others.
# Differnce between optimized and debug version is this large.
# The absolute error is very small however so use a test the 
# checks not only the sig digits but also the absolute value of the difference.
sig_digits = 5
abs_diff = 1e-12

# if ![pftestFile $runname.out.perm_x.pfb "Max difference in perm_x" $sig_digits] {
#     set passed 0
# }
# if ![pftestFile $runname.out.perm_y.pfb "Max difference in perm_y" $sig_digits] {
#     set passed 0
# }
# if ![pftestFile $runname.out.perm_z.pfb "Max difference in perm_z" $sig_digits] {
#     set passed 0
# }

# foreach i "00000 00001" {
#     if ![pftestFile $runname.out.press.$i.pfb "Max difference in Pressure for timestep $i" $sig_digits] {
# 	set passed 0
#     }

#     if ![pftestFileWithAbs $runname.out.phasex.0.$i.pfb "Max difference in phase x for timestep $i" $sig_digits $abs_diff] {
# 	set passed 0
#     }

#     if ![pftestFileWithAbs $runname.out.phasey.0.$i.pfb "Max difference phase y for timestep $i" $sig_digits $abs_diff] {
# 	set passed 0
#     }

#     if ![pftestFileWithAbs $runname.out.phasez.0.$i.pfb "Max difference in phase z for timestep $i" $sig_digits $abs_diff] {
# 	set passed 0
#     }
# }

# if $passed {
#     puts "$runname : PASSED"
# } {
#     puts "$runname : FAILED"
# }
uvm_flow.run()
