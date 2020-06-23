# run_LW_v1.py
# second version of script to convert the LW_Test tcl script to Python
# v1: making key assignments more pythonic adn object-oriented

#import parflow as pf
#import pftools
#import shutil

# copy files from adjacent directory
#shutil.copy("../parflow_input/LW.slopex.pfb", ".")
#shutil.copy("../parflow_input/LW.slopey.pfb", ".")


run = pf.Run('LW')

#-----------------------------------------------------------------------------
# Set Processor topology
#-----------------------------------------------------------------------------

# replacing the original dictionary value assignments with more compact classes
run.setProcessTopology(P=1, Q=1, R=1)

#-----------------------------------------------------------------------------
# Computational Grid
#-----------------------------------------------------------------------------

run.getComputationalGrid()
  .setDelta(X=1000.0, Y=1000.0, Z=2.0)
  .setDimensions(X=41, Y=41, Z=50)
  .setLower(X=0, Y=0, Z=0)

#-----------------------------------------------------------------------------
# Names of the GeomInputs
#-----------------------------------------------------------------------------

run.addGeomInput(
  pf.Box('box_input',
         name='domain')

domain.setLower(X=0, Y=0, Z=0)
domain.setUpper(X=41000.0, Y=41000.0, Z=100.0)
domain.setPatches('x-lower', 'x-upper', 'y-lower' 'y-upper', 'z-lower', 'z-upper')


# version 1: more readable
run.addGeomInput(
  pf.IndicatorField(
      'indi_input',
      FileName = 'IndicatorFile_Gleeson.50z.pfb'
      GeomNames = {
          's1': 1,
          's2': 2,
          's3': 3,
          's4': 4,
          's5': 5,
          's6': 6,
          's7': 7,
          's8': 8,
          's9': 9,
          's10': 10,
          's11': 11,
          's12': 12,
          's13': 13,
          'g1': 21,
          'g2': 22,
          'g3': 23,
          'g4': 24,
          'g5': 25,
          'g6': 26,
          'g7': 27,
          'g8': 28
          }
    )
)


# version 2: condensed with loops
run.addGeomInput(
  pf.IndicatorField(
      'indi_input',
      FileName = 'IndicatorFile_Gleeson.50z.pfb'
      GeomNames = {f's{i}': i for i in range(1, 14)}
GeomNames.update({f'g{i}': i + 20 for i in range(1, 9)})
    )
)


# version 3: example of function that would allow user to read in a table
# along with the pfb indicator file to establish all geologic properties in domain.

run.addGeomInput(
  pf.ConstantIndicator(ind_file = 'IndicatorFile_Gleeson.50z.pfb',
                       param_file = 'LW_params.csv')
)


#-----------------------------------------------------------------------------
# Properties (not necessary with version 3 above)
#-----------------------------------------------------------------------------

# Option 1: setting properties line-by-line

domain.setConstantPerm(0.2)
domain.setConstantPorosity(0.4)
domain.setRelPermAlpha(2.0)
domain.setRelPermN(3.0)
domain.setSaturationSRes(0.2)
domain.setSaturationSSat(1.0)
domain.setConstSpecificStorage(1.0e-5)
domain.setPermTensor(TensorType = 'TensorByGeom',
                     X = 1.0,
                     Y = 1.0,
                     Z = 1.0)

s1 = run.createGeo('s1')
s1.setConstantPerm(0.269022595)
s1.setConstantPorosity(0.375)
s1.setRelPermAlpha(3.548)
s1.setRelPermN(4.162)
s1.setSaturationSRes(0.000001)
s1.setSaturationSSat(1.0)


# Option 2: setting properties with YAML file or pasting in YAML formatting

run.getGeo('s2').yamlSet('''
    Perm:
      Type: Constant
      Value: 0.043630356
    Porosity:
      Type: Constant
      Value: 0.39
    RelPerm:
      Alpha: 3.467
      N: 2.738
    Saturation:
      Alpha: 3.467
      N: 2.738
      SRes: 0.000001
      SSat: 1.0
    ''')


#-----------------------------------------------------------------------------
# Phases - setting default values for water
#-----------------------------------------------------------------------------

run.Phase('water', default = True)

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
               StartCount = 0.0,
               StartTime = 0.0,
               StopTime = 24.0,
               DumpInterval = 1.0)

run.ConstantTimeStep(1.0)

#-----------------------------------------------------------------------------
# Domain
#-----------------------------------------------------------------------------

run.setDomain('domain')

#-----------------------------------------------------------------------------
# Wells
#-----------------------------------------------------------------------------

run.Wells('')

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
    if name == 'z-upper':
        name.BCPressure(Type = 'OverlandFlow')
    else:
        name.BCPressure(Type = 'FluxConst')
    name.BCPressure(Cycle = 'constant',
                    CycleName = 'alltime',
                    Value = 0.0)

#-----------------------------------------------------------------------------
# Topo slopes
#-----------------------------------------------------------------------------
    
run.setTopoSlopes(Type = 'PFBFile',
                   GeomNames = 'domain',
                   'FileName_X' = 'LW.slopex.pfb',
                   'FileName_Y' = 'LW.slopey.pfb')

#-----------------------------------------------------------------------------
# Mannings coefficient
#-----------------------------------------------------------------------------

domain.setMannings(Type = 'Constant',
                   Value = 5.52e-6)

#----------------------------------------------------------------
# CLM Settings:
# ---------------------------------------------------------------

CLM = run.setLSM('CLM')

CLM.set(CLMFileDir = "clm_output/",
        Print1dOut = False,
        DailyRST = True,
        SingleFile = True,
        CLMDumpInterval = 1,
        MetForcing = 3D,
        MetFileName = 'NLDAS',
        MetFilePath = '../NLDAS/',
        MetFileNT = 24,
        IstepStart = 1,
        EvapBeta = 'Linear',
        VegWaterStress = 'Saturation'
        ResSat = 0.1,
        WiltingPoint = 0.12,
        FieldCapacity = 0.98,
        IrrigationType = None)

#---------------------------------------------------------
# Initial conditions: water pressure
#---------------------------------------------------------

run.setICPressure(Type = 'PFBFile')
domain.ICPressure(RefPatch = 'z-upper',
                  FileName = 'press.init.pfb')

#----------------------------------------------------------------
# Outputs
# ---------------------------------------------------------------

run.write(SiloSubsurfData = True)
run.WriteSiloSubsurfData()
run.WriteSiloPressure()
run.WriteSiloSaturation()
run.WriteSiloSlopes()
run.WriteSiloCLM()
run.WriteSiloMannings()
run.PrintCLM()

#-----------------------------------------------------------------------------
# Distribute, run, undistribute
#-----------------------------------------------------------------------------

run.getComputationalGrid()
  .setDimensions(X=41, Y=41, Z=1)
run.dist(slopex, slopey)

run.getComputationalGrid()
  .setDimensions(X=41, Y=41, Z=50)
run.dist(indicator, ipressure)

run.run()

run.undist(slopex, slopey, indicator)

print('ParFlow run complete')
