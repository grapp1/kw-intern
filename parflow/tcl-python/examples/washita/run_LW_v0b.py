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

LW = DotMap()
#run = pf.Run('LW')

#-----------------------------------------------------------------------------
# Set Processor topology
#-----------------------------------------------------------------------------

LW.Process.Topology.P = 1
LW.Process.Topology.Q = 1
LW.Process.Topology.R = 1

#-----------------------------------------------------------------------------
# Computational Grid
#-----------------------------------------------------------------------------

LW.ComputationalGrid.Lower.X = 0.0
LW.ComputationalGrid.Lower.Y = 0.0
LW.ComputationalGrid.Lower.Z = 0.0

LW.ComputationalGrid.DX = 1000.0
LW.ComputationalGrid.DY = 1000.0
LW.ComputationalGrid.DZ = 2.0

LW.ComputationalGrid.NX = 41
LW.ComputationalGrid.NY = 41
LW.ComputationalGrid.NZ = 50

#-----------------------------------------------------------------------------
# Domain Geometry Input
#-----------------------------------------------------------------------------

LW.GeomInput.box_input.InputType = 'Box'
LW.GeomInput.box_input.GeomName = 'domain'

#-----------------------------------------------------------------------------
# Domain Geometry
#-----------------------------------------------------------------------------

LW.Geom.domain.Lower.X = 0.0
LW.Geom.domain.Lower.Y = 0.0
LW.Geom.domain.Lower.Z = 0.0

LW.Geom.domain.Upper.X = 41000.0
LW.Geom.domain.Upper.Y = 41000.0
LW.Geom.domain.Upper.Z = 100.0

LW.Geom.domain.Patches = dict.fromkeys(['x-lower', 'x-upper', 'y-lower', 'y-upper', 'z-lower', 'z-upper'])

#-----------------------------------------------------------------------------
# Indicator Geometry Input
#-----------------------------------------------------------------------------
field = ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11', 's12', 's13', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8']
ind_vals = list(range(1,14))
ind_vals.extend(list(range(21,29)))

LW.GeomInput.indi_input.InputType = 'IndicatorField'
LW.GeomInput.indi_input.GeomNames = field
LW.Geom.indi_input.FileName = 'IndicatorFile_Gleeson.50z.pfb'
    
for name, val in zip(field, ind_vals):
    LW.GeomInput[name].Value = val
    
#-----------------------------------------------------------------------------
# Permeability (values in m/hr)
#-----------------------------------------------------------------------------

perm_names = ['domain','s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 'g2', 'g3', 'g6', 'g8']
perm_vals = [0.2, 0.269, 0.0436, 0.0158, 0.0075, 0.0182, 0.005, 0.0054, 0.0047, 0.0034, 0.025, 0.059, 0.2, 0.68]

LW.Geom.Perm.Names = perm_names
    
for name, val in zip(perm_names, perm_vals):
    LW.Geom[name].Perm.Type = 'Constant'
    LW.Geom[name].Perm.Value = val

LW.Perm.TensorType = 'TensorByGeom'
LW.Geom.Perm.TensorByGeom.Names = 'domain'
LW.Geom.domain.Perm.TensorValX = 1.0
LW.Geom.domain.Perm.TensorValY = 1.0
LW.Geom.domain.Perm.TensorValZ = 1.0

#-----------------------------------------------------------------------------
# Specific Storage
#-----------------------------------------------------------------------------

LW.SpecificStorage.Type = 'Constant'
LW.SpecificStorage.GeomNames = 'domain'
LW.Geom.domain.SpecificStorage.Value = 1.0e-5

#-----------------------------------------------------------------------------
# Phases
#-----------------------------------------------------------------------------

Phase = DotMap()
LW.Phase.Names = 'water'
LW.Phase.water.Density.Type = 'Constant'
LW.Phase.water.Density.Value = 1.0
LW.Phase.water.Viscosity.Type = 'Constant'
LW.Phase.water.Viscosity.Value = 1.0

#-----------------------------------------------------------------------------
# Contaminants
#-----------------------------------------------------------------------------

LW.Contaminants.Names = ''

#-----------------------------------------------------------------------------
# Gravity
#-----------------------------------------------------------------------------

LW.Gravity = 1.0

#-----------------------------------------------------------------------------
# Timing (time units is set by units of permeability)
#-----------------------------------------------------------------------------

LW.TimingInfo.BaseUnit = 1.0
LW.TimingInfo.StartCount = 0.0
LW.TimingInfo.StartTime = 0.0
LW.TimingInfo.StopTime = 24.0
LW.TimingInfo.DumpInterval = 1.0

LW.TimeStep.Type = 'Constant'
LW.TimeStep.Value = 1.0

#-----------------------------------------------------------------------------
# Porosity
#-----------------------------------------------------------------------------

porosity_names = ['domain','s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9']
porosity_vals = [0.4, 0.375, 0.39, 0.387, 0.439, 0.489, 0.399, 0.384, 0.482, 0.442]

LW.Geom.Porosity.Names = porosity_names

for name, val in zip(porosity_names, porosity_vals):
    LW.Geom[name].Porosity.Type = 'Constant'
    LW.Geom[name].Porosity.Value = val
    
#-----------------------------------------------------------------------------
# Domain
#-----------------------------------------------------------------------------

LW.Domain.GeomName = 'domain'

#----------------------------------------------------------------------------
# Mobility
#----------------------------------------------------------------------------

LW.Phase.water.Mobility.Type = 'Constant'
LW.Phase.water.Mobility.Value = 1.0

#-----------------------------------------------------------------------------
# Wells
#-----------------------------------------------------------------------------

LW.Wells.Names = ''

#-----------------------------------------------------------------------------
# Time Cycles
#-----------------------------------------------------------------------------

LW.Cycle.Names = 'constant'
LW.Cycle.constant.Names = 'alltime'
LW.Cycle.constant.alltime.Length = 1
LW.Cycle.constant.Repeat = -1

#-----------------------------------------------------------------------------
# Boundary Conditions
#-----------------------------------------------------------------------------

LW.BCPressure.PatchNames = Geom.domain.get('Patches')

for key in LW.BCPressure.PatchNames:
    if key == 'z-upper':
        LW.Patch[key].BCPressure.Type = 'OverlandFlow'
    else:
        LW.Patch[key].BCPressure.Type = 'FluxConst'
    LW.Patch[key].BCPressure.Cycle = 'constant'
    LW.Patch[key].BCPressure.alltime.Value = 0.0

#-----------------------------------------------------------------------------
# Topo slopes in x-direction
#-----------------------------------------------------------------------------

LW.TopoSlopesX.Type = 'PFBFile'
LW.TopoSlopesX.GeomNames = 'domain'
LW.TopoSlopesX.FileName = 'LW.slopex.pfb'

#-----------------------------------------------------------------------------
# Topo slopes in y-direction
#-----------------------------------------------------------------------------

LW.TopoSlopesY.Type = 'PFBFile'
LW.TopoSlopesY.GeomNames = 'domain'
LW.TopoSlopesY.FileName = 'LW.slopey.pfb'

#-----------------------------------------------------------------------------
# Mannings coefficient
#-----------------------------------------------------------------------------

LW.Mannings.Type = 'constant'
LW.Mannings.GeomNames = 'domain'
LW.Mannings.Geom.domain.Value = 5.52e-6

# ...
    
    



