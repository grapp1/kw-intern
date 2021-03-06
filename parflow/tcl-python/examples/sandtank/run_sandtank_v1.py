# run_sandtank_v1.py
# version of script to convert the sandtank run.tcl script to Python
# similar to run_LW_v1.py

#import parflow as pf
#import pftools
#import shutil

runname = 'sandtank'
run = pf.Run(runname)

#-----------------------------------------------------------------------------
# Set Processor topology
#-----------------------------------------------------------------------------

# replacing the original dictionary value assignments with more compact classes
run.setProcessTopology(P=1, Q=1, R=1)

#-----------------------------------------------------------------------------
# Reading config file
#-----------------------------------------------------------------------------

# similar to the existing config file, this could be a two-column table with
# key variables and values
config = run.getConfig(filename = 'config.txt')

# -----------------------------------------------------------------------------
# Computational Grid
# sandtank actual demensions are 30cm by 15cm
# -----------------------------------------------------------------------------

run.getComputationalGrid()
  .setDelta(X=1.0, Y=1.0, Z=1.0)
  .setDimensions(X=100, Y=1, Z=50)
  .setLower(X=0, Y=0, Z=0)

#-----------------------------------------------------------------------------
# Names of the GeomInputs
#-----------------------------------------------------------------------------

run.addGeomInput(
  pf.SolidFile('solidinput',
         name = 'domain',
         FileName = 'SandTank.pfsol')

domain.setLower(X=0, Y=0, Z=0)
domain.setUpper(X=100.0, Y=1.0, Z=50.0)
domain.setPatches('x-lower', 'x-upper', 'y-lower' 'y-upper', 'z-lower', 'z-upper')

run.addGeomInput(
  pf.IndicatorField(
      'indi_input',
      FileName = 'SandTank_Indicator.pfb'
      GeomNames = {
          's1': 1,
          's2': 2,
          's3': 3,
          's4': 4
          }
    )
)


#-----------------------------------------------------------------------------
# Properties
#-----------------------------------------------------------------------------

# setting properties line-by-line

domain.setConstantPorosity(0.4)
domain.setRelPermAlpha(2.0)
domain.setRelPermN(3.0)
domain.setSaturationAlpha(2.0)
domain.setSaturationN(3.0)
domain.setSaturationSRes(0.2)
domain.setSaturationSSat(1.0)

s1 = run.createGeo('s1')
s1.setConstantPerm(config[k_1]) # getting variable from config file
s1.setConstantPorosity(0.4)

s2 = run.createGeo('s2')
s2.setConstantPerm(config[k_2]) # getting variable from config file
s2.setConstantPorosity(0.25)

s3 = run.createGeo('s3')
s3.setConstantPerm(config[k_3]) # getting variable from config file
s3.setConstantPorosity(0.3)

s4 = run.createGeo('s4')
s4.setConstantPerm(config[k_4]) # getting variable from config file
s4.setConstantPorosity(0.35)

#-----------------------------------------------------------------------------
# Phases
#-----------------------------------------------------------------------------

water = run.Phase('water')
water.setConstant(Density = 1.0,
                  Viscosity = 1.0,
                  Mobility = 1.0)

#-----------------------------------------------------------------------------
# Contaminants
#-----------------------------------------------------------------------------

run.Contaminants('')

#-----------------------------------------------------------------------------
# Gravity
#-----------------------------------------------------------------------------

run.setGravity(1.0)

#-----------------------------------------------------------------------------
# Timing (time units is set by units of permeability)
#-----------------------------------------------------------------------------

run.setTimingInfo(BaseUnit = 1.0,
               StartCount = config['StartNumber'],
               StartTime = 0.0,
               StopTime = config['RunLength'],
               DumpInterval = -1)

run.ConstantTimeStep(1.0)

#-----------------------------------------------------------------------------
# Domain
#-----------------------------------------------------------------------------

run.setDomain('domain')

#-----------------------------------------------------------------------------
# Wells
#-----------------------------------------------------------------------------

# could also assign these keys using an input file
w1 = run.createWell('w1')
w1.setInputType('Vertical')
w1.setType('Flux')
w1.setCoords(X = 11.5,
    Y = 0.5,
    Zupper = 15.9,
    ZLower = 15.1)
w1.Cycle('Constant')
w1.setSaturation(Cycle = 'alltime',
    Phase = 'water',
    Value = 1.0)
w1.setMethod('Standard')
w1.setAction(config['well_1_action'])
w1.setFlux(Cycle = 'alltime',
    Phase = 'water',
    Value = 1.0)


#-----------------------------------------------------------------------------
# Time Cycles
#-----------------------------------------------------------------------------

constant = run.setCycle('constant')
alltime = constant.Names('alltime')
alltime.constant.Length = 1
constant.Repeat = -1

#-----------------------------------------------------------------------------
# Boundary Conditions
#-----------------------------------------------------------------------------

run.setBCPressure(PatchNames = get(domain.setPatches))

for name in PatchNames:
    name.BCPressure(Cycle = 'constant',
                    CycleName = 'alltime')

x-lower.BCPressure(Type = 'DirEquilRefPatch',
    RefGeom = 'domain',
    RefPatch = 'z-lower',
    Value = config['hleft'])

x-upper.BCPressure(Type = 'DirEquilRefPatch',
    RefGeom = 'domain',
    RefPatch = 'z-lower',
    Value = config['hright'])

y-lower.BCPressure(Type = 'FluxConst',
    Value = 0.0)

y-lower.BCPressure(Type = 'FluxConst',
    Value = 0.0)

y-lower.BCPressure(Type = 'FluxConst',
    Value = 0.0)

if config['lake'] == 1:
    z-upper.BCPressure(Type = 'FluxConst', Value = 0.0)
else:
    z-upper.BCPressure(Type = 'OverlandFlow', Value = 0.0)


#-----------------------------------------------------------------------------
# Topo slopes in x-direction
#-----------------------------------------------------------------------------

run.setTopoSlopesX(Type = 'Constant',
                   GeomNames = 'domain',
                   Value = 0.0)

#-----------------------------------------------------------------------------
# Topo slopes in y-direction
#-----------------------------------------------------------------------------

run.setTopoSlopesY(Type = 'Constant',
                   GeomNames = 'domain',
                   Value = 0.05)

#-----------------------------------------------------------------------------
# Mannings coefficient
#-----------------------------------------------------------------------------

domain.setMannings(Type = 'Constant',
                   Value = 5.e-6)

#-----------------------------------------------------------------------------
# Phase sources:
#-----------------------------------------------------------------------------

water.domain.setPhaseSource(Type = 'Constant',
                            Value = 0.0)

# -----------------------------------------------------------------------------
# Exact solution specification for error calculations
# -----------------------------------------------------------------------------

set.KnownSolution = NoKnownSolution

# -----------------------------------------------------------------------------
# Set solver parameters
# -----------------------------------------------------------------------------

run.setOverlandFlowDiffusive(0)
solver = run.setSolver('Richards')
solver.setMaxIter(2500000)

solver.Nonlinear(MaxIter = 100,
                ...)

solver.setOutput(PfbMannings = True,
    PfbSlopes = True,
    Mask = True,
    Velocities = True)

#---------------------------------------------------------
# Initial conditions: water pressure
#---------------------------------------------------------

if config['reset'] == 1:
    run.setICPressure(Type = 'HydroStaticPatch')
    domain.ICPressure(RefPatch = 'z-lower',
                      Value = 30.0)
else:
    run.setICPressure(Type = 'PFBFile')
    fname_ic = f"{runname}.out.press.{config['StartNumber']:05d}.pfb"
    domain.ICPressure(RefPatch = 'z-upper',
                      FileName = fname_ic)
    run.dist(fname_ic)

#----------------------------------------------------------------
# Writing EcoSLIM file - this should be hidden as a function, but shown here for
# completeness
# ---------------------------------------------------------------

print(f'Writing EcoSLIM input file with {runname}')

# works if you already have the slimin.txt file
with open('slimin.txt', 'r') as file:
    data = file.readlines()

data[1] = f'"./{runname}"\n'

if config['reset'] == 1:
    data[6] = '0      !no particles per cell at start of simulation\n'
else:
    data[6] = '-1     !read particle restart file'

data[12] = f'''{config['StartNumber'] + 1}    ! Parflow t1: ParFlow file number to start from (initial condition is pft1-1)\n'''
data[13] = f'''{config['StartNumber'] + config['RunLength']}    ! Parflow t2: ParFlow file number to stop at\n'''

with open('slimin.txt', 'w') as file:
    file.write(''.join(data))

# -----------------------------------------------------------------------------
# Run and Unload the n ParFlow output files
# -----------------------------------------------------------------------------

run.dist('SandTank_Indicator.pfb')

run.run()

run.undist(slopex, slopey, indicator)

print(f'{runname} is done')
