# Generator to convert yaml files to markdown

import yaml

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


Markdown:

## Process.Topology.P
*Integer* **[default: 1]**  This allocates the number of processes to the grid-cells in x.
'''

with open(r'../parflow/database/definitions/core.yaml') as file:
  core = yaml.load(file, Loader=yaml.FullLoader)

not_keys=['__doc__', 'help', 'domains', 'default']

def keyBuilder:
  for key, value in core.items():
    if value not in not_keys:
      print(value)

