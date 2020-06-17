# first version of script to convert the LW_Test tcl script to Python
# need to include pfset function for variables

#import parflow as pf
#import pftools
#import shutil

# copy files from adjacent directory
#shutil.copy("../parflow_input/LW.slopex.pfb", ".")
#shutil.copy("../parflow_input/LW.slopey.pfb", ".")


#run = pf.Run('LW')

#-----------------------------------------------------------------------------
# Set Processor topology
#-----------------------------------------------------------------------------

ProcessTopology = {}
ProcessTopology['P'] = 1
ProcessTopology['Q'] = 1
ProcessTopology['R'] = 1

#-----------------------------------------------------------------------------
# Computational Grid
#-----------------------------------------------------------------------------

ComputationalGrid = {}

ComputationalGrid['Lower'] = {}
ComputationalGrid['Lower']['X'] = 0.0
ComputationalGrid['Lower']['Y'] = 0.0
ComputationalGrid['Lower']['Z'] = 0.0

ComputationalGrid['DX'] = 1000.0
ComputationalGrid['DY'] = 1000.0
ComputationalGrid['DZ'] = 2.0

ComputationalGrid['NX'] = 41
ComputationalGrid['NY'] = 41
ComputationalGrid['NZ'] = 50

#-----------------------------------------------------------------------------
# Names of the GeomInputs
#-----------------------------------------------------------------------------
GeomInput = {}
GeomInput['box_input'] = {}
GeomInput['indi_input'] = {}

#-----------------------------------------------------------------------------
# Domain Geometry Input
#-----------------------------------------------------------------------------
GeomInput['box_input']['InputType'] = 'Box'
GeomInput['box_input']['GeomNames'] = 'domain'

#-----------------------------------------------------------------------------
# Domain Geometry
#-----------------------------------------------------------------------------
Geom = {}
Geom['domain'] = {}

Geom['domain']['Lower'] = {}
Geom['domain']['Lower']['X'] = 0.0
Geom['domain']['Lower']['Y'] = 0.0
Geom['domain']['Lower']['Z'] = 0.0

Geom['domain']['Upper'] = {}
Geom['domain']['Upper']['X'] = 41000.0
Geom['domain']['Upper']['Y'] = 41000.0
Geom['domain']['Upper']['Z'] = 100.0

Geom['domain']['Patches'] = ['x-lower', 'x-upper', 'y-lower', 'y-upper', 'z-lower', 'z-upper']

#-----------------------------------------------------------------------------
# Indicator Geometry Input
#-----------------------------------------------------------------------------
field = ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11', 's12', 's13', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8']
ind_vals = list(range(1,14))
ind_vals.extend(list(range(21,29)))

GeomInput['indi_input']['InputType'] = 'IndicatorField'
GeomInput['indi_input']['GeomNames'] = field
GeomInput['indi_input']['FileName'] = 'IndicatorFile_Gleeson.50z.pfb'

for i in range(len(field)):
    GeomInput[field[i]] = {}
    GeomInput[field[i]]['Value'] = ind_vals[i]
    
#-----------------------------------------------------------------------------
# Permeability (values in m/hr)
#-----------------------------------------------------------------------------

perm_names = ['domain','s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 'g2', 'g3', 'g6', 'g8']
perm_vals = [0.2, 0.269, 0.0436, 0.0158, 0.0075, 0.0182, 0.005, 0.0054, 0.0047, 0.0034, 0.025, 0.059, 0.2, 0.68]

Geom['Perm'] = {}
Geom['Perm']['Names'] = perm_names

for i in range(len(perm_names)):
    Geom[perm_names[i]] = {}
    Geom[perm_names[i]]['Perm'] = {}
    Geom[perm_names[i]]['Perm']['Type'] = 'Constant'
    Geom[perm_names[i]]['Perm']['Value'] = perm_vals[i]
    

print(Geom)

Perm = {}
Perm['TensorType'] = 'TensorByGeom'
Geom['Perm']['TensorByGeom'] = {}
Geom['Perm']['TensorByGeom']['Names'] = 'domain'
Geom['domain']['Perm']['TensorValX'] = 1.0
Geom['domain']['Perm']['TensorValY'] = 1.0
Geom['domain']['Perm']['TensorValZ'] = 1.0




