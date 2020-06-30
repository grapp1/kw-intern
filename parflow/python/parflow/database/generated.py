r'''
This file is generated - DO NOT EDIT
'''

from .core import PFDBObj

class Process(PFDBObj):
    def __init__(self):
        self.Topology = Topology()

class Topology(PFDBObj):
    """
    This section describes how processors are
    assigned in order to solve the domain in parallel.
    """
    def __init__(self):
        self.P = 1
        self.Q = 1
        self.R = 1
        self._details = {
            'P': {
                'domain': {
                    'type': 'IntRangeDomain',
                    'kwargs': {
                        'minValue': 1,
                        'maxValue': 1000,
                    }
                },
                'help': '{Type: integer} P allocates the number of processors to the grid cells in x.'
            },
            'Q': {
                'domain': {
                    'type': 'IntRangeDomain',
                    'kwargs': {
                        'minValue': 1,
                        'maxValue': 1000,
                    }
                },
                'help': '{Type: integer} Q allocates the number of processors to the grid cells in y.'
            },
            'R': {
                'domain': {
                    'type': 'IntRangeDomain',
                    'kwargs': {
                        'minValue': 1,
                        'maxValue': 1000,
                    }
                },
                'help': '{Type: integer} R allocates the number of processors to the grid cells in z. Please note R '
                        'should always be 1 if you are running with Solver Richards unless you are running a totally '
                        'saturated domain (solver IMPES).'
            }
        }


class GeomInput(PFDBObj):
    """GeomInput defines all 'geometrical' information needed by ParFlow. For example, the domain, lithology or
    hydrostratigraphic units, faults, initial plume shapes, and so on, are considered geometries.
    """

    def __init__(self):
        self.Names = ''
        self._details = {
            'Names': {
                'domain': {
                    'type': 'AnyStringDomain'
                },
                'help': '{Type: string} This is a list of the geometry input names which define the containers for all '
                        'the geometries defined for this problem. Input names should be separated by spaces.'
            }
        }

    def setnames(self):
        print(self.Names)


class Geom(PFDBObj):
    """This builds off of GeomInput
    """
    def __init__(self, name):
        pass
