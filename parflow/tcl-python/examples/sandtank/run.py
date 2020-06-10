# first version of script to convert the sandtank tcl script to Python
# need to include pfset function for variables
# does not include EcoSLIM

#import parflow
#import pftools
#import numpy as np
#import os

runname = 'sandtank_py'

# -----------------------------------------------------------------------------
# Set Processor topology
# -----------------------------------------------------------------------------

process_topology = {'P': 1,'Q': 1, 'R': 1}

#---------------------------------------------------------
# Computational Grid
#---------------------------------------------------------
ComputationalGrid = {'lower': {'X': 0.0,'Y': 0.0, 'Z': 0.0},
    'delta' : {'DX': 1.0,'DY': 1.0, 'DZ': 1.0},
    'numcells' : {'NX': 100.0,'NY': 1.0, 'NZ': 50.0}}

# -----------------------------------------------------------------------------
# Domain Geometry Input
# -----------------------------------------------------------------------------

Domain_GeomName = 'domain'

# -----------------------------------------------------------------------------
# Names of the GeomInputs (SolidFile and Indicator)
# -----------------------------------------------------------------------------

GeomInput = {'solidinput':{'InputType':'SolidFile',
    'Patches':{'domain': 'z-upper z-lower x-lower x-upper y-lower y-upper'},
    'FileName': 'SandTank.pfsol'},

# s1: gravel, s2: fine sand, s3: coarse sand, s4: clay
    'indi_input':{'InputType':'IndicatorField',
        'GeomNames':{'s1':{'Value': 1},
            's2':{'Value': 2},
            's3':{'Value': 3},
            's4':{'Value': 4}},
        'FileName': 'SandTank_Indicator.pfb'}}

# -----------------------------------------------------------------------------
# Domain Geometry
# -----------------------------------------------------------------------------

DomainGeom = {'Lower': {'X': 0.0,'Y': 0.0, 'Z': 0.0},
    'Upper' : {'X': 100.0,'Y': 1.0, 'Z': 50.0}}

# -----------------------------------------------------------------------------
# Permeability (values in cm/s)
# -----------------------------------------------------------------------------

Perm = {'s1':{'Type': 'Constant',
    'Value': 1.0},
    	's2':{'Type': 'Constant',
    'Value': 0.6},
    	's3':{'Type': 'Constant',
    'Value': 0.2},
    	's4':{'Type': 'Constant',
    'Value': 0.05}}

TensorByGeom = {'domain': {'X': 1.0,'Y': 1.0, 'Z': 1.0}}

# -----------------------------------------------------------------------------
# Specific Storage
# -----------------------------------------------------------------------------

SpecificStorage_Type = 'Constant'
SpecificStorage = {'domain':{'Value': 1.0e-5}}

# -----------------------------------------------------------------------------
# Phases
# -----------------------------------------------------------------------------

PhaseInfo = {'water': {'Density':{'Type': 'Constant','Value': 1.0},
	'Viscosity':{'Type': 'Constant','Value': 1.0},
    'Mobility':{'Type': 'Constant','Value': 1.0}}}

PhaseSources = {'domain':{'Type': 'Constant','Value': 0.0}} ## come back to this

# -----------------------------------------------------------------------------
# Contaminants
# -----------------------------------------------------------------------------

Contaminants = {''}

# -----------------------------------------------------------------------------
# Gravity
# -----------------------------------------------------------------------------

Gravity = 1.0

# -----------------------------------------------------------------------------
# Timing (time units is set by units of permeability)
# -----------------------------------------------------------------------------

TimingInfo = {'BaseUnit': 1.0,
	'DumpInterval': -1,
    'StartCount': 0,
    'StartTime': 0.0,
    'StopTime': 10}

TimeStep = {'Type': 'Constant',
    'Value': 1.0}

# -----------------------------------------------------------------------------
# Porosity
# -----------------------------------------------------------------------------

Porosity = {'domain':{'Type': 'Constant',
    'Value': 0.4},
    	's1':{'Type': 'Constant',
    'Value': 0.4},
    	's2':{'Type': 'Constant',
    'Value': 0.25},
    	's3':{'Type': 'Constant',
    'Value': 0.3},
    	's4':{'Type': 'Constant',
    'Value': 0.35}}

# -----------------------------------------------------------------------------
# Relative Permeability
# -----------------------------------------------------------------------------

RelPerm_Type = 'VanGenuchten'
RelPerm = {'domain':{'Alpha': '2.0',
    'N': 3.0}}

# -----------------------------------------------------------------------------
# Saturation
# -----------------------------------------------------------------------------

Saturation_Type = 'VanGenuchten'
Saturation = {'domain':{'Alpha': '2.0',
    'N': 3.0,
    'SRes': 0.2,
    'SSat': 1.0}}

# -----------------------------------------------------------------------------
# Wells
# -----------------------------------------------------------------------------

Wells = {'w1':{'InputType': 'Vertical',
    'Type': 'Flux',
    'X': 11.5,
    'Y': 0.5,
    'ZUpper': 15.9,
    'ZLower': 15.1,
    'Cycle': 'Constant',
    'Saturation': {'alltime':{'water':{'Value': 1.0}}},
    'Method': 'Flux',
    'Action': 'Flux',
    'Flux': 'Flux',
}}

## add more wells accordingly within Wells dictionary

# -----------------------------------------------------------------------------
# Time Cycles
# -----------------------------------------------------------------------------

Cycle = {'constant':{'alltime':{'Length': 1,
    'Repeat': -1}}}

# -----------------------------------------------------------------------------
# Boundary Conditions
# -----------------------------------------------------------------------------


BCPressure = {'x-lower':{'Type': 'DirEquilRefPatch',
	'Cycle': 'constant',
    'RefGeom': 'domain',
    'RefPatch': 'z-lower',
    'Value': 20.0},
    	'y-lower':{'Type': 'FluxConst',
	'Cycle': 'constant',
    'RefGeom': '',
    'RefPatch': '',
    'Value': 0.0},
    	'z-lower':{'Type': 'FluxConst',
	'Cycle': 'constant',
    'RefGeom': '',
    'RefPatch': '',
    'Value': 0.0},
    	'x-upper':{'Type': 'DirEquilRefPatch',
	'Cycle': 'constant',
    'RefGeom': 'domain',
    'RefPatch': 'z-lower',
    'Value': 20.0},
        'y-upper':{'Type': 'FluxConst',
	'Cycle': 'constant',
    'RefGeom': '',
    'RefPatch': '',
    'Value': 0.0},
        'z-upper':{'Type': 'FluxConst',
	'Cycle': 'constant',
    'RefGeom': '',
    'RefPatch': '',
    'Value': 0.0}}

# -----------------------------------------------------------------------------
# Topo slopes
# -----------------------------------------------------------------------------

Slopes = {'X':{'Type': 'Constant',
	'GeomNames': 'domain',
    'FileName': '',
    'Value': 0.0},
        'Y':{'Type': 'Constant',
    'GeomNames': 'domain',
    'FileName': '',
    'Value': 0.05}}

# -----------------------------------------------------------------------------
# Mannings coefficient
# -----------------------------------------------------------------------------

Mannings_Type = 'Constant'
Mannings = {'domain':{'Value': 5e-6}}

# -----------------------------------------------------------------------------
# Exact solution specification for error calculations
# -----------------------------------------------------------------------------

KnownSolution = 'NoKnownSolution'

# -----------------------------------------------------------------------------
# Set solver parameters
# -----------------------------------------------------------------------------

Solver = { 'Type': 'Richards',
    'MaxIter': 2500000,
    'OverlandFlowDiffusive': 0,
    'Drop': 1e-20,
    'AbsTol': 1e-7,
    'Nonlinear': {'MaxIter':100,
        'ResidualTol':1e-5,
        'EtaValue':0.01,
        'UseJacobian':True,
        'DerivativeEpsilon':1e-8,
        'StepTol':1e-20,
        'Globalization':'LineSearch'
    },
    'Linear': {'KrylovDimension':100,
        'MaxRestarts':5,
        'Preconditioner':'PFMG',
    },
    'WritePfbMannings': True,
    'WritePfbSlopes': True,
    'PrintSubsurf': True,
    'PrintMask': True,
    'PrintVelocities': True
}

# -----------------------------------------------------------------------------
# Initial conditions: water pressure
# -----------------------------------------------------------------------------

# currently not including option for restart file

ICPressure_Type = 'HydroStaticPatch'
ICPressure = {'domain':{'Value': 30.0,
    'RefGeom': 'domain',
    'RefPatch': 'z-lower'}}

# -----------------------------------------------------------------------------
# Run and Unload the ParFlow output files
# -----------------------------------------------------------------------------

#pfdist SandTank_Indicator.pfb

#pfrun     $runname
#pfundist  $runname

#puts "$runname is done"
