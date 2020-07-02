from parflow import Run

lw = Run('Little Washita')

# -----------------------------------------------------------------------------
# Setup database keys
# -----------------------------------------------------------------------------

# lw.enableLineError()
# lw.enableExitError()

lw.Process.Topology.Q = 1
lw.Process.Topology.P = -1.5

lw.GeomInput.Names = "domain s1 s2"
# lw.GeomInput.Names = ['domain', 's1', 's2']
# lw.GeomInput.s1.X = 10

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

lw.write('./output/demo1_lw.yaml')
lw.write('./output/demo1_lw.pfidb')
lw.write('./output/demo1_lw.json')
