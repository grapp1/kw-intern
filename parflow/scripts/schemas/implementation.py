# implementation.py

from schema_v2 import parflow as pf
from schema_v2 import PFDict

test = pf('test')
print(test.runname)
print(test.pf['Process']['Topology']['R'])
test.pf['Process']['Topology']['R'] = 5
print(test.pf['Process']['Topology']['R'])

a = {'root': 3, 'parent': {'child': 2}}
pf_dict = PFDict(a)
print(pf_dict)
print(pf_dict['root'])

