r'''
--- DO NOT EDIT ---
File automatically generated - any manual change will be lost
Generated on 2020/08/11 - 12:56:46
Created 151 classes
 => We found overlapping classNames (39)
   + Lower was defined 2 times
   + ICSaturation was defined 2 times
   + ICPressure was defined 2 times
   + Perm was defined 3 times
   + SpecificStorage was defined 2 times
   + dzScale was defined 3 times
   + Geom was defined 8 times
   + Porosity was defined 2 times
   + Retardation was defined 2 times
   + RelPerm was defined 2 times
   + Alpha was defined 2 times
   + N was defined 2 times
   + Coeff was defined 2 times
   + CapPressure was defined 2 times
   + Saturation was defined 3 times
   + ThermalConductivity was defined 2 times
   + FBx was defined 2 times
   + FBy was defined 2 times
   + FBz was defined 2 times
   + HeatCapacity was defined 3 times
   + EvapTrans was defined 2 times
   + Pressure was defined 3 times
   + Flux was defined 3 times
   + Concentration was defined 2 times
   + VanGenuchten was defined 2 times
   + BCPressure was defined 2 times
   + BCSaturation was defined 2 times
Defined 431 fields were found
'''
from .core import PFDBObj

# ------------------------------------------------------------------------------

class Process(PFDBObj):
  '''
  run.Process input options are: Topology
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Topology = Topology(self)

# ------------------------------------------------------------------------------

class Topology(PFDBObj):
  '''
  This section describes how processors are assigned in order to solve the domain in parallel.
    - P allocates the number of processes to the grid-cells in x.
    - Q allocates the number of processes to the grid-cells in y.
    - R allocates the number of processes to the grid-cells in z.
  Please note R should always be 1 if you are running with Solver Richards unless you are running a totally saturated domain (solver IMPES).
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.P = 1
    self.Q = 1
    self.R = 1
    self._details = {
      "P": {
        "help": "[Type: int] P allocates the number of processes to the grid-cells in x.\n",
        "default": 1,
        "domains": {
          "MandatoryValue": None,
          "IntValue": {
            "minValue": 1
          }
        }
      },
      "Q": {
        "help": "[Type: int] Q allocates the number of processes to the grid-cells in y.\n",
        "default": 1,
        "domains": {
          "MandatoryValue": None,
          "IntValue": {
            "minValue": 1
          }
        }
      },
      "R": {
        "help": "[Type: int] R allocates the number of processes to the grid-cells in z. Please note R should always be 1 if you are running with Solver Richards unless you are running a totally saturated domain (solver IMPES).\n",
        "default": 1,
        "domains": {
          "MandatoryValue": None,
          "IntValue": {
            "minValue": 1
          }
        }
      }
    }

# ------------------------------------------------------------------------------

class ComputationalGrid(PFDBObj):
  '''
  The computational grid keys set the bottom left corner of the domain to a specific point in space. If using a .pfsol file, the bottom left corner location of the .pfsol file must be the points designated in the computational grid. The user can also assign the x, y and z location to correspond to a specific coordinate system (i.e. UTM). run.ComputationalGrid input options are: Lower.[X, Y, Z], [NX, NY, NZ], [DX, DY, DZ]
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Lower = Lower(self)
    self.NX = None
    self.NY = None
    self.NZ = None
    self.DX = None
    self.DY = None
    self.DZ = None
    self._details = {
      "NX": {
        "help": "[Type: int] This assigns the number of grid cells in the x direction for the computational grid.\n",
        "domains": {
          "MandatoryValue": None,
          "IntValue": {
            "minValue": 1
          }
        }
      },
      "NY": {
        "help": "[Type: int] This assigns the number of grid cells in the y direction for the computational grid.\n",
        "domains": {
          "MandatoryValue": None,
          "IntValue": {
            "minValue": 1
          }
        }
      },
      "NZ": {
        "help": "[Type: int] This assigns the number of grid cells in the z direction for the computational grid.\n",
        "domains": {
          "MandatoryValue": None,
          "IntValue": {
            "minValue": 1
          }
        }
      },
      "DX": {
        "help": "[Type: double] This defines the size of grid cells in the x direction. Units are L and are defined by the units of the hydraulic conductivity used in the problem.\n",
        "domains": {
          "MandatoryValue": None,
          "DoubleValue": {
            "minValue": 0.0
          }
        }
      },
      "DY": {
        "help": "[Type: double] This defines the size of grid cells in the y direction. Units are L and are defined by the units of the hydraulic conductivity used in the problem.\n",
        "domains": {
          "MandatoryValue": None,
          "DoubleValue": {
            "minValue": 0.0
          }
        }
      },
      "DZ": {
        "help": "[Type: double] This defines the size of grid cells in the z direction. Units are L and are defined by the units of the hydraulic conductivity used in the problem.\n",
        "domains": {
          "MandatoryValue": None,
          "DoubleValue": {
            "minValue": 0.0
          }
        }
      }
    }

# ------------------------------------------------------------------------------

class Lower(PFDBObj):
  '''
  This section sets the lower coordinate locations for the computational grid (X, Y, Z).
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.X = None
    self.Y = None
    self.Z = None
    self._details = {
      "X": {
        "help": "[Type: double] This assigns the lower x coordinate location for the computational grid.\n",
        "domains": {
          "MandatoryValue": None,
          "DoubleValue": None
        }
      },
      "Y": {
        "help": "[Type: double] This assigns the lower y coordinate location for the computational grid.\n",
        "domains": {
          "MandatoryValue": None,
          "DoubleValue": None
        }
      },
      "Z": {
        "help": "[Type: double] This assigns the lower z coordinate location for the computational grid.\n",
        "domains": {
          "MandatoryValue": None,
          "DoubleValue": None
        }
      }
    }

# ------------------------------------------------------------------------------

class Domain(PFDBObj):
  '''
  The domain may be represented by any of the solid types in GeomInput.{geom_input_name}.InputType that allow the definition of surface patches. These surface patches are used to define boundary conditions. Subsequently, it is required that the union (or combination) of the defined surface patches equal the entire domain surface. NOTE: This requirement is NOT checked in the code.
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.GeomName = None
    self._details = {
      "GeomName": {
        "help": "[Type: string] This key specifies which of the named geometries is the problem domain.\n",
        "domains": {
          "MandatoryValue": None,
          "AnyString": None
        }
      }
    }

# ------------------------------------------------------------------------------

class ICSaturation(PFDBObj):
  '''
  This section needs to be defined only for multi-phase flow and should not be defined for single-phase and Richards' equation cases.
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Type = None
    self.GeomNames = None
    self._details = {
      "Type": {
        "help": "[Type: string] This key specifies the type of initial condition that will be applied to different geometries for given phase, phase_name. The only key currently available is Constant. The choice Constant will apply constants values within geometries for the phase.\n",
        "domains": {
          "EnumDomain": {
            "enumList": [
              "Constant"
            ]
          }
        }
      },
      "GeomNames": {
        "help": "[Type: string] This key specifies the geometries on which an initial condition will be given if the type is set to Constant. Note that geometries listed later \u201coverlay\u201d geometries listed earlier.\n",
        "domains": {
          "AnyString": None
        }
      }
    }

# ------------------------------------------------------------------------------

class ICPressure(PFDBObj):
  '''
  The keys in this section are used to specify pressure initial conditions for Richards’ equation cases only. These keys will be ignored if any other case is run.
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.GeomNames = None
    self.Type = None
    self._details = {
      "GeomNames": {
        "help": "[Type: string] This key specifies the geometry names on which the initial pressure data will be given. These geometries must comprise the entire domain. Note that conditions for regions that overlap other regions will have unpredictable results. The regions given must be disjoint.\n",
        "domains": {
          "AnyString": None
        }
      },
      "Type": {
        "help": "[Type: string] This key specifies the type of initial condition given. The choices for this key are Constant, HydroStaticDepth, HydroStaticPatch and PFBFile. The choice Constant specifies that the initial pressure will be constant over the regions given. The choice HydroStaticDepth specifies that the initial pressure within a region will be in hydrostatic equilibrium with a given pressure specified at a given depth. The choice HydroStaticPatch specifies that the initial pressure within a region will be in hydrostatic equilibrium with a given pressure on a specified patch. Note that all regions must have the same type of initial data - different regions cannot have different types of initial data. However, the parameters for the type may be different. The PFBFile specification means that the initial pressure will be taken as a spatially varying function given by data in a ParFlow binary (.pfb) file.\n",
        "domains": {
          "EnumDomain": {
            "enumList": [
              "Constant",
              "PFBFile",
              "HydroStaticPatch",
              "NCFile"
            ]
          }
        }
      }
    }

# ------------------------------------------------------------------------------

class GeomInput(PFDBObj):
  '''
  Here we define all “geometrical” information needed by ParFlow. For example, the domain (and patches on the domain where boundary conditions are to be imposed), lithology or hydrostratigraphic units, faults, initial plume shapes, and so on, are considered geometries.
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Names = None
    self._details = {
      "Names": {
        "help": "[Type: string] List of names to use for defining geometry regions\n",
        "domains": {
          "AnyString": None
        },
        "handlers": {
          "GeomInputUpdater": {
            "type": "ChildrenHandler",
            "className": "GeomInputItem",
            "location": "."
          },
          "GeomUpdater": {
            "type": "ChildrenHandler",
            "className": "GeomItem",
            "location": "/Geom"
          }
        }
      }
    }

# ------------------------------------------------------------------------------

class GeomInputItem(PFDBObj):
  '''
  One of the user-defined names for defining a geometry region
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.InputType = None
    self.GeomName = None
    self.GeomNames = None
    self.FileName = None
    self.Value = None
    self._details = {
      "InputType": {
        "help": "[Type: string] This defines the type for the geometry input with the given input name. This key must be one of: SolidFile, IndicatorField, or Box.\n",
        "domains": {
          "EnumDomain": {
            "enumList": [
              "SolidFile",
              "IndicatorField",
              "Box"
            ]
          }
        }
      },
      "GeomName": {
        "help": "[Type: string] This is a name of a single geometry defined by the geometry input. This should be used for a geometry input type of Box, which only requires a single name.\n",
        "domains": {
          "AnyString": None
        },
        "handlers": {
          "GeomInputUpdater": {
            "type": "ChildrenHandler",
            "className": "GeomInputItem",
            "location": ".."
          },
          "GeomUpdater": {
            "type": "ChildrenHandler",
            "className": "GeomItem",
            "location": "/Geom"
          }
        }
      },
      "GeomNames": {
        "help": "[Type: string] This is a list of the names of the geometries defined by the geometry input. For a geometry input type of Box, the singular GeomName should be used. For the SolidFile geometry type this should contain a list with the same number of geometries as were defined using GMS. The order of geometries in the SolidFile should match the names. For IndicatorField types you need to specify the value in the input field which matches the name using GeomInput.geom_input_name.Value.\n",
        "domains": {
          "AnyString": None
        },
        "handlers": {
          "GeomInputUpdater": {
            "type": "ChildrenHandler",
            "className": "GeomInputItem",
            "location": ".."
          },
          "GeomUpdater": {
            "type": "ChildrenHandler",
            "className": "GeomItem",
            "location": "/Geom"
          }
        }
      },
      "FileName": {
        "help": "[Type: string] For IndicatorField and SolidFile geometry inputs, this key specifies the input filename which contains the field or solid information.\n",
        "domains": {
          "AnyString": None,
          "ValidFile": None
        }
      },
      "Value": {
        "help": "[Type: int] For IndicatorField geometry inputs, you need to specify the mapping between values in the input file and the geometry names. The named geometry will be defined wherever the input file is equal to the specified value.\n",
        "domains": {
          "IntValue": None
        }
      }
    }

# ------------------------------------------------------------------------------

class Perm(PFDBObj):
  '''
  run.Perm input options are: TensorType, Conditioning
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Conditioning = Conditioning(self)
    self.TensorType = None
    self._details = {
      "TensorType": {
        "help": "[Type: string] This key specifies whether the permeability tensor entries kx; ky and kz will be specified as three constants within a set of regions covering the domain or whether the entries will be specified cell-wise by files. The choices for this key are TensorByGeom and TensorByFile.\n",
        "domains": {
          "EnumDomain": {
            "enumList": [
              "TensorByGeom",
              "TensorByFile"
            ]
          }
        }
      }
    }

# ------------------------------------------------------------------------------

class Conditioning(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.FileName = 'NA'
    self._details = {
      "FileName": {
        "help": "[Type: string] This key specifies the name of the file that contains the conditioning data. The default string NA indicates that conditioning data is not applicable.\n",
        "default": "NA",
        "domains": {
          "AnyString": None
        }
      }
    }

# ------------------------------------------------------------------------------

class SpecificStorage(PFDBObj):
  '''
  run.Perm input options are: GeomNames, Type
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.GeomNames = None
    self.Type = None
    self._details = {
      "GeomNames": {
        "help": "[Type: string] This key specifies all of the geometries on which a different specific storage value will be assigned. These geometries must cover the entire computational domain.\n",
        "domains": {
          "AnyString": None
        }
      },
      "Type": {
        "help": "[Type: string] This key specifies which method is to be used to assign specific storage data. The only choice currently available is Constant which indicates that a constant is to be assigned to all grid cells within a geometry.\n",
        "domains": {
          "EnumDomain": {
            "enumList": [
              "Constant"
            ]
          }
        }
      }
    }

# ------------------------------------------------------------------------------

class dzScale(PFDBObj):
  '''
  This is where dZ multipliers are assigned within geounits using one of several methods.
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.GeomNames = None
    self.Type = None
    self.nzListNumber = None
    self._details = {
      "GeomNames": {
        "help": "[Type: string] This key specifies which problem domain is being applied a variable dz subsurface. These geometries must cover the entire computational domain.\n",
        "domains": {
          "AnyString": None
        }
      },
      "Type": {
        "help": "[Type: string] This key specifies which method is to be used to assign variable vertical grid spacing. The choices currently available are Constant which indicates that a constant is to be assigned to all grid cells within a geometry, nzList which assigns all layers of a given model to a list value, and PFBFile which reads in values from a distributed pfb file.\n",
        "domains": {
          "AnyString": None
        }
      },
      "nzListNumber": {
        "help": "[Type: int] This key indicates the number of layers with variable dz in the subsurface. This value is the same as the ComputationalGrid.NZ key.\n",
        "domains": {
          "IntValue": {
            "minValue": 1,
            "intoList": True
          }
        },
        "handlers": {
          "nzListNumUpdater": {
            "type": "ChildrenHandler",
            "className": "CellnzItem",
            "location": "../Cell"
          }
        }
      }
    }

# ------------------------------------------------------------------------------

class Cell(PFDBObj):
  '''
  Setting the Cell.nzListNumber.dzScale.Value
  '''

# ------------------------------------------------------------------------------

class CellnzItem(PFDBObj):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.dzScale = dzScale_1(self)

# ------------------------------------------------------------------------------

class dzScale_1(PFDBObj):
  '''
  Setting the Cell.nzListNumber.dzScale.Value
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Value = None
    self._details = {
      "Value": {
        "help": "[Type: double] This key assigns the thickness of each layer defined by nzListNumber. ParFlow assigns the layers from the bottom-up (i.e. the bottom of the domain is layer 0, the top is layer NZ-1). The total domain depth (Geom.domain.Upper.Z) does not change with variable dz. The layer thickness is calculated by ComputationalGrid.DZ *dZScale.\n",
        "domains": {
          "DoubleValue": {
            "minValue": 0.0
          }
        }
      }
    }

# ------------------------------------------------------------------------------

class Geom(PFDBObj):
  '''
  This maps the various properties to the user-defined geometric inputs.
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Perm = Perm_1(self)
    self.Porosity = Porosity(self)
    self.Retardation = Retardation(self)

# ------------------------------------------------------------------------------

class Perm_1(PFDBObj):
  '''
  run.Geom.Perm input options are: Names, TensorByGeom.Names
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.TensorByGeom = TensorByGeom(self)
    self.Names = None
    self._details = {
      "Names": {
        "help": "[Type: string] This key specifies all of the geometries to which a permeability field will be assigned. These geometries must cover the entire computational domain.\n",
        "domains": {
          "AnyString": None
        }
      }
    }

# ------------------------------------------------------------------------------

class TensorByGeom(PFDBObj):
  '''
  run.Geom.Perm.TensorByGeom input options are: Names
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Names = None
    self._details = {
      "Names": {
        "help": "This key specifies all of the geometries to which permeability tensor entries will be assigned. These geometries must cover the entire computational domain.\n",
        "domains": {
          "AnyString": None
        }
      }
    }

# ------------------------------------------------------------------------------

class Porosity(PFDBObj):
  '''
  run.Geom.Porosity input options are: GeomNames
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.GeomNames = None
    self._details = {
      "GeomNames": {
        "help": "[Type: string] This key specifies all of the geometries to which a porosity will be assigned. These geometries must cover the entire computational domain.\n",
        "domains": {
          "AnyString": None
        }
      }
    }

# ------------------------------------------------------------------------------

class Retardation(PFDBObj):
  '''
  run.Geom.Retardation input options are: GeomNames
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.GeomNames = None
    self._details = {
      "GeomNames": {
        "help": "[Type: string] This key specifies all of the geometries to which the contaminants will have a retardation function applied.\n",
        "domains": {
          "AnyString": None
        },
        "handlers": {
          "ContRetNameUpdater": {
            "type": "ChildrenHandler",
            "className": "GeomItem",
            "location": ".."
          }
        }
      }
    }

# ------------------------------------------------------------------------------

class GeomItem(PFDBObj):
  '''
  User-defined geometric instance. GeomItem names are taken from either GeomInput.Names or GeomItem.GeomNames.
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Lower = Lower_1(self)
    self.Upper = Upper(self)
    self.Perm = Perm_2(self)
    self.Porosity = Porosity_1(self)
    self.SpecificStorage = SpecificStorage_1(self)
    self.RelPerm = RelPerm(self)
    self.CapPressure = CapPressure(self)
    self.CapPressurePhase = CapPressurePhase(self)
    self.Saturation = Saturation(self)
    self.dzScale = dzScale_2(self)
    self.ThermalConductivity = ThermalConductivity(self)
    self.FBx = FBx(self)
    self.FBy = FBy(self)
    self.FBz = FBz(self)
    self.HeatCapacity = HeatCapacity(self)
    self.ICPressure = ICPressure_1(self)
    self.ICSaturation = ICSaturation_1(self)
    self.FileName = None
    self.Patches = None
    self._details = {
      "FileName": {
        "help": "[Type: string] This specifies some sort of filename for the specified geometry.\n",
        "domains": {
          "AnyString": None,
          "ValidFile": None
        }
      },
      "Patches": {
        "help": "[Type: string] Patches are defined on the surfaces of geometries. Currently you can only define patches on Box geometries and on the the first geometry in a SolidFile. For a Box the order is fixed (left right front back bottom top) but you can name the sides anything you want.\n",
        "domains": {
          "AnyString": None
        },
        "handlers": {
          "GeomPatchNameUpdater": {
            "type": "ChildrenHandler",
            "className": "GeomItem",
            "location": ".."
          }
        }
      }
    }
    self._dynamic = {
      "GeomContItem": "/Contaminants/Names"
    }
    self.processDynamic()

# ------------------------------------------------------------------------------

class Lower_1(PFDBObj):
  '''
  This section sets the lower coordinate locations for the box geometry.
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.X = None
    self.Y = None
    self.Z = None
    self._details = {
      "X": {
        "help": "[Type: double] This gives the lower X real space coordinate value of the previously specified box geometry of name box_geom_name.\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "Y": {
        "help": "[Type: double] This gives the lower Y real space coordinate value of the previously specified box geometry of name box_geom_name.\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "Z": {
        "help": "[Type: double] This gives the lower Z real space coordinate value of the previously specified box geometry of name box_geom_name.\n",
        "domains": {
          "DoubleValue": None
        }
      }
    }

# ------------------------------------------------------------------------------

class Upper(PFDBObj):
  '''
  This section sets the lower coordinate locations for the box geometry.
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.X = None
    self.Y = None
    self.Z = None
    self._details = {
      "X": {
        "help": "[Type: double] This gives the upper X real space coordinate value of the previously specified box geometry of name box_geom_name.\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "Y": {
        "help": "[Type: double] This gives the upper Y real space coordinate value of the previously specified box geometry of name box_geom_name.\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "Z": {
        "help": "[Type: double] This gives the upper Z real space coordinate value of the previously specified box geometry of name box_geom_name.\n",
        "domains": {
          "DoubleValue": None
        }
      }
    }

# ------------------------------------------------------------------------------

class Perm_2(PFDBObj):
  '''
  Permeability values
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Type = None
    self.Value = None
    self.LambdaX = None
    self.LambdaY = None
    self.LambdaZ = None
    self.GeomMean = None
    self.Sigma = None
    self.Seed = 1
    self.NumLines = 100
    self.RZeta = 5.0
    self.KMax = 100.0
    self.DelK = 0.2
    self.MaxNPts = None
    self.MaxCpts = None
    self.LogNormal = 'LogTruncated'
    self.StratType = 'Bottom'
    self.LowCutoff = None
    self.HighCutoff = None
    self.MaxSearchRad = None
    self.FileName = None
    self.TensorValX = None
    self.TensorValY = None
    self.TensorValZ = None
    self.TensorFileX = None
    self.TensorFileY = None
    self.TensorFileZ = None
    self._details = {
      "Type": {
        "help": "[Type: string] This key specifies which method is to be used to assign permeability data to the named geometry, geometry_name. It must be either Constant, TurnBands, ParGauss, or PFBFile.\n",
        "domains": {
          "EnumDomain": {
            "enumList": [
              "Constant",
              "TurnBands",
              "ParGauss",
              "PFBFile"
            ]
          }
        }
      },
      "Value": {
        "help": "[Type: double] This key specifies the value assigned to all points in the named geometry, geometry_name, if the type was set to constant.\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "LambdaX": {
        "help": "[Type: double] This key specifies the x correlation length of the field generated for the named geometry, geometry_name, if either the Turning Bands or Parallel Gaussian Simulator are chosen.\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "LambdaY": {
        "help": "[Type: double] This key specifies the y correlation length of the field generated for the named geometry, geometry_name, if either the Turning Bands or Parallel Gaussian Simulator are chosen.\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "LambdaZ": {
        "help": "[Type: double] This key specifies the z correlation length of the field generated for the named geometry, geometry_name, if either the Turning Bands or Parallel Gaussian Simulator are chosen.\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "GeomMean": {
        "help": "[Type: double] This key specifies the geometric mean of the log normal field generated for the named geometry, geometry_name, if either the Turning Bands or Parallel Gaussian Simulator are chosen.\n",
        "domains": {
          "DoubleValue": {
            "minValue": 0.0
          }
        }
      },
      "Sigma": {
        "help": "[Type: double] This key specifies the standard deviation of the normal field generated for the named geometry, geometry_name, if either the Turning Bands or Parallel Gaussian Simulator are chosen.\n",
        "domains": {
          "DoubleValue": {
            "minValue": 0.0
          }
        }
      },
      "Seed": {
        "help": "[Type: int] This key specifies the initial seed for the random number generator used to generate the field for the named geometry, geometry_name, if either the Turning Bands or Parallel Gaussian Simulator are chosen. This number must be positive.\n",
        "default": 1,
        "domains": {
          "IntValue": {
            "minValue": 1
          }
        }
      },
      "NumLines": {
        "help": "[Type: int] This key specifies the number of lines to be used in the Turning Bands algorithm for the named geometry, geometry_name.\n",
        "default": 100,
        "domains": {
          "IntValue": {
            "minValue": 1
          }
        }
      },
      "RZeta": {
        "help": "[Type: double] This key specifies the resolution of the line processes, in terms of the minimum grid spacing, to be used in the Turning Bands algorithm for the named geometry, geometry_name. Large values imply high resolution.\n",
        "default": 5.0,
        "domains": {
          "DoubleValue": {
            "minValue": 0.0
          }
        }
      },
      "KMax": {
        "help": "[Type: double] This key specifies the the maximum normalized frequency, Kmax, to be used in the Turning Bands algorithm for the named geometry, geometry_name.\n",
        "default": 100.0,
        "domains": {
          "DoubleValue": {
            "minValue": 0.0
          }
        }
      },
      "DelK": {
        "help": "[Type: double] This key specifies the normalized frequency increment to be used in the Turning Bands algorithm for the named geometry, geometry_name.\n",
        "default": 0.2,
        "domains": {
          "DoubleValue": {
            "minValue": 0.0
          }
        }
      },
      "MaxNPts": {
        "help": "[Type: int] This key sets limits on the number of simulated points in the search neighborhood to be used in the Parallel Gaussian Simulator for the named geometry, geometry_name.\n",
        "domains": {
          "IntValue": {
            "minValue": 1
          }
        }
      },
      "MaxCpts": {
        "help": "[Type: int] This key sets limits on the number of external conditioning points in the search neighborhood to be used in the Parallel Gaussian Simulator for the named geometry, geometry_name.\n",
        "domains": {
          "IntValue": {
            "minValue": 1
          }
        }
      },
      "LogNormal": {
        "help": "[Type: string] The key specifies when a normal, log normal, truncated normal or truncated log normal field is to be generated by the method for the named geometry, geometry_name. This value must be one of Normal, Log, NormalTruncated or LogTruncated and can be used with either Turning Bands or the Parallel Gaussian Simulator.\n",
        "default": "LogTruncated",
        "domains": {
          "EnumDomain": {
            "enumList": [
              "Normal",
              "Log",
              "NormalTruncated",
              "LogTruncated"
            ]
          }
        }
      },
      "StratType": {
        "help": "[Type: string] This key specifies the stratification of the permeability field generated by the method for the named geometry, geometry_name. The value must be one of Horizontal, Bottom or Top and can be used with either the Turning Bands or the Parallel Gaussian Simulator.\n",
        "default": "Bottom",
        "domains": {
          "EnumDomain": {
            "enumList": [
              "Horizontal",
              "Bottom",
              "Top"
            ]
          }
        }
      },
      "LowCutoff": {
        "help": "[Type: double] This key specifies the low cutoff value for truncating the generated field for the named geometry, geometry_name, when either the NormalTruncated or LogTruncated values are chosen.\n",
        "domains": {
          "DoubleValue": {
            "minValue": 0.0
          }
        }
      },
      "HighCutoff": {
        "help": "[Type: double] This key specifies the high cutoff value for truncating the generated field for the named geometry, geometry_name, when either the NormalTruncated or LogTruncated values are chosen.\n",
        "domains": {
          "DoubleValue": {
            "minValue": 0.0
          }
        }
      },
      "MaxSearchRad": {
        "help": "[Type: int] A key to improve correlation structure of RF in testing.\n",
        "domains": {
          "IntValue": {
            "minValue": 1
          }
        }
      },
      "FileName": {
        "help": "[Type: string] This key specifies that permeability values for the specified geometry, geometry_name, are given according to a user-supplied description in the \u201cParFlow Binary\u201d file whose filename is given as the value. For a description of the ParFlow Binary file format, see the manual. The ParFlow Binary file associated with the named geometry must contain a collection of permeability values corresponding in a one-to-one manner to the entire computational grid. That is to say, when the contents of the file are read into the simulator, a complete permeability description for the entire domain is supplied. Only those values associated with computational cells residing within the geometry (as it is represented on the computational grid) will be copied into data structures used during the course of a simulation. Thus, the values associated with cells outside of the geounit are irrelevant. For clarity, consider a couple of different scenarios. For example, the user may create a file for each geometry such that appropriate permeability values are given for the geometry and \u201cgarbage\" values (e.g., some flag value) are given for the rest of the computational domain. In this case, a separate binary file is specified for each geometry. Alternatively, one may place all values representing the permeability field on the union of the geometries into a single binary file. Note that the permeability values must be represented in precisely the same configuration as the computational grid. Then, the same file could be specified for each geounit in the input file. Or, the computational domain could be described as a single geouint (in the ParFlow input file) in which case the permeability values would be read in only once.\n",
        "domains": {
          "AnyString": None
        }
      },
      "TensorValX": {
        "help": "[Type: double] This key specifies the value of kx for the geometry given by geometry_name.\n",
        "domains": {
          "DoubleValue": {
            "minValue": 0.0
          }
        }
      },
      "TensorValY": {
        "help": "[Type: double] This key specifies the value of ky for the geometry given by geometry_name.\n",
        "domains": {
          "DoubleValue": {
            "minValue": 0.0
          }
        }
      },
      "TensorValZ": {
        "help": "[Type: double] This key specifies the value of kz for the geometry given by geometry_name.\n",
        "domains": {
          "DoubleValue": {
            "minValue": 0.0
          }
        }
      },
      "TensorFileX": {
        "help": "[Type: string] This key specifies that kx values for the specified geometry, geometry_name, are given according to a user-supplied description in the \u201cParFlow Binary\u201d file whose filename is given as the value. The only choice for the value of geometry_name is \u201cdomain\u201d.\n",
        "domains": {
          "AnyString": None
        }
      },
      "TensorFileY": {
        "help": "[Type: string] This key specifies that ky values for the specified geometry, geometry_name, are given according to a user-supplied description in the \u201cParFlow Binary\u201d file whose filename is given as the value. The only choice for the value of geometry_name is \u201cdomain\u201d.\n",
        "domains": {
          "AnyString": None
        }
      },
      "TensorFileZ": {
        "help": "[Type: string] This key specifies that kz values for the specified geometry, geometry_name, are given according to a user-supplied description in the \u201cParFlow Binary\u201d file whose filename is given as the value. The only choice for the value of geometry_name is \u201cdomain\u201d.\n",
        "domains": {
          "AnyString": None
        }
      }
    }

# ------------------------------------------------------------------------------

class Porosity_1(PFDBObj):
  '''
  Setting porosity values to elements of domain
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Type = None
    self.Value = None
    self.FileName = None
    self._details = {
      "Type": {
        "help": "[Type: string] This key specifies which method is to be used to assign porosity data to the named geometry, geometry_name. The only choice currently available is Constant which indicates that a constant is to be assigned to all grid cells within a geometry.\n",
        "domains": {
          "EnumDomain": {
            "enumList": [
              "Constant"
            ]
          }
        }
      },
      "Value": {
        "help": "[Type: double] This key specifies the value assigned to all points in the named geometry, geometry_name, if the type was set to constant.\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "FileName": {
        "help": "[Type: string] This key specifies that porosity values for the specified geometry, geometry_name, are given according to a user-supplied description in the \u201cParFlow Binary\u201d file whose filename is given as the value. The only choice for the value of geometry_name is \u201cdomain\u201d.\n",
        "domains": {
          "AnyString": None
        }
      }
    }

# ------------------------------------------------------------------------------

class SpecificStorage_1(PFDBObj):
  '''
  Setting specific storage values to elements of domain
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Value = None
    self._details = {
      "Value": {
        "help": "[Type: double] This key specifies the value assigned to all points in the named geometry, geometry_name, if the type was set to constant.\n",
        "domains": {
          "DoubleValue": None
        }
      }
    }

# ------------------------------------------------------------------------------

class RelPerm(PFDBObj):
  '''
  Setting relative permeability value to geometries
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Alpha = Alpha(self)
    self.N = N(self)
    self.Coeff = Coeff(self)
    self.Value = None
    self.NumSamplePoints = 0
    self.MinPressureHead = None
    self.A = None
    self.Gamma = None
    self.Degree = None
    self.InterpolationMethod = None
    self._details = {
      "Value": {
        "help": "[Type: double] This key specifies the constant relative permeability value on the specified geometry.\n",
        "domains": {
          "DoubleValue": {
            "minValue": 0.0
          }
        }
      },
      "NumSamplePoints": {
        "help": "[Type: int] This key specifies the number of sample points for a spline base interpolation table for the Van Genuchten function specified on geom_name. If this number is 0 (the default) then the function is evaluated directly. Using the interpolation table is faster but is less accurate.\n",
        "default": 0,
        "domains": {
          "IntValue": {
            "minValue": 0
          }
        }
      },
      "MinPressureHead": {
        "help": "[Type: int] This key specifies the lower value for a spline base interpolation table for the Van Genuchten function specified on geom_name. The upper value of the range is 0. This value is used only when the table lookup method is used (NumSamplePoints is greater than 0).\n",
        "domains": {
          "IntValue": None
        }
      },
      "A": {
        "help": "[Type: double] This key specifies the A parameter for the Haverkamp relative permeability on geom_name.\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "Gamma": {
        "help": "[Type: double] This key specifies the gamma parameter for the Haverkamp relative permeability on geom_name.\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "Degree": {
        "help": "[Type: int] This key specifies the degree of the polynomial for the Polynomial relative permeability given on geom_name.\n",
        "domains": {
          "IntValue": None
        }
      },
      "InterpolationMethod": {
        "help": "[Type: string] Specify the interpolation method for the relative permeability.\n",
        "domains": {
          "AnyString": None
        }
      }
    }

# ------------------------------------------------------------------------------

class Alpha(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self._value = None
    self.FileName = None
    self._details = {
      "_value": {
        "help": "[Type: double] This key specifies the alpha parameter for the Van Genuchten function specified on geom_name.\n",
        "domains": {
          "DoubleValue": {
            "minValue": 0.0
          }
        }
      },
      "FileName": {
        "help": "[Type: string] This key specifies a pfb filename containing the alpha parameters for the VanGenuchten function cell-by-cell. The ONLY option for geom_name is \"domain.\"\n",
        "domains": {
          "AnyString": None
        }
      }
    }

# ------------------------------------------------------------------------------

class N(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self._value = None
    self.FileName = None
    self._details = {
      "_value": {
        "help": "[Type: double] This key specifies the alpha parameter for the Van Genuchten function specified on geom_name.\n",
        "domains": {
          "DoubleValue": {
            "minValue": 0.0
          }
        }
      },
      "FileName": {
        "help": "[Type: string] This key specifies a pfb filename containing the N parameters for the VanGenuchten function cell-by-cell. The ONLY option for geom_name is \"domain.\"\n",
        "domains": {
          "AnyString": None
        }
      }
    }

# ------------------------------------------------------------------------------

class Coeff(PFDBObj):
  '''
  Setting the coefficients for the polynomial relative permeability curve.
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Coeff_number = None
    self._details = {
      "Coeff_number": {
        "__rst__": {
          "name": "Geom.{geom_name}.RelPerm.Coeff.{coeff_number}"
        },
        "help": "[Type: double] This key specifies the 'coeff_number'th coefficient of the Polynomial relative permeability given on geom_name.\n",
        "domains": {
          "DoubleValue": None
        }
      }
    }

# ------------------------------------------------------------------------------

class CapPressure(PFDBObj):
  '''
  Setting capillary pressures for specified geometries
  '''

# ------------------------------------------------------------------------------

class CapPressurePhase(PFDBObj):
  '''
  Setting phase name for capillary pressure of a specified geometry.
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Value = 0.0
    self._details = {
      "Value": {
        "__rst__": {
          "name": "Geom.{geom_name}.CapPressure.{phase_name}.Value"
        },
        "help": "[Type: double] This key specifies the value of the capillary pressure in the named geometry, geometry_name, for the named phase, phase_name. IMPORTANT NOTE: the code currently works only for capillary pressure equal zero.\n",
        "default": 0.0,
        "domains": {
          "DoubleValue": None
        }
      }
    }

# ------------------------------------------------------------------------------

class Saturation(PFDBObj):
  '''
  Setting saturation values to geometries
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Alpha = Alpha_1(self)
    self.N = N_1(self)
    self.SRes = SRes(self)
    self.SSat = SSat(self)
    self.Coeff = Coeff_1(self)
    self.Value = None
    self.A = None
    self.Gamma = None
    self.Degree = None
    self.FileName = None
    self._details = {
      "Value": {
        "help": "[Type: double] This key specifies the constant saturation value on the specified geometry.\n",
        "domains": {
          "DoubleValue": {
            "minValue": 0.0,
            "maxValue": 1.0
          }
        }
      },
      "A": {
        "help": "[Type: double] This key specifies the A parameter for the Haverkamp saturation on geom_name.\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "Gamma": {
        "help": "[Type: double] This key specifies the gamma parameter for the Haverkamp saturation on geom_name.\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "Degree": {
        "help": "[Type: int] This key specifies the degree of the polynomial for the Polynomial saturation given on geom_name.\n",
        "domains": {
          "IntValue": None
        }
      },
      "FileName": {
        "help": "[Type: string] This key specifies the name of the file containing saturation values for the domain. It is assumed that geom_name is \u201cdomain\u201d for this key.\n",
        "domains": {
          "AnyString": None
        }
      }
    }

# ------------------------------------------------------------------------------

class Alpha_1(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self._value = None
    self.FileName = None
    self._details = {
      "_value": {
        "help": "[Type: double] This key specifies the alpha parameter for the Van Genuchten function specified on geom_name.\n",
        "domains": {
          "DoubleValue": {
            "minValue": 0.0
          }
        }
      },
      "FileName": {
        "help": "[Type: string] This key specifies a pfb filename containing the alpha parameters for the VanGenuchten function cell-by-cell. The ONLY option for geom_name is \"domain.\"\n",
        "domains": {
          "AnyString": None
        }
      }
    }

# ------------------------------------------------------------------------------

class N_1(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self._value = None
    self.FileName = None
    self._details = {
      "_value": {
        "help": "[Type: double] This key specifies the alpha parameter for the Van Genuchten function specified on geom_name.\n",
        "domains": {
          "DoubleValue": {
            "minValue": 0.0
          }
        }
      },
      "FileName": {
        "help": "[Type: string] This key specifies a pfb filename containing the N parameters for the VanGenuchten function cell-by-cell. The ONLY option for geom_name is \"domain.\"\n",
        "domains": {
          "AnyString": None
        }
      }
    }

# ------------------------------------------------------------------------------

class SRes(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self._value = None
    self.Filename = None
    self._details = {
      "_value": {
        "help": "[Type: double] This key specifies the residual saturation on geom_name.\n",
        "domains": {
          "DoubleValue": {
            "minValue": 0.0,
            "maxValue": 1.0
          }
        }
      },
      "Filename": {
        "help": "[Type: string] This key specifies a pfb filename containing the residual saturation parameters for the VanGenuchten function cell-by-cell. The ONLY option for geom_name is \"domain.\"\n",
        "domains": {
          "AnyString": None
        }
      }
    }

# ------------------------------------------------------------------------------

class SSat(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self._value = None
    self.FileName = None
    self._details = {
      "_value": {
        "help": "[Type: double] This key specifies the saturation at saturated conditions on geom_name.\n",
        "domains": {
          "DoubleValue": {
            "minValue": 0.0,
            "maxValue": 1.0
          }
        }
      },
      "FileName": {
        "help": "[Type: string] This key specifies a pfb filename containing the SSat parameters for the VanGenuchten function cell-by-cell. The ONLY option for geom_name is \"domain.\"\n",
        "domains": {
          "AnyString": None
        }
      }
    }

# ------------------------------------------------------------------------------

class Coeff_1(PFDBObj):
  '''
  Setting the coefficients for the polynomial saturation curve.
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Coeff_number = None
    self._details = {
      "Coeff_number": {
        "__rst__": {
          "name": "Geom.{geom_name}.Saturation.Coeff.{coeff_number}"
        },
        "help": "[Type: double] This key specifies the 'coeff_number'th coefficient of the Polynomial saturation given on geom_name.\n",
        "domains": {
          "DoubleValue": None
        }
      }
    }

# ------------------------------------------------------------------------------

class dzScale_2(PFDBObj):
  '''
  Setting properties for the dz Scale.
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Value = None
    self.FileName = None
    self._details = {
      "Value": {
        "help": "[Type: double] This key specifies the value assigned to all points in the named geometry, geometry_name, if the type was set to constant.\n",
        "domains": {
          "DoubleValue": {
            "minValue": 0.0
          }
        }
      },
      "FileName": {
        "help": "[Type: string] This key specifies file to be read in for variable dz values for the given geometry, geometry_name, if the type was set to PFBFile.\n",
        "domains": {
          "AnyString": None
        }
      }
    }

# ------------------------------------------------------------------------------

class ThermalConductivity(PFDBObj):
  '''
  Setting thermal conductivity values for various geometries
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.KDry = KDry(self)
    self.KWet = KWet(self)
    self.Value = None
    self._details = {
      "Value": {
        "help": "[Type: double] This key specifies the thermal conductivity value on the specified geometry.\n",
        "domains": {
          "DoubleValue": {
            "minValue": 0.0
          }
        }
      }
    }

# ------------------------------------------------------------------------------

class KDry(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self._value = None
    self.FileName = None
    self._details = {
      "_value": {
        "help": "[Type: double] This key specifies the thermal conductivity under dry conditions on geom_name.\n",
        "domains": {
          "DoubleValue": {
            "minValue": 0.0
          }
        }
      },
      "FileName": {
        "help": "[Type: string] This key specifies a pfb filename containing the dry thermal conductivity function cell-by-cell. The ONLY option for geom_name is \"domain.\"\n",
        "domains": {
          "AnyString": None
        }
      }
    }

# ------------------------------------------------------------------------------

class KWet(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self._value = None
    self.FileName = None
    self._details = {
      "_value": {
        "help": "[Type: double] This key specifies the thermal conductivity under saturated conditions on geom_name.\n",
        "domains": {
          "DoubleValue": {
            "minValue": 0.0
          }
        }
      },
      "FileName": {
        "help": "[Type: string] This key specifies a pfb filename containing the wet thermal conductivity function cell-by-cell. The ONLY option for geom_name is \"domain.\"\n",
        "domains": {
          "AnyString": None
        }
      }
    }

# ------------------------------------------------------------------------------

class FBx(PFDBObj):
  '''
  Setting file name for flow barriers in X. FBx.Type must equal PFBFile.
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.FileName = None
    self._details = {
      "FileName": {
        "help": "[Type: string] This key specifies file to be read in for the X flow barrier values for the domain, if the type was set to PFBFile.\n",
        "domains": {
          "AnyString": None
        }
      }
    }

# ------------------------------------------------------------------------------

class FBy(PFDBObj):
  '''
  Setting file name for flow barriers in Y. FBy.Type must equal PFBFile.
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.FileName = None
    self._details = {
      "FileName": {
        "help": "[Type: string] This key specifies file to be read in for the Y flow barrier values for the domain, if the type was set to PFBFile.\n",
        "domains": {
          "AnyString": None
        }
      }
    }

# ------------------------------------------------------------------------------

class FBz(PFDBObj):
  '''
  Setting file name for flow barriers in Z. FBz.Type must equal PFBFile.
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.FileName = None
    self._details = {
      "FileName": {
        "help": "[Type: string] This key specifies file to be read in for the Z flow barrier values for the domain, if the type was set to PFBFile.\n",
        "domains": {
          "AnyString": None
        }
      }
    }

# ------------------------------------------------------------------------------

class HeatCapacity(PFDBObj):
  '''
  Setting heat capacity properties for specified geometries.
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Value = None
    self._details = {
      "Value": {
        "help": "[Type: double] This key specifies the heat capacity of the given geometry. Units are J*g^-1*C^-1.\n",
        "domains": {
          "DoubleValue": {
            "minValue": 0.0
          }
        }
      }
    }

# ------------------------------------------------------------------------------

class ICPressure_1(PFDBObj):
  '''
  Setting the initial conditions for pressure for specific geometries.
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.FileName = None
    self.RefElevation = None
    self.RefGeom = None
    self.RefPatch = None
    self.Value = None
    self._details = {
      "FileName": {
        "help": "This key specifies the name of the file containing pressure values for the domain. It is assumed that geom_name is \u201cdomain\u201d for this key.\n",
        "domains": {
          "AnyString": None
        }
      },
      "RefElevation": {
        "help": "[Type: double] This key specifies the reference elevation on which the reference pressure is given for type HydroStaticDepth initial pressures.\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "RefGeom": {
        "help": "[Type: string] This key specifies the geometry on which the reference patch resides for type HydroStaticPatch initial pressures.\n",
        "domains": {
          "AnyString": None
        }
      },
      "RefPatch": {
        "help": "[Type: string] This key specifies the patch on which the reference pressure is given for type HydorStaticPatch initial pressures.\n",
        "domains": {
          "AnyString": None
        }
      },
      "Value": {
        "help": "[Type: double] This key specifies the initial pressure value for type Constant initial pressures and the reference pressure value for types HydroStaticDepth and HydroStaticPatch.\n",
        "domains": {
          "DoubleValue": None
        }
      }
    }

# ------------------------------------------------------------------------------

class ICSaturation_1(PFDBObj):
  '''
  '''

# ------------------------------------------------------------------------------

class GeomICSaturationPhaseItem(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Value = None
    self._details = {
      "Value": {
        "help": "[Type: double] This key specifies the initial condition value assigned to all points in the named geometry, geom_input_name, if the type was set to Constant.\n",
        "domains": {
          "DoubleValue": None
        }
      }
    }

# ------------------------------------------------------------------------------

class GeomContItem(PFDBObj):
  '''
  Setting retardation properties for specific contaminants and specific geometries
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Retardation = Retardation_1(self)

# ------------------------------------------------------------------------------

class Retardation_1(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Type = None
    self.Value = None
    self.Rate = None
    self._details = {
      "Type": {
        "help": "[Type: string] This key specifies which function is to be used to compute the retardation for the named contaminant, contaminant_ name, in the named geometry, geometry_name. The only choice currently available is Linear which indicates that a simple linear retardation function is to be used to compute the retardation.\n",
        "domains": {
          "EnumDomain": {
            "enumList": [
              "Linear"
            ]
          }
        }
      },
      "Value": {
        "help": "[Type: double] This key specifies the distribution coefficient for the linear function used to compute the retardation of the named contaminant, contaminant_name, in the named geometry, geometry_name. The value should be scaled by the density of the material in the geometry.\n",
        "domains": {
          "DoubleValue": {
            "minValue": 0.0
          }
        }
      },
      "Rate": {
        "help": "[Type: double] This key specifies the distribution coefficient for the linear function used to compute the retardation of the named contaminant, contaminant_name, in the named geometry, geometry_name. The value should be scaled by the density of the material in the geometry.\n",
        "domains": {
          "DoubleValue": {
            "minValue": 0.0
          }
        }
      }
    }

# ------------------------------------------------------------------------------

class TopoSlopes(PFDBObj):
  '''
  Setting filename for elevation data from which ParFlow will calculate slopes
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Elevation = Elevation(self)

# ------------------------------------------------------------------------------

class Elevation(PFDBObj):
  '''
  Setting filename for elevation data from which ParFlow will calculate slopes
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.FileName = None
    self._details = {
      "FileName": {
        "help": "[Type: string] This key is the name of the PFB file that contains elevations which ParFlow uses to derive slopes. This is optional but can be useful when post-processing terrain-following grids.\n",
        "domains": {
          "Anystring": None
        }
      }
    }

# ------------------------------------------------------------------------------

class TopoSlopesX(PFDBObj):
  '''
  Setting data for domain slopes in the X direction
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Geom = Geom_1(self)
    self.GeomNames = None
    self.Type = None
    self.FileName = None
    self._details = {
      "GeomNames": {
        "help": "[Type: string] This key specifies all of the geometries on which a different x topographic slope values will be assigned. Topographic slopes may be assigned by PFBFile or as Constant by geometry. These geometries must cover the entire upper surface of the computational domain.\n",
        "domains": {
          "AnyString": None
        },
        "handlers": {
          "TopoSlopesXUpdater": {
            "type": "ChildrenHandler",
            "className": "TopoSlopesXItem",
            "location": "./Geom"
          }
        }
      },
      "Type": {
        "help": "[Type: string] This key specifies which method is to be used to assign topographic slopes. The choices currently available are Constant which indicates that a constant is to be assigned to all grid cells within a geometry and PFBFile which indicates that all values are read in from a distributed, grid-based ParFlow binary file. If NetCDF is used, NCFile can be specified, which will read in slopes from a NetCDF file.\n",
        "domains": {
          "EnumDomain": {
            "enumList": [
              "Constant",
              "PFBFile",
              "NCFile"
            ]
          }
        }
      },
      "FileName": {
        "help": "[Type: string] This key specifies the value assigned to all points be read in from a ParFlow binary file.\n",
        "domains": {
          "AnyString": None
        }
      }
    }

# ------------------------------------------------------------------------------

class Geom_1(PFDBObj):
  '''
  '''

# ------------------------------------------------------------------------------

class TopoSlopesXItem(PFDBObj):
  '''
  Setting value for slopes in the X direction
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Value = None
    self._details = {
      "Value": {
        "help": "[Type: double] This key specifies the value assigned to all points in the named geometry, geometry_name, if the type was set to constant.\n",
        "domains": {
          "DoubleValue": None
        }
      }
    }

# ------------------------------------------------------------------------------

class TopoSlopesY(PFDBObj):
  '''
  Setting data for domain slopes in the Y direction
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Geom = Geom_2(self)
    self.GeomNames = None
    self.Type = None
    self.FileName = None
    self._details = {
      "GeomNames": {
        "help": "[Type: string] This key specifies all of the geometries on which a different y topographic slope values will be assigned. Topographic slopes may be assigned by PFBFile or as Constant by geometry. These geometries must cover the entire upper surface of the computational domain.\n",
        "domains": {
          "AnyString": None
        },
        "handlers": {
          "TopoSlopesYUpdater": {
            "type": "ChildrenHandler",
            "className": "TopoSlopesYItem",
            "location": "./Geom"
          }
        }
      },
      "Type": {
        "help": "[Type: string] This key specifies which method is to be used to assign topographic slopes. The choices currently available are Constant which indicates that a constant is to be assigned to all grid cells within a geometry and PFBFile which indicates that all values are read in from a distributed, grid-based ParFlow binary file. If NetCDF is used, NCFile can be specified, which will read in slopes from a NetCDF file.\n",
        "domains": {
          "EnumDomain": {
            "enumList": [
              "Constant",
              "PFBFile",
              "NCFile"
            ]
          }
        }
      },
      "FileName": {
        "help": "[Type: string] This key specifies the value assigned to all points be read in from a ParFlow binary file.\n",
        "domains": {
          "AnyString": None
        }
      }
    }

# ------------------------------------------------------------------------------

class Geom_2(PFDBObj):
  '''
  '''

# ------------------------------------------------------------------------------

class TopoSlopesYItem(PFDBObj):
  '''
  Setting value for slopes in the Y direction
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Value = None
    self._details = {
      "Value": {
        "help": "[Type: double] This key specifies the value assigned to all points in the named geometry, geometry_name, if the type was set to constant.\n",
        "domains": {
          "DoubleValue": None
        }
      }
    }

# ------------------------------------------------------------------------------

class CapPressure_1(PFDBObj):
  '''
  Setting capillary pressures for different phases
  '''

# ------------------------------------------------------------------------------

class CapPressurePhaseItem(PFDBObj):
  '''
  Phase name on which capillary pressure will be specified.
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Type = 'Constant'
    self.GeomNames = None
    self._details = {
      "Type": {
        "help": "[Type: string] This key specifies the capillary pressure between phase 0 and the named phase, phase_name. The only choice available is Constant which indicates that a constant capillary pressure exists between the phases.\n",
        "default": "Constant",
        "domains": {
          "EnumDomain": {
            "enumList": [
              "Constant"
            ]
          }
        }
      },
      "GeomNames": {
        "help": "[Type: string] This key specifies the geometries that capillary pressures will be computed for in the named phase, phase_name. Regions listed later \u201coverlay\u201d regions listed earlier. Any geometries not listed will be assigned 0:0 capillary pressure by ParFlow.\n",
        "domains": {
          "AnyString": None
        }
      }
    }

# ------------------------------------------------------------------------------

class Mannings(PFDBObj):
  '''
  Here, Manning's roughness values (n) are assigned to the upper boundary of the domain.
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Geom = Geom_3(self)
    self.GeomNames = None
    self.Type = None
    self.FileName = None
    self._details = {
      "GeomNames": {
        "help": "[Type: string] This key specifies all of the geometries on which a different Mannings roughness value will be assigned. Mannings values may be assigned by PFBFile or as Constant by geometry. These geometries must cover the entire upper surface of the computational domain.\n",
        "domains": {
          "AnyString": None
        },
        "handlers": {
          "ManningsGeomUpdater": {
            "type": "ChildrenHandler",
            "className": "ManningsGeomItem",
            "location": "./Geom"
          }
        }
      },
      "Type": {
        "help": "[Type: string] This key specifies which method is to be used to assign Mannings roughness data. The choices currently available are Constant which indicates that a constant is to be assigned to all grid cells within a geometry and PFBFile which indicates that all values are read in from a distributed, grid-based ParFlow binary file.\n",
        "domains": {
          "EnumDomain": {
            "enumList": [
              "Constant",
              "PFBFile"
            ]
          }
        }
      },
      "FileName": {
        "help": "[Type: string] This key specifies the name of the ParFlow binary file with Manning's values.\n",
        "domains": {
          "AnyString": None
        }
      }
    }

# ------------------------------------------------------------------------------

class Geom_3(PFDBObj):
  '''
  '''

# ------------------------------------------------------------------------------

class ManningsGeomItem(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Value = None
    self._details = {
      "Value": {
        "help": "[Type: double] This key specifies the value assigned to all points in the named geometry, geometry_name, if the type was set to constant.\n",
        "domains": {
          "DoubleValue": None
        }
      }
    }

# ------------------------------------------------------------------------------

class FBx_1(PFDBObj):
  '''
  Setting FBx.Type
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Type = None
    self._details = {
      "Type": {
        "help": "[Type: string] This key specifies which method is to be used to assign flow barriers in X. The only choice currently available is PFBFile which reads in values from a distributed pfb file.\n",
        "domains": {
          "EnumDomain": {
            "enumList": [
              "PFBFile"
            ]
          }
        }
      }
    }

# ------------------------------------------------------------------------------

class FBy_1(PFDBObj):
  '''
  Setting FBy.Type
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Type = None
    self._details = {
      "Type": {
        "help": "[Type: string] This key specifies which method is to be used to assign flow barriers in Y. The only choice currently available is PFBFile which reads in values from a distributed pfb file.\n",
        "domains": {
          "EnumDomain": {
            "enumList": [
              "PFBFile"
            ]
          }
        }
      }
    }

# ------------------------------------------------------------------------------

class FBz_1(PFDBObj):
  '''
  Setting FBz.Type
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Type = None
    self._details = {
      "Type": {
        "help": "[Type: string] This key specifies which method is to be used to assign flow barriers in Z. The only choice currently available is PFBFile which reads in values from a distributed pfb file.\n",
        "domains": {
          "EnumDomain": {
            "enumList": [
              "PFBFile"
            ]
          }
        }
      }
    }

# ------------------------------------------------------------------------------

class Solver(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self._value = 'Impes'
    self.CLM = CLM(self)
    self.EvapTrans = EvapTrans(self)
    self.OverlandDiffusive = OverlandDiffusive(self)
    self.OverlandKinematic = OverlandKinematic(self)
    self.TerrainFollowingGrid = TerrainFollowingGrid(self)
    self.Linear = Linear(self)
    self.Nonlinear = Nonlinear(self)
    self.AbsTol = 1e-09
    self.AdvectOrder = 2
    self.BetaFluid = None
    self.BetaFracture = None
    self.BetaPerm = None
    self.BetaPore = None
    self.BoxSizePowerOf2 = None
    self.CFL = 0.7
    self.CoarseSolve = None
    self.CompCompress = None
    self.DiagScale = None
    self.DiagSolver = None
    self.Drop = 1e-08
    self.DropTol = None
    self.EvapTransFile = False
    self.EvapTransFileTransient = False
    self.Jacobian = None
    self.LSM = 'none'
    self.MaxConvergenceFailures = 3
    self.MaxIter = 1000000
    self.MaxLevels = None
    self.MaxMinNX = None
    self.MaxMinNY = None
    self.MaxMinNZ = None
    self.PolyDegree = None
    self.PolyPC = None
    self.PrintCLM = False
    self.PrintConcentration = True
    self.PrintDZMultiplier = None
    self.PrintEvapTrans = None
    self.PrintEvapTransSum = None
    self.PrintLSMSink = False
    self.PrintMannings = False
    self.PrintMask = False
    self.PrintOverlandBCFlux = False
    self.PrintOverlandSum = False
    self.PrintPressure = True
    self.PrintSaturation = True
    self.PrintSlopes = True
    self.PrintSpecificStorage = True
    self.PrintSubsurf = True
    self.PrintSubsurfData = True
    self.PrintTop = False
    self.PrintVelocities = False
    self.PrintWells = True
    self.RAPType = None
    self.RelTol = 1.0
    self.SadvectOrder = 2
    self.Smoother = None
    self.Spinup = None
    self.Symmetric = None
    self.TwoNorm = None
    self.Weight = None
    self.WriteCLMBinary = True
    self.NonlinearSolver = None
    self.WriteSiloCLM = False
    self.WriteSiloConcentration = False
    self.WriteSiloDZMultiplier = False
    self.WriteSiloEvapTrans = False
    self.WriteSiloEvapTransSum = False
    self.WriteSiloMannings = False
    self.WriteSiloMask = False
    self.WriteSiloOverlandBCFlux = False
    self.WriteSiloOverlandSum = False
    self.WriteSiloPMPIOConcentration = False
    self.WriteSiloPMPIODZMultiplier = False
    self.WriteSiloPMPIOEvapTrans = False
    self.WriteSiloPMPIOEvapTransSum = False
    self.WriteSiloPMPIOMannings = False
    self.WriteSiloPMPIOMask = False
    self.WriteSiloPMPIOOverlandBCFlux = False
    self.WriteSiloPMPIOOverlandSum = False
    self.WriteSiloPMPIOPressure = False
    self.WriteSiloPMPIOSaturation = False
    self.WriteSiloPMPIOSlopes = False
    self.WriteSiloPMPIOSpecificStorage = False
    self.WriteSiloPMPIOSubsurfData = False
    self.WriteSiloPMPIOTop = False
    self.WriteSiloPMPIOVelocities = False
    self.WriteSiloPressure = False
    self.WriteSiloSaturation = False
    self.WriteSiloSlopes = False
    self.WriteSiloSpecificStorage = False
    self.WriteSiloSubsurfData = False
    self.WriteSiloTop = False
    self.WriteSiloVelocities = False
    self._details = {
      "_value": {
        "help": "[Type: string] ParFlow can operate using a number of different solvers. Two of these solvers, IMPES (running in single-phase, fully-saturated mode, not multiphase) and RICHARDS (running in variably-saturated mode, not multiphase, with the options of land surface processes and coupled overland flow) are detailed below. This is a brief summary of solver settings used to simulate under three sets of conditions, fully-saturated, variably saturated and variably-saturated with overland flow. To simulate fully saturated, steady-state conditions set the solver to IMPES. This is also the default solver in ParFlow, so if no solver is specified, the code solves using IMPES. To simulate variably-saturated, transient conditions, using Richards\u2019 equation, variably/fully saturated, transient with compressible storage set the solver to RICHARDS. This is also the solver used to simulate surface flow or coupled surface-subsurface flow.\n",
        "default": "Impes",
        "domains": {
          "MandatoryValue": None,
          "EnumDomain": {
            "enumList": [
              "Impes",
              "Richards"
            ]
          }
        }
      },
      "AbsTol": {
        "help": "[Type: double] This value gives the absolute tolerance for the linear solve algorithm.\n",
        "default": 1e-09,
        "domains": {
          "DoubleValue": {
            "minValue": 0.0
          }
        }
      },
      "AdvectOrder": {
        "help": "[Type: int] This key controls the order of the explicit method used in advancing the concentrations. This value can be either 1 for a standard upwind first order or 2 for a second order Godunov method.\n",
        "default": 2,
        "domains": {
          "IntValue": {
            "minValue": 1,
            "maxValue": 2
          }
        }
      },
      "BetaFluid": {
        "help": "[Type: int]\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "BetaFracture": {
        "help": "[Type: int]\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "BetaPerm": {
        "help": "[Type: int]\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "BetaPore": {
        "help": "[Type: int]\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "BoxSizePowerOf2": {
        "help": "[Type: int]\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "CFL": {
        "help": "[Type: double] This key gives the value of the weight put on the computed CFL limit before computing a global timestep value. Values greater than 1 are not suggested and in fact because this is an approximation, values slightly less than 1 can also produce instabilities.\n",
        "default": 0.7,
        "domains": {
          "DoubleValue": None
        }
      },
      "CoarseSolve": {
        "help": "[Type: int]\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "CompCompress": {
        "help": "[Type: int]\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "DiagScale": {
        "help": "[Type: int]\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "DiagSolver": {
        "help": "[Type: int]\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "Drop": {
        "help": "[Type: double] This key gives a clipping value for data written to PFSB files. Data values greater than the negative of this value and less than the value itself are treated as zero and not written to PFSB files.\n",
        "default": 1e-08,
        "domains": {
          "DoubleValue": {
            "minValue": 0
          }
        }
      },
      "DropTol": {
        "help": "[Type: int]\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "EvapTransFile": {
        "help": "[Type: boolean/string] This key specifies specifies that the Flux terms for Richards\u2019 equation are read in from a .pfb file. This file has [T-1] units. Note this key is for a steady-state flux and should not be used in conjunction with the transient key below.\n",
        "default": False,
        "domains": {
          "BoolDomain": None
        }
      },
      "EvapTransFileTransient": {
        "help": "[Type: boolean/string] This key specifies specifies that the Flux terms for Richards\u2019 equation are read in from a series of flux .pfb file. Each file has [T-1] units. Note this key should not be used with the key above, only one of these keys should be set to True at a time, not both.\n",
        "default": False,
        "domains": {
          "BoolDomain": None
        }
      },
      "Jacobian": {
        "help": "[Type: int]\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "LSM": {
        "help": "[Type: string] This key specifies whether a land surface model, such as CLM, will be called each solver timestep. Choices for this key include none and CLM. Note that CLM must be compiled and linked at runtime for this option to be active.\n",
        "default": "none",
        "domains": {
          "MandatoryValue": None,
          "EnumDomain": {
            "enumList": [
              "none",
              "CLM"
            ]
          }
        }
      },
      "MaxConvergenceFailures": {
        "help": "[Type: int] This key gives the maximum number of convergence failures allowed. Each convergence failure cuts the timestep in half and the solver tries to advance the solution with the reduced timestep. The default value is 3. Note that setting this value to a value greater than 9 may result in errors in how time cycles are calculated. Time is discretized in terms of the base time unit and if the solver begins to take very small timesteps smallerthanbasetimeunit1000 the values based on time cycles will be change at slightly incorrect times. If the problem is failing converge so poorly that a large number of restarts are required, consider setting the timestep to a smaller value.\n",
        "default": 3,
        "domains": {
          "IntValue": {
            "minValue": 1
          }
        }
      },
      "MaxIter": {
        "help": "[Type: int] This key gives the maximum number of iterations that will be allowed for time-stepping. This is to prevent a run-away simulation.\n",
        "default": 1000000,
        "domains": {
          "IntValue": None
        }
      },
      "MaxLevels": {
        "help": "[Type: int]\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "MaxMinNX": {
        "help": "[Type: int]\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "MaxMinNY": {
        "help": "[Type: int]\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "MaxMinNZ": {
        "help": "[Type: int]\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "PolyDegree": {
        "help": "[Type: int]\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "PolyPC": {
        "help": "[Type: int]\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "PrintCLM": {
        "help": "[Type: boolean/string] This key specifies whether the CLM writes two dimensional binary output files to a PFB binary format. Note that CLM must be compiled and linked at runtime for this option to be active. These files are all written according to the standard format used for all ParFlow variables, using the runname, and istep. Variables are either two-dimensional or over the number of CLM layers (default of ten).\n",
        "default": False,
        "domains": {
          "BoolDomain": None,
          "RequiresModule": "CLM"
        }
      },
      "PrintConcentration": {
        "help": "[Type: boolean/string] This key is used to turn on printing of the concentration data. The printing of the data is controlled by values in the timing information section. The data is written as a PFB file.\n",
        "default": True,
        "domains": {
          "BoolDomain": None
        }
      },
      "PrintDZMultiplier": {
        "help": "[Type: int]\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "PrintEvapTrans": {
        "help": "[Type: int]\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "PrintEvapTransSum": {
        "help": "[Type: int]\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "PrintLSMSink": {
        "help": "[Type: boolean/string] This key is used to turn on printing of the flux array passed from CLM to ParFlow. Printing occurs at each DumpInterval time.\n",
        "default": False,
        "domains": {
          "BoolDomain": None
        }
      },
      "PrintMannings": {
        "help": "[Type: boolean/string] This key is used to turn on printing of the flux array passed from CLM to ParFlow. Printing occurs at each DumpInterval time.\n",
        "default": False,
        "domains": {
          "BoolDomain": None
        }
      },
      "PrintMask": {
        "help": "[Type: boolean/string] This key is used to turn on printing of the flux array passed from CLM to ParFlow. Printing occurs at each DumpInterval time.\n",
        "default": False,
        "domains": {
          "BoolDomain": None
        }
      },
      "PrintOverlandBCFlux": {
        "help": "[Type: boolean/string] This key is used to turn on printing of the flux array passed from CLM to ParFlow. Printing occurs at each DumpInterval time.\n",
        "default": False,
        "domains": {
          "BoolDomain": None
        }
      },
      "PrintOverlandSum": {
        "help": "[Type: boolean/string] This key is used to turn on printing of the flux array passed from CLM to ParFlow. Printing occurs at each DumpInterval time.\n",
        "default": False,
        "domains": {
          "BoolDomain": None
        }
      },
      "PrintPressure": {
        "help": "[Type: boolean/string] This key is used to turn on printing of the pressure data. The printing of the data is controlled by values in the timing information section. The data is written as a PFB file.\n",
        "default": True,
        "domains": {
          "BoolDomain": None
        }
      },
      "PrintSaturation": {
        "help": "[Type: boolean/string] This key is used to turn on printing of the saturation data. The printing of the data is controlled by values in the timing information section. The data is written as a PFB file.\n",
        "default": True,
        "domains": {
          "BoolDomain": None
        }
      },
      "PrintSlopes": {
        "help": "[Type: boolean/string] This key is used to turn on printing of the saturation data. The printing of the data is controlled by values in the timing information section. The data is written as a PFB file.\n",
        "default": True,
        "domains": {
          "BoolDomain": None
        }
      },
      "PrintSpecificStorage": {
        "help": "[Type: boolean/string] This key is used to turn on printing of the saturation data. The printing of the data is controlled by values in the timing information section. The data is written as a PFB file.\n",
        "default": True,
        "domains": {
          "BoolDomain": None
        }
      },
      "PrintSubsurf": {
        "help": "[Type: boolean/string] This key is used to turn on printing of the subsurface data, Permeability and Porosity. The data is printed after it is generated and before the main time stepping loop - only once during the run. The data is written as a PFB file.\n",
        "default": True,
        "domains": {
          "BoolDomain": None
        }
      },
      "PrintSubsurfData": {
        "help": "[Type: boolean/string] This key is used to turn on printing of the subsurface data, Permeability and Porosity. The data is printed after it is generated and before the main time stepping loop - only once during the run. The data is written as a PFB file.\n",
        "default": True,
        "domains": {
          "BoolDomain": None
        }
      },
      "PrintTop": {
        "help": "[Type: boolean/string] ?\n",
        "default": False,
        "domains": {
          "BoolDomain": None
        }
      },
      "PrintVelocities": {
        "help": "[Type: boolean/string] This key is used to turn on printing of the x,y, and z velocity data. The printing of the data is controlled by values in the timing information section. The data is written as a PFB file.\n",
        "default": False,
        "domains": {
          "BoolDomain": None
        }
      },
      "PrintWells": {
        "help": "[Type: boolean/string] This key is used to turn on collection and printing of the well data. The data is collected at intervals given by values in the timing information section. Printing occurs at the end of the run when all collected data is written.\n",
        "default": True,
        "domains": {
          "BoolDomain": None
        }
      },
      "RAPType": {
        "help": "[Type: int]\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "RelTol": {
        "help": "[Type: double] This value gives the relative tolerance for the linear solve algorithm.\n",
        "default": 1.0,
        "domains": {
          "DoubleValue": None
        }
      },
      "SadvectOrder": {
        "help": "[Type: int] This key controls the order of the explicit method used in advancing the concentrations. This value can be either 1 for a standard upwind first order or 2 for a second order Godunov method.\n",
        "default": 2,
        "domains": {
          "IntValue": {
            "minValue": 1,
            "maxValue": 2
          }
        }
      },
      "Smoother": {
        "help": "[Type: int]\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "Spinup": {
        "help": "[Type: boolean]\n",
        "domains": {
          "BoolDomain": None
        }
      },
      "Symmetric": {
        "help": "[Type: int]\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "TwoNorm": {
        "help": "[Type: int]\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "Weight": {
        "help": "[Type: int]\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "WriteCLMBinary": {
        "help": "[Type: boolean/string] This key specifies whether the CLM writes two dimensional binary output files in a generic binary format. Note that CLM must be compiled and linked at runtime for this option to be active.\n",
        "default": True,
        "domains": {
          "BoolDomain": None
        }
      },
      "NonlinearSolver": {
        "help": "[Type: int]\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "WriteSiloCLM": {
        "help": "[Type: boolean/string] This key specifies whether the CLM writes two dimensional binary output files to a silo binary format. This data may be read in by VisIT and other visualization packages. Note that CLM and silo must be compiled and linked at runtime for this option to be active. These files are all written according to the standard format used for all ParFlow variables, using the runname, and istep. Variables are either two-dimensional or over the number of CLM layers (default of ten).\n",
        "default": False,
        "domains": {
          "BoolDomain": None,
          "RequiresModule": "SILO"
        }
      },
      "WriteSiloConcentration": {
        "help": "[Type: boolean/string] This key is used to specify printing of the concentration data in silo binary format. The printing of the data is controlled by values in the timing information section.\n",
        "default": False,
        "domains": {
          "BoolDomain": None,
          "RequiresModule": "SILO"
        }
      },
      "WriteSiloDZMultiplier": {
        "help": "[Type: boolean/string]\n",
        "default": False,
        "domains": {
          "BoolDomain": None,
          "RequiresModule": "SILO"
        }
      },
      "WriteSiloEvapTrans": {
        "help": "[Type: boolean/string] This key is used to specify printing of the evaporation and rainfall flux data using silo binary format. This data comes from either clm or from external calls to ParFlow such as WRF. This data is in units of [L3T-1]. The printing of the data is controlled by values in the timing information section.\n",
        "default": False,
        "domains": {
          "BoolDomain": None,
          "RequiresModule": "SILO"
        }
      },
      "WriteSiloEvapTransSum": {
        "help": "[Type: boolean/string] This key is used to specify printing of the evaporation and rainfall flux data using silo binary format as a running, cumulative amount. This data comes from either clm or from external calls to ParFlow such as WRF. This data is in units of [L3]. The printing of the data is controlled by values in the timing information section.\n",
        "default": False,
        "domains": {
          "BoolDomain": None,
          "RequiresModule": "SILO"
        }
      },
      "WriteSiloMannings": {
        "help": "[Type: boolean/string] This key is used to specify printing of the Manning\u2019s roughness data in silo binary format. The printing of the data is controlled by values in the timing information section.\n",
        "default": False,
        "domains": {
          "BoolDomain": None,
          "RequiresModule": "SILO"
        }
      },
      "WriteSiloMask": {
        "help": "[Type: boolean/string] This key is used to specify printing of the mask data using silo binary format. The mask contains values equal to one for active cells and zero for inactive cells. The printing of the data is controlled by values in the timing information section.\n",
        "default": False,
        "domains": {
          "BoolDomain": None,
          "RequiresModule": "SILO"
        }
      },
      "WriteSiloOverlandBCFlux": {
        "help": "[Type: boolean/string]\n",
        "default": False,
        "domains": {
          "BoolDomain": None,
          "RequiresModule": "SILO"
        }
      },
      "WriteSiloOverlandSum": {
        "help": "[Type: boolean/string] This key is used to specify calculation and printing of the total overland outflow from the domain using silo binary format as a running cumulative amount. This is integrated along all domain boundaries and is calculated any location that slopes at the edge of the domain point outward. This data is in units of [L3]. The printing of the data is controlled by values in the timing information section.\n",
        "default": False,
        "domains": {
          "BoolDomain": None,
          "RequiresModule": "SILO"
        }
      },
      "WriteSiloPMPIOConcentration": {
        "help": "[Type: boolean/string]\n",
        "default": False,
        "domains": {
          "BoolDomain": None,
          "RequiresModule": "SILO"
        }
      },
      "WriteSiloPMPIODZMultiplier": {
        "help": "[Type: boolean/string]\n",
        "default": False,
        "domains": {
          "BoolDomain": None,
          "RequiresModule": "SILO"
        }
      },
      "WriteSiloPMPIOEvapTrans": {
        "help": "[Type: boolean/string]\n",
        "default": False,
        "domains": {
          "BoolDomain": None,
          "RequiresModule": "SILO"
        }
      },
      "WriteSiloPMPIOEvapTransSum": {
        "help": "[Type: boolean/string]\n",
        "default": False,
        "domains": {
          "BoolDomain": None,
          "RequiresModule": "SILO"
        }
      },
      "WriteSiloPMPIOMannings": {
        "help": "[Type: boolean/string]\n",
        "default": False,
        "domains": {
          "BoolDomain": None,
          "RequiresModule": "SILO"
        }
      },
      "WriteSiloPMPIOMask": {
        "help": "[Type: boolean/string]\n",
        "default": False,
        "domains": {
          "BoolDomain": None,
          "RequiresModule": "SILO"
        }
      },
      "WriteSiloPMPIOOverlandBCFlux": {
        "help": "[Type: boolean/string]\n",
        "default": False,
        "domains": {
          "BoolDomain": None,
          "RequiresModule": "SILO"
        }
      },
      "WriteSiloPMPIOOverlandSum": {
        "help": "[Type: boolean/string]\n",
        "default": False,
        "domains": {
          "BoolDomain": None,
          "RequiresModule": "SILO"
        }
      },
      "WriteSiloPMPIOPressure": {
        "help": "[Type: boolean/string]\n",
        "default": False,
        "domains": {
          "BoolDomain": None,
          "RequiresModule": "SILO"
        }
      },
      "WriteSiloPMPIOSaturation": {
        "help": "[Type: boolean/string]\n",
        "default": False,
        "domains": {
          "BoolDomain": None,
          "RequiresModule": "SILO"
        }
      },
      "WriteSiloPMPIOSlopes": {
        "help": "[Type: boolean/string]\n",
        "default": False,
        "domains": {
          "BoolDomain": None,
          "RequiresModule": "SILO"
        }
      },
      "WriteSiloPMPIOSpecificStorage": {
        "help": "[Type: boolean/string]\n",
        "default": False,
        "domains": {
          "BoolDomain": None,
          "RequiresModule": "SILO"
        }
      },
      "WriteSiloPMPIOSubsurfData": {
        "help": "[Type: boolean/string]\n",
        "default": False,
        "domains": {
          "BoolDomain": None,
          "RequiresModule": "SILO"
        }
      },
      "WriteSiloPMPIOTop": {
        "help": "[Type: boolean/string]\n",
        "default": False,
        "domains": {
          "BoolDomain": None,
          "RequiresModule": "SILO"
        }
      },
      "WriteSiloPMPIOVelocities": {
        "help": "[Type: boolean/string]\n",
        "default": False,
        "domains": {
          "BoolDomain": None,
          "RequiresModule": "SILO"
        }
      },
      "WriteSiloPressure": {
        "help": "[Type: boolean/string] This key is used to specify printing of the pressure data in silo binary format. The printing of the data is controlled by values in the timing information section. This data may be read in by VisIT and other visualization packages.\n",
        "default": False,
        "domains": {
          "BoolDomain": None,
          "RequiresModule": "SILO"
        }
      },
      "WriteSiloSaturation": {
        "help": "[Type: boolean/string] This key is used to specify printing of the saturation data using silo binary format. The printing of the data is controlled by values in the timing information section.\n",
        "default": False,
        "domains": {
          "BoolDomain": None,
          "RequiresModule": "SILO"
        }
      },
      "WriteSiloSlopes": {
        "help": "[Type: boolean/string] This key is used to turn on printing of the x adn y slope data in silo binary format. The printing of the data is controlled by values in the timing information section. The data is written as a PFB file.\n",
        "default": False,
        "domains": {
          "BoolDomain": None,
          "RequiresModule": "SILO"
        }
      },
      "WriteSiloSpecificStorage": {
        "help": "[Type: boolean/string] This key is used to specify printing of the specific storage data in silo binary format. The printing of the data is controlled by values in the timing information section.\n",
        "default": False,
        "domains": {
          "BoolDomain": None,
          "RequiresModule": "SILO"
        }
      },
      "WriteSiloSubsurfData": {
        "help": "[Type: boolean/string] This key is used to specify printing of the subsurface data, Permeability and Porosity in silo binary file format. The data is printed after it is generated and before the main time stepping loop - only once during the run. This data may be read in by VisIT and other visualization packages.\n",
        "default": False,
        "domains": {
          "BoolDomain": None,
          "RequiresModule": "SILO"
        }
      },
      "WriteSiloTop": {
        "help": "[Type: boolean/string] This key is used to turn on printing of the x,y, and z velocity data. The printing of the data is controlled by values in the timing information section. The data is written as a PFB file.\n",
        "default": False,
        "domains": {
          "BoolDomain": None,
          "RequiresModule": "SILO"
        }
      },
      "WriteSiloVelocities": {
        "help": "[Type: boolean/string] This key is used to turn on printing of the x,y, and z velocity data in silo binary format. The printing of the data is controlled by values in the timing information section. The data is written as a PFB file.\n",
        "default": False,
        "domains": {
          "BoolDomain": None,
          "RequiresModule": "SILO"
        }
      }
    }

# ------------------------------------------------------------------------------

class CLM(PFDBObj):
  '''
  Setting CLM parameters
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.BinaryOutDir = True
    self.CLMDumpInterval = 1
    self.CLMFileDir = None
    self.DailyRST = True
    self.EvapBeta = 'Linear'
    self.FieldCapacity = 1.0
    self.ForceVegetation = False
    self.FstepStart = None
    self.IrrigationCycle = 'Constant'
    self.IrrigationRate = None
    self.IrrigationStartTime = None
    self.IrrigationStopTime = None
    self.IrrigationThreshold = 0.5
    self.IrrigationThresholdType = None
    self.IrrigationType = 'none'
    self.IstepStart = 1
    self.MetFileNT = None
    self.MetFileName = None
    self.MetFilePath = None
    self.MetFileSubdir = None
    self.MetForcing = None
    self.Print1dOut = False
    self.ResSat = 0.1
    self.ReuseCount = 1
    self.RootZoneNZ = 10
    self.RZWaterStress = None
    self.SingleFile = False
    self.SoiLayer = 7
    self.VegWaterStress = 'Saturation'
    self.WiltingPoint = 0.1
    self.WriteLastRST = False
    self.WriteLogs = True
    self._details = {
      "BinaryOutDir": {
        "help": "[Type: boolean/string] This key specifies whether the CLM writes each set of two dimensional binary output files to a corresponding directory. These directories my be created before ParFlow is run (using the tcl script, for example). Choices for this key include True and False. Note that CLM must be compiled and linked at runtime for this option to be active.\n",
        "default": True,
        "domains": {
          "BoolDomain": None,
          "RequiresModule": "CLM"
        }
      },
      "CLMDumpInterval": {
        "help": "[Type: int] This key specifies how often output from the CLM is written. This key is in integer multipliers of the CLM timestep. Note that CLM must be compiled and linked at runtime for this option to be active.\n",
        "default": 1,
        "domains": {
          "IntValue": {
            "minValue": 1
          },
          "RequiresModule": "CLM"
        }
      },
      "CLMFileDir": {
        "help": "[Type: string] This key specifies what directory all output from the CLM is written to. This key may be set to \"./\" or \"\" to write output to the ParFlow run directory. This directory must be created before ParFlow is run. Note that CLM must be compiled and linked at runtime for this option to be active.\n",
        "domains": {
          "AnyString": None,
          "RequiresModule": "CLM"
        }
      },
      "DailyRST": {
        "help": "[Type: boolean/string] Controls whether CLM writes daily restart files (default) or at every time step when set to False; outputs are numbered according to the istep from ParFlow. If ReuseCount=n, with n greater than 1, the output will be written every n steps (i.e. it still writes hourly restart files if your time step is 0.5 or 0.25, etc...). Fully compatible with WriteLastRST=False so that each daily output is overwritten to time 00000 in restart file name.00000.p where p is the processor number.\n",
        "default": True,
        "domains": {
          "BoolDomain": None,
          "RequiresModule": "CLM"
        }
      },
      "EvapBeta": {
        "help": "[Type: string] This key specifies the form of the bare soil evaporation parameter in CLM. The valid types for this key are None, Linear, Cosine.\n",
        "default": "Linear",
        "domains": {
          "EnumDomain": {
            "enumList": [
              "None",
              "Linear",
              "Cosine"
            ]
          },
          "RequiresModule": "CLM"
        }
      },
      "FieldCapacity": {
        "help": "[Type: double] This key specifies the field capacity for the beta-t function in CLM. Note that the units for this function are pressure [m] for a Pressure formulation and saturation [-] for a Saturation formulation. Note that CLM must be compiled and linked at runtime for this option to be active.\n",
        "default": 1.0,
        "domains": {
          "DoubleValue": {
            "minValue": 0.0,
            "maxValue": 1.0
          },
          "RequiresModule": "CLM"
        }
      },
      "ForceVegetation": {
        "help": "[Type: boolean/string] This key specifies whether vegetation should be forced in CLM. Currently this option only works for 1D and 3D forcings, as specified by the key Solver.CLM.MetForcing. Choices for this key include True and False. Forced vegetation variables are : LAI: Leaf Area Index [-] SAI: Stem Area Index [-] Z0M: Aerodynamic roughness length [m] DISPLA: Displacement height [m] In the case of 1D meteorological forcings, CLM requires four files for vegetation time series and one vegetation map. The four files should be named respectively lai.dat, sai.dat, z0m.dat, displa.dat. They are ASCII files and contain 18 time-series columns (one per IGBP vegetation class, and each timestep per row). The vegetation map should be a properly distributed 2D ParFlow binary file (.pfb) which contains vegetation indices (from 1 to 18). The vegetation map filename is veg_map.pfb. ParFlow uses the vegetation map to pass to CLM a 2D map for each vegetation variable at each time step. In the case of 3D meteorological forcings, ParFlow expects four distincts properly distributed ParFlow binary file (.pfb), the third dimension being the timesteps. The files should be named LAI.pfb, SAI.pfb, Z0M.pfb, DISPLA.pfb. No vegetation map is needed in this case.\n",
        "default": False,
        "domains": {
          "BoolDomain": None,
          "RequiresModule": "CLM"
        }
      },
      "FstepStart": {
        "help": "[Type: int]\n",
        "domains": {
          "DoubleValue": None,
          "RequiresModule": "CLM"
        }
      },
      "IrrigationCycle": {
        "help": "[Type: string] This key specifies the cycle of the irrigation in CLM. The valid types for this key are Constant, Deficit. Note only Constant is currently implemented. Constant cycle applies irrigation each day from IrrigationStartTime to IrrigationStopTime in GMT.\n",
        "default": "Constant",
        "domains": {
          "EnumDomain": {
            "enumList": [
              "Constant",
              "Deficit"
            ]
          },
          "RequiresModule": "CLM"
        }
      },
      "IrrigationRate": {
        "help": "[Type: double] This key specifies the rate of the irrigation in CLM in [mm/s].\n",
        "domains": {
          "DoubleValue": {
            "minValue": 0.0
          },
          "RequiresModule": "CLM"
        }
      },
      "IrrigationStartTime": {
        "help": "[Type: double] This key specifies the start time of the irrigation in CLM GMT.\n",
        "domains": {
          "DoubleValue": {
            "minValue": 0.0,
            "maxValue": 2400.0
          },
          "RequiresModule": "CLM"
        }
      },
      "IrrigationStopTime": {
        "help": "[Type: double] This key specifies the stop time of the irrigation in CLM GMT.\n",
        "domains": {
          "DoubleValue": {
            "minValue": 0.0,
            "maxValue": 2400.0
          },
          "RequiresModule": "CLM"
        }
      },
      "IrrigationThreshold": {
        "help": "[Type: double] This key specifies the threshold value for the irrigation in CLM [-].\n",
        "default": 0.5,
        "domains": {
          "DoubleValue": {
            "minValue": 0.0
          },
          "RequiresModule": "CLM"
        }
      },
      "IrrigationThresholdType": {
        "help": "[Type: string]\n",
        "domains": {
          "DoubleValue": None,
          "RequiresModule": "CLM"
        }
      },
      "IrrigationType": {
        "help": "[Type: string] This key specifies the form of the irrigation in CLM. The valid types for this key are none, Spray, Drip, Instant.\n",
        "default": "none",
        "domains": {
          "EnumDomain": {
            "enumList": [
              "none",
              "Spray",
              "Drip",
              "Instant"
            ]
          },
          "RequiresModule": "CLM"
        }
      },
      "IstepStart": {
        "help": "[Type: int] This key specifies the value of the counter, istep in CLM. This key primarily determines the start of the output counter for CLM.It is used to restart a run by setting the key to the ending step of the previous run plus one. Note that CLM must be compiled and linked at runtime for this option to be active.\n",
        "default": 1,
        "domains": {
          "IntValue": None,
          "RequiresModule": "CLM"
        }
      },
      "MetFileNT": {
        "help": "[Type: int] This key specifies the number of timesteps per file for 3D forcing data.\n",
        "domains": {
          "IntValue": None,
          "RequiresModule": "CLM"
        }
      },
      "MetFileName": {
        "help": "[Type: string] This key specifies defines the file name for 1D, 2D or 3D forcing data. 1D meteorological forcing files are text files with single columns for each variable and each timestep per row, while 2D and 3D forcing files are distributed ParFlow binary files, one for each variable and timestep (2D) or one for each variable and multiple timesteps (3D). Behavior of this key is different for 1D and 2D and 3D cases, as sepcified by the Solver.CLM.MetForcing key above. For 1D cases, it is the FULL FILE NAME. Note that in this configuration, this forcing file is not distributed, the user does not provide copies such as narr.1hr.txt.0, narr.1hr.txt.1 for each processor. ParFlow only needs the single original file (e.g. narr.1hr.txt). For 2D cases, this key is the BASE FILE NAME for the 2D forcing files, currently set to NLDAS, with individual files determined as follows NLDAS.<variable>.<time step>.pfb. Where the <variable> is the forcing variable and <timestep> is the integer file counter corresponding to istep above. Forcing is needed for following variables: DSWR: Downward Visible or Short-Wave radiation [W/m2]. DLWR: Downward Infa-Red or Long-Wave radiation [W/m2] APCP: Precipitation rate [mm/s] Temp: Air temperature [K] UGRD: West-to-East or U-component of wind [m/s] VGRD: South-to-North or V-component of wind [m/s] Press: Atmospheric Pressure [pa] SPFH: Water-vapor specific humidity [kg/kg] Note that CLM must be compiled and linked at runtime for this option to be active.\n",
        "domains": {
          "AnyString": None,
          "RequiresModule": "CLM"
        }
      },
      "MetFilePath": {
        "help": "[Type: string] This key specifies defines the location of 1D, 2D or 3D forcing data. For 1D cases, this is the path to a single forcing file (e.g. narr.1hr.txt). For 2D and 3D cases, this is the path to the directory containing all forcing files. Note that CLM must be compiled and linked at runtime for this option to be active.\n",
        "domains": {
          "AnyString": None,
          "RequiresModule": "CLM"
        }
      },
      "MetFileSubdir": {
        "help": "[Type: int]\n",
        "domains": {
          "DoubleValue": None,
          "RequiresModule": "CLM"
        }
      },
      "MetForcing": {
        "help": "[Type: string] This key specifies defines whether 1D (uniform over the domain), 2D (spatially distributed) or 3D (spatially distributed with multiple timesteps per .pfb forcing file) forcing data is used. Choices for this key are 1D, 2D and 3D. This key has no default so the user must set it to 1D, 2D or 3D. Failure to set this key will cause CLM to still be run but with unpredictable values causing CLM to eventually crash. 1D meteorological forcing files are text files with single columns for each variable and each timestep per row, while 2D forcing files are distributed ParFlow binary files, one for each variable and timestep. File names are specified in the Solver.CLM.MetFileName variable below. Note that CLM must be compiled and linked at runtime for this option to be active.\n",
        "domains": {
          "EnumDomain": {
            "enumList": [
              "1D",
              "2D",
              "3D"
            ]
          },
          "RequiresModule": "CLM"
        }
      },
      "Print1dOut": {
        "help": "[Type: boolean/string] This key specifies whether the CLM one dimensional (averaged over each processor) output file is written or not. Choices for this key include True and False. Note that CLM must be compiled and linked at runtime for this option to be active.\n",
        "default": False,
        "domains": {
          "BoolDomain": None,
          "RequiresModule": "CLM"
        }
      },
      "ResSat": {
        "help": "[Type: double] This key specifies the residual saturation for the saturation function in CLM. Note that CLM must be compiled and linked at runtime for this option to be active.\n",
        "default": 0.1,
        "domains": {
          "DoubleValue": {
            "minValue": 0.0
          },
          "RequiresModule": "CLM"
        }
      },
      "ReuseCount": {
        "help": "[Type: int] How many times to reuse a CLM atmospheric forcing file input. For example timestep=1, reuse =1 is normal behavior but reuse=2 and timestep=0.5 subdivides the time step using the same CLM input for both halves instead of needing two files. This is particually useful for large, distributed runs when the user wants to run ParFlow at a smaller timestep than the CLM forcing. Forcing files will be re-used and total fluxes adjusted accordingly without needing duplicate files.\n",
        "default": 1,
        "domains": {
          "IntValue": {
            "minValue": 0
          },
          "RequiresModule": "CLM"
        }
      },
      "RootZoneNZ": {
        "help": "[Type: int] This key sets the number of soil layers the ParFlow expects from CLM. It will allocate and format all the arrays for passing variables to and from CLM accordingly. This value now sets the CLM number as well so recompilation is not required anymore. Most likely the key Solver.CLM.SoiLayer will also need to be changed.\n",
        "default": 10,
        "domains": {
          "IntValue": {
            "minValue": 1
          },
          "RequiresModule": "CLM"
        }
      },
      "RZWaterStress": {
        "help": "[Type: ???]\n",
        "domains": {
          "RequiresModule": "CLM"
        }
      },
      "SingleFile": {
        "help": "[Type: boolean/string] Controls whether ParFlow writes all CLM output variables as a single file per time step. When \"True\", this combines the output of all the CLM output variables into a special multi-layer PFB with the file extension \".C.pfb\". The first 13 layers correspond to the 2-D CLM outputs and the remaining layers are the soil temperatures in each layer. For example, a model with 4 soil layers will create a SingleFile CLM output with 17 layers at each time step. The file pseudo code is given below in \u00a7 6.4 and the variables and units are as specified in the multiple PFB and SILO formats as above.\n",
        "default": False,
        "domains": {
          "BoolDomain": None,
          "RequiresModule": "CLM"
        }
      },
      "SoiLayer": {
        "help": "[Type: int] This key sets the soil layer, and thus the soil depth, that CLM uses for the seasonal temperature adjustment for all leaf and stem area indices.\n",
        "default": 7,
        "domains": {
          "IntValue": {
            "minValue": 1
          },
          "RequiresModule": "CLM"
        }
      },
      "VegWaterStress": {
        "help": "[Type: string] This key specifies the form of the plant water stress function parameter in CLM. The valid types for this key are None, Saturation, Pressure.\n",
        "default": "Saturation",
        "domains": {
          "EnumDomain": {
            "enumList": [
              "None",
              "Saturation",
              "Pressure"
            ]
          },
          "RequiresModule": "CLM"
        }
      },
      "WiltingPoint": {
        "help": "[Type: double] This key specifies the wilting point for the bets-t function in CLM. Note that the units for this function are pressure [m] for a Pressure formulation and saturation [-] for a Saturation formulation. Note that CLM must be compiled and linked at runtime for this option to be active.\n",
        "default": 0.1,
        "domains": {
          "DoubleValue": {
            "minValue": 0.0
          },
          "RequiresModule": "CLM"
        }
      },
      "WriteLastRST": {
        "help": "[Type: boolean/string] Controls whether CLM restart files are sequentially written or whether a single file restart file name.00000.p is overwritten each time the restart file is output, where p is the processor number. If \"True\" only one file is written/overwritten and if \"False\" outputs are written more frequently. Compatible with DailyRST and ReuseCount; for the latter, outputs are written every n steps where n is the value of ReuseCount.\n",
        "default": False,
        "domains": {
          "BoolDomain": None,
          "RequiresModule": "CLM"
        }
      },
      "WriteLogs": {
        "help": "[Type: boolean/string] When False, this disables writing of the CLM output log files for each processor. For example, in the clm.tcl test case, if this flag is added False, washita.output.txt.p and washita.para.out.dat.p (were p is the processor #) are not created, assuming washita is the run name.\n",
        "default": True,
        "domains": {
          "BoolDomain": None,
          "RequiresModule": "CLM"
        }
      }
    }

# ------------------------------------------------------------------------------

class EvapTrans(PFDBObj):
  '''
  Setting EvapTrans files
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.FileLooping = None
    self.FileName = None
    self._details = {
      "FileLooping": {
        "help": "[Type: boolean/string]\n",
        "domains": {
          "BoolDomain": None
        }
      },
      "FileName": {
        "help": "[Type: string] This key specifies specifies filename for the distributed .pfb file that contains the flux values for Richards\u2019 equation. This file has [T-1] units. For the steady-state option (Solver.EvapTransFile=True) this key should be the complete filename. For the transient option (Solver.EvapTransFileTransient=True then the filename is a header and ParFlow will load one file per timestep, with the form filename.00000.pfb.\n",
        "domains": {
          "AnyString": None
        }
      }
    }

# ------------------------------------------------------------------------------

class OverlandDiffusive(PFDBObj):
  '''
  Setting epsilon value for the diffusive overland flow formulation.
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Epsilon = 1e-05
    self._details = {
      "Epsilon": {
        "help": "[Type: double] This key provides a minimum value for the Sf used in the OverlandDiffusive boundary condition.\n",
        "default": 1e-05,
        "domains": {
          "DoubleValue": {
            "minValue": 0.0
          }
        }
      }
    }

# ------------------------------------------------------------------------------

class OverlandKinematic(PFDBObj):
  '''
  Setting epsilon value for the diffusive kinematic flow formulation.
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Epsilon = 1e-05
    self._details = {
      "Epsilon": {
        "help": "[Type: double] This key provides a minimum value for the Sf used in the OverlandKinematic boundary condition.\n",
        "default": 1e-05,
        "domains": {
          "DoubleValue": {
            "minValue": 0.0
          }
        }
      }
    }

# ------------------------------------------------------------------------------

class TerrainFollowingGrid(PFDBObj):
  '''
  Assigning properties to TerrainFollowingGrid and TerrainFollowingGrid.SlopeUpwindFormulation
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self._value = False
    self.SlopeUpwindFormulation = 'Original'
    self._details = {
      "_value": {
        "help": "[Type: boolean/string] This key specifies that a terrain-following coordinate transform is used for solver Richards. This key sets x and y subsurface slopes to be the same as the Topographic slopes (a value of False sets these subsurface slopes to zero). These slopes are used in the Darcy fluxes to add a density, gravity -dependent term. This key will not change the output files (that is the output is still orthogonal) or the geometries (they will still follow the computational grid)\u2013 these two things are both to do items. This key only changes solver Richards, not solver Impes.\n",
        "default": False,
        "domains": {
          "BoolDomain": None
        }
      },
      "SlopeUpwindFormulation": {
        "help": "[Type: string] This key specifies optional modifications to the terrain following grid formulation (Equation 5.8) . Choices for this key are Original, Upwind, UpwindSine. Original is the original TFG formulation shown in Equation 5.8 in the manual. The Original option calculates the theta-x and theta-y for a cell face as the average of the two adjacent cell slopes (i.e. assuming a cell centered slope calculation). The Upwind option uses the the theta-x and theta-y of a cell directly without averaging (i.e. assuming a face centered slope calculation). The UpwindSine is the same as the Upwind option but it also removes the Sine term from 5.8. Note the UpwindSine option is for experimental purposes only and should not be used in standard simulations. Also note that the choice of upwind orOriginal formulation should consistent with the choice of overland flow boundary condition if overland flow is being used. The upwind and UpwindSine are consistent with OverlandDiffusive and OverlandKinematic while Original is consistent with OverlandFlow.\n",
        "default": "Original",
        "domains": {
          "EnumDomain": {
            "enumList": [
              "Original",
              "Upwind",
              "UpwindSine"
            ]
          }
        }
      }
    }

# ------------------------------------------------------------------------------

class Linear(PFDBObj):
  '''
  Assigning properties to Solver.Linear
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self._value = 'PCG'
    self.Preconditioner = Preconditioner(self)
    self.KrylovDimension = 10
    self.MaxRestarts = 0
    self.MaxRestart = 0
    self._details = {
      "_value": {
        "help": "[Type: string] This key specifies the linear solver used for solver IMPES. Choices for this key are MGSemi, PPCG, PCG, and CGHS. The choice MGSemi is an algebraic mulitgrid linear solver (not a preconditioned conjugate gradient) which may be less robust than PCG as described in [3]. The choice PPCG is a preconditioned conjugate gradient solver. The choice PCG is a conjugate gradient solver with a multigrid preconditioner. The choice CGHS is a conjugate gradient solver.\n",
        "default": "PCG",
        "domains": {
          "EnumDomain": {
            "enumList": [
              "MGSemi",
              "PPCG",
              "PCG",
              "CGHS"
            ]
          }
        }
      },
      "KrylovDimension": {
        "help": "[Type: int] This key specifies the maximum number of vectors to be used in setting up the Krylov subspace in the GMRES iterative solver. These vectors are of problem size and it should be noted that large increases in this parameter can limit problem sizes. However, increasing this parameter can sometimes help nonlinear solver convergence.\n",
        "default": 10,
        "domains": {
          "MandatoryValue": None,
          "IntValue": {
            "minValue": 1
          }
        }
      },
      "MaxRestarts": {
        "help": "[Type: int] This key specifies the number of restarts allowed to the GMRES solver. Restarts start the development of the Krylov subspace over using the current iterate as the initial iterate for the next pass.\n",
        "default": 0,
        "domains": {
          "IntValue": {
            "minValue": 0
          }
        }
      },
      "MaxRestart": {
        "help": "[Type: int] This key specifies the number of restarts allowed to the GMRES solver. Restarts start the development of the Krylov subspace over using the current iterate as the initial iterate for the next pass.\n",
        "default": 0,
        "domains": {
          "IntValue": {
            "minValue": 0
          }
        }
      }
    }

# ------------------------------------------------------------------------------

class Preconditioner(PFDBObj):
  '''
  Setting properties for Solver.Linear.Preconditioner
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self._value = 'MGSemi'
    self.SymmetricMat = 'Symmetric'
    self.PCMatrixType = None
    self._details = {
      "_value": {
        "help": "[Type: string] This key specifies which preconditioner to use. Currently, the three choices are NoPC, MGSemi, PFMG, PFMGOctree and SMG. The choice NoPC specifies that no preconditioner should be used. The choice MGSemi specifies a semi-coarsening multigrid algorithm which uses a point relaxation method. The choice SMG specifies a semi-coarsening multigrid algorithm which uses plane relaxations. This method is more robust than MGSemi, but generally requires more memory and compute time. The choice PFMGOctree can be more efficient for problems with large numbers of inactive cells.\n",
        "default": "MGSemi",
        "domains": {
          "EnumDomain": {
            "enumList": [
              "NoPC",
              "MGSemi",
              "PFMG",
              "PFMGOctree",
              "SMG"
            ]
          }
        },
        "handlers": {
          "LPreMethodUpdater": {
            "type": "ChildrenHandler",
            "className": "PrecondMethodItem",
            "location": "./Preconditioner"
          }
        }
      },
      "SymmetricMat": {
        "help": "[Type: string] This key specifies whether the preconditioning matrix is symmetric. Choices fo rthis key are Symmetric and Nonsymmetric. The choice Symmetric specifies that the symmetric part of the Jacobian will be used as the preconditioning matrix. The choice Nonsymmetric specifies that the full Jacobian will be used as the preconditioning matrix. NOTE: ONLY Symmetric CAN BE USED IF MGSemi IS THE SPECIFIED PRECONDITIONER!\n",
        "default": "Symmetric",
        "domains": {
          "EnumDomain": {
            "enumList": [
              "Symmetric",
              "Nonsymmetric"
            ]
          }
        }
      },
      "PCMatrixType": {
        "help": "[Type: string]\n",
        "domains": {
          "EnumDomain": {
            "enumList": [
              "FullJacobian"
            ]
          }
        }
      }
    }

# ------------------------------------------------------------------------------

class PrecondMethodItem(PFDBObj):
  '''
  Setting Solver.Linear.Preconditioner.{precond_method} keys
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.MaxIter = 1
    self.MaxLevels = None
    self.NumPreRelax = 1
    self.NumPostRelax = 1
    self.Smoother = None
    self.RAPType = 'NonGalerkin'
    self._details = {
      "MaxIter": {
        "help": "[Type: int] This key specifies the maximum number of iterations to take in solving the preconditioner system with precond_ method solver.\n",
        "default": 1,
        "domains": {
          "IntValue": {
            "minValue": 1
          }
        }
      },
      "MaxLevels": {
        "help": "[Type: int] Max Levels\n",
        "domains": {
          "IntValue": {
            "minValue": 1
          }
        }
      },
      "NumPreRelax": {
        "help": "[Type: int] This key specifies the number of relaxations to take before coarsening in the specified preconditioner method. Note that this key is only relevant to the SMG multigrid preconditioner.\n",
        "default": 1,
        "domains": {
          "IntValue": {
            "minValue": 1
          }
        }
      },
      "NumPostRelax": {
        "help": "[Type: int] This key specifies the number of relaxations to take after coarsening in the specified preconditioner method. Note that this key is only relevant to the SMG multigrid preconditioner.\n",
        "default": 1,
        "domains": {
          "IntValue": {
            "minValue": 1
          }
        }
      },
      "Smoother": {
        "help": "[Type: string]\n",
        "domains": {
          "AnyString": None
        }
      },
      "RAPType": {
        "help": "[Type: string] For the PFMG solver, this key specifies the Hypre RAP type. Valid values are Galerkin or NonGalerkin\n",
        "default": "NonGalerkin",
        "domains": {
          "EnumDomain": {
            "enumList": [
              "Galerkin",
              "NonGalerkin"
            ]
          }
        }
      }
    }

# ------------------------------------------------------------------------------

class Nonlinear(PFDBObj):
  '''
  Setting nonlinear solver keys
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.VariableDz = False
    self.FlowBarrierX = False
    self.FlowBarrierY = False
    self.FlowBarrierZ = False
    self.ResidualTol = 1e-07
    self.StepTol = 1e-07
    self.MaxIter = 15
    self.PrintFlag = 'HighVerbosity'
    self.EtaChoice = 'Walker2'
    self.EtaValue = 0.0001
    self.EtaAlpha = 2.0
    self.EtaGamma = 0.9
    self.UseJacobian = False
    self.DerivativeEpsilon = 1e-07
    self.Globalization = 'LineSearch'
    self._details = {
      "VariableDz": {
        "help": "[Type: boolean/string] This key specifies whether dZ multipliers are to be used, the default is False. The default indicates a false or non-active variable dz and each layer thickness is 1.0 [L].\n",
        "default": False,
        "domains": {
          "BoolDomain": None
        }
      },
      "FlowBarrierX": {
        "help": "[Type: boolean/string] This key specifies whether Flow Barriers are to be used in the X direction, the default is False. The default indicates a false or FBx value of one [-] everywhere in the domain.\n",
        "default": False,
        "domains": {
          "BoolDomain": None
        }
      },
      "FlowBarrierY": {
        "help": "[Type: boolean/string] This key specifies whether Flow Barriers are to be used in the Y direction, the default is False. The default indicates a false or FBy value of one [-] everywhere in the domain.\n",
        "default": False,
        "domains": {
          "BoolDomain": None
        }
      },
      "FlowBarrierZ": {
        "help": "[Type: boolean/string] This key specifies whether Flow Barriers are to be used in the Z direction, the default is False. The default indicates a false or FBz value of one [-] everywhere in the domain.\n",
        "default": False,
        "domains": {
          "BoolDomain": None
        }
      },
      "ResidualTol": {
        "help": "[Type: double] This key specifies the tolerance that measures how much the relative reduction in the nonlinear residual should be before nonlinear iterations stop. The magnitude of the residual is measured with the l1 (max) norm.\n",
        "default": 1e-07,
        "domains": {
          "DoubleValue": {
            "minValue": 0.0
          }
        }
      },
      "StepTol": {
        "help": "[Type: double] This key specifies the tolerance that measures how small the difference between two consecutive nonlinear steps can be before nonlinear iterations stop.\n",
        "default": 1e-07,
        "domains": {
          "DoubleValue": {
            "minValue": 0.0
          }
        }
      },
      "MaxIter": {
        "help": "[Type: int] This key specifies the maximum number of nonlinear iterations allowed before iterations stop with a convergence failure.\n",
        "default": 15,
        "domains": {
          "IntValue": {
            "minValue": 1
          }
        }
      },
      "PrintFlag": {
        "help": "[Type: string] This key specifies the amount of informational data that is printed to the *.out.kinsol.log file. Choices for this key are NoVerbosity, LowVerbosity, NormalVerbosity and HighVerbosity. The choice NoVerbosity prints no statistics about the nonlinear convergence process. The choice LowVerbosity outputs the nonlinear iteration count, the scaled norm of the nonlinear function, and the number of function calls. The choice NormalVerbosity prints the same as for LowVerbosity and also the global strategy statistics. The choice HighVerbosity prints the same as for NormalVerbosity with the addition of further Krylov iteration statistics.\n",
        "default": "HighVerbosity",
        "domains": {
          "EnumDomain": {
            "enumList": [
              "NoVerbosity",
              "LowVerbosity",
              "NormalVerbosity",
              "HighVerbosity"
            ]
          }
        }
      },
      "EtaChoice": {
        "help": "[Type: string] This key specifies how the linear system tolerance will be selected. The linear system is solved until a relative residual reduction of n is achieved. Linear residual norms are measured in the l^2 norm. Choices for this key include EtaConstant, Walker1 and Walker2. If the choice EtaConstant is specified, then n will be taken as constant. The choices Walker1 and Walker2 specify choices for n developed by Eisenstat and Walker (see reference in manual). For both of the last two choices, n is never allowed to be less than 1e-4.\n",
        "default": "Walker2",
        "domains": {
          "EnumDomain": {
            "enumList": [
              "EtaConstant",
              "Walker1",
              "Walker2"
            ]
          }
        }
      },
      "EtaValue": {
        "help": "[Type: double] This key specifies the constant value of n for the EtaChoice key EtaConstant.\n",
        "default": 0.0001,
        "domains": {
          "DoubleValue": {
            "minValue": 0.0
          }
        }
      },
      "EtaAlpha": {
        "help": "[Type: double] This key specifies the value of alpha for the case of EtaChoice being Walker2.\n",
        "default": 2.0,
        "domains": {
          "DoubleValue": {
            "minValue": 0.0
          }
        }
      },
      "EtaGamma": {
        "help": "[Type: double] This key specifies the value of gamma for the case of EtaChoice being Walker2.\n",
        "default": 0.9,
        "domains": {
          "DoubleValue": {
            "minValue": 0.0
          }
        }
      },
      "UseJacobian": {
        "help": "[Type: boolean/string] This key specifies whether the Jacobian will be used in matrix-vector products or whether a matrix-free version of the code will run. Choices for this key are False and True. Using the Jacobian will most likely decrease the number of nonlinear iterations but require more memory to run.\n",
        "default": False,
        "domains": {
          "BoolDomain": None
        }
      },
      "DerivativeEpsilon": {
        "help": "[Type: double] This key specifies the value of epsilon used in approximating the action of the Jacobian on a vector with approximate directional derivatives of the nonlinear function. This parameter is only used when the UseJacobian key is False.\n",
        "default": 1e-07,
        "domains": {
          "DoubleValue": {
            "minValue": 0.0
          }
        }
      },
      "Globalization": {
        "help": "[Type: string] This key specifies the type of global strategy to use. Possible choices for this key are InexactNewton and LineSearch. The choice InexactNewton specifies no global strategy, and the choice LineSearch specifies that a line search strategy should be used where the nonlinear step can be lengthened or decreased to satisfy certain criteria.\n",
        "default": "LineSearch",
        "domains": {
          "EnumDomain": {
            "enumList": [
              "LineSearch",
              "InexactNewton"
            ]
          }
        }
      }
    }

# ------------------------------------------------------------------------------

class SILO(PFDBObj):
  '''
  These keys are used to control how SILO writes data. SILO allows writing to PDB and HDF5 file formats. SILO also allows data compression to be used, which can save significant amounts of disk space for some problems.
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Filetype = 'PDB'
    self.CompressionOptions = None
    self._details = {
      "Filetype": {
        "help": "[Type: string] This key is used to specify the SILO filetype. Allowed values are PDB and HDF5. Note that you must have configured SILO with HDF5 in order to use that option.\n",
        "default": "PDB",
        "domains": {
          "enumDomain": {
            "enumList": [
              "PDB",
              "HDF5"
            ]
          },
          "RequiresModule": "SILO"
        }
      },
      "CompressionOptions": {
        "help": "[Type: string] This key is used to specify the SILO compression options. See the SILO manual for the DB_SetCompression command for information on available options. NOTE: the options available are highly dependent on the configure options when building SILO.\n",
        "domains": {
          "AnyString": None,
          "RequiresModule": "SILO"
        }
      }
    }

# ------------------------------------------------------------------------------

class KnownSolution(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self._value = None
    self.Value = None
    self._details = {
      "_value": {
        "help": "[Type: string] This specifies the predefined function that will be used as the known solution. Possible choices for this key are No- KnownSolution, Constant, X, XPlusYPlusZ, X3Y2PlusSinXYPlus1, X3Y4PlusX2PlusSinXYCosYPlus1, XYZTPlus1 and XYZTPlus1PermTensor. Choices for this key correspond to solutions as follows: NoKnownSolution: No solution is known for this problem. Constant: p = constant X: p = x XPlusYPlusZ: p = x + y + z X3Y2PlusSinXYPlus1: p = x3y2 + sin(xy) + 1 X3Y4PlusX2PlusSinXYCosYPlus1: p = x3y4 + x2 + sin(xy) cos y + 1 XYZTPlus1: p = xyzt + 1 XYZTPlus1: p = xyzt + 1\n",
        "domains": {
          "MandatoryValue": None,
          "EnumDomain": {
            "enumList": [
              "NoKnownSolution",
              "Constant",
              "X",
              "XPlusYPlusZ",
              "X3Y2PlusSinXYPlus1",
              "X3Y4PlusX2PlusSinXYCosYPlus1",
              "XYZTPlus1",
              "XYZTPlus1"
            ]
          }
        }
      },
      "Value": {
        "help": "[Type: double] This key specifies the constant value of the known solution for type Constant known solutions.\n",
        "domains": {
          "DoubleValue": None
        }
      }
    }

# ------------------------------------------------------------------------------

class Wells(PFDBObj):
  '''
  Here we define the wells for the model.
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Names = None
    self._details = {
      "Names": {
        "help": "[Type: string] This key specifies the names fo the wells for which input data will be given.\n",
        "domains": {
          "AnyString": None
        },
        "handlers": {
          "WellUpdater": {
            "type": "ChildrenHandler",
            "className": "WellItem"
          }
        }
      }
    }

# ------------------------------------------------------------------------------

class WellItem(PFDBObj):
  '''
  Specifying properties for wells
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.InputType = None
    self.Action = None
    self.Type = None
    self.ExtractionType = None
    self.InjectionType = None
    self.X = None
    self.Y = None
    self.ZUpper = None
    self.ExtractionZUpper = None
    self.InjectionZUpper = None
    self.ZLower = None
    self.ExtractionZLower = None
    self.InjectionZLower = None
    self.Method = None
    self.ExtractionMethod = None
    self.InjectionMethod = None
    self.Cycle = None
    self._details = {
      "InputType": {
        "help": "[Type: string] This key specifies the type of well to be defined for the given well, well_name. This key can be either Vertical or Recirc. The value Vertical indicates that this is a single segmented well whose action will be specified by the user. The value Recirc indicates that this is a dual segmented, recirculating, well with one segment being an extraction well and another being an injection well. The extraction well filters out a specified fraction of each contaminant and recirculates the remainder to the injection well where the diluted fluid is injected back in. The phase saturations at the extraction well are passed without modification to the injection well. Note with the recirculating well, several input options are not needed as the extraction well will provide these values to the injection well.\n",
        "domains": {
          "EnumDomain": {
            "enumList": [
              "Vertical",
              "Recirc"
            ]
          }
        }
      },
      "Action": {
        "help": "[Type: string] This key specifies the pumping action of the well. This key can be either Injection or Extraction. A value of Injection indicates that this is an injection well. A value of Extraction indicates that this is an extraction well.\n",
        "domains": {
          "EnumDomain": {
            "enumList": [
              "Injection",
              "Extraction"
            ]
          }
        }
      },
      "Type": {
        "help": "[Type: string] This key specifies the mechanism by which the well works (how ParFlow works with the well data) if the input type key is set to Vertical. This key can be either Pressure or Flux. A value of Pressure indicates that the data provided for the well is in terms of hydrostatic pressure and ParFlow will ensure that the computed pressure field satisfies this condition in the computational cells which define the well. A value of Flux indicates that the data provided is in terms of volumetric flux rates and ParFlow will ensure that the flux field satisfies this condition in the computational cells which define the well.\n",
        "domains": {
          "EnumDomain": {
            "enumList": [
              "Pressure",
              "Flux"
            ]
          }
        }
      },
      "ExtractionType": {
        "help": "[Type: string] This key specifies the mechanism by which the extraction well works (how ParFlow works with the well data) if the input type key is set to Recirc. This key can be either Pressure or Flux. A value of Pressure indicates that the data provided for the well is in terms of hydrostatic pressure and ParFlow will ensure that the computed pressure field satisfies this condition in the computational cells which define the well. A value of Flux indicates that the data provided is in terms of volumetric flux rates and ParFlow will ensure that the flux field satisfies this condition in the computational cells which define the well.\n",
        "domains": {
          "EnumDomain": {
            "enumList": [
              "Pressure",
              "Flux"
            ]
          }
        }
      },
      "InjectionType": {
        "help": "[Type: string] This key specifies the mechanism by which the injection well works (how ParFlow works with the well data) if the input type key is set to Recirc. This key can be either Pressure or Flux. A value of Pressure indicates that the data provided for the well is in terms of hydrostatic pressure and ParFlow will ensure that the computed pressure field satisfies this condition in the computational cells which define the well. A value of Flux indicates that the data provided is in terms of volumetric flux rates and ParFlow will ensure that the flux field satisfies this condition in the computational cells which define the well.\n",
        "domains": {
          "EnumDomain": {
            "enumList": [
              "Pressure",
              "Flux"
            ]
          }
        }
      },
      "X": {
        "help": "[Type: double] This key specifies the x location of the vertical well if the input type is set to Vertical or of both the extraction and injection wells if the input type is set to Recirc.\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "Y": {
        "help": "[Type: double] This key specifies the y location of the vertical well if the input type is set to Vertical or of both the extraction and injection wells if the input type is set to Recirc.\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "ZUpper": {
        "help": "[Type: double] This key specifies the z location of the upper extent of a vertical well if the input type is set to Vertical.\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "ExtractionZUpper": {
        "help": "[Type: double] This key specifies the z location of the upper extent of a extraction well if the input type is set to Recirc.\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "InjectionZUpper": {
        "help": "[Type: double] This key specifies the z location of the upper extent of an injection well if the input type is set to Recirc.\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "ZLower": {
        "help": "[Type: double] This key specifies the z location of the lower extent of a vertical well if the input type is set to Vertical.\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "ExtractionZLower": {
        "help": "[Type: double] This key specifies the z location of the upper extent of a extraction well if the input type is set to Recirc.\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "InjectionZLower": {
        "help": "[Type: double] This key specifies the z location of the upper extent of an injection well if the input type is set to Recirc.\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "Method": {
        "help": "[Type: string] This key specifies a method by which pressure or flux for a vertical well will be weighted before assignment to computational cells. This key can only be Standard if the type key is set to Pressure; or this key can be either Standard,Weighted or Patterned if the type key is set to Flux. A value of Standard indicates that the pressure or flux data will be used as is. A value of Weighted indicates that the flux data is to be weighted by the cells permeability divided by the sum of all cell permeabilities which define the well. The value of Patterned is not implemented.\n",
        "domains": {
          "EnumDomain": {
            "enumList": [
              "Standard",
              "Weighted",
              "Patterned"
            ]
          }
        }
      },
      "ExtractionMethod": {
        "help": "[Type: string] This key specifies a method by which pressure or flux for an extraction well will be weighted before assignment to computational cells. This key can only be Standard if the type key is set to Pressure; or this key can be either Standard, Weighted or Patterned if the type key is set to Flux. A value of Standard indicates that the pressure or flux data will be used as is. A value of Weighted indicates that the flux data is to be weighted by the cells permeability divided by the sum of all cell permeabilities which define the well. The value of Patterned is not implemented.\n",
        "domains": {
          "EnumDomain": {
            "enumList": [
              "Standard",
              "Weighted",
              "Patterned"
            ]
          }
        }
      },
      "InjectionMethod": {
        "help": "[Type: string] This key specifies a method by which pressure or flux for an injection well will be weighted before assignment to computational cells. This key can only be Standard if the type key is set to Pressure; or this key can be either Standard, Weighted or Patterned if the type key is set to Flux. A value of Standard indicates that the pressure or flux data will be used as is. A value of Weighted indicates that the flux data is to be weighted by the cells permeability divided by the sum of all cell permeabilities which define the well. The value of Patterned is not implemented.\n",
        "domains": {
          "EnumDomain": {
            "enumList": [
              "Standard",
              "Weighted",
              "Patterned"
            ]
          }
        }
      },
      "Cycle": {
        "help": "[Type: string] This key specifies the time cycles to which data for the well well_name corresponds.\n",
        "domains": {
          "AnyString": None
        }
      }
    }
    self._dynamic = {
      "WellIntervalItem": "/Cycle/{CycleItem}/Names"
    }
    self.processDynamic()

# ------------------------------------------------------------------------------

class WellIntervalItem(PFDBObj):
  '''
  This is to set properties for named wells within specified cycles.
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Pressure = Pressure(self)
    self.Saturation = Saturation_1(self)
    self.Flux = Flux(self)
    self.Concentration = Concentration(self)
    self.Extraction = Extraction(self)
    self.Injection = Injection(self)

# ------------------------------------------------------------------------------

class Pressure(PFDBObj):
  '''
  Setting pressure for a named well within a specified cycle.
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Value = None
    self._details = {
      "Value": {
        "__rst__": {
          "name": "Wells.{well_name}.{interval_name}.Pressure.Value"
        },
        "help": "[Type: double] This key specifies the hydrostatic pressure value for a vertical well if the type key is set to Pressure. Note This value gives the pressure of the primary phase (water) at z = 0. The other phase pressures (if any) are computed from the physical relationships that exist between the phases.\n",
        "domains": {
          "DoubleValue": None
        }
      }
    }

# ------------------------------------------------------------------------------

class Saturation_1(PFDBObj):
  '''
  Setting saturation for a named well within a specified cycle for a specific phase.
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Value = None
    self._details = {
      "Value": {
        "__rst__": {
          "name": "Wells.{well_name}.{interval_name}.Saturation.{phase_name}.Value"
        },
        "help": "[Type: double] This key specifies the saturation value of a vertical well.\n",
        "domains": {
          "DoubleValue": {
            "minValue": 0.0,
            "maxValue": 1.0
          }
        }
      }
    }

# ------------------------------------------------------------------------------

class Flux(PFDBObj):
  '''
  Setting flux for a named well within a specified cycle for a specific phase.
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Value = None
    self._details = {
      "Value": {
        "__rst__": {
          "name": "Wells.{well_name}.{interval_name}.Flux.{phase_name}.Value"
        },
        "help": "[Type: double] This key specifies the volumetric flux for a vertical well if the type key is set to Flux. Note only a positive number should be entered, ParFlow assigns the correct sign based on the chosen action for the well.\n",
        "domains": {
          "DoubleValue": None
        }
      }
    }

# ------------------------------------------------------------------------------

class Concentration(PFDBObj):
  '''
  Setting contaminant value of vertical well.
  '''

# ------------------------------------------------------------------------------

class ConcentrationPhaseItem(PFDBObj):
  '''
  '''

# ------------------------------------------------------------------------------

class ConcentrationPhaseContItem(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Value = None
    self._details = {
      "Value": {
        "help": "[Type: double] This key specifies the contaminant value of a vertical well.\n",
        "domains": {
          "DoubleValue": None
        }
      }
    }

# ------------------------------------------------------------------------------

class Extraction(PFDBObj):
  '''
  Setting extraction pressure for a named well within a specified cycle.
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Pressure = Pressure_1(self)
    self.Flux = Flux_1(self)

# ------------------------------------------------------------------------------

class Pressure_1(PFDBObj):
  '''
  Setting extraction pressure for a named well within a specified cycle.
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Value = None
    self._details = {
      "Value": {
        "__rst__": {
          "name": "Wells.{well_name}.{interval_name}.Extraction.Pressure.Value"
        },
        "help": "[Type: double] This key specifies the hydrostatic pressure value for an extraction well if the extraction type key is set to Pressure. Note This value gives the pressure of the primary phase (water) at z = 0. The other phase pressures (if any) are computed from the physical relationships that exist between the phases.\n",
        "domains": {
          "DoubleValue": None
        }
      }
    }

# ------------------------------------------------------------------------------

class Flux_1(PFDBObj):
  '''
  Setting flux for a named well within a specified cycle for a specific phase in an extraction well.
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self._dynamic = {
      "ExtractionFluxPhaseItem": "/Phase/Names"
    }
    self.processDynamic()

# ------------------------------------------------------------------------------

class ExtractionFluxPhaseItem(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Value = None
    self._details = {
      "Value": {
        "__rst__": {
          "name": "Wells.{well_name}.{interval_name}.Extraction.Flux.{phase_name}.Value"
        },
        "help": "[Type: double] This key specifies the volumetric flux for an extraction well if the extraction type key is set to Flux. Note only a positive number should be entered, ParFlow assigns the correct sign based on the chosen action for the well.\n",
        "domains": {
          "DoubleValue": None
        }
      }
    }

# ------------------------------------------------------------------------------

class Injection(PFDBObj):
  '''
  Setting extraction pressure for a named well within a specified cycle.
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Pressure = Pressure_2(self)
    self.Flux = Flux_2(self)
    self.Concentration = Concentration_1(self)

# ------------------------------------------------------------------------------

class Pressure_2(PFDBObj):
  '''
  Setting extraction pressure for a named well within a specified cycle.
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Value = None
    self._details = {
      "Value": {
        "__rst__": {
          "name": "Wells.{well_name}.{interval_name}.Injection.Pressure.Value"
        },
        "help": "[Type: double] This key specifies the hydrostatic pressure value for an extraction well if the extraction type key is set to Pressure. Note This value gives the pressure of the primary phase (water) at z = 0. The other phase pressures (if any) are computed from the physical relationships that exist between the phases.\n",
        "domains": {
          "DoubleValue": None
        }
      }
    }

# ------------------------------------------------------------------------------

class Flux_2(PFDBObj):
  '''
  Setting flux for a named well within a specified cycle for a specific phase in an injection well.
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self._dynamic = {
      "InjectionFluxPhaseItem": "/Phase/Names"
    }
    self.processDynamic()

# ------------------------------------------------------------------------------

class InjectionFluxPhaseItem(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Value = None
    self._details = {
      "Value": {
        "__rst__": {
          "name": "Wells.{well_name}.{interval_name}.Injection.Flux.{phase_name}.Value"
        },
        "help": "[Type: double] This key specifies the volumetric flux for an injection well if the injection type key is set to Flux. Note only a positive number should be entered, ParFlow assigns the correct sign based on the chosen action for the well.\n",
        "domains": {
          "DoubleValue": None
        }
      }
    }

# ------------------------------------------------------------------------------

class Concentration_1(PFDBObj):
  '''
  Setting the fraction of the extracted contaminant which gets resupplied to the injection well.
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self._dynamic = {
      "InjectionConcentrationPhaseItem": "/Phase/Names"
    }
    self.processDynamic()

# ------------------------------------------------------------------------------

class InjectionConcentrationPhaseItem(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self._dynamic = {
      "InjectionConcentrationPhaseContaminantItem": "/Contaminants/Names"
    }
    self.processDynamic()

# ------------------------------------------------------------------------------

class InjectionConcentrationPhaseContaminantItem(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Fraction = None
    self._details = {
      "Fraction": {
        "help": "[Type: double] This key specifies the fraction of the extracted contaminant which gets resupplied to the injection well.\n",
        "domains": {
          "DoubleValue": {
            "minValue": 0.0,
            "maxValue": 1.0
          }
        }
      }
    }

# ------------------------------------------------------------------------------

class TimingInfo(PFDBObj):
  '''
  Setting timing parameters
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.BaseUnit = None
    self.StartCount = None
    self.StartTime = None
    self.StopTime = None
    self.DumpInterval = None
    self.DumpIntervalExecutionTimeLimit = 0
    self._details = {
      "BaseUnit": {
        "help": "[Type: double] This key is used to indicate the base unit of time for entering time values. All time should be expressed as a multiple of this value. This should be set to the smallest interval of time to be used in the problem. For example, a base unit of \u201c1\u201d means that all times will be integer valued. A base unit of \u201c0.5\u201d would allow integers and fractions of 0.5 to be used for time input values. The rationale behind this restriction is to allow time to be discretized on some interval to enable integer arithmetic to be used when computing/comparing times. This avoids the problems associated with real value comparisons which can lead to events occurring at different timesteps on different architectures or compilers. This value is also used when describing \u201ctime cycling data\u201d in, currently, the well and boundary condition sections. The lengths of the cycles in those sections will be integer multiples of this value, therefore it needs to be the smallest divisor which produces an integral result for every \u201creal time\u201d cycle interval length needed.\n",
        "domains": {
          "DoubleValue": {
            "minValue": 0.0
          }
        }
      },
      "StartCount": {
        "help": "[Type: int] This key is used to indicate the time step number that will be associated with the first advection cycle in a transient problem. The value -1 indicates that advection is not to be done. The value 0 indicates that advection should begin with the given initial conditions. Values greater than 0 are intended to mean \u201crestart\u201d from some previous \u201ccheckpoint\u201d time-step, but this has not yet been implemented.\n",
        "domains": {
          "IntValue": {
            "minValue": -1,
            "maxValue": 0
          }
        }
      },
      "StartTime": {
        "help": "[Type: double] This key is used to indicate the starting time for the simulation.\n",
        "domains": {
          "MandatoryValue": None,
          "DoubleValue": None
        }
      },
      "StopTime": {
        "help": "[Type: double] This key is used to indicate the stopping time for the simulation.\n",
        "domains": {
          "MandatoryValue": None,
          "DoubleValue": None
        }
      },
      "DumpInterval": {
        "help": "[Type: double] This key is the real time interval at which time-dependent output should be written. A value of 0 will produce undefined behavior. If the value is negative, output will be dumped out every n time steps, where n is the absolute value of the integer part of the value.\n",
        "domains": {
          "MandatoryValue": None,
          "DoubleValue": {
            "negInt": True
          }
        }
      },
      "DumpIntervalExecutionTimeLimit": {
        "help": "[Type: int] This key is used to indicate a wall clock time to halt the execution of a run. At the end of each dump interval the time remaining in the batch job is compared with the user supplied value, if remaining time is less than or equal to the supplied value the execution is halted. Typically used when running on batch systems with time limits to force a clean shutdown near the end of the batch job. Time units is seconds, a value of 0 (the default) disables the check. Currently only supported on SLURM based systems, \u201c\u2013with-slurm\u201d must be specified at configure time to enable.\n",
        "default": 0,
        "domains": {
          "IntValue": None
        }
      }
    }

# ------------------------------------------------------------------------------

class TimeStep(PFDBObj):
  '''
  Setting parameters for modeled time steps
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Type = None
    self.Value = None
    self.InitialStep = None
    self.GrowthFactor = None
    self.MaxStep = None
    self.MinStep = None
    self._details = {
      "Type": {
        "help": "[Type: string] This key must be one of: Constant or Growth. The value Constant defines a constant time step. The value Growth defines a time step that starts as dt0 and is defined for other steps as dtnew = gamma*dtold such that dtnew is less than or equal to dtmax and dtnew is greater than or equal to dtmin.\n",
        "domains": {
          "MandatoryValue": None,
          "EnumDomain": {
            "enumList": [
              "Constant",
              "Growth"
            ]
          }
        }
      },
      "Value": {
        "help": "[Type: double] This key is used only if a constant time step is selected and indicates the value of the time step for all steps taken.\n",
        "domains": {
          "DoubleValue": None
        },
        "crosscheck": {
          "MandatoryIf": {
            "TimeStep.Type": "Constant"
          }
        }
      },
      "InitialStep": {
        "help": "[Type: double] This key specifies the initial time step dt0 if the Growth type time step is selected.\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "GrowthFactor": {
        "help": "[Type: double] This key specifies the growth factor gamma by which a time step will be multiplied to get the new time step when the Growth type time step is selected.\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "MaxStep": {
        "help": "[Type: double] This key specifies the maximum time step allowed, dtmax, when the Growth type time step is selected.\n",
        "domains": {
          "DoubleValue": {
            "minValue": 0.0
          }
        }
      },
      "MinStep": {
        "help": "[Type: double] This key specifies the minimum time step allowed, dtmin, when the Growth type time step is selected.\n",
        "domains": {
          "DoubleValue": {
            "minValue": 0.0
          }
        }
      }
    }

# ------------------------------------------------------------------------------

class Cycle(PFDBObj):
  '''
  Setting properties for cycles and intervals within those cycles.
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Names = None
    self._details = {
      "Names": {
        "help": "[Type: string] This key is used to specify the named time cycles to be used in a simulation. It is a list of names and each name defines a time cycle and the number of items determines the total number of time cycles specified. Each named cycle is described using a number of keys defined under Cycle.\n",
        "domains": {
          "AnyString": None
        },
        "handlers": {
          "CycleUpdater": {
            "type": "ChildrenHandler",
            "className": "CycleItem",
            "location": "."
          }
        }
      }
    }

# ------------------------------------------------------------------------------

class CycleItem(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Names = None
    self.Repeat = None
    self._details = {
      "Names": {
        "help": "[Type: string] This key is used to specify the named time intervals for each cycle. It is a list of names and each name defines a time interval when a specific boundary condition is applied and the number of items determines the total number of intervals in that time cycle.\n",
        "domains": {
          "AnyString": None
        },
        "handlers": {
          "CycleUpdater": {
            "type": "ChildrenHandler",
            "className": "CycleIntItem",
            "location": "."
          },
          "WellIntervalItemUpdater": {
            "type": "ChildrenHandler",
            "className": "WellIntervalItem",
            "location": "/Wells/{WellItem}"
          }
        }
      },
      "Repeat": {
        "help": "[Type: int] This key is used to specify the how many times a named time interval repeats. A positive value specifies a number of repeat cycles a value of -1 specifies that the cycle repeat for the entire simulation.\n",
        "domains": {
          "MandatoryValue": None,
          "IntValue": {
            "minValue": -1
          }
        }
      }
    }

# ------------------------------------------------------------------------------

class CycleIntItem(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Length = None
    self._details = {
      "Length": {
        "help": "[Type: int] This key is used to specify the length of a named time intervals. It is an integer multiplier of the value set for the TimingInfo.BaseUnit key described above. The total length of a given time cycle is the sum of all the intervals multiplied by the base unit.\n",
        "domains": {
          "IntValue": {
            "minValue": 1
          }
        }
      }
    }

# ------------------------------------------------------------------------------

class Phase(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.RelPerm = RelPerm_1(self)
    self.Saturation = Saturation_2(self)
    self.ThermalConductivity = ThermalConductivity_1(self)
    self.Names = None
    self._details = {
      "Names": {
        "help": "[Type: string] This specifies the names of phases to be modeled. Currently only 1 or 2 phases may be modeled.\n",
        "domains": {
          "AnyString": None
        },
        "handlers": {
          "PhaseUpdater": {
            "type": "ChildrenHandler",
            "className": "PhaseNameItem",
            "location": "."
          },
          "PhaseSourceUpdater": {
            "type": "ChildrenHandler",
            "className": "PhaseSourceNameItem",
            "location": "/PhaseSources"
          },
          "PhaseConcenUpdater": {
            "type": "ChildrenHandler",
            "className": "PhaseConcenPhaseNameItem",
            "location": "/PhaseConcen"
          },
          "ExtractionFluxPhaseUpdater": {
            "type": "ChildrenHandler",
            "className": "ExtractionFluxPhaseItem",
            "location": "/Wells/{WellItem}/{WellIntervalItem}/Extraction/Flux"
          },
          "InjectionFluxPhaseUpdater": {
            "type": "ChildrenHandler",
            "className": "InjectionFluxPhaseItem",
            "location": "/Wells/{WellItem}/{WellIntervalItem}/Injection/Flux"
          },
          "InjectionConcentrationPhaseUpdater": {
            "type": "ChildrenHandler",
            "className": "InjectionConcentrationPhaseItem",
            "location": "/Wells/{WellItem}/{WellIntervalItem}/Injection/Concentration"
          },
          "ICSaturationPhaseUpdater": {
            "type": "ChildrenHandler",
            "className": "GeomICSaturationPhaseItem",
            "location": "/Geom/{GeomItem}/ICSaturation"
          }
        }
      }
    }

# ------------------------------------------------------------------------------

class RelPerm_1(PFDBObj):
  '''
  The following keys are used to describe relative permeability input for the Richards’ equation implementation. They will be ignored if a full two-phase formulation is used.
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.VanGenuchten = VanGenuchten(self)
    self.Type = None
    self.GeomNames = None
    self._details = {
      "Type": {
        "help": "[Type: string] This key specifies the type of relative permeability function that will be used on all specified geometries. Note that only one type of relative permeability may be used for the entire problem. However, parameters may be different for that type in different geometries. For instance, if the problem consists of three geometries, then VanGenuchten may be specified with three different sets of parameters for the three different geometries. However, once VanGenuchten is specified, one geometry cannot later be specified to have Data as its relative permeability. The possible values for this key are Constant, VanGenuchten, Haverkamp, Data, and Polynomial.\n",
        "domains": {
          "EnumDomain": {
            "enumList": [
              "Constant",
              "VanGenuchten",
              "Haverkamp",
              "Data",
              "Polynomial"
            ]
          }
        }
      },
      "GeomNames": {
        "help": "[Type: string] This key specifies the geometries on which relative permeability will be given. The union of these geometries must cover the entire computational domain.\n",
        "domains": {
          "AnyString": None
        }
      }
    }

# ------------------------------------------------------------------------------

class VanGenuchten(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.File = 0
    self._details = {
      "File": {
        "help": "[Type: int] This key specifies whether soil parameters for the VanGenuchten function are specified in a pfb file or by region. The options are either 0 for specification by region, or 1 for specification in a file. Note that either all parameters are specified in files (each has their own input file) or none are specified by files. Parameters specified by files are: alpha and N.\n",
        "default": 0,
        "domains": {
          "IntValue": {
            "minValue": 0,
            "maxValue": 1
          }
        }
      }
    }

# ------------------------------------------------------------------------------

class Saturation_2(PFDBObj):
  '''
  This section is only relevant to the Richards’ equation cases. All keys relating to this section will be ignored for other cases. The following keys are used to define the saturation-pressure curve.
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.VanGenuchten = VanGenuchten_1(self)
    self.Type = None
    self.GeomNames = None
    self._details = {
      "Type": {
        "help": "[Type: string] This key specifies the type of saturation function that will be used on all specified geometries. Note that only one type of saturation may be used for the entire problem. However, parameters may be different for that type in different geometries. For instance, if the problem consists of three geometries, then VanGenuchten may be specified with three different sets of parameters for the three different goemetries. However, once VanGenuchten is specified, one geometry cannot later be specified to have Data as its saturation. The possible values for this key are Constant, VanGenuchten, Haverkamp, Data, Polynomial and PFBFile.\n",
        "domains": {
          "EnumDomain": {
            "enumList": [
              "Constant",
              "VanGenuchten",
              "Haverkamp",
              "Data",
              "Polynomial",
              "PFBFile"
            ]
          }
        }
      },
      "GeomNames": {
        "help": "[Type: string] This key specifies the geometries on which saturation will be given. The union of these geometries must cover the entire computational domain.\n",
        "domains": {
          "AnyString": None
        }
      }
    }

# ------------------------------------------------------------------------------

class VanGenuchten_1(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.File = 0
    self._details = {
      "File": {
        "help": "[Type: int] This key specifies whether soil parameters for the VanGenuchten function are specified in a pfb file or by region. The options are either 0 for specification by region, or 1 for specification in a file. Note that either all parameters are specified in files (each has their own input file) or none are specified by files. Parameters specified by files are alpha, N, SRes, and SSat.\n",
        "default": 0,
        "domains": {
          "IntValue": {
            "minValue": 0,
            "maxValue": 1
          }
        }
      }
    }

# ------------------------------------------------------------------------------

class ThermalConductivity_1(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Function1 = Function1(self)

# ------------------------------------------------------------------------------

class Function1(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.File = None
    self._details = {
      "File": {
        "help": "[Type: string] This specifies the file name for the thermal conductivity function.\n",
        "domains": {
          "AnyString": None
        }
      }
    }

# ------------------------------------------------------------------------------

class PhaseNameItem(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Density = Density(self)
    self.Viscosity = Viscosity(self)
    self.Mobility = Mobility(self)
    self.HeatCapacity = HeatCapacity_1(self)
    self.InternalEnergy = InternalEnergy(self)
    self.Geom = Geom_4(self)

# ------------------------------------------------------------------------------

class Density(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Type = None
    self.Value = None
    self.ReferenceDensity = None
    self.CompressibilityConstant = None
    self._details = {
      "Type": {
        "help": "[Type: string] This key specifies whether density will be a constant value or if it will be given by an equation of state of the form (rd)exp(cP), where P is pressure, rd is the density at atmospheric pressure, and c is the phase compressibility constant. This key must be either Constant or EquationOfState.\n",
        "domains": {
          "EnumDomain": {
            "enumList": [
              "Constant",
              "EquationOfState"
            ]
          }
        }
      },
      "Value": {
        "help": "[Type: double] This specifies the value of density if this phase was specified to have a constant density value for the phase phase_name.\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "ReferenceDensity": {
        "help": "[Type: double] This key specifies the reference density if an equation of state density function is specified for the phase phase_name.\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "CompressibilityConstant": {
        "help": "[Type: double] This key specifies the phase compressibility constant if an equation of state density function is specified for the phase phase_name.\n",
        "domains": {
          "DoubleValue": None
        }
      }
    }

# ------------------------------------------------------------------------------

class Viscosity(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Type = 'Constant'
    self.Value = None
    self._details = {
      "Type": {
        "help": "[Type: string] This key specifies whether viscosity will be a constant value. Currently, the only choice for this key is Constant.\n",
        "default": "Constant",
        "domains": {
          "MandatoryValue": None,
          "EnumDomain": {
            "enumList": [
              "Constant"
            ]
          }
        }
      },
      "Value": {
        "help": "[Type: double] This specifies the value of density if this phase was specified to have a constant density value for the phase phase_name.\n",
        "domains": {
          "MandatoryValue": None,
          "DoubleValue": None
        }
      }
    }

# ------------------------------------------------------------------------------

class Mobility(PFDBObj):
  '''
  Here we define phase mobilities by specifying the relative permeability function. Input is specified differently depending on what problem is being specified. For full multi-phase problems, the following input keys are used. See the next section for the correct Richards’ equation input format.
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Type = 'Constant'
    self.Value = None
    self.Exponent = 2.0
    self.IrreducibleSaturation = 0.0
    self._details = {
      "Type": {
        "help": "[Type: string] This key specifies whether the mobility for phase_name will be a given constant or a polynomial of the form, (S-So)^a, where S is saturation, So is irreducible saturation, and a is some exponent. The possibilities for this key are Constant and Polynomial.\n",
        "default": "Constant",
        "domains": {
          "EnumDomain": {
            "enumList": [
              "Constant",
              "Polynomial"
            ]
          }
        }
      },
      "Value": {
        "help": "[Type: double] This key specifies the constant mobility value for phase phase_name.\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "Exponent": {
        "help": "[Type: double] This key specifies the exponent used in a polynomial representation of the relative permeability. Currently, only a value of 2.0 is allowed for this key.\n",
        "default": 2.0,
        "domains": {
          "DoubleValue": {
            "minValue": 2.0,
            "maxValue": 2.0
          }
        }
      },
      "IrreducibleSaturation": {
        "help": "[Type: double] This key specifies the irreducible saturation used in a polynomial representation of the relative permeability. Currently, only a value of 0.0 is allowed for this key.\n",
        "default": 0.0,
        "domains": {
          "DoubleValue": {
            "minValue": 0.0,
            "maxValue": 0.0
          }
        }
      }
    }

# ------------------------------------------------------------------------------

class HeatCapacity_1(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.GeomNames = None
    self.Type = None
    self._details = {
      "GeomNames": {
        "help": "[Type: string] This specifies the geometry names for setting the heat capacity.\n",
        "domains": {
          "AnyString": None
        },
        "handlers": {
          "PhaseNameHeatGeomItemUpdater": {
            "type": "ChildrenHandler",
            "className": "PhaseNameHeatGeomItem",
            "location": "/Phase/{PhaseNameItem}/Geom"
          }
        }
      },
      "Type": {
        "help": "[Type: string] This specifies the type of heat capacity.\n",
        "domains": {
          "AnyString": None
        }
      }
    }

# ------------------------------------------------------------------------------

class InternalEnergy(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Type = None
    self.Value = None
    self._details = {
      "Type": {
        "help": "[Type: string] This specifies the type of internal energy.\n",
        "domains": {
          "AnyString": None
        }
      },
      "Value": {
        "help": "[Type: double] This specifies the value for the internal energy.\n",
        "domains": {
          "DoubleValue": None
        }
      }
    }

# ------------------------------------------------------------------------------

class Geom_4(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self._dynamic = {
      "PhaseNameHeatGeomItem": "/Phase/{PhaseNameItem}/HeatCapacity/GeomNames"
    }
    self.processDynamic()

# ------------------------------------------------------------------------------

class PhaseNameHeatGeomItem(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.HeatCapacity = HeatCapacity_2(self)

# ------------------------------------------------------------------------------

class HeatCapacity_2(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Value = None
    self._details = {
      "Value": {
        "help": "[Type: double] This specifies the heat capacity value for the specified geometric unit.\n",
        "domains": {
          "DoubleValue": None
        }
      }
    }

# ------------------------------------------------------------------------------

class PhaseConcen(PFDBObj):
  '''
  Here we define initial concentration conditions for contaminants.
  '''

# ------------------------------------------------------------------------------

class PhaseConcenPhaseNameItem(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self._dynamic = {
      "PhaseConcenContaminantItem": "/Contaminants/Names"
    }
    self.processDynamic()

# ------------------------------------------------------------------------------

class PhaseConcenContaminantItem(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Geom = Geom_5(self)
    self.GeomNames = None
    self.Type = None
    self.FileName = None
    self._details = {
      "GeomNames": {
        "help": "[Type: string] This key specifies the geometries on which an initial condition will be given, if the type was set to Constant. Note that geometries listed later \u201coverlay\u201d geometries listed earlier.\n",
        "domains": {
          "AnyString": None
        },
        "handlers": {
          "PhaseConcenContaminantGeomItemUpdater": {
            "type": "ChildrenHandler",
            "className": "PhaseConcenContaminantGeomItem",
            "location": "/PhaseConcen/{PhaseConcenPhaseNameItem}/{PhaseConcenContaminantItem}/Geom"
          }
        }
      },
      "Type": {
        "help": "[Type: string] This key specifies the type of initial condition that will be applied to different geometries for given phase, phase_name, and the given contaminant, contaminant_name. The choices for this key are Constant or PFBFile. The choice Constant will apply constants values to different geometries. The choice PFBFile will read values from a \u201cParFlow Binary\u201d file.\n",
        "domains": {
          "EnumDomain": {
            "enumList": [
              "Constant",
              "PFBFile"
            ]
          }
        }
      },
      "FileName": {
        "help": "[Type: string] This key specifies the name of the \u201cParFlow Binary\u201d file which contains the initial condition values if the type was set to PFBFile.\n",
        "domains": {
          "AnyString": None
        }
      }
    }

# ------------------------------------------------------------------------------

class Geom_5(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self._dynamic = {
      "PhaseConcenContaminantGeomItem": "/PhaseConcen/{PhaseConcenPhaseNameItem}/{PhaseConcenContaminantItem}/GeomNames"
    }
    self.processDynamic()

# ------------------------------------------------------------------------------

class PhaseConcenContaminantGeomItem(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Value = None
    self._details = {
      "Value": {
        "help": "[Type: double] This key specifies the initial condition value assigned to all points in the named geometry, geom_input_name, if the type was set to Constant.\n",
        "domains": {
          "DoubleValue": None
        }
      }
    }

# ------------------------------------------------------------------------------

class PhaseSources(PFDBObj):
  '''
  The following keys are used to specify phase source terms. The units of the source term are 1=T . So, for example, to specify a region with constant flux rate of L3=T , one must be careful to convert this rate to the proper units by dividing by the volume of the enclosing region. For Richards’ equation input, the source term must be given as a flux multiplied by density.
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Geom = Geom_6(self)

# ------------------------------------------------------------------------------

class Geom_6(PFDBObj):
  '''
  '''

# ------------------------------------------------------------------------------

class PhaseSourceGeomItem(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Value = None
    self._details = {
      "Value": {
        "help": "[Type: double] This key specifies the value of a constant source term applied to phase phase _name on geometry geom_name.\n",
        "domains": {
          "DoubleValue": None
        }
      }
    }

# ------------------------------------------------------------------------------

class PhaseSourceNameItem(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Geom = Geom_7(self)
    self.Type = None
    self.GeomNames = None
    self.PredefinedFunction = None
    self._details = {
      "Type": {
        "help": "[Type: string] This key specifies the type of source to use for phase phase_name. Possible values for this key are Constant and PredefinedFunction. Constant type phase sources specify a constant phase source value for a given set of regions. PredefinedFunction type phase sources use a preset function (choices are listed below) to specify the source. Note that the PredefinedFunction type can only be used to set a single source over the entire domain and not separate sources over different regions.\n",
        "domains": {
          "EnumDomain": {
            "enumList": [
              "Constant",
              "PredefinedFunction"
            ]
          }
        }
      },
      "GeomNames": {
        "help": "[Type: string] This key specifies the names of the geometries on which source terms will be specified. This is used only for Constant type phase sources. Regions listed later \u201coverlay\u201d regions listed earlier.\n",
        "domains": {
          "AnyString": None
        },
        "handlers": {
          "PhaseSourceGeomUpdater": {
            "type": "ChildrenHandler",
            "className": "PhaseSourcePhaseGeomItem",
            "location": "./Geom"
          }
        }
      },
      "PredefinedFunction": {
        "help": "[Type: string] This key specifies which of the predefined functions will be used for the source. Possible values for this key are X, XPlusYPlusZ, X3Y2PlusSinXYPlus1, X3Y4PlusX2PlusSinXYCosYPlus1, XYZTPlus1 and XYZTPlus1PermTensor.\n",
        "domains": {
          "EnumDomain": {
            "enumList": [
              "X",
              "XPlusYPlusZ",
              "X3Y2PlusSinXYPlus1",
              "X3Y4PlusX2PlusSinXYCosYPlus1",
              "XYZTPlus1",
              "XYZTPlus1PermTensor"
            ]
          }
        }
      }
    }

# ------------------------------------------------------------------------------

class Geom_7(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self._dynamic = {
      "PhaseSourcePhaseGeomItem": "/PhaseSources/{PhaseSourceNameItem}/GeomNames"
    }
    self.processDynamic()

# ------------------------------------------------------------------------------

class PhaseSourcePhaseGeomItem(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Value = None
    self._details = {
      "Value": {
        "help": "[Type: double] This key specifies the value of a constant source term applied to phase phase _name on geometry geom_name.\n",
        "domains": {
          "DoubleValue": None
        }
      }
    }

# ------------------------------------------------------------------------------

class Contaminants(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Names = None
    self._details = {
      "Names": {
        "help": "[Type: string] This specifies the names of contaminants to be advected.\n",
        "domains": {
          "AnyString": None
        },
        "handlers": {
          "ContaminantNameUpdater": {
            "type": "ChildrenHandler",
            "className": "ContNameItem",
            "location": "."
          },
          "ContaminantGeomNameUpdater": {
            "type": "ChildrenHandler",
            "className": "GeomContItem",
            "location": "/Geom/{GeomItem}/"
          },
          "InjectionConcentrationPhaseContaminantUpdater": {
            "type": "ChildrenHandler",
            "className": "InjectionConcentrationPhaseContaminantItem",
            "location": "/Wells/{WellItem}/{WellIntervalItem}/Injection/Concentration/{InjectionConcentrationPhaseItem}"
          },
          "PhaseConcenContNameItemUpdater": {
            "type": "ChildrenHandler",
            "className": "PhaseConcenContaminantItem",
            "location": "/PhaseConcen/{PhaseConcenPhaseNameItem}/"
          }
        }
      }
    }

# ------------------------------------------------------------------------------

class ContNameItem(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Degradation = Degradation(self)

# ------------------------------------------------------------------------------

class Degradation(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Value = None
    self._details = {
      "Value": {
        "help": "[Type: double] This key specifies the half-life decay rate of the named contaminant, contaminant_name. At present only first- order decay reactions are implemented and it is assumed that one contaminant cannot decay into another.\n",
        "domains": {
          "DoubleValue": None
        }
      }
    }

# ------------------------------------------------------------------------------

class InternalBC(PFDBObj):
  '''
  In this section, we define internal Dirichlet boundary conditions by setting the pressure at points in the domain.
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Names = None
    self._details = {
      "Names": {
        "help": "[Type: string] This key specifies the names for the internal boundary conditions. At each named point, x, y and z will specify the coordinate locations and h will specify the hydraulic head value of the condition. This real location is \u201csnapped\u201d to the nearest gridpoint in ParFlow. NOTE: Currently, ParFlow assumes that internal boundary conditions and pressure wells are separated by at least one cell from any external boundary. The user should be careful of this when defining the input file and grid.\n",
        "domains": {
          "AnyString": None
        },
        "handlers": {
          "IntBCUpdater": {
            "type": "ChildrenHandler",
            "className": "InternalBCItem"
          }
        }
      }
    }

# ------------------------------------------------------------------------------

class InternalBCItem(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.X = None
    self.Y = None
    self.Z = None
    self.Value = None
    self._details = {
      "X": {
        "help": "[Type: double] This key specifies the x-coordinate, x, of the named, internal_bc_name, condition.\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "Y": {
        "help": "[Type: double] This key specifies the y-coordinate, y, of the named, internal_bc_name, condition.\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "Z": {
        "help": "[Type: double] This key specifies the z-coordinate, z, of the named, internal_bc_name, condition.\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "Value": {
        "help": "[Type: double] This key specifies the value of the named, internal_bc_name, condition.\n",
        "domains": {
          "DoubleValue": None
        }
      }
    }

# ------------------------------------------------------------------------------

class BCPressure(PFDBObj):
  '''
  Here we define the pressure boundary conditions. The Dirichlet conditions below are hydrostatic conditions, and it is assumed that at each phase interface the pressure is constant. It is also assumed here that all phases are distributed within the domain at all times such that the lighter phases are vertically higher than the heavier phases. Boundary condition input is associated with domain patches. Note that different patches may have different types of boundary conditions on them.
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.PatchNames = None
    self._details = {
      "PatchNames": {
        "help": "[Type: string] This key specifies the names of patches on which pressure boundary conditions will be specified. Note that these must all be patches on the external boundary of the domain and these patches must \u201ccover\u201d that external boundary.\n",
        "domains": {
          "AnyString": None
        },
        "handlers": {
          "BCItemUpdater": {
            "type": "ChildrenHandler",
            "className": "BCItem",
            "location": "../Patch"
          }
        }
      }
    }

# ------------------------------------------------------------------------------

class BCSaturation(PFDBObj):
  '''
  Note: this section needs to be defined only for multi-phase flow and should not be defined for the single phase and Richards’ equation cases. Here we define the boundary conditions for the saturations. Boundary condition input is associated with domain patches. Note that different patches may have different types of boundary conditions on them.
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.PatchNames = None
    self._details = {
      "PatchNames": {
        "help": "[Type: string] This key specifies the names of patches on which saturation boundary conditions will be specified. Note that these must all be patches on the external boundary of the domain and these patches must \u201ccover\u201d that external boundary.\n",
        "domains": {
          "AnyString": None
        },
        "handlers": {
          "BCItemUpdater": {
            "type": "ChildrenHandler",
            "className": "BCItem",
            "location": "../Patch"
          }
        }
      }
    }

# ------------------------------------------------------------------------------

class Patch(PFDBObj):
  '''
  '''

# ------------------------------------------------------------------------------

class BCItem(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.BCPressure = BCPressure_1(self)
    self.BCSaturation = BCSaturation_1(self)

# ------------------------------------------------------------------------------

class BCPressure_1(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Type = None
    self.Cycle = None
    self.RefGeom = None
    self.RefPatch = None
    self._details = {
      "Type": {
        "help": "[Type: string] This key specifies the type of boundary condition data given for patch patch_name. Possible values for this key are DirEquilRefPatch, DirEquilPLinear, FluxConst, FluxVolumetric, PressureFile, FluxFile, OverlandFlow, OverlandFlowPFB, SeepageFace, OverlandKinematic, OverlandDiffusive and ExactSolution. The choice DirEquilRefPatch specifies that the pressure on the specified patch will be in hydrostatic equilibrium with a constant reference pressure given on a reference patch. The choice DirEquilPLinear specifies that the pressure on the specified patch will be in hydrostatic equilibrium with pressure given along a piecewise line at elevation z = 0. The choice FluxConst defines a constant normal flux boundary condition through the domain patch. This flux must be specified in units of [L]=[T]. For Richards\u2019 equation, fluxes must be specified as a mass flux and given as the above flux multiplied by the density. Thus, this choice of input type for a Richards\u2019 equation problem has units of ([L]=[T])([M]=[L]3). The choice FluxVolumetric defines a volumetric flux boundary condition through the domain patch. The units should be consistent with all other user input for the problem. For Richards\u2019 equation fluxes must be specified as a mass flux and given as the above flux multiplied by the density. The choice PressureFile defines a hydraulic head boundary condition that is read from a properly distributed .pfb file. Only the values needed for the patch are used. The choice FluxFile defines a flux boundary condition that is read form a properly distributed .pfb file defined on a grid consistent with the pressure field grid. Only the values needed for the patch are used. The choices OverlandFlow and OverlandFlowPFB both turn on fully-coupled overland flow routing as described in [40] and in \u00a7 5.5. The key OverlandFlow corresponds to a Value key with a positive or negative value, to indicate uniform fluxes (such as rainfall or evapotranspiration) over the entire domain while the key OverlandFlowPFB allows a .pfb file to contain grid-based, spatially-variable fluxes. The OverlandKinematic and OverlandDiffusive both turn on an kinematic and diffusive wave overland flow routing boundary that solve equation 5.18 and do the upwinding internally (i.e. assuming that the user provides cell face slopes, as opposed to the traditional cell centered slopes). The key SeepageFace simulates a boundary that allows flow to exit but keeps the surface pressure at zero. The choice ExactSolution specifies that an exact known solution is to be applied as a Dirichlet boundary condition on the respective patch. Note that this does not change according to any cycle. Instead, time dependence is handled by evaluating at the time the boundary condition value is desired. The solution is specified by using a predefined function (choices are described below). NOTE: These last six types of boundary condition input is for Richards\u2019 equation cases only!\n",
        "domains": {
          "EnumDomain": {
            "enumList": [
              "DirEquilRefPatch",
              "DirEquilPLinear",
              "FluxConst",
              "FluxVolumetric",
              "PressureFile",
              "FluxFile",
              "OverlandFlow",
              "OverlandFlowPFB",
              "SeepageFace",
              "OverlandKinematic",
              "OverlandDiffusive",
              "ExactSolution"
            ]
          }
        }
      },
      "Cycle": {
        "help": "[Type: string] This key specifies the time cycle to which boundary condition data for patch patch_name corresponds.\n",
        "domains": {
          "AnyString": None
        }
      },
      "RefGeom": {
        "help": "[Type: string] This key specifies the name of the solid on which the reference patch for the DirEquilRefPatch boundary condition data is given. Care should be taken to make sure the correct solid is specified in cases of layered domains.\n",
        "domains": {
          "AnyString": None
        }
      },
      "RefPatch": {
        "help": "[Type: string] This key specifies the reference patch on which the DirEquilRefPatch boundary condition data is given. This patch must be on the reference solid specified by the Patch.patch_name.BCPressure.RefGeom key.\n",
        "domains": {
          "AnyString": None
        }
      }
    }
    self._dynamic = {
      "BCPressureIntervalItem": "/Cycle/{CycleItem}/Names"
    }
    self.processDynamic()

# ------------------------------------------------------------------------------

class BCPressureIntervalItem(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Value = None
    self.XLower = None
    self.YLower = None
    self.XUpper = None
    self.YUpper = None
    self.NumPoints = None
    self.FileName = None
    self.PredefinedFunction = None
    self._details = {
      "Value": {
        "help": "[Type: double] This key specifies the reference pressure value for the DirEquilRefPatch boundary condition or the constant flux value for the FluxConst boundary condition, or the constant volumetric flux for the FluxVolumetric boundary condition.\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "XLower": {
        "help": "[Type: double] This key specifies the lower x coordinate of a line in the xy-plane.\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "YLower": {
        "help": "[Type: double] This key specifies the lower y coordinate of a line in the xy-plane.\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "XUpper": {
        "help": "[Type: double] This key specifies the upper x coordinate of a line in the xy-plane.\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "YUpper": {
        "help": "[Type: double] This key specifies the upper y coordinate of a line in the xy-plane.\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "NumPoints": {
        "help": "[Type: int] This key specifies the number of points on which pressure data is given along the line used in the type DirEquilPLinear boundary conditions.\n",
        "domains": {
          "IntValue": {
            "minValue": 1
          }
        }
      },
      "FileName": {
        "help": "[Type: string] This key specifies the name of a properly distributed .pfb file that contains boundary data to be read for types PressureFile and FluxFile. For flux data, the data must be defined over a grid consistent with the pressure field. In both cases, only the values needed for the patch will be used. The rest of the data is ignored.\n",
        "domains": {
          "AnyString": None
        }
      },
      "PredefinedFunction": {
        "help": "[Type: string] This key specifies the predefined function that will be used to specify Dirichlet boundary conditions on patch patch_name. Note that this does not change according to any cycle. Instead, time dependence is handled by evaluating at the time the boundary condition value is desired. Choices for this key include X, XPlusYPlusZ, X3Y2PlusSinXYPlus1, X3Y4PlusX2PlusSinXYCosYPlus1, XYZTPlus1 and XYZTPlus1PermTensor.\n",
        "domains": {
          "EnumDomain": {
            "enumList": [
              "X",
              "XPlusYPlusZ",
              "X3Y2PlusSinXYPlus1",
              "X3Y4PlusX2PlusSinXYCosYPlus1",
              "XYZTPlus1",
              "XYZTPlus1PermTensor"
            ]
          }
        }
      }
    }

# ------------------------------------------------------------------------------

class BCPressIntPhaseItem(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.IntValue = None
    self._details = {
      "IntValue": {
        "help": "[Type: double] Note that the reference conditions for types DirEquilPLinear and DirEquilRefPatch boundary conditions are for phase 0 only. This key specifies the constant pressure value along the interface with phase phase_name for cases with two phases present.\n",
        "domains": {
          "DoubleValue": None
        }
      }
    }

# ------------------------------------------------------------------------------

class BCPressIntPntItem(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Location = None
    self.Value = None
    self._details = {
      "Location": {
        "help": "[Type: double] This key specifies a number between 0 and 1 which represents the location of a point on the line on which data is given for type DirEquilPLinear boundary conditions. Here 0 corresponds to the lower end of the line, and 1 corresponds to the upper end.\n",
        "domains": {
          "DoubleValue": {
            "minValue": 0.0,
            "maxValue": 1.0
          }
        }
      },
      "Value": {
        "help": "[Type: double] This key specifies the pressure value for phase 0 at point number point_number and z = 0 for type DirEquilPLinear boundary conditions. All pressure values on the patch are determined by first projecting the boundary condition coordinate onto the line, then linearly interpolating between the neighboring point pressure values on the line.\n",
        "domains": {
          "DoubleValue": None
        }
      }
    }

# ------------------------------------------------------------------------------

class BCSaturation_1(PFDBObj):
  '''
  '''

# ------------------------------------------------------------------------------

class BCSatPhaseItem(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Type = None
    self.Value = None
    self.XLower = None
    self.YLower = None
    self.XUpper = None
    self.YUpper = None
    self.NumPoints = None
    self._details = {
      "Type": {
        "help": "[Type: string] This key specifies the type of boundary condition data given for the given phase, phase_name, on the given patch patch_name. Possible values for this key are DirConstant, ConstantWTHeight and PLinearWTHeight. The choice DirConstant specifies that the saturation is constant on the whole patch. The choice ConstantWTHeight specifies a constant height of the water-table on the whole patch. The choice PLinearWTHeight specifies that the height of the water-table on the patch will be given by a piecewise linear function. Note: the types ConstantWTHeight and PLinearWTHeight assume we are running a 2-phase problem where phase 0 is the water phase.\n",
        "domains": {
          "EnumDomain": {
            "enumList": [
              "DirConstant",
              "ConstantWTHeight",
              "PLinearWTHeight"
            ]
          }
        }
      },
      "Value": {
        "help": "[Type: double] This key specifies either the constant saturation value if DirConstant is selected or the constant water-table height if ConstantWTHeight is selected.\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "XLower": {
        "help": "[Type: double] This key specifies the lower x coordinate of a line in the xy-plane if type PLinearWTHeight boundary conditions are specified.\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "YLower": {
        "help": "[Type: double] This key specifies the lower y coordinate of a line in the xy-plane if type PLinearWTHeight boundary conditions are specified.\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "XUpper": {
        "help": "[Type: double] This key specifies the upper x coordinate of a line in the xy-plane if type PLinearWTHeight boundary conditions are specified.\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "YUpper": {
        "help": "[Type: double] This key specifies the upper y coordinate of a line in the xy-plane if type PLinearWTHeight boundary conditions are specified.\n",
        "domains": {
          "DoubleValue": None
        }
      },
      "NumPoints": {
        "help": "[Type: int] This key specifies the number of points on which saturation data is given along the line used in the type DirEquilPLinear boundary conditions.\n",
        "domains": {
          "IntValue": {
            "minValue": 1
          }
        },
        "handlers": {
          "BCSatPhasePointItemUpdater": {
            "type": "ChildrenHandler",
            "className": "BCSatPhasePointItem"
          }
        }
      }
    }

# ------------------------------------------------------------------------------

class BCSatPhasePointItem(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Location = None
    self.Value = None
    self._details = {
      "Location": {
        "help": "[Type: double] This key specifies a number between 0 and 1 which represents the location of a point on the line for which data is given in type DirEquilPLinear boundary conditions. The line is parameterized so that 0 corresponds to the lower end of the line, and 1 corresponds to the upper end.\n",
        "domains": {
          "DoubleValue": {
            "minValue": 0.0,
            "maxValue": 1.0
          }
        }
      },
      "Value": {
        "help": "[Type: double] This key specifies the water-table height for the given point if type DirEquilPLinear boundary conditions are selected. All saturation values on the patch are determined by first projecting the water-table height value onto the line, then linearly interpolating between the neighboring water-table height values onto the line.\n",
        "domains": {
          "DoubleValue": None
        }
      }
    }

# ------------------------------------------------------------------------------

class NetCDF(PFDBObj):
  '''
  NetCDF4 parallel I/O is being implemented in ParFlow. As of now only output capability is implemented. Input functionality will be added in later version. Currently user has option of printing 3-D time varying pressure or saturation or both in a single NetCDF file containing multiple time steps. User should configure ParFlow (pfsimulator part) "- -with-netcdf" option and link the appropriate NetCDF4 library. Naming convention of output files is analogues to binary file names. Following options are available for NetCDF4 output along with various performance tuning options. User is advised to explore NetCDF4 chunking and ROMIO hints option for better I/O performance. HDF5 Library version 1.8.16 or higher is required for NetCDF4 parallel I/O
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.EvapTrans = EvapTrans_1(self)
    self.NumStepsPerFile = None
    self.WritePressure = False
    self.WriteSaturation = False
    self.WriteMannings = False
    self.WriteSubsurface = False
    self.WriteSlopes = False
    self.WriteMask = False
    self.WriteDZMultiplier = False
    self.WriteEvapTrans = False
    self.WriteEvapTransSum = False
    self.WriteOverlandSum = False
    self.WriteOverlandBCFlux = False
    self.Chunking = False
    self.ChunkX = None
    self.ChunkY = None
    self.ChunkZ = None
    self.ROMIOhints = None
    self.NodeLevelIO = None
    self.EvapTransFileTransient = None
    self.CLMNumStepsPerFile = None
    self.WriteCLM = False
    self._details = {
      "NumStepsPerFile": {
        "help": "[Type: int] This key sets number of time steps user wishes to output in a NetCDF4 file. Once the time step count increases beyond this number, a new file is automatically created.\n",
        "domains": {
          "IntValue": None,
          "RequiresModule": "NETCDF"
        }
      },
      "WritePressure": {
        "help": "[Type: boolean/string] This key sets pressure variable to be written in NetCDF4 file.\n",
        "default": False,
        "domains": {
          "BoolDomain": None,
          "RequiresModule": "NETCDF"
        }
      },
      "WriteSaturation": {
        "help": "[Type: boolean/string] This key sets saturation variable to be written in NetCDF4 file.\n",
        "default": False,
        "domains": {
          "BoolDomain": None,
          "RequiresModule": "NETCDF"
        }
      },
      "WriteMannings": {
        "help": "[Type: boolean/string] This key sets Mannings coefficients to be written in NetCDF4 file.\n",
        "default": False,
        "domains": {
          "BoolDomain": None,
          "RequiresModule": "NETCDF"
        }
      },
      "WriteSubsurface": {
        "help": "[Type: boolean/string] This key sets subsurface data(permeabilities, porosity, specific storage) to be written in NetCDF4 file.\n",
        "default": False,
        "domains": {
          "BoolDomain": None,
          "RequiresModule": "NETCDF"
        }
      },
      "WriteSlopes": {
        "help": "[Type: boolean/string] This key sets x and y slopes to be written in NetCDF4 file.\n",
        "default": False,
        "domains": {
          "BoolDomain": None,
          "RequiresModule": "NETCDF"
        }
      },
      "WriteMask": {
        "help": "[Type: boolean/string] This key sets mask to be written in NetCDF4 file.\n",
        "default": False,
        "domains": {
          "BoolDomain": None,
          "RequiresModule": "NETCDF"
        }
      },
      "WriteDZMultiplier": {
        "help": "[Type: boolean/string] This key sets DZ multipliers to be written in NetCDF4 file.\n",
        "default": False,
        "domains": {
          "BoolDomain": None,
          "RequiresModule": "NETCDF"
        }
      },
      "WriteEvapTrans": {
        "help": "[Type: boolean/string] This key sets Evaptrans to be written in NetCDF4 file.\n",
        "default": False,
        "domains": {
          "BoolDomain": None,
          "RequiresModule": "NETCDF"
        }
      },
      "WriteEvapTransSum": {
        "help": "[Type: boolean/string] This key sets Evaptrans sum to be written in NetCDF4 file.\n",
        "default": False,
        "domains": {
          "BoolDomain": None,
          "RequiresModule": "NETCDF"
        }
      },
      "WriteOverlandSum": {
        "help": "[Type: boolean/string] This key sets overland sum to be written in NetCDF4 file.\n",
        "default": False,
        "domains": {
          "BoolDomain": None,
          "RequiresModule": "NETCDF"
        }
      },
      "WriteOverlandBCFlux": {
        "help": "[Type: boolean/string] This key sets overland bc flux to be written in NetCDF4 file.\n",
        "default": False,
        "domains": {
          "BoolDomain": None,
          "RequiresModule": "NETCDF"
        }
      },
      "Chunking": {
        "help": "[Type: boolean/string] This key sets chunking for each time varying 3-D variable in NetCDF4 file.\n",
        "default": False,
        "domains": {
          "BoolDomain": None,
          "RequiresModule": "NETCDF"
        }
      },
      "ChunkX": {
        "help": "[Type: int] This key sets chunking size in x-direction.\n",
        "domains": {
          "IntValue": {
            "minValue": 1
          },
          "RequiresModule": "NETCDF"
        }
      },
      "ChunkY": {
        "help": "[Type: int] This key sets chunking size in y-direction.\n",
        "domains": {
          "IntValue": {
            "minValue": 1
          },
          "RequiresModule": "NETCDF"
        }
      },
      "ChunkZ": {
        "help": "[Type: int] This key sets chunking size in z-direction.\n",
        "domains": {
          "IntValue": {
            "minValue": 1
          },
          "RequiresModule": "NETCDF"
        }
      },
      "ROMIOhints": {
        "help": "[Type: string] This key sets ROMIO hints file to be passed on to NetCDF4 interface.If this key is set, the file must be present and readable in experiment directory.\n",
        "domains": {
          "AnyString": None,
          "RequiresModule": "NETCDF"
        }
      },
      "NodeLevelIO": {
        "help": "[Type: boolean/string] This key sets flag for node level collective I/O.\n",
        "domains": {
          "BoolDomain": None,
          "RequiresModule": "NETCDF"
        }
      },
      "EvapTransFileTransient": {
        "help": "[Type: boolean/string] This key sets flag for transient evaptrans forcing to be read from a NetCDF file.\n",
        "domains": {
          "BoolDomain": None,
          "RequiresModule": "NETCDF"
        }
      },
      "CLMNumStepsPerFile": {
        "help": "[Type: int] This key sets number of time steps to be written to a single NetCDF file.\n",
        "domains": {
          "IntValue": {
            "minValue": 1
          },
          "RequiresModule": [
            "NETCDF",
            "CLM"
          ]
        }
      },
      "WriteCLM": {
        "help": "[Type: boolean/string] This key sets CLM variables to be written in a NetCDF file.\n",
        "default": False,
        "domains": {
          "BoolDomain": None,
          "RequiresModule": [
            "NETCDF",
            "CLM"
          ]
        }
      }
    }

# ------------------------------------------------------------------------------

class EvapTrans_1(PFDBObj):
  '''
  '''
  def __init__(self, parent=None):
    super().__init__(parent)
    self.FileName = None
    self._details = {
      "FileName": {
        "help": "[Type: string] This key sets flag for transient evaptrans forcing to be read from a NetCDF file.\n",
        "domains": {
          "AnyString": None,
          "RequiresModule": "NETCDF"
        }
      }
    }

# ------------------------------------------------------------------------------

class BaseRun(PFDBObj):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.Process = Process(self)
    self.ComputationalGrid = ComputationalGrid(self)
    self.GeomInput = GeomInput(self)
    self.Geom = Geom(self)
    self.dzScale = dzScale(self)
    self.Cell = Cell(self)
    self.Solver = Solver(self)
    self.TimingInfo = TimingInfo(self)
    self.TimeStep = TimeStep(self)
    self.Cycle = Cycle(self)
    self.Perm = Perm(self)
    self.SpecificStorage = SpecificStorage(self)
    self.Phase = Phase(self)
    self.PhaseSources = PhaseSources(self)
    self.PhaseConcen = PhaseConcen(self)
    self.Contaminants = Contaminants(self)
    self.Domain = Domain(self)
    self.Wells = Wells(self)
    self.TopoSlopesX = TopoSlopesX(self)
    self.TopoSlopesY = TopoSlopesY(self)
    self.Mannings = Mannings(self)
    self.ICPressure = ICPressure(self)
    self.InternalBC = InternalBC(self)
    self.BCSaturation = BCSaturation(self)
    self.BCPressure = BCPressure(self)
    self.Patch = Patch(self)
    self.NetCDF = NetCDF(self)
    self.FBx = FBx(self)
    self.FBy = FBy(self)
    self.FBz = FBz(self)
    self.KnownSolution = KnownSolution(self)
    self.FileVersion = 4
    self.Gravity = None
    self.UseClustering = False
    self.OverlandFlowSpinUp = 0
    self.OverlandFlowSpinUpDampP1 = 0.0
    self.OverlandFlowSpinUpDampP2 = 0.0
    self._details = {
      "FileVersion": {
        "help": "[Type: int] This gives the value of the input file version number that this file fits. As development of the ParFlow code continues, the input file format may vary. We have thus included an input file format number as a way of verifying that the correct format type is being used. The user can check in the parflow/config/file_versions.h file to verify that the format number specified in the input file matches the defined value of PFIN_VERSION.\n",
        "default": 4,
        "domains": {
          "MandatoryValue": None,
          "IntValue": None
        }
      },
      "Gravity": {
        "help": "[Type: double] Specifies the gravity constant to be used.\n",
        "domains": {
          "MandatoryValue": None,
          "DoubleValue": {
            "minValue": 0.0
          }
        }
      },
      "UseClustering": {
        "help": "[Type: string/boolean] Run a clustering algorithm to create boxes in index space for iteration. By default an octree representation is used for iteration, this may result in iterating over many nodes in the octree. Th UseClustering key will run a clustering algorithm to build a set of boxes for iteration. This does not always have a significant impact on performance and the clustering algorithm can be expensive to compute. For small problems and short running problems clustering is not recommended. Long running problems may or may not see a benefit. The result varies significantly based on the geometries in the problem. The Berger-Rigoutsos algorithm is currently used for clustering.\n",
        "default": False,
        "domains": {
          "BoolDomain": None
        }
      },
      "OverlandFlowSpinUp": {
        "help": "[Type: int] This key specifies that a simplified form of the overland flow boundary condition (Equation 5.17) be used in place of the full equation. This formulation removes lateral flow and drives and ponded water pressures to zero using a SeepageFace boundary condition. While this can be helpful in spinning up the subsurface, this is no longer coupled subsurface-surface flow. If set to zero (the default) this key behaves normally.\n",
        "default": 0,
        "domains": {
          "IntValue": {
            "minValue": 0,
            "maxValue": 1
          }
        }
      },
      "OverlandFlowSpinUpDampP1": {
        "help": "This key sets P1 and provides exponential dampening to the pressure relationship in the overland flow equation by adding the following term: P2*exp[(pressure)*P2]\n",
        "default": 0.0,
        "domains": {
          "DoubleValue": {
            "minValue": 0.0
          }
        }
      },
      "OverlandFlowSpinUpDampP2": {
        "help": "This key sets P2 and provides exponential dampening to the pressure relationship in the overland flow equation by adding the following term: P2*exp[(pressure)*P2]\n",
        "default": 0.0,
        "domains": {
          "DoubleValue": {
            "minValue": 0.0
          }
        }
      }
    }
