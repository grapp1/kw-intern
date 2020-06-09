# first version of script to convert the LW_Test tcl script to Python
# need to include pfset function for variables

import parflow as pf
import pftools
import shutil

## copy files from adjacent directory
shutil.copy("../parflow_input/LW.slopex.pfb", ".")
shutil.copy("../parflow_input/LW.slopey.pfb", ".")


run = pf.Run('LW')

run.setProcessTopology(P=1, Q=1, R=1) # 1, 1, 1

run.getComputationalGrid()
  .setDelta(X=1000, Y=1000, Z=2) # or (1, 1, 1)
  .setDimensions(X=41, Y=41, Z=50) # or (100, 1, 50)
  .setLower(X=0, Y=0, Z=0) # or (0, 0, 0) (Origin)

s1 = run.createGeo('s1')
s1.yamlSet('''
Porosity:
  Type: Constant
  Value: 0.4
Perm:
  Type: Constant
  Value: 1
''')

s2 = run.createGeo('s2')
s2.setConstantPorosity(0.25)
  .setConstantPerm(0.6)

s3 = run.createGeo('s3')
run.getGeo('s3')
   .setConstantPorosity(0.3)
   .setConstantPerm(0.2)

run.getGeo('s4').yamlSet('''
Porosity:
  Type: Constant
  Value: 0.35
Perm:
  Type: Constant
  Value: 0.05
''')

boxDomain = run.createDomain(
  'z-upper', 'z-lower',
  'x-lower', 'x-upper',
  'y-lower', 'y-upper'
)

run.addGeomInput(
  pf.Box()
)

run.addGeomInput(
  pf.IndicatorFile(
    FileName='./IndicatorFile_Gleeson.50z.pfb',
    InputType='IndicatorField',
    GeomNames={
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

# Check is the input is valid for possible run
run.validate(Level=DEBUG)

run.writeYAMLConfig('./tmp.yaml')

# pfdist ??
run.run()
run.dist('IndicatorFile_Gleeson.50z.pfb')
