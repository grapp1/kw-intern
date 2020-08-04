from parflow import Run

lw = Run('Little Washita')

# -----------------------------------------------------------------------------
# Required for validation
# -----------------------------------------------------------------------------

lw.Process.Topology.P = 1

lw.ComputationalGrid.Lower.X = 1.0
lw.ComputationalGrid.Lower.Y = 1.0
lw.ComputationalGrid.Lower.Z = 1.0

lw.ComputationalGrid.NX = 1
lw.ComputationalGrid.NY = 1
lw.ComputationalGrid.NZ = 1

lw.ComputationalGrid.DX = 1.0
lw.ComputationalGrid.DY = 1.0
lw.ComputationalGrid.DZ = 1.0

lw.TimingInfo.StartTime = 0.0
lw.TimingInfo.StopTime = 10.0
lw.TimingInfo.DumpInterval = 2.0

lw.TimeStep.Type = 'Constant'
lw.TimeStep.Value = 1.0

lw.Domain.GeomName = 'domain'

lw.Gravity = 9.8

lw.KnownSolution = 'Constant'

#---------------------------------------------------------
# The Names of the GeomInputs
#---------------------------------------------------------
lw.GeomInput.Names = "domain_input"


#---------------------------------------------------------
# Domain Geometry Input
#---------------------------------------------------------
lw.GeomInput.domain_input.InputType = 'Box'
lw.GeomInput.domain_input.GeomName = 'domain'

#---------------------------------------------------------
# Domain Geometry
#---------------------------------------------------------
lw.Geom.domain.Lower.X = -10.0
lw.Geom.domain.Lower.Y = 10.0
lw.Geom.domain.Lower.Z = 1.0

lw.Geom.domain.Upper.X = 150.0
lw.Geom.domain.Upper.Y = 170.0
lw.Geom.domain.Upper.Z = 9.0

lw.Geom.domain.Patches = "left right front back bottom top"

# -----------------------------------------------------------------------------
# Setup database keys
# -----------------------------------------------------------------------------

lw.Solver = 'Richards'
lw.Solver.Linear = 'MGSemi'
lw.Solver.Linear.Preconditioner = 'SMG'

lw.Solver.TerrainFollowingGrid = True
lw.Solver.TerrainFollowingGrid.SlopeUpwindFormulation = 'Upwind'

# lw.Geom.domain.RelPerm.Alpha.FileName = 'alpha_file.pfb'
lw.Geom.domain.RelPerm.Alpha = 3.5

# lw.Solver.help()
# print('+'*10)
# lw.help('Solver')

# -----------------------------------------------------------------------------
# Validation process
# -----------------------------------------------------------------------------

print('-'*80)
print('User ask for validation')
print('-'*80)
lw.validate()
print('-'*80)

# lw.write()
# lw.run()

lw.write('./output/value_obj.yaml')
lw.write('./output/value_obj.pfidb')
lw.write('./output/value_obj.json')
