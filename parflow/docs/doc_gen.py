# Generator to convert yaml files to RST, eventually importing to readthedocs

import yaml
from datetime import datetime
'''
Example:

YAML:

Process:
  __doc__: >
    run.Process input options are: Topology

  Topology:
    __doc__: >
      [Type: int] Documentation

    P:
      help: >
        [Type: int] P allocates the number of processes to the grid-cells in x.
      default: 1
      domains:
        IntValue:
          minValue: 1


RST:

Process
=========
run.Process input options are: Topology

Process.Topology
------------------------
[Type: int] Documentation

### Process.Topology.P
------------------------

[Type: int] P allocates the number of processes to the grid-cells in x.

:default: 1
:domains: Must be an integer greater than or equal to 1

'''

with open(r'../parflow/database/definitions/core.yaml') as file:
  core = yaml.load(file, Loader=yaml.FullLoader)

# not_keys=['__doc__', 'help', 'domains', 'default']
#
# def keyBuilder(input, not_keys, key_all=None):
#   for key, value in input.items():
#     if isinstance(value, dict):
#       for k in value.keys():
#         # excluding the documentation strings in the key building
#         if k not in not_keys:
#           if key_all == None:
#             key_all = str(k)
#           else:
#             key_all += '.' + str(k)
#           keyBuilder(value, not_keys, key_all)
#           key_all = None
#
#   print(key_all)

class PFKeyDoc:
  def __init__(self, indent=2):
    self.content = [
      "r'''",
      "*************************",
      "ParFlow Key Documentation",
      "*************************",
      f"Generated on {datetime.now().strftime('%Y/%m/%d - %H:%M:%S')}",
      "",
      "'''",
    ]
    self.strIndent = ' '*indent

  def addLine(self, content=''):
    self.content.append(content)

  def write(self, filePath):
    with open(filePath, 'w') as output:
      output.write(self.content)




def keyBuilder(input):

  doc_obj = PFKeyDoc()

  for key in input.keys():
    doc_obj.addLine(f'{key}')
    doc_obj.addLine('=' * len(key))


  return doc_obj


filePath = './pf_keys_test.rst'
doc_keys = keyBuilder(core)
doc_keys.write(filePath)
print(type(filePath))












