# run_LW_v0b.py
# first version of script to convert the LW_Test tcl script to Python
# v0b: using dot notation for dictionary assignment (similar to existing TCL)

#import parflow as pf
#import pftools
#import shutil
from dotmap import DotMap

# copy files from adjacent directory
#shutil.copy("../parflow_input/LW.slopex.pfb", ".")
#shutil.copy("../parflow_input/LW.slopey.pfb", ".")


#run = pf.Run('LW')

#-----------------------------------------------------------------------------
# Set Processor topology
#-----------------------------------------------------------------------------

Process = DotMap()
Process.Topology.P = 1
Process.Topology.Q = 1
Process.Topology.R = 1

#-----------------------------------------------------------------------------
# Computational Grid
#-----------------------------------------------------------------------------

ComputationalGrid = DotMap()

ComputationalGrid.Lower.X = 0.0
ComputationalGrid.Lower.Y = 0.0
ComputationalGrid.Lower.Z = 0.0

ComputationalGrid.DX = 1000.0
ComputationalGrid.DY = 1000.0
ComputationalGrid.DZ = 2.0

ComputationalGrid.NX = 41
ComputationalGrid.NY = 41
ComputationalGrid.NZ = 50

#-----------------------------------------------------------------------------
# Domain Geometry Input
#-----------------------------------------------------------------------------
GeomInput = DotMap()
GeomInput.box_input.InputType = 'Box'
GeomInput.box_input.GeomName = 'domain'

#-----------------------------------------------------------------------------
# Domain Geometry
#-----------------------------------------------------------------------------
Geom = DotMap()

Geom.domain.Lower.X = 0.0
Geom.domain.Lower.Y = 0.0
Geom.domain.Lower.Z = 0.0

Geom.domain.Upper.X = 41000.0
Geom.domain.Upper.Y = 41000.0
Geom.domain.Upper.Z = 100.0

Geom.domain.Patches = dict.fromkeys(['x-lower', 'x-upper', 'y-lower', 'y-upper', 'z-lower', 'z-upper'])

#-----------------------------------------------------------------------------
# Indicator Geometry Input
#-----------------------------------------------------------------------------
field = ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11', 's12', 's13', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8']
ind_vals = list(range(1,14))
ind_vals.extend(list(range(21,29)))

GeomInput.indi_input.InputType = 'IndicatorField'
GeomInput.indi_input.GeomNames = field
Geom.indi_input.FileName = 'IndicatorFile_Gleeson.50z.pfb'
    
for name, val in zip(field, ind_vals):
    GeomInput[name].Value = val
    
#-----------------------------------------------------------------------------
# Permeability (values in m/hr)
#-----------------------------------------------------------------------------

perm_names = ['domain','s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 'g2', 'g3', 'g6', 'g8']
perm_vals = [0.2, 0.269, 0.0436, 0.0158, 0.0075, 0.0182, 0.005, 0.0054, 0.0047, 0.0034, 0.025, 0.059, 0.2, 0.68]

Geom.Perm.Names = perm_names
    
for name, val in zip(perm_names, perm_vals):
    Geom[name].Perm.Type = 'Constant'
    Geom[name].Perm.Value = val

Perm = DotMap()
Perm.TensorType = 'TensorByGeom'
Geom.Perm.TensorByGeom.Names = 'domain'
Geom.domain.Perm.TensorValX = 1.0
Geom.domain.Perm.TensorValY = 1.0
Geom.domain.Perm.TensorValZ = 1.0

#-----------------------------------------------------------------------------
# Specific Storage
#-----------------------------------------------------------------------------

SpecificStorage = DotMap()
SpecificStorage.Type = 'Constant'
SpecificStorage.GeomNames = 'domain'
Geom.domain.SpecificStorage.Value = 1.0e-5

#-----------------------------------------------------------------------------
# Phases
#-----------------------------------------------------------------------------

Phase = DotMap()
Phase.Names = 'water'
Phase.water.Density.Type = 'Constant'
Phase.water.Density.Value = 1.0
Phase.water.Viscosity.Type = 'Constant'
Phase.water.Viscosity.Value = 1.0

#-----------------------------------------------------------------------------
# Contaminants
#-----------------------------------------------------------------------------

Contaminants = DotMap()
Contaminants.Names = ''

#-----------------------------------------------------------------------------
# Gravity
#-----------------------------------------------------------------------------

Gravity = 1.0

#-----------------------------------------------------------------------------
# Timing (time units is set by units of permeability)
#-----------------------------------------------------------------------------

TimingInfo = DotMap()
TimingInfo.BaseUnit = 1.0
TimingInfo.StartCount = 0.0
TimingInfo.StartTime = 0.0
TimingInfo.StopTime = 24.0
TimingInfo.DumpInterval = 1.0

TimeStep = DotMap()
TimeStep.Type = 'Constant'
TimeStep.Value = 1.0

#-----------------------------------------------------------------------------
# Porosity
#-----------------------------------------------------------------------------

porosity_names = ['domain','s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9']
porosity_vals = [0.4, 0.375, 0.39, 0.387, 0.439, 0.489, 0.399, 0.384, 0.482, 0.442]

Geom.Porosity.Names = porosity_names

for name, val in zip(porosity_names, porosity_vals):
    Geom[name].Porosity.Type = 'Constant'
    Geom[name].Porosity.Value = val
    
#-----------------------------------------------------------------------------
# Domain
#-----------------------------------------------------------------------------

Domain = DotMap()
Domain.GeomName = 'domain'

#----------------------------------------------------------------------------
# Mobility
#----------------------------------------------------------------------------

Phase.water.Mobility.Type = 'Constant'
Phase.water.Mobility.Value = 1.0

#-----------------------------------------------------------------------------
# Wells
#-----------------------------------------------------------------------------

Wells = DotMap()
Wells.Names = ''

#-----------------------------------------------------------------------------
# Time Cycles
#-----------------------------------------------------------------------------

Cycle = DotMap()
Cycle.Names = 'constant'
Cycle.constant.Names = 'alltime'
Cycle.constant.alltime.Length = 1
Cycle.constant.Repeat = -1

#-----------------------------------------------------------------------------
# Boundary Conditions
#-----------------------------------------------------------------------------

BCPressure = DotMap()
BCPressure.PatchNames = Geom.domain.get('Patches')

Patch = DotMap()
for key in BCPressure.PatchNames:
    if key == 'z-upper':
        Patch[key].BCPressure.Type = 'OverlandFlow'
    else:
        Patch[key].BCPressure.Type = 'FluxConst'
    Patch[key].BCPressure.Cycle = 'constant'
    Patch[key].BCPressure.alltime.Value = 0.0

#-----------------------------------------------------------------------------
# Topo slopes in x-direction
#-----------------------------------------------------------------------------
    
TopoSlopesX = DotMap()
TopoSlopesX.Type = 'PFBFile'
TopoSlopesX.GeomNames = 'domain'
TopoSlopesX.FileName = 'LW.slopex.pfb'

#-----------------------------------------------------------------------------
# Topo slopes in y-direction
#-----------------------------------------------------------------------------

TopoSlopesY = DotMap()
TopoSlopesY.Type = 'PFBFile'
TopoSlopesY.GeomNames = 'domain'
TopoSlopesY.FileName = 'LW.slopey.pfb'

#-----------------------------------------------------------------------------
# Mannings coefficient
#-----------------------------------------------------------------------------

Mannings = DotMap()
Mannings.Type = 'constant'
Mannings.GeomNames = 'domain'
Mannings.Geom.domain.Value = 5.52e-6


    
    



