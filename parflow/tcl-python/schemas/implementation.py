# implementation.py: examples of implementing schemas

# schema_v1
# from schema_v1 import parflow as pf
#
# test1 = pf('test1')
# print(test1.runname)
# print(pf.__doc__)
# test1.pf.Process.Topology.P = 5
# print(test1.pf.Process.Topology.P)





# schema_v2
# from schema_v2 import parflow as pf
# from schema_v2 import PFDict
#
# test2 = pf(runname = 'test2')
# test2 = PFDict(test2.pf)
# print(test2.Process.Topology.R) # autocompletes - prints default value
# test2.Process.Topology.R = 4
# print(test2.Process.Topology.R)




# schema_v3
from schema_v3 import parflow


test3 = parflow()
print(test3.Process.__doc__)
print(test3.Process.Topology.R) # autocompletes - prints default value
test3.Process.Topology.R = 4
print(test3.Process.Topology.R)
