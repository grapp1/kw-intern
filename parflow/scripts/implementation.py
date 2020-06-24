# implementation.py

from schema import parflow as pf

test = pf('test')
print(test.runname)
test.Process.Topology.R = 9
print(test.Process.Topology.R)
help('schema.parflow.setProcessTopology')

