# first version of script to convert the sandtank tcl script to Python
# need to include pfset function for variables
# does not include EcoSLIM

import parflow as pf
import pftools

run = pf.Run('sandtank')

run.setProcessTopology(P=1, Q=1, R=1)

run.getComputationalGrid()
  .setDelta(X=1, Y=1, Z=1) # or (1, 1, 1)
  .setDimensions(X=100, Y=1, Z=50) # or (100, 1, 50)
  .setLower(X=0, Y=0, Z=0) # or (0, 0, 0)

s1 = run.createGeo('s1')
s1.yamlSet('''
Prosity:
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
Prosity:
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
  pf.SolidFile(
    FileName='./SandTank.pfsol',
    Patches=boxDomain,
  )
)

run.addGeomInput(pf.IndicatorFile(
  FileName='./SandTank_Indicator.pfb',
  InputType='IndicatorField',
  GeomNames={
    's1': 1,
    's2': 2,
    's3': 3,
    's4': 4,
  }
))

# Check is the input is valid for possible run
run.validate(Level=DEBUG)

# pfdist ??
run.run()
run.dist('SandTank_Indicator.pfb')

