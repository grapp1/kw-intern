********************************************************************************
ParFlow Key Documentation
********************************************************************************

Process
================================================================================

run.Process input options are: Topology



Process.Topology
--------------------------------------------------------------------------------

This section describes how processors are assigned in order to solve the domain in parallel.
  - P allocates the number of processes to the grid-cells in x.
  - Q allocates the number of processes to the grid-cells in y.
  - R allocates the number of processes to the grid-cells in z.
Please note R should always be 1 if you are running with Solver Richards unless you are running a totally saturated domain (solver IMPES).



Process.Topology.P
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: int] P allocates the number of processes to the grid-cells in x.


:default: 1
.. note::
    The value is required
    The value must be an Integer
      - with a value greater than or equal to 1



Process.Topology.Q
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: int] Q allocates the number of processes to the grid-cells in y.


:default: 1
.. note::
    The value is required
    The value must be an Integer
      - with a value greater than or equal to 1



Process.Topology.R
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: int] R allocates the number of processes to the grid-cells in z. Please note R should always be 1 if you are running with Solver Richards unless you are running a totally saturated domain (solver IMPES).


:default: 1
.. note::
    The value is required
    The value must be an Integer
      - with a value greater than or equal to 1



ComputationalGrid
================================================================================

The computational grid keys set the bottom left corner of the domain to a specific point in space. If using a .pfsol file, the bottom left corner location of the .pfsol file must be the points designated in the computational grid. The user can also assign the x, y and z location to correspond to a specific coordinate system (i.e. UTM). run.ComputationalGrid input options are: Lower.[X, Y, Z], [NX, NY, NZ], [DX, DY, DZ]



ComputationalGrid.Lower
--------------------------------------------------------------------------------

This section sets the lower coordinate locations for the computational grid (X, Y, Z).



ComputationalGrid.Lower.X
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: double] This assigns the lower x coordinate location for the computational grid.


.. note::
    The value is required
    The value must be an Integer


ComputationalGrid.Lower.Y
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: double] This assigns the lower y coordinate location for the computational grid.


.. note::
    The value is required
    The value must be an Integer


ComputationalGrid.Lower.Z
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: double] This assigns the lower z coordinate location for the computational grid.


.. note::
    The value is required
    The value must be an Integer


ComputationalGrid.NX
--------------------------------------------------------------------------------

[Type: int] This assigns the number of grid cells in the x direction for the computational grid.


.. note::
    The value is required
    The value must be an Integer
      - with a value greater than or equal to 1



ComputationalGrid.NY
--------------------------------------------------------------------------------

[Type: int] This assigns the number of grid cells in the y direction for the computational grid.


.. note::
    The value is required
    The value must be an Integer
      - with a value greater than or equal to 1



ComputationalGrid.NZ
--------------------------------------------------------------------------------

[Type: int] This assigns the number of grid cells in the z direction for the computational grid.


.. note::
    The value is required
    The value must be an Integer
      - with a value greater than or equal to 1



ComputationalGrid.DX
--------------------------------------------------------------------------------

[Type: double] This defines the size of grid cells in the x direction. Units are L and are defined by the units of the hydraulic conductivity used in the problem.


.. note::
    The value is required
    The value must be an Integer
      - with a value greater than or equal to 0.0



ComputationalGrid.DY
--------------------------------------------------------------------------------

[Type: double] This defines the size of grid cells in the y direction. Units are L and are defined by the units of the hydraulic conductivity used in the problem.


.. note::
    The value is required
    The value must be an Integer
      - with a value greater than or equal to 0.0



ComputationalGrid.DZ
--------------------------------------------------------------------------------

[Type: double] This defines the size of grid cells in the z direction. Units are L and are defined by the units of the hydraulic conductivity used in the problem.


.. note::
    The value is required
    The value must be an Integer
      - with a value greater than or equal to 0.0



Domain
================================================================================

The domain may be represented by any of the solid types in GeomInput.{geom_input_name}.InputType that allow the definition of surface patches. These surface patches are used to define boundary conditions. Subsequently, it is required that the union (or combination) of the defined surface patches equal the entire domain surface. NOTE: This requirement is NOT checked in the code.



Domain.GeomName
--------------------------------------------------------------------------------

[Type: string] This key specifies which of the named geometries is the problem domain.


.. note::
    The value is required
    The value must be a string


ICSaturation.{phase_name}
================================================================================

This section needs to be defined only for multi-phase flow and should not be defined for single-phase and Richards' equation cases.



ICSaturation.{phase_name}.Type
--------------------------------------------------------------------------------

[Type: string] This key specifies the type of initial condition that will be applied to different geometries for given phase, phase_name. The only key currently available is Constant. The choice Constant will apply constants values within geometries for the phase.


.. note::
    The value must be one of the following options: Constant


ICSaturation.{phase_name}.GeomNames
--------------------------------------------------------------------------------

[Type: string] This key specifies the geometries on which an initial condition will be given if the type is set to Constant. Note that geometries listed later “overlay” geometries listed earlier.


.. note::
    The value must be a string


ICPressure
================================================================================

The keys in this section are used to specify pressure initial conditions for Richards’ equation cases only. These keys will be ignored if any other case is run.



ICPressure.GeomNames
--------------------------------------------------------------------------------

[Type: string] This key specifies the geometry names on which the initial pressure data will be given. These geometries must comprise the entire domain. Note that conditions for regions that overlap other regions will have unpredictable results. The regions given must be disjoint.


.. note::
    The value must be a string


ICPressure.Type
--------------------------------------------------------------------------------

[Type: string] This key specifies the type of initial condition given. The choices for this key are Constant, HydroStaticDepth, HydroStaticPatch and PFBFile. The choice Constant specifies that the initial pressure will be constant over the regions given. The choice HydroStaticDepth specifies that the initial pressure within a region will be in hydrostatic equilibrium with a given pressure specified at a given depth. The choice HydroStaticPatch specifies that the initial pressure within a region will be in hydrostatic equilibrium with a given pressure on a specified patch. Note that all regions must have the same type of initial data - different regions cannot have different types of initial data. However, the parameters for the type may be different. The PFBFile specification means that the initial pressure will be taken as a spatially varying function given by data in a ParFlow binary (.pfb) file.


.. note::
    The value must be one of the following options: Constant, PFBFile, HydroStaticPatch, NCFile


GeomInput
================================================================================

Here we define all “geometrical” information needed by ParFlow. For example, the domain (and patches on the domain where boundary conditions are to be imposed), lithology or hydrostratigraphic units, faults, initial plume shapes, and so on, are considered geometries.



GeomInput.Names
--------------------------------------------------------------------------------

[Type: string] List of names to use for defining geometry regions


.. note::
    The value must be a string


GeomInput.{geom_name}
--------------------------------------------------------------------------------

One of the user-defined names for defining a geometry region



GeomInput.{geom_name}.InputType
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: string] This defines the type for the geometry input with the given input name. This key must be one of: SolidFile, IndicatorField, or Box.


.. note::
    The value must be one of the following options: SolidFile, IndicatorField, Box


GeomInput.{geom_name}.GeomName
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: string] This is a name of a single geometry defined by the geometry input. This should be used for a geometry input type of Box, which only requires a single name.


.. note::
    The value must be a string


GeomInput.{geom_name}.GeomNames
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: string] This is a list of the names of the geometries defined by the geometry input. For a geometry input type of Box, the singular GeomName should be used. For the SolidFile geometry type this should contain a list with the same number of geometries as were defined using GMS. The order of geometries in the SolidFile should match the names. For IndicatorField types you need to specify the value in the input field which matches the name using GeomInput.geom_input_name.Value.


.. note::
    The value must be a string


GeomInput.{geom_name}.FileName
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: string] For IndicatorField and SolidFile geometry inputs, this key specifies the input filename which contains the field or solid information.


.. note::
    The value must be a string



GeomInput.{geom_name}.Value
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: int] For IndicatorField geometry inputs, you need to specify the mapping between values in the input file and the geometry names. The named geometry will be defined wherever the input file is equal to the specified value.


.. note::
    The value must be an Integer


Perm
================================================================================

run.Perm input options are: TensorType, Conditioning



Perm.TensorType
--------------------------------------------------------------------------------

[Type: string] This key specifies whether the permeability tensor entries kx; ky and kz will be specified as three constants within a set of regions covering the domain or whether the entries will be specified cell-wise by files. The choices for this key are TensorByGeom and TensorByFile.


.. note::
    The value must be one of the following options: TensorByGeom, TensorByFile


FileName
--------------------------------------------------------------------------------

[Type: string] This key specifies the name of the file that contains the conditioning data. The default string NA indicates that conditioning data is not applicable.


:default: NA
.. note::
    The value must be a string


SpecificStorage
================================================================================

run.Perm input options are: GeomNames, Type



SpecificStorage.GeomNames
--------------------------------------------------------------------------------

[Type: string] This key specifies all of the geometries on which a different specific storage value will be assigned. These geometries must cover the entire computational domain.


.. note::
    The value must be a string


SpecificStorage.Type
--------------------------------------------------------------------------------

[Type: string] This key specifies which method is to be used to assign specific storage data. The only choice currently available is Constant which indicates that a constant is to be assigned to all grid cells within a geometry.


.. note::
    The value must be one of the following options: Constant


dzScale
================================================================================

This is where dZ multipliers are assigned within geounits using one of several methods.



dzScale.GeomNames
--------------------------------------------------------------------------------

[Type: string] This key specifies which problem domain is being applied a variable dz subsurface. These geometries must cover the entire computational domain.


.. note::
    The value must be a string


dzScale.Type
--------------------------------------------------------------------------------

[Type: string] This key specifies which method is to be used to assign variable vertical grid spacing. The choices currently available are Constant which indicates that a constant is to be assigned to all grid cells within a geometry, nzList which assigns all layers of a given model to a list value, and PFBFile which reads in values from a distributed pfb file.


.. note::
    The value must be a string


dzScale.nzListNumber
--------------------------------------------------------------------------------

[Type: int] This key indicates the number of layers with variable dz in the subsurface. This value is the same as the ComputationalGrid.NZ key.


.. note::
    The value must be an Integer
      - with a value greater than or equal to 1



Cell.{nzListNumber}
================================================================================




Cell.{nzListNumber}.dzScale
--------------------------------------------------------------------------------

Setting the Cell.nzListNumber.dzScale.Value



Cell.{nzListNumber}.dzScale.Value
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: double] This key assigns the thickness of each layer defined by nzListNumber. ParFlow assigns the layers from the bottom-up (i.e. the bottom of the domain is layer 0, the top is layer NZ-1). The total domain depth (Geom.domain.Upper.Z) does not change with variable dz. The layer thickness is calculated by ComputationalGrid.DZ *dZScale.


.. note::
    The value must be an Integer
      - with a value greater than or equal to 0.0



Geom
================================================================================

This maps the various properties to the user-defined geometric inputs.



Geom.Perm
--------------------------------------------------------------------------------

run.Geom.Perm input options are: Names, TensorByGeom.Names



Geom.Perm.Names
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: string] This key specifies all of the geometries to which a permeability field will be assigned. These geometries must cover the entire computational domain.


.. note::
    The value must be a string


Geom.Perm.TensorByGeom
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

run.Geom.Perm.TensorByGeom input options are: Names



Geom.Perm.TensorByGeom.Names
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

This key specifies all of the geometries to which permeability tensor entries will be assigned. These geometries must cover the entire computational domain.


.. note::
    The value must be a string


Geom.Porosity
--------------------------------------------------------------------------------

run.Geom.Porosity input options are: GeomNames



Geom.Porosity.GeomNames
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: string] This key specifies all of the geometries to which a porosity will be assigned. These geometries must cover the entire computational domain.


.. note::
    The value must be a string


Geom.Retardation
--------------------------------------------------------------------------------

run.Geom.Retardation input options are: GeomNames



Geom.Retardation.GeomNames
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: string] This key specifies all of the geometries to which the contaminants will have a retardation function applied.


.. note::
    The value must be a string


Geom..{geom_name}
--------------------------------------------------------------------------------

User-defined geometric instance. GeomItem names are taken from either GeomInput.Names or GeomItem.GeomNames.



Geom..{geom_name}.FileName
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: string] This specifies some sort of filename for the specified geometry.


.. note::
    The value must be a string



Geom..{geom_name}.Lower
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section sets the lower coordinate locations for the box geometry.



Geom..{geom_name}.Lower.X
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: double] This gives the lower X real space coordinate value of the previously specified box geometry of name box_geom_name.


.. note::
    The value must be an Integer


Geom..{geom_name}.Lower.Y
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: double] This gives the lower Y real space coordinate value of the previously specified box geometry of name box_geom_name.


.. note::
    The value must be an Integer


Geom..{geom_name}.Lower.Z
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: double] This gives the lower Z real space coordinate value of the previously specified box geometry of name box_geom_name.


.. note::
    The value must be an Integer


Geom..{geom_name}.Upper
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section sets the lower coordinate locations for the box geometry.



Geom..{geom_name}.Upper.X
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: double] This gives the upper X real space coordinate value of the previously specified box geometry of name box_geom_name.


.. note::
    The value must be an Integer


Geom..{geom_name}.Upper.Y
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: double] This gives the upper Y real space coordinate value of the previously specified box geometry of name box_geom_name.


.. note::
    The value must be an Integer


Geom..{geom_name}.Upper.Z
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: double] This gives the upper Z real space coordinate value of the previously specified box geometry of name box_geom_name.


.. note::
    The value must be an Integer


Geom..{geom_name}.Patches
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: string] Patches are defined on the surfaces of geometries. Currently you can only define patches on Box geometries and on the the first geometry in a SolidFile. For a Box the order is fixed (left right front back bottom top) but you can name the sides anything you want.


.. note::
    The value must be a string


Geom..{geom_name}.Perm
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Permeability values



Geom..{geom_name}.Perm.Type
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: string] This key specifies which method is to be used to assign permeability data to the named geometry, geometry_name. It must be either Constant, TurnBands, ParGauss, or PFBFile.


.. note::
    The value must be one of the following options: Constant, TurnBands, ParGauss, PFBFile


Geom..{geom_name}.Perm.Value
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: double] This key specifies the value assigned to all points in the named geometry, geometry_name, if the type was set to constant.


.. note::
    The value must be an Integer


Geom..{geom_name}.Perm.LambdaX
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: double] This key specifies the x correlation length of the field generated for the named geometry, geometry_name, if either the Turning Bands or Parallel Gaussian Simulator are chosen.


.. note::
    The value must be an Integer


Geom..{geom_name}.Perm.LambdaY
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: double] This key specifies the y correlation length of the field generated for the named geometry, geometry_name, if either the Turning Bands or Parallel Gaussian Simulator are chosen.


.. note::
    The value must be an Integer


Geom..{geom_name}.Perm.LambdaZ
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: double] This key specifies the z correlation length of the field generated for the named geometry, geometry_name, if either the Turning Bands or Parallel Gaussian Simulator are chosen.


.. note::
    The value must be an Integer


Geom..{geom_name}.Perm.GeomMean
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: double] This key specifies the geometric mean of the log normal field generated for the named geometry, geometry_name, if either the Turning Bands or Parallel Gaussian Simulator are chosen.


.. note::
    The value must be an Integer
      - with a value greater than or equal to 0.0



Geom..{geom_name}.Perm.Sigma
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: double] This key specifies the standard deviation of the normal field generated for the named geometry, geometry_name, if either the Turning Bands or Parallel Gaussian Simulator are chosen.


.. note::
    The value must be an Integer
      - with a value greater than or equal to 0.0



Geom..{geom_name}.Perm.Seed
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: int] This key specifies the initial seed for the random number generator used to generate the field for the named geometry, geometry_name, if either the Turning Bands or Parallel Gaussian Simulator are chosen. This number must be positive.


:default: 1
.. note::
    The value must be an Integer
      - with a value greater than or equal to 1



Geom..{geom_name}.Perm.NumLines
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: int] This key specifies the number of lines to be used in the Turning Bands algorithm for the named geometry, geometry_name.


:default: 100
.. note::
    The value must be an Integer
      - with a value greater than or equal to 1



Geom..{geom_name}.Perm.RZeta
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: double] This key specifies the resolution of the line processes, in terms of the minimum grid spacing, to be used in the Turning Bands algorithm for the named geometry, geometry_name. Large values imply high resolution.


:default: 5.0
.. note::
    The value must be an Integer
      - with a value greater than or equal to 0.0



Geom..{geom_name}.Perm.KMax
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: double] This key specifies the the maximum normalized frequency, Kmax, to be used in the Turning Bands algorithm for the named geometry, geometry_name.


:default: 100.0
.. note::
    The value must be an Integer
      - with a value greater than or equal to 0.0



Geom..{geom_name}.Perm.DelK
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: double] This key specifies the normalized frequency increment to be used in the Turning Bands algorithm for the named geometry, geometry_name.


:default: 0.2
.. note::
    The value must be an Integer
      - with a value greater than or equal to 0.0



Geom..{geom_name}.Perm.MaxNPts
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: int] This key sets limits on the number of simulated points in the search neighborhood to be used in the Parallel Gaussian Simulator for the named geometry, geometry_name.


.. note::
    The value must be an Integer
      - with a value greater than or equal to 1



Geom..{geom_name}.Perm.MaxCpts
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: int] This key sets limits on the number of external conditioning points in the search neighborhood to be used in the Parallel Gaussian Simulator for the named geometry, geometry_name.


.. note::
    The value must be an Integer
      - with a value greater than or equal to 1



Geom..{geom_name}.Perm.LogNormal
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: string] The key specifies when a normal, log normal, truncated normal or truncated log normal field is to be generated by the method for the named geometry, geometry_name. This value must be one of Normal, Log, NormalTruncated or LogTruncated and can be used with either Turning Bands or the Parallel Gaussian Simulator.


:default: LogTruncated
.. note::
    The value must be one of the following options: Normal, Log, NormalTruncated, LogTruncated


Geom..{geom_name}.Perm.StratType
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: string] This key specifies the stratification of the permeability field generated by the method for the named geometry, geometry_name. The value must be one of Horizontal, Bottom or Top and can be used with either the Turning Bands or the Parallel Gaussian Simulator.


:default: Bottom
.. note::
    The value must be one of the following options: Horizontal, Bottom, Top


Geom..{geom_name}.Perm.LowCutoff
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: double] This key specifies the low cutoff value for truncating the generated field for the named geometry, geometry_name, when either the NormalTruncated or LogTruncated values are chosen.


.. note::
    The value must be an Integer
      - with a value greater than or equal to 0.0



Geom..{geom_name}.Perm.HighCutoff
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: double] This key specifies the high cutoff value for truncating the generated field for the named geometry, geometry_name, when either the NormalTruncated or LogTruncated values are chosen.


.. note::
    The value must be an Integer
      - with a value greater than or equal to 0.0



Geom..{geom_name}.Perm.MaxSearchRad
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: int] A key to improve correlation structure of RF in testing.


.. note::
    The value must be an Integer
      - with a value greater than or equal to 1



Geom..{geom_name}.Perm.FileName
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: string] This key specifies that permeability values for the specified geometry, geometry_name, are given according to a user-supplied description in the “ParFlow Binary” file whose filename is given as the value. For a description of the ParFlow Binary file format, see the manual. The ParFlow Binary file associated with the named geometry must contain a collection of permeability values corresponding in a one-to-one manner to the entire computational grid. That is to say, when the contents of the file are read into the simulator, a complete permeability description for the entire domain is supplied. Only those values associated with computational cells residing within the geometry (as it is represented on the computational grid) will be copied into data structures used during the course of a simulation. Thus, the values associated with cells outside of the geounit are irrelevant. For clarity, consider a couple of different scenarios. For example, the user may create a file for each geometry such that appropriate permeability values are given for the geometry and “garbage" values (e.g., some flag value) are given for the rest of the computational domain. In this case, a separate binary file is specified for each geometry. Alternatively, one may place all values representing the permeability field on the union of the geometries into a single binary file. Note that the permeability values must be represented in precisely the same configuration as the computational grid. Then, the same file could be specified for each geounit in the input file. Or, the computational domain could be described as a single geouint (in the ParFlow input file) in which case the permeability values would be read in only once.


.. note::
    The value must be a string


Geom..{geom_name}.Perm.TensorValX
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: double] This key specifies the value of kx for the geometry given by geometry_name.


.. note::
    The value must be an Integer
      - with a value greater than or equal to 0.0



Geom..{geom_name}.Perm.TensorValY
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: double] This key specifies the value of ky for the geometry given by geometry_name.


.. note::
    The value must be an Integer
      - with a value greater than or equal to 0.0



Geom..{geom_name}.Perm.TensorValZ
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: double] This key specifies the value of kz for the geometry given by geometry_name.


.. note::
    The value must be an Integer
      - with a value greater than or equal to 0.0



Geom..{geom_name}.Perm.TensorFileX
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: string] This key specifies that kx values for the specified geometry, geometry_name, are given according to a user-supplied description in the “ParFlow Binary” file whose filename is given as the value. The only choice for the value of geometry_name is “domain”.


.. note::
    The value must be a string


Geom..{geom_name}.Perm.TensorFileY
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: string] This key specifies that ky values for the specified geometry, geometry_name, are given according to a user-supplied description in the “ParFlow Binary” file whose filename is given as the value. The only choice for the value of geometry_name is “domain”.


.. note::
    The value must be a string


Geom..{geom_name}.Perm.TensorFileZ
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: string] This key specifies that kz values for the specified geometry, geometry_name, are given according to a user-supplied description in the “ParFlow Binary” file whose filename is given as the value. The only choice for the value of geometry_name is “domain”.


.. note::
    The value must be a string


Geom..{geom_name}.Porosity
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Setting porosity values to elements of domain



Geom..{geom_name}.Porosity.Type
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: string] This key specifies which method is to be used to assign porosity data to the named geometry, geometry_name. The only choice currently available is Constant which indicates that a constant is to be assigned to all grid cells within a geometry.


.. note::
    The value must be one of the following options: Constant


Geom..{geom_name}.Porosity.Value
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: double] This key specifies the value assigned to all points in the named geometry, geometry_name, if the type was set to constant.


.. note::
    The value must be an Integer


Geom..{geom_name}.Porosity.FileName
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: string] This key specifies that porosity values for the specified geometry, geometry_name, are given according to a user-supplied description in the “ParFlow Binary” file whose filename is given as the value. The only choice for the value of geometry_name is “domain”.


.. note::
    The value must be a string


Geom..{geom_name}.SpecificStorage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Setting specific storage values to elements of domain



Geom..{geom_name}.SpecificStorage.Value
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: double] This key specifies the value assigned to all points in the named geometry, geometry_name, if the type was set to constant.


.. note::
    The value must be an Integer


Geom..{geom_name}.RelPerm
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Setting relative permeability value to geometries



Geom..{geom_name}.RelPerm.Value
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: double] This key specifies the constant relative permeability value on the specified geometry.


.. note::
    The value must be an Integer
      - with a value greater than or equal to 0.0



Geom..{geom_name}.RelPerm.Alpha
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: double] This key specifies the alpha parameter for the Van Genuchten function specified on geom_name.


.. note::
    The value must be an Integer
      - with a value greater than or equal to 0.0



Geom..{geom_name}.RelPerm.Alpha
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""




Geom..{geom_name}.RelPerm.Alpha.FileName
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: string] This key specifies a pfb filename containing the alpha parameters for the VanGenuchten function cell-by-cell. The ONLY option for geom_name is "domain."


.. note::
    The value must be a string


Geom..{geom_name}.RelPerm.N
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: double] This key specifies the alpha parameter for the Van Genuchten function specified on geom_name.


.. note::
    The value must be an Integer
      - with a value greater than or equal to 0.0



Geom..{geom_name}.RelPerm.N
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""




Geom..{geom_name}.RelPerm.N.FileName
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: string] This key specifies a pfb filename containing the N parameters for the VanGenuchten function cell-by-cell. The ONLY option for geom_name is "domain."


.. note::
    The value must be a string


Geom..{geom_name}.RelPerm.NumSamplePoints
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: int] This key specifies the number of sample points for a spline base interpolation table for the Van Genuchten function specified on geom_name. If this number is 0 (the default) then the function is evaluated directly. Using the interpolation table is faster but is less accurate.


:default: 0
.. note::
    The value must be an Integer
      - with a value greater than or equal to 0



Geom..{geom_name}.RelPerm.MinPressureHead
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: int] This key specifies the lower value for a spline base interpolation table for the Van Genuchten function specified on geom_name. The upper value of the range is 0. This value is used only when the table lookup method is used (NumSamplePoints is greater than 0).


.. note::
    The value must be an Integer


Geom..{geom_name}.RelPerm.A
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: double] This key specifies the A parameter for the Haverkamp relative permeability on geom_name.


.. note::
    The value must be an Integer


Geom..{geom_name}.RelPerm.Gamma
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: double] This key specifies the gamma parameter for the Haverkamp relative permeability on geom_name.


.. note::
    The value must be an Integer


Geom..{geom_name}.RelPerm.Degree
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: int] This key specifies the degree of the polynomial for the Polynomial relative permeability given on geom_name.


.. note::
    The value must be an Integer


Geom..{geom_name}.RelPerm.Coeff
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Setting the coefficients for the polynomial relative permeability curve.



Geom.{geom_name}.RelPerm.Coeff.{coeff_number}
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: double] This key specifies the 'coeff_number'th coefficient of the Polynomial relative permeability given on geom_name.


.. note::
    The value must be an Integer


Geom..{geom_name}.CapPressure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Setting capillary pressures for specified geometries



Geom.{geom_name}.CapPressure.{phase_name}.Value
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: double] This key specifies the value of the capillary pressure in the named geometry, geometry_name, for the named phase, phase_name. IMPORTANT NOTE: the code currently works only for capillary pressure equal zero.


:default: 0.0
.. note::
    The value must be an Integer


Geom..{geom_name}.Saturation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Setting saturation values to geometries



Geom..{geom_name}.Saturation.Value
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: double] This key specifies the constant saturation value on the specified geometry.


.. note::
    The value must be an Integer
      - with a value greater than or equal to 0.0
      - with a value less than or equal to 1.0



Geom..{geom_name}.Saturation.Alpha
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: double] This key specifies the alpha parameter for the Van Genuchten function specified on geom_name.


.. note::
    The value must be an Integer
      - with a value greater than or equal to 0.0



Geom..{geom_name}.Saturation.Alpha
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""




Geom..{geom_name}.Saturation.Alpha.FileName
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: string] This key specifies a pfb filename containing the alpha parameters for the VanGenuchten function cell-by-cell. The ONLY option for geom_name is "domain."


.. note::
    The value must be a string


Geom..{geom_name}.Saturation.N
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: double] This key specifies the alpha parameter for the Van Genuchten function specified on geom_name.


.. note::
    The value must be an Integer
      - with a value greater than or equal to 0.0



Geom..{geom_name}.Saturation.N
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""




Geom..{geom_name}.Saturation.N.FileName
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: string] This key specifies a pfb filename containing the N parameters for the VanGenuchten function cell-by-cell. The ONLY option for geom_name is "domain."


.. note::
    The value must be a string


Geom..{geom_name}.Saturation.SRes
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: double] This key specifies the residual saturation on geom_name.


.. note::
    The value must be an Integer
      - with a value greater than or equal to 0.0
      - with a value less than or equal to 1.0



Geom..{geom_name}.Saturation.SRes
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""




Geom..{geom_name}.Saturation.SRes.Filename
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: string] This key specifies a pfb filename containing the residual saturation parameters for the VanGenuchten function cell-by-cell. The ONLY option for geom_name is "domain."


.. note::
    The value must be a string


Geom..{geom_name}.Saturation.SSat
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: double] This key specifies the saturation at saturated conditions on geom_name.


.. note::
    The value must be an Integer
      - with a value greater than or equal to 0.0
      - with a value less than or equal to 1.0



Geom..{geom_name}.Saturation.SSat
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""




Geom..{geom_name}.Saturation.SSat.FileName
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: string] This key specifies a pfb filename containing the SSat parameters for the VanGenuchten function cell-by-cell. The ONLY option for geom_name is "domain."


.. note::
    The value must be a string


Geom..{geom_name}.Saturation.A
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: double] This key specifies the A parameter for the Haverkamp saturation on geom_name.


.. note::
    The value must be an Integer


Geom..{geom_name}.Saturation.Gamma
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: double] This key specifies the gamma parameter for the Haverkamp saturation on geom_name.


.. note::
    The value must be an Integer


Geom..{geom_name}.Saturation.Degree
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: int] This key specifies the degree of the polynomial for the Polynomial saturation given on geom_name.


.. note::
    The value must be an Integer


Geom..{geom_name}.Saturation.Coeff
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Setting the coefficients for the polynomial saturation curve.



Geom..{geom_name}.Saturation.CoeffNumber
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: double] This key specifies the 'coeff_number'th coefficient of the Polynomial saturation given on geom_name.


.. note::
    The value must be an Integer


Geom..{geom_name}.Saturation.FileName
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: string] This key specifies the name of the file containing saturation values for the domain. It is assumed that geom_name is “domain” for this key.


.. note::
    The value must be a string


Geom..{geom_name}.dzScale
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Setting properties for the dz Scale.



Geom..{geom_name}.dzScale.Value
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: double] This key specifies the value assigned to all points in the named geometry, geometry_name, if the type was set to constant.


.. note::
    The value must be an Integer
      - with a value greater than or equal to 0.0



Geom..{geom_name}.dzScale.FileName
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: string] This key specifies file to be read in for variable dz values for the given geometry, geometry_name, if the type was set to PFBFile.


.. note::
    The value must be a string


Geom..{geom_name}.ThermalConductivity
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Setting thermal conductivity values for various geometries



Geom..{geom_name}.ThermalConductivity.Value
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: double] This key specifies the thermal conductivity value on the specified geometry.


.. note::
    The value must be an Integer
      - with a value greater than or equal to 0.0



Geom..{geom_name}.ThermalConductivity.KDry
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: double] This key specifies the thermal conductivity under dry conditions on geom_name.


.. note::
    The value must be an Integer
      - with a value greater than or equal to 0.0



Geom..{geom_name}.ThermalConductivity.KDry
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""




Geom..{geom_name}.ThermalConductivity.KDry.FileName
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: string] This key specifies a pfb filename containing the dry thermal conductivity function cell-by-cell. The ONLY option for geom_name is "domain."


.. note::
    The value must be a string


Geom..{geom_name}.ThermalConductivity.KWet
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: double] This key specifies the thermal conductivity under saturated conditions on geom_name.


.. note::
    The value must be an Integer
      - with a value greater than or equal to 0.0



Geom..{geom_name}.ThermalConductivity.KWet
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""




Geom..{geom_name}.ThermalConductivity.KWet.FileName
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: string] This key specifies a pfb filename containing the wet thermal conductivity function cell-by-cell. The ONLY option for geom_name is "domain."


.. note::
    The value must be a string


Geom..{geom_name}.FBx
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Setting file name for flow barriers in X. FBx.Type must equal PFBFile (see solvers.py).



Geom..{geom_name}.FBx.FileName
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: string] This key specifies file to be read in for the X flow barrier values for the domain, if the type was set to PFBFile.


.. note::
    The value must be a string


Geom..{geom_name}.FBy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Setting file name for flow barriers in Y. FBy.Type must equal PFBFile (see solvers.py).



Geom..{geom_name}.FBy.FileName
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: string] This key specifies file to be read in for the Y flow barrier values for the domain, if the type was set to PFBFile.


.. note::
    The value must be a string


Geom..{geom_name}.FBz
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Setting file name for flow barriers in Z. FBz.Type must equal PFBFile (see solvers.py).



Geom..{geom_name}.FBz.FileName
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: string] This key specifies file to be read in for the Z flow barrier values for the domain, if the type was set to PFBFile.


.. note::
    The value must be a string


Geom..{geom_name}.HeatCapacity
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Setting heat capacity properties for specified geometries.



Geom..{geom_name}.HeatCapacity.Value
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: double] This key specifies the heat capacity of the given geometry. Units are J*g^-1*C^-1.


.. note::
    The value must be an Integer
      - with a value greater than or equal to 0.0



Geom.{geom_name}.ICPressure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Setting the initial conditions for pressure for specific geometries.



Geom.{geom_name}.ICPressure.FileName
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

This key specifies the name of the file containing pressure values for the domain. It is assumed that geom_name is “domain” for this key.


.. note::
    The value must be a string


Geom.{geom_name}.ICPressure.RefElevation
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: double] This key specifies the reference elevation on which the reference pressure is given for type HydroStaticDepth initial pressures.


.. note::
    The value must be an Integer


Geom.{geom_name}.ICPressure.RefGeom
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: string] This key specifies the geometry on which the reference patch resides for type HydroStaticPatch initial pressures.


.. note::
    The value must be a string


Geom.{geom_name}.ICPressure.RefPatch
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: string] This key specifies the patch on which the reference pressure is given for type HydorStaticPatch initial pressures.


.. note::
    The value must be a string


Geom.{geom_name}.ICPressure.Value
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: double] This key specifies the initial pressure value for type Constant initial pressures and the reference pressure value for types HydroStaticDepth and HydroStaticPatch.


.. note::
    The value must be an Integer


Geom.{geom_name}.ICSaturation.{phase_name}
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Setting Geom.geom_input_name.ICSaturation.phase_name.Value



Geom.{geom_name}.ICSaturation.{phase_name}.Value
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: double] Setting


.. note::
    The value must be an Integer


Geom.{geom_name}.{contaminant}
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Setting retardation properties for specific contaminants and specific geometries.



Type
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: string] This key specifies which function is to be used to compute the retardation for the named contaminant, contaminant_ name, in the named geometry, geometry_name. The only choice currently available is Linear which indicates that a simple linear retardation function is to be used to compute the retardation.


.. note::
    The value must be one of the following options: Linear


Value
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: double] This key specifies the distribution coefficient for the linear function used to compute the retardation of the named contaminant, contaminant_name, in the named geometry, geometry_name. The value should be scaled by the density of the material in the geometry.


.. note::
    The value must be an Integer
      - with a value greater than or equal to 0.0



Rate
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: double] This key specifies the distribution coefficient for the linear function used to compute the retardation of the named contaminant, contaminant_name, in the named geometry, geometry_name. The value should be scaled by the density of the material in the geometry.


.. note::
    The value must be an Integer
      - with a value greater than or equal to 0.0



TopoSlopes
================================================================================

Setting filename for elevation data from which ParFlow will calculate slopes



TopoSlopes.Elevation
--------------------------------------------------------------------------------

Setting filename for elevation data from which ParFlow will calculate slopes



TopoSlopes.Elevation.FileName
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: string] This key is the name of the PFB file that contains elevations which ParFlow uses to derive slopes. This is optional but can be useful when post-processing terrain-following grids.


.. note::



TopoSlopesX
================================================================================

Setting data for domain slopes in the X direction



TopoSlopesX.GeomNames
--------------------------------------------------------------------------------

[Type: string] This key specifies all of the geometries on which a different x topographic slope values will be assigned. Topographic slopes may be assigned by PFBFile or as Constant by geometry. These geometries must cover the entire upper surface of the computational domain.


.. note::
    The value must be a string


TopoSlopesX.Type
--------------------------------------------------------------------------------

[Type: string] This key specifies which method is to be used to assign topographic slopes. The choices currently available are Constant which indicates that a constant is to be assigned to all grid cells within a geometry and PFBFile which indicates that all values are read in from a distributed, grid-based ParFlow binary file. If NetCDF is used, NCFile can be specified, which will read in slopes from a NetCDF file.


.. note::
    The value must be one of the following options: Constant, PFBFile, NCFile


TopoSlopesX.FileName
--------------------------------------------------------------------------------

[Type: string] This key specifies the value assigned to all points be read in from a ParFlow binary file.


.. note::
    The value must be a string


TopoSlopesX.Geom.{geom_name}
--------------------------------------------------------------------------------

Setting value for slopes in the X direction



TopoSlopesX.Geom.{geom_name}.Value
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: double] This key specifies the value assigned to all points in the named geometry, geometry_name, if the type was set to constant.


.. note::
    The value must be an Integer


TopoSlopesY
================================================================================

Setting data for domain slopes in the Y direction



TopoSlopesY.GeomNames
--------------------------------------------------------------------------------

[Type: string] This key specifies all of the geometries on which a different y topographic slope values will be assigned. Topographic slopes may be assigned by PFBFile or as Constant by geometry. These geometries must cover the entire upper surface of the computational domain.


.. note::
    The value must be a string


TopoSlopesY.Type
--------------------------------------------------------------------------------

[Type: string] This key specifies which method is to be used to assign topographic slopes. The choices currently available are Constant which indicates that a constant is to be assigned to all grid cells within a geometry and PFBFile which indicates that all values are read in from a distributed, grid-based ParFlow binary file. If NetCDF is used, NCFile can be specified, which will read in slopes from a NetCDF file.


.. note::
    The value must be one of the following options: Constant, PFBFile, NCFile


TopoSlopesY.FileName
--------------------------------------------------------------------------------

[Type: string] This key specifies the value assigned to all points be read in from a ParFlow binary file.


.. note::
    The value must be a string


TopoSlopesY.Geom.{geom_name}
--------------------------------------------------------------------------------

Setting value for slopes in the Y direction



TopoSlopesY.Geom.{geom_name}.Value
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: double] This key specifies the value assigned to all points in the named geometry, geometry_name, if the type was set to constant.


.. note::
    The value must be an Integer


CapPressure
================================================================================

Setting capillary pressures for different phases



CapPressure.{phase_name}
================================================================================

Phase name on which capillary pressure will be specified.



CapPressure.{phase_name}.Type
--------------------------------------------------------------------------------

[Type: string] This key specifies the capillary pressure between phase 0 and the named phase, phase_name. The only choice available is Constant which indicates that a constant capillary pressure exists between the phases.


:default: Constant
.. note::
    The value must be one of the following options: Constant


CapPressure.{phase_name}.GeomNames
--------------------------------------------------------------------------------

[Type: string] This key specifies the geometries that capillary pressures will be computed for in the named phase, phase_name. Regions listed later “overlay” regions listed earlier. Any geometries not listed will be assigned 0:0 capillary pressure by ParFlow.


.. note::
    The value must be a string


Mannings
================================================================================

Here, Manning's roughness values (n) are assigned to the upper boundary of the domain.



Mannings.GeomNames
--------------------------------------------------------------------------------

[Type: string] This key specifies all of the geometries on which a different Mannings roughness value will be assigned. Mannings values may be assigned by PFBFile or as Constant by geometry. These geometries must cover the entire upper surface of the computational domain.


.. note::
    The value must be a string


Mannings.Type
--------------------------------------------------------------------------------

[Type: string] This key specifies which method is to be used to assign Mannings roughness data. The choices currently available are Constant which indicates that a constant is to be assigned to all grid cells within a geometry and PFBFile which indicates that all values are read in from a distributed, grid-based ParFlow binary file.


.. note::
    The value must be one of the following options: Constant, PFBFile


Mannings.FileName
--------------------------------------------------------------------------------

[Type: string] This key specifies the name of the ParFlow binary file with Manning's values.


.. note::
    The value must be a string


Value
--------------------------------------------------------------------------------

[Type: double] This key specifies the value assigned to all points in the named geometry, geometry_name, if the type was set to constant.


.. note::
    The value must be an Integer


Solver
================================================================================

[Type: string] ParFlow can operate using a number of different solvers. Two of these solvers, IMPES (running in single-phase, fully-saturated mode, not multiphase) and RICHARDS (running in variably-saturated mode, not multiphase, with the options of land surface processes and coupled overland flow) are detailed below. This is a brief summary of solver settings used to simulate under three sets of conditions, fully-saturated, variably saturated and variably-saturated with overland flow. To simulate fully saturated, steady-state conditions set the solver to IMPES. This is also the default solver in ParFlow, so if no solver is specified, the code solves using IMPES. To simulate variably-saturated, transient conditions, using Richards’ equation, variably/fully saturated, transient with compressible storage set the solver to RICHARDS. This is also the solver used to simulate surface flow or coupled surface-subsurface flow.


:default: Impes
.. note::
    The value is required
    The value must be one of the following options: Impes, Richards


Solver
================================================================================

Assigning properties to solver



Solver.AbsTol
--------------------------------------------------------------------------------

[Type: double] This value gives the absolute tolerance for the linear solve algorithm.


:default: 1e-9
.. note::
    The value must be an Integer
      - with a value greater than or equal to 0.0



Solver.AdvectOrder
--------------------------------------------------------------------------------

[Type: int] This key controls the order of the explicit method used in advancing the concentrations. This value can be either 1 for a standard upwind first order or 2 for a second order Godunov method.


:default: 2
.. note::
    The value must be an Integer
      - with a value greater than or equal to 1
      - with a value less than or equal to 2



Solver.BetaFluid
--------------------------------------------------------------------------------

[Type: int]


.. note::
    The value must be an Integer


Solver.BetaFracture
--------------------------------------------------------------------------------

[Type: int]


.. note::
    The value must be an Integer


Solver.BetaPerm
--------------------------------------------------------------------------------

[Type: int]


.. note::
    The value must be an Integer


Solver.BetaPore
--------------------------------------------------------------------------------

[Type: int]


.. note::
    The value must be an Integer


Solver.BoxSizePowerOf2
--------------------------------------------------------------------------------

[Type: int]


.. note::
    The value must be an Integer


Solver.CFL
--------------------------------------------------------------------------------

[Type: double] This key gives the value of the weight put on the computed CFL limit before computing a global timestep value. Values greater than 1 are not suggested and in fact because this is an approximation, values slightly less than 1 can also produce instabilities.


:default: 0.7
.. note::
    The value must be an Integer


Solver.CLM
--------------------------------------------------------------------------------

Setting CLM parameters



Solver.CLM.BinaryOutDir
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: boolean/string] This key specifies whether the CLM writes each set of two dimensional binary output files to a corresponding directory. These directories my be created before ParFlow is run (using the tcl script, for example). Choices for this key include True and False. Note that CLM must be compiled and linked at runtime for this option to be active.


:default: True
.. note::
    The value must be True or False


Solver.CLM.CLMDumpInterval
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: int] This key specifies how often output from the CLM is written. This key is in integer multipliers of the CLM timestep. Note that CLM must be compiled and linked at runtime for this option to be active.


:default: 1
.. note::
    The value must be an Integer
      - with a value greater than or equal to 1



Solver.CLM.CLMFileDir
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: string] This key specifies what directory all output from the CLM is written to. This key may be set to "./" or "" to write output to the ParFlow run directory. This directory must be created before ParFlow is run. Note that CLM must be compiled and linked at runtime for this option to be active.


.. note::
    The value must be a string


Solver.CLM.DailyRST
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: boolean/string] Controls whether CLM writes daily restart files (default) or at every time step when set to False; outputs are numbered according to the istep from ParFlow. If ReuseCount=n, with n greater than 1, the output will be written every n steps (i.e. it still writes hourly restart files if your time step is 0.5 or 0.25, etc...). Fully compatible with WriteLastRST=False so that each daily output is overwritten to time 00000 in restart file name.00000.p where p is the processor number.


:default: True
.. note::
    The value must be True or False


Solver.CLM.EvapBeta
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: string] This key specifies the form of the bare soil evaporation parameter in CLM. The valid types for this key are None, Linear, Cosine.


:default: Linear
.. note::
    The value must be one of the following options: None, Linear, Cosine


Solver.CLM.FieldCapacity
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: double] This key specifies the field capacity for the beta-t function in CLM. Note that the units for this function are pressure [m] for a Pressure formulation and saturation [-] for a Saturation formulation. Note that CLM must be compiled and linked at runtime for this option to be active.


:default: 1.0
.. note::
    The value must be an Integer
      - with a value greater than or equal to 0.0
      - with a value less than or equal to 1.0



Solver.CLM.ForceVegetation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: boolean/string] This key specifies whether vegetation should be forced in CLM. Currently this option only works for 1D and 3D forcings, as specified by the key Solver.CLM.MetForcing. Choices for this key include True and False. Forced vegetation variables are : LAI: Leaf Area Index [-] SAI: Stem Area Index [-] Z0M: Aerodynamic roughness length [m] DISPLA: Displacement height [m] In the case of 1D meteorological forcings, CLM requires four files for vegetation time series and one vegetation map. The four files should be named respectively lai.dat, sai.dat, z0m.dat, displa.dat. They are ASCII files and contain 18 time-series columns (one per IGBP vegetation class, and each timestep per row). The vegetation map should be a properly distributed 2D ParFlow binary file (.pfb) which contains vegetation indices (from 1 to 18). The vegetation map filename is veg_map.pfb. ParFlow uses the vegetation map to pass to CLM a 2D map for each vegetation variable at each time step. In the case of 3D meteorological forcings, ParFlow expects four distincts properly distributed ParFlow binary file (.pfb), the third dimension being the timesteps. The files should be named LAI.pfb, SAI.pfb, Z0M.pfb, DISPLA.pfb. No vegetation map is needed in this case.


:default: False
.. note::
    The value must be True or False


Solver.CLM.FstepStart
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: int]


.. note::
    The value must be an Integer


Solver.CLM.IrrigationCycle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: string] This key specifies the cycle of the irrigation in CLM. The valid types for this key are Constant, Deficit. Note only Constant is currently implemented. Constant cycle applies irrigation each day from IrrigationStartTime to IrrigationStopTime in GMT.


:default: Constant
.. note::
    The value must be one of the following options: Constant, Deficit


Solver.CLM.IrrigationRate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: double] This key specifies the rate of the irrigation in CLM in [mm/s].


.. note::
    The value must be an Integer
      - with a value greater than or equal to 0.0



Solver.CLM.IrrigationStartTime
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: double] This key specifies the start time of the irrigation in CLM GMT.


.. note::
    The value must be an Integer
      - with a value greater than or equal to 0.0
      - with a value less than or equal to 2400.0



Solver.CLM.IrrigationStopTime
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: double] This key specifies the stop time of the irrigation in CLM GMT.


.. note::
    The value must be an Integer
      - with a value greater than or equal to 0.0
      - with a value less than or equal to 2400.0



Solver.CLM.IrrigationThreshold
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: double] This key specifies the threshold value for the irrigation in CLM [-].


:default: 0.5
.. note::
    The value must be an Integer
      - with a value greater than or equal to 0.0



Solver.CLM.IrrigationThresholdType
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: string]


.. note::
    The value must be an Integer


Solver.CLM.IrrigationType
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: string] This key specifies the form of the irrigation in CLM. The valid types for this key are none, Spray, Drip, Instant.


:default: none
.. note::
    The value must be one of the following options: none, Spray, Drip, Instant


Solver.CLM.IstepStart
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: int] This key specifies the value of the counter, istep in CLM. This key primarily determines the start of the output counter for CLM.It is used to restart a run by setting the key to the ending step of the previous run plus one. Note that CLM must be compiled and linked at runtime for this option to be active.


:default: 1
.. note::
    The value must be an Integer


Solver.CLM.MetFileNT
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: int] This key specifies the number of timesteps per file for 3D forcing data.


.. note::
    The value must be an Integer


Solver.CLM.MetFileName
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: string] This key specifies defines the file name for 1D, 2D or 3D forcing data. 1D meteorological forcing files are text files with single columns for each variable and each timestep per row, while 2D and 3D forcing files are distributed ParFlow binary files, one for each variable and timestep (2D) or one for each variable and multiple timesteps (3D). Behavior of this key is different for 1D and 2D and 3D cases, as sepcified by the Solver.CLM.MetForcing key above. For 1D cases, it is the FULL FILE NAME. Note that in this configuration, this forcing file is not distributed, the user does not provide copies such as narr.1hr.txt.0, narr.1hr.txt.1 for each processor. ParFlow only needs the single original file (e.g. narr.1hr.txt). For 2D cases, this key is the BASE FILE NAME for the 2D forcing files, currently set to NLDAS, with individual files determined as follows NLDAS.<variable>.<time step>.pfb. Where the <variable> is the forcing variable and <timestep> is the integer file counter corresponding to istep above. Forcing is needed for following variables: DSWR: Downward Visible or Short-Wave radiation [W/m2]. DLWR: Downward Infa-Red or Long-Wave radiation [W/m2] APCP: Precipitation rate [mm/s] Temp: Air temperature [K] UGRD: West-to-East or U-component of wind [m/s] VGRD: South-to-North or V-component of wind [m/s] Press: Atmospheric Pressure [pa] SPFH: Water-vapor specific humidity [kg/kg] Note that CLM must be compiled and linked at runtime for this option to be active.


.. note::
    The value must be a string


Solver.CLM.MetFilePath
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: string] This key specifies defines the location of 1D, 2D or 3D forcing data. For 1D cases, this is the path to a single forcing file (e.g. narr.1hr.txt). For 2D and 3D cases, this is the path to the directory containing all forcing files. Note that CLM must be compiled and linked at runtime for this option to be active.


.. note::
    The value must be a string


Solver.CLM.MetFileSubdir
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: int]


.. note::
    The value must be an Integer


Solver.CLM.MetForcing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: string] This key specifies defines whether 1D (uniform over the domain), 2D (spatially distributed) or 3D (spatially distributed with multiple timesteps per .pfb forcing file) forcing data is used. Choices for this key are 1D, 2D and 3D. This key has no default so the user must set it to 1D, 2D or 3D. Failure to set this key will cause CLM to still be run but with unpredictable values causing CLM to eventually crash. 1D meteorological forcing files are text files with single columns for each variable and each timestep per row, while 2D forcing files are distributed ParFlow binary files, one for each variable and timestep. File names are specified in the Solver.CLM.MetFileName variable below. Note that CLM must be compiled and linked at runtime for this option to be active.


.. note::
    The value must be one of the following options: 1D, 2D, 3D


Solver.CLM.Print1dOut
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: boolean/string] This key specifies whether the CLM one dimensional (averaged over each processor) output file is written or not. Choices for this key include True and False. Note that CLM must be compiled and linked at runtime for this option to be active.


:default: False
.. note::
    The value must be True or False


Solver.CLM.ResSat
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: double] This key specifies the residual saturation for the saturation function in CLM. Note that CLM must be compiled and linked at runtime for this option to be active.


:default: 0.1
.. note::
    The value must be an Integer
      - with a value greater than or equal to 0.0



Solver.CLM.ReuseCount
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: int] How many times to reuse a CLM atmospheric forcing file input. For example timestep=1, reuse =1 is normal behavior but reuse=2 and timestep=0.5 subdivides the time step using the same CLM input for both halves instead of needing two files. This is particually useful for large, distributed runs when the user wants to run ParFlow at a smaller timestep than the CLM forcing. Forcing files will be re-used and total fluxes adjusted accordingly without needing duplicate files.


:default: 1
.. note::
    The value must be an Integer
      - with a value greater than or equal to 0



Solver.CLM.RootZoneNZ
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: int] This key sets the number of soil layers the ParFlow expects from CLM. It will allocate and format all the arrays for passing variables to and from CLM accordingly. This value now sets the CLM number as well so recompilation is not required anymore. Most likely the key Solver.CLM.SoiLayer will also need to be changed.


:default: 10
.. note::
    The value must be an Integer
      - with a value greater than or equal to 1



Solver.CLM.SingleFile
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: boolean/string] Controls whether ParFlow writes all CLM output variables as a single file per time step. When "True", this combines the output of all the CLM output variables into a special multi-layer PFB with the file extension ".C.pfb". The first 13 layers correspond to the 2-D CLM outputs and the remaining layers are the soil temperatures in each layer. For example, a model with 4 soil layers will create a SingleFile CLM output with 17 layers at each time step. The file pseudo code is given below in § 6.4 and the variables and units are as specified in the multiple PFB and SILO formats as above.


:default: False
.. note::
    The value must be True or False


Solver.CLM.SoiLayer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: int] This key sets the soil layer, and thus the soil depth, that CLM uses for the seasonal temperature adjustment for all leaf and stem area indices.


:default: 7
.. note::
    The value must be an Integer
      - with a value greater than or equal to 1



Solver.CLM.VegWaterStress
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: string] This key specifies the form of the plant water stress function parameter in CLM. The valid types for this key are None, Saturation, Pressure.


:default: Saturation
.. note::
    The value must be one of the following options: None, Saturation, Pressure


Solver.CLM.WiltingPoint
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: double] This key specifies the wilting point for the bets-t function in CLM. Note that the units for this function are pressure [m] for a Pressure formulation and saturation [-] for a Saturation formulation. Note that CLM must be compiled and linked at runtime for this option to be active.


:default: 0.1
.. note::
    The value must be an Integer
      - with a value greater than or equal to 0.0



Solver.CLM.WriteLastRST
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: boolean/string] Controls whether CLM restart files are sequentially written or whether a single file restart file name.00000.p is overwritten each time the restart file is output, where p is the processor number. If "True" only one file is written/overwritten and if "False" outputs are written more frequently. Compatible with DailyRST and ReuseCount; for the latter, outputs are written every n steps where n is the value of ReuseCount.


:default: False
.. note::
    The value must be True or False


Solver.CLM.WriteLogs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: boolean/string] When False, this disables writing of the CLM output log files for each processor. For example, in the clm.tcl test case, if this flag is added False, washita.output.txt.p and washita.para.out.dat.p (were p is the processor #) are not created, assuming washita is the run name.


:default: True
.. note::
    The value must be True or False


Solver.CoarseSolve
--------------------------------------------------------------------------------

[Type: int]


.. note::
    The value must be an Integer


Solver.CompCompress
--------------------------------------------------------------------------------

[Type: int]


.. note::
    The value must be an Integer


Solver.DiagScale
--------------------------------------------------------------------------------

[Type: int]


.. note::
    The value must be an Integer


Solver.DiagSolver
--------------------------------------------------------------------------------

[Type: int]


.. note::
    The value must be an Integer


Solver.Drop
--------------------------------------------------------------------------------

[Type: double] This key gives a clipping value for data written to PFSB files. Data values greater than the negative of this value and less than the value itself are treated as zero and not written to PFSB files.


:default: 1e-8
.. note::
    The value must be an Integer
      - with a value greater than or equal to 0



Solver.DropTol
--------------------------------------------------------------------------------

[Type: int]


.. note::
    The value must be an Integer


Solver.EvapTrans
--------------------------------------------------------------------------------

Setting EvapTrans files



Solver.EvapTrans.FileLooping
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: boolean/string]


.. note::
    The value must be True or False


Solver.EvapTrans.FileName
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: string] This key specifies specifies filename for the distributed .pfb file that contains the flux values for Richards’ equation. This file has [T-1] units. For the steady-state option (Solver.EvapTransFile=True) this key should be the complete filename. For the transient option (Solver.EvapTransFileTransient=True then the filename is a header and ParFlow will load one file per timestep, with the form filename.00000.pfb.


.. note::
    The value must be a string


Solver.EvapTransFile
--------------------------------------------------------------------------------

[Type: boolean/string] This key specifies specifies that the Flux terms for Richards’ equation are read in from a .pfb file. This file has [T-1] units. Note this key is for a steady-state flux and should not be used in conjunction with the transient key below.


:default: False
.. note::
    The value must be True or False


Solver.EvapTransFileTransient
--------------------------------------------------------------------------------

[Type: boolean/string] This key specifies specifies that the Flux terms for Richards’ equation are read in from a series of flux .pfb file. Each file has [T-1] units. Note this key should not be used with the key above, only one of these keys should be set to True at a time, not both.


:default: False
.. note::
    The value must be True or False


Solver.Jacobian
--------------------------------------------------------------------------------

[Type: int]


.. note::
    The value must be an Integer


Solver.LSM
--------------------------------------------------------------------------------

[Type: string] This key specifies whether a land surface model, such as CLM, will be called each solver timestep. Choices for this key include none and CLM. Note that CLM must be compiled and linked at runtime for this option to be active.


:default: none
.. note::
    The value is required
    The value must be one of the following options: none, CLM


Solver.MaxConvergenceFailures
--------------------------------------------------------------------------------

[Type: int] This key gives the maximum number of convergence failures allowed. Each convergence failure cuts the timestep in half and the solver tries to advance the solution with the reduced timestep. The default value is 3. Note that setting this value to a value greater than 9 may result in errors in how time cycles are calculated. Time is discretized in terms of the base time unit and if the solver begins to take very small timesteps smallerthanbasetimeunit1000 the values based on time cycles will be change at slightly incorrect times. If the problem is failing converge so poorly that a large number of restarts are required, consider setting the timestep to a smaller value.


:default: 3
.. note::
    The value must be an Integer
      - with a value greater than or equal to 1



Solver.MaxIter
--------------------------------------------------------------------------------

[Type: int] This key gives the maximum number of iterations that will be allowed for time-stepping. This is to prevent a run-away simulation.


:default: 1000000
.. note::
    The value must be an Integer


Solver.MaxLevels
--------------------------------------------------------------------------------

[Type: int]


.. note::
    The value must be an Integer


Solver.MaxMinNX
--------------------------------------------------------------------------------

[Type: int]


.. note::
    The value must be an Integer


Solver.MaxMinNY
--------------------------------------------------------------------------------

[Type: int]


.. note::
    The value must be an Integer


Solver.MaxMinNZ
--------------------------------------------------------------------------------

[Type: int]


.. note::
    The value must be an Integer


Solver.OverlandDiffusive
--------------------------------------------------------------------------------

Setting epsilon value for the diffusive overland flow formulation.



Solver.OverlandDiffusive.Epsilon
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: double] This key provides a minimum value for the Sf used in the OverlandDiffusive boundary condition.


:default: 1e-05
.. note::
    The value must be an Integer
      - with a value greater than or equal to 0.0



Solver.OverlandKinematic
--------------------------------------------------------------------------------

Setting epsilon value for the diffusive kinematic flow formulation.



Solver.OverlandKinematic.Epsilon
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: double] This key provides a minimum value for the Sf used in the OverlandKinematic boundary condition.


:default: 1e-05
.. note::
    The value must be an Integer
      - with a value greater than or equal to 0.0



Solver.PCMatrixType
--------------------------------------------------------------------------------

[Type: int]


.. note::
    The value must be an Integer


Solver.PolyDegree
--------------------------------------------------------------------------------

[Type: int]


.. note::
    The value must be an Integer


Solver.PolyPC
--------------------------------------------------------------------------------

[Type: int]


.. note::
    The value must be an Integer


Solver.PrintCLM
--------------------------------------------------------------------------------

[Type: boolean/string] This key specifies whether the CLM writes two dimensional binary output files to a PFB binary format. Note that CLM must be compiled and linked at runtime for this option to be active. These files are all written according to the standard format used for all ParFlow variables, using the runname, and istep. Variables are either two-dimensional or over the number of CLM layers (default of ten).


:default: False
.. note::
    The value must be True or False


Solver.PrintConcentration
--------------------------------------------------------------------------------

[Type: boolean/string] This key is used to turn on printing of the concentration data. The printing of the data is controlled by values in the timing information section. The data is written as a PFB file.


:default: True
.. note::
    The value must be True or False


Solver.PrintDZMultiplier
--------------------------------------------------------------------------------

[Type: int]


.. note::
    The value must be an Integer


Solver.PrintEvapTrans
--------------------------------------------------------------------------------

[Type: int]


.. note::
    The value must be an Integer


Solver.PrintEvapTransSum
--------------------------------------------------------------------------------

[Type: int]


.. note::
    The value must be an Integer


Solver.PrintLSMSink
--------------------------------------------------------------------------------

[Type: boolean/string] This key is used to turn on printing of the flux array passed from CLM to ParFlow. Printing occurs at each DumpInterval time.


:default: False
.. note::
    The value must be True or False


Solver.PrintMannings
--------------------------------------------------------------------------------

[Type: boolean/string] This key is used to turn on printing of the flux array passed from CLM to ParFlow. Printing occurs at each DumpInterval time.


:default: False
.. note::
    The value must be True or False


Solver.PrintMask
--------------------------------------------------------------------------------

[Type: boolean/string] This key is used to turn on printing of the flux array passed from CLM to ParFlow. Printing occurs at each DumpInterval time.


:default: False
.. note::
    The value must be True or False


Solver.PrintOverlandBCFlux
--------------------------------------------------------------------------------

[Type: boolean/string] This key is used to turn on printing of the flux array passed from CLM to ParFlow. Printing occurs at each DumpInterval time.


:default: False
.. note::
    The value must be True or False


Solver.PrintOverlandSum
--------------------------------------------------------------------------------

[Type: boolean/string] This key is used to turn on printing of the flux array passed from CLM to ParFlow. Printing occurs at each DumpInterval time.


:default: False
.. note::
    The value must be True or False


Solver.PrintPressure
--------------------------------------------------------------------------------

[Type: boolean/string] This key is used to turn on printing of the pressure data. The printing of the data is controlled by values in the timing information section. The data is written as a PFB file.


:default: True
.. note::
    The value must be True or False


Solver.PrintSaturation
--------------------------------------------------------------------------------

[Type: boolean/string] This key is used to turn on printing of the saturation data. The printing of the data is controlled by values in the timing information section. The data is written as a PFB file.


:default: True
.. note::
    The value must be True or False


Solver.PrintSlopes
--------------------------------------------------------------------------------

[Type: boolean/string] This key is used to turn on printing of the saturation data. The printing of the data is controlled by values in the timing information section. The data is written as a PFB file.


:default: True
.. note::
    The value must be True or False


Solver.PrintSpecificStorage
--------------------------------------------------------------------------------

[Type: boolean/string] This key is used to turn on printing of the saturation data. The printing of the data is controlled by values in the timing information section. The data is written as a PFB file.


:default: True
.. note::
    The value must be True or False


Solver.PrintSubsurf
--------------------------------------------------------------------------------

[Type: boolean/string] This key is used to turn on printing of the subsurface data, Permeability and Porosity. The data is printed after it is generated and before the main time stepping loop - only once during the run. The data is written as a PFB file.


:default: True
.. note::
    The value must be True or False


Solver.PrintSubsurfData
--------------------------------------------------------------------------------

[Type: boolean/string] This key is used to turn on printing of the subsurface data, Permeability and Porosity. The data is printed after it is generated and before the main time stepping loop - only once during the run. The data is written as a PFB file.


:default: True
.. note::
    The value must be True or False


Solver.PrintTop
--------------------------------------------------------------------------------

[Type: boolean/string] ?


:default: False
.. note::
    The value must be True or False


Solver.PrintVelocities
--------------------------------------------------------------------------------

[Type: boolean/string] This key is used to turn on printing of the x,y, and z velocity data. The printing of the data is controlled by values in the timing information section. The data is written as a PFB file.


:default: False
.. note::
    The value must be True or False


Solver.PrintWells
--------------------------------------------------------------------------------

[Type: boolean/string] This key is used to turn on collection and printing of the well data. The data is collected at intervals given by values in the timing information section. Printing occurs at the end of the run when all collected data is written.


:default: True
.. note::
    The value must be True or False


Solver.RAPType
--------------------------------------------------------------------------------

[Type: int]


.. note::
    The value must be an Integer


Solver.RelTol
--------------------------------------------------------------------------------

[Type: double] This value gives the relative tolerance for the linear solve algorithm.


:default: 1.0
.. note::
    The value must be an Integer


Solver.SadvectOrder
--------------------------------------------------------------------------------

[Type: int] This key controls the order of the explicit method used in advancing the concentrations. This value can be either 1 for a standard upwind first order or 2 for a second order Godunov method.


:default: 2
.. note::
    The value must be an Integer
      - with a value greater than or equal to 1
      - with a value less than or equal to 2



Solver.Smoother
--------------------------------------------------------------------------------

[Type: int]


.. note::
    The value must be an Integer


Solver.Spinup
--------------------------------------------------------------------------------

[Type: int]


.. note::
    The value must be an Integer


Solver.Symmetric
--------------------------------------------------------------------------------

[Type: int]


.. note::
    The value must be an Integer


Solver.TerrainFollowingGrid
--------------------------------------------------------------------------------

[Type: boolean/string] This key specifies that a terrain-following coordinate transform is used for solver Richards. This key sets x and y subsurface slopes to be the same as the Topographic slopes (a value of False sets these subsurface slopes to zero). These slopes are used in the Darcy fluxes to add a density, gravity -dependent term. This key will not change the output files (that is the output is still orthogonal) or the geometries (they will still follow the computational grid)– these two things are both to do items. This key only changes solver Richards, not solver Impes.


:default: False
.. note::
    The value must be True or False


Solver.TerrainFollowingGrid
--------------------------------------------------------------------------------

Assigning properties to TerrainFollowingGrid and TerrainFollowingGrid.SlopeUpwindFormulation



Solver.TerrainFollowingGrid.SlopeUpwindFormulation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: string] This key specifies optional modifications to the terrain following grid formulation (Equation 5.8) . Choices for this key are Original, Upwind, UpwindSine. Original is the original TFG formulation shown in Equation 5.8 in the manual. The Original option calculates the theta-x and theta-y for a cell face as the average of the two adjacent cell slopes (i.e. assuming a cell centered slope calculation). The Upwind option uses the the theta-x and theta-y of a cell directly without averaging (i.e. assuming a face centered slope calculation). The UpwindSine is the same as the Upwind option but it also removes the Sine term from 5.8. Note the UpwindSine option is for experimental purposes only and should not be used in standard simulations. Also note that the choice of upwind orOriginal formulation should consistent with the choice of overland flow boundary condition if overland flow is being used. The upwind and UpwindSine are consistent with OverlandDiffusive and OverlandKinematic while Original is consistent with OverlandFlow.


:default: Original
.. note::
    The value must be one of the following options: Original, Upwind, UpwindSine


Solver.TwoNorm
--------------------------------------------------------------------------------

[Type: int]


.. note::
    The value must be an Integer


Solver.Weight
--------------------------------------------------------------------------------

[Type: int]


.. note::
    The value must be an Integer


Solver.WriteCLMBinary
--------------------------------------------------------------------------------

[Type: boolean/string] This key specifies whether the CLM writes two dimensional binary output files in a generic binary format. Note that CLM must be compiled and linked at runtime for this option to be active.


:default: True
.. note::
    The value must be True or False


Solver.Linear
--------------------------------------------------------------------------------

[Type: string] This key specifies the linear solver used for solver IMPES. Choices for this key are MGSemi, PPCG, PCG, and CGHS. The choice MGSemi is an algebraic mulitgrid linear solver (not a preconditioned conjugate gradient) which may be less robust than PCG as described in [3]. The choice PPCG is a preconditioned conjugate gradient solver. The choice PCG is a conjugate gradient solver with a multigrid preconditioner. The choice CGHS is a conjugate gradient solver.


:default: PCG
.. note::
    The value must be one of the following options: MGSemi, PPCG, PCG, CGHS


Solver.Linear
--------------------------------------------------------------------------------

Assigning properties to Solver.Linear



Solver.Linear.KrylovDimension
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: int] This key specifies the maximum number of vectors to be used in setting up the Krylov subspace in the GMRES iterative solver. These vectors are of problem size and it should be noted that large increases in this parameter can limit problem sizes. However, increasing this parameter can sometimes help nonlinear solver convergence.


:default: 10
.. note::
    The value is required
    The value must be an Integer
      - with a value greater than or equal to 1



Solver.Linear.MaxRestarts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: int] This key specifies the number of restarts allowed to the GMRES solver. Restarts start the development of the Krylov subspace over using the current iterate as the initial iterate for the next pass.


:default: 0
.. note::
    The value must be an Integer
      - with a value greater than or equal to 0



Solver.Linear.MaxRestart
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: int] This key specifies the number of restarts allowed to the GMRES solver. Restarts start the development of the Krylov subspace over using the current iterate as the initial iterate for the next pass.


:default: 0
.. note::
    The value must be an Integer
      - with a value greater than or equal to 0



SymmetricMat
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: string] This key specifies whether the preconditioning matrix is symmetric. Choices fo rthis key are Symmetric and Nonsymmetric. The choice Symmetric specifies that the symmetric part of the Jacobian will be used as the preconditioning matrix. The choice Nonsymmetric specifies that the full Jacobian will be used as the preconditioning matrix. NOTE: ONLY Symmetric CAN BE USED IF MGSemi IS THE SPECIFIED PRECONDITIONER!


:default: Symmetric
.. note::
    The value must be one of the following options: Symmetric, Nonsymmetric


.{precond_method}
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Setting Solver.Linear.Preconditioner.{precond_method} keys



.{precond_method}.MaxIter
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: int] This key specifies the maximum number of iterations to take in solving the preconditioner system with precond_ method solver.


:default: 1
.. note::
    The value must be an Integer
      - with a value greater than or equal to 1



.{precond_method}.MaxLevels
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: int] Max Levels


.. note::
    The value must be an Integer
      - with a value greater than or equal to 1



.{precond_method}.NumPreRelax
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: int] This key specifies the number of relaxations to take before coarsening in the specified preconditioner method. Note that this key is only relevant to the SMG multigrid preconditioner.


:default: 1
.. note::
    The value must be an Integer
      - with a value greater than or equal to 1



.{precond_method}.NumPostRelax
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: int] This key specifies the number of relaxations to take after coarsening in the specified preconditioner method. Note that this key is only relevant to the SMG multigrid preconditioner.


:default: 1
.. note::
    The value must be an Integer
      - with a value greater than or equal to 1



.{precond_method}.Smoother
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: string]


.. note::
    The value must be a string


.{precond_method}.RAPType
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: string] For the PFMG solver, this key specifies the Hypre RAP type. Valid values are Galerkin or NonGalerkin


:default: NonGalerkin
.. note::
    The value must be one of the following options: Galerkin, NonGalerkin


Solver.NonlinearSolver
--------------------------------------------------------------------------------

[Type: int]


.. note::
    The value must be an Integer


Solver.Nonlinear
--------------------------------------------------------------------------------

Setting nonlinear solver keys



Solver.Nonlinear.VariableDz
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: boolean/string] This key specifies whether dZ multipliers are to be used, the default is False. The default indicates a false or non-active variable dz and each layer thickness is 1.0 [L].


:default: False
.. note::
    The value must be True or False


Solver.Nonlinear.FlowBarrierX
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: boolean/string] This key specifies whether Flow Barriers are to be used in the X direction, the default is False. The default indicates a false or FBx value of one [-] everywhere in the domain.


:default: False
.. note::
    The value must be True or False


Solver.Nonlinear.FlowBarrierY
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: boolean/string] This key specifies whether Flow Barriers are to be used in the Y direction, the default is False. The default indicates a false or FBy value of one [-] everywhere in the domain.


:default: False
.. note::
    The value must be True or False


Solver.Nonlinear.FlowBarrierZ
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: boolean/string] This key specifies whether Flow Barriers are to be used in the Z direction, the default is False. The default indicates a false or FBz value of one [-] everywhere in the domain.


:default: False
.. note::
    The value must be True or False


Solver.Nonlinear.ResidualTol
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: double] This key specifies the tolerance that measures how much the relative reduction in the nonlinear residual should be before nonlinear iterations stop. The magnitude of the residual is measured with the l1 (max) norm.


:default: 1e-7
.. note::
    The value must be an Integer
      - with a value greater than or equal to 0.0



Solver.Nonlinear.StepTol
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: double] This key specifies the tolerance that measures how small the difference between two consecutive nonlinear steps can be before nonlinear iterations stop.


:default: 1e-7
.. note::
    The value must be an Integer
      - with a value greater than or equal to 0.0



Solver.Nonlinear.MaxIter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: int] This key specifies the maximum number of nonlinear iterations allowed before iterations stop with a convergence failure.


:default: 15
.. note::
    The value must be an Integer
      - with a value greater than or equal to 1



Solver.Nonlinear.PrintFlag
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: string] This key specifies the amount of informational data that is printed to the *.out.kinsol.log file. Choices for this key are NoVerbosity, LowVerbosity, NormalVerbosity and HighVerbosity. The choice NoVerbosity prints no statistics about the nonlinear convergence process. The choice LowVerbosity outputs the nonlinear iteration count, the scaled norm of the nonlinear function, and the number of function calls. The choice NormalVerbosity prints the same as for LowVerbosity and also the global strategy statistics. The choice HighVerbosity prints the same as for NormalVerbosity with the addition of further Krylov iteration statistics.


:default: HighVerbosity
.. note::
    The value must be one of the following options: NoVerbosity, LowVerbosity, NormalVerbosity, HighVerbosity


Solver.Nonlinear.EtaChoice
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: string] This key specifies how the linear system tolerance will be selected. The linear system is solved until a relative residual reduction of n is achieved. Linear residual norms are measured in the l^2 norm. Choices for this key include EtaConstant, Walker1 and Walker2. If the choice EtaConstant is specified, then n will be taken as constant. The choices Walker1 and Walker2 specify choices for n developed by Eisenstat and Walker (see reference in manual). For both of the last two choices, n is never allowed to be less than 1e-4.


:default: Walker2
.. note::
    The value must be one of the following options: EtaConstant, Walker1, Walker2


Solver.Nonlinear.EtaValue
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: double] This key specifies the constant value of n for the EtaChoice key EtaConstant.


:default: 1e-4
.. note::
    The value must be an Integer
      - with a value greater than or equal to 0.0



Solver.Nonlinear.EtaAlpha
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: double] This key specifies the value of alpha for the case of EtaChoice being Walker2.


:default: 2.0
.. note::
    The value must be an Integer
      - with a value greater than or equal to 0.0



Solver.Nonlinear.EtaGamma
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: double] This key specifies the value of gamma for the case of EtaChoice being Walker2.


:default: 0.9
.. note::
    The value must be an Integer
      - with a value greater than or equal to 0.0



Solver.Nonlinear.UseJacobian
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: boolean/string] This key specifies whether the Jacobian will be used in matrix-vector products or whether a matrix-free version of the code will run. Choices for this key are False and True. Using the Jacobian will most likely decrease the number of nonlinear iterations but require more memory to run.


:default: False
.. note::
    The value must be True or False


Solver.Nonlinear.DerivativeEpsilon
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: double] This key specifies the value of epsilon used in approximating the action of the Jacobian on a vector with approximate directional derivatives of the nonlinear function. This parameter is only used when the UseJacobian key is False.


:default: 1e-7
.. note::
    The value must be an Integer
      - with a value greater than or equal to 0.0



Solver.Nonlinear.Globalization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: string] This key specifies the type of global strategy to use. Possible choices for this key are InexactNewton and LineSearch. The choice InexactNewton specifies no global strategy, and the choice LineSearch specifies that a line search strategy should be used where the nonlinear step can be lengthened or decreased to satisfy certain criteria.


:default: LineSearch
.. note::
    The value must be one of the following options: LineSearch, InexactNewton


Wells
================================================================================

Here we define the wells for the model.



Wells.Names
--------------------------------------------------------------------------------

[Type: string] This key specifies the names fo the wells for which input data will be given.


.. note::
    The value must be a string


Wells.{well_name}
--------------------------------------------------------------------------------

Specifying properties for wells



Wells.{well_name}.InputType
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: string] This key specifies the type of well to be defined for the given well, well_name. This key can be either Vertical or Recirc. The value Vertical indicates that this is a single segmented well whose action will be specified by the user. The value Recirc indicates that this is a dual segmented, recirculating, well with one segment being an extraction well and another being an injection well. The extraction well filters out a specified fraction of each contaminant and recirculates the remainder to the injection well where the diluted fluid is injected back in. The phase saturations at the extraction well are passed without modification to the injection well. Note with the recirculating well, several input options are not needed as the extraction well will provide these values to the injection well.


.. note::
    The value must be one of the following options: Vertical, Recirc


Wells.{well_name}.Action
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: string] This key specifies the pumping action of the well. This key can be either Injection or Extraction. A value of Injection indicates that this is an injection well. A value of Extraction indicates that this is an extraction well.


.. note::
    The value must be one of the following options: Injection, Extraction


Wells.{well_name}.Type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: string] This key specifies the mechanism by which the well works (how ParFlow works with the well data) if the input type key is set to Vertical. This key can be either Pressure or Flux. A value of Pressure indicates that the data provided for the well is in terms of hydrostatic pressure and ParFlow will ensure that the computed pressure field satisfies this condition in the computational cells which define the well. A value of Flux indicates that the data provided is in terms of volumetric flux rates and ParFlow will ensure that the flux field satisfies this condition in the computational cells which define the well.


.. note::
    The value must be one of the following options: Pressure, Flux


Wells.{well_name}.ExtractionType
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: string] This key specifies the mechanism by which the extraction well works (how ParFlow works with the well data) if the input type key is set to Recirc. This key can be either Pressure or Flux. A value of Pressure indicates that the data provided for the well is in terms of hydrostatic pressure and ParFlow will ensure that the computed pressure field satisfies this condition in the computational cells which define the well. A value of Flux indicates that the data provided is in terms of volumetric flux rates and ParFlow will ensure that the flux field satisfies this condition in the computational cells which define the well.


.. note::
    The value must be one of the following options: Pressure, Flux


Wells.{well_name}.InjectionType
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: string] This key specifies the mechanism by which the injection well works (how ParFlow works with the well data) if the input type key is set to Recirc. This key can be either Pressure or Flux. A value of Pressure indicates that the data provided for the well is in terms of hydrostatic pressure and ParFlow will ensure that the computed pressure field satisfies this condition in the computational cells which define the well. A value of Flux indicates that the data provided is in terms of volumetric flux rates and ParFlow will ensure that the flux field satisfies this condition in the computational cells which define the well.


.. note::
    The value must be one of the following options: Pressure, Flux


Wells.{well_name}.X
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: double] This key specifies the x location of the vertical well if the input type is set to Vertical or of both the extraction and injection wells if the input type is set to Recirc.


.. note::
    The value must be an Integer


Wells.{well_name}.Y
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: double] This key specifies the y location of the vertical well if the input type is set to Vertical or of both the extraction and injection wells if the input type is set to Recirc.


.. note::
    The value must be an Integer


Wells.{well_name}.ZUpper
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: double] This key specifies the z location of the upper extent of a vertical well if the input type is set to Vertical.


.. note::
    The value must be an Integer


Wells.{well_name}.ExtractionZUpper
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: double] This key specifies the z location of the upper extent of a extraction well if the input type is set to Recirc.


.. note::
    The value must be an Integer


Wells.{well_name}.InjectionZUpper
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: double] This key specifies the z location of the upper extent of an injection well if the input type is set to Recirc.


.. note::
    The value must be an Integer


Wells.{well_name}.ZLower
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: double] This key specifies the z location of the lower extent of a vertical well if the input type is set to Vertical.


.. note::
    The value must be an Integer


Wells.{well_name}.ExtractionZLower
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: double] This key specifies the z location of the upper extent of a extraction well if the input type is set to Recirc.


.. note::
    The value must be an Integer


Wells.{well_name}.InjectionZLower
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: double] This key specifies the z location of the upper extent of an injection well if the input type is set to Recirc.


.. note::
    The value must be an Integer


Wells.{well_name}.Method
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: string] This key specifies a method by which pressure or flux for a vertical well will be weighted before assignment to computational cells. This key can only be Standard if the type key is set to Pressure; or this key can be either Standard,Weighted or Patterned if the type key is set to Flux. A value of Standard indicates that the pressure or flux data will be used as is. A value of Weighted indicates that the flux data is to be weighted by the cells permeability divided by the sum of all cell permeabilities which define the well. The value of Patterned is not implemented.


.. note::
    The value must be one of the following options: Standard, Weighted, Patterned


Wells.{well_name}.ExtractionMethod
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: string] This key specifies a method by which pressure or flux for an extraction well will be weighted before assignment to computational cells. This key can only be Standard if the type key is set to Pressure; or this key can be either Standard, Weighted or Patterned if the type key is set to Flux. A value of Standard indicates that the pressure or flux data will be used as is. A value of Weighted indicates that the flux data is to be weighted by the cells permeability divided by the sum of all cell permeabilities which define the well. The value of Patterned is not implemented.


.. note::
    The value must be one of the following options: Standard, Weighted, Patterned


Wells.{well_name}.InjectionMethod
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: string] This key specifies a method by which pressure or flux for an injection well will be weighted before assignment to computational cells. This key can only be Standard if the type key is set to Pressure; or this key can be either Standard, Weighted or Patterned if the type key is set to Flux. A value of Standard indicates that the pressure or flux data will be used as is. A value of Weighted indicates that the flux data is to be weighted by the cells permeability divided by the sum of all cell permeabilities which define the well. The value of Patterned is not implemented.


.. note::
    The value must be one of the following options: Standard, Weighted, Patterned


Wells.{well_name}.Cycle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: string] This key specifies the time cycles to which data for the well well_name corresponds.


.. note::
    The value must be a string


Wells.{well_name}.{interval_name}.Pressure.Value
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: double] This key specifies the hydrostatic pressure value for a vertical well if the type key is set to Pressure. Note This value gives the pressure of the primary phase (water) at z = 0. The other phase pressures (if any) are computed from the physical relationships that exist between the phases.


.. note::
    The value must be an Integer


Wells.{well_name}.{interval_name}.Saturation.{phase_name}.Value
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: double] This key specifies the saturation value of a vertical well.


.. note::
    The value must be an Integer
      - with a value greater than or equal to 0.0
      - with a value less than or equal to 1.0



Wells.{well_name}.{interval_name}.Flux.{phase_name}.Value
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: double] This key specifies the volumetric flux for a vertical well if the type key is set to Flux. Note only a positive number should be entered, ParFlow assigns the correct sign based on the chosen action for the well.


.. note::
    The value must be an Integer


Concentration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Setting contaminant value of vertical well.



Value
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: double] This key specifies the contaminant value of a vertical well.


.. note::
    The value must be an Integer


Wells.{well_name}.{interval_name}.Extraction.Pressure.Value
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: double] This key specifies the hydrostatic pressure value for an extraction well if the extraction type key is set to Pressure. Note This value gives the pressure of the primary phase (water) at z = 0. The other phase pressures (if any) are computed from the physical relationships that exist between the phases.


.. note::
    The value must be an Integer


Wells.{well_name}.{interval_name}.Extraction.Flux.{phase_name}.Value
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: double] This key specifies the volumetric flux for an extraction well if the extraction type key is set to Flux. Note only a positive number should be entered, ParFlow assigns the correct sign based on the chosen action for the well.


.. note::
    The value must be an Integer


Wells.{well_name}.{interval_name}.Injection.Pressure.Value
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: double] This key specifies the hydrostatic pressure value for an extraction well if the extraction type key is set to Pressure. Note This value gives the pressure of the primary phase (water) at z = 0. The other phase pressures (if any) are computed from the physical relationships that exist between the phases.


.. note::
    The value must be an Integer


Wells.{well_name}.{interval_name}.Injection.Flux.{phase_name}.Value
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: double] This key specifies the volumetric flux for an injection well if the injection type key is set to Flux. Note only a positive number should be entered, ParFlow assigns the correct sign based on the chosen action for the well.


.. note::
    The value must be an Integer


Fraction
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: double] This key specifies the fraction of the extracted contaminant which gets resupplied to the injection well.


.. note::
    The value must be an Integer
      - with a value greater than or equal to 0.0
      - with a value less than or equal to 1.0



Phase
================================================================================




Phase.Names
--------------------------------------------------------------------------------

[Type: string] This specifies the names of phases to be modeled. Currently only 1 or 2 phases may be modeled.


.. note::
    The value must be a string


Phase.RelPerm
--------------------------------------------------------------------------------

The following keys are used to describe relative permeability input for the Richards’ equation implementation. They will be ignored if a full two-phase formulation is used.



Phase.RelPerm.Type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: string] This key specifies the type of relative permeability function that will be used on all specified geometries. Note that only one type of relative permeability may be used for the entire problem. However, parameters may be different for that type in different geometries. For instance, if the problem consists of three geometries, then VanGenuchten may be specified with three different sets of parameters for the three different geometries. However, once VanGenuchten is specified, one geometry cannot later be specified to have Data as its relative permeability. The possible values for this key are Constant, VanGenuchten, Haverkamp, Data, and Polynomial.


.. note::
    The value must be one of the following options: Constant, VanGenuchten, Haverkamp, Data, Polynomial


Phase.RelPerm.GeomNames
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: string] This key specifies the geometries on which relative permeability will be given. The union of these geometries must cover the entire computational domain.


.. note::
    The value must be a string


Phase.RelPerm.VanGenuchten
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^




Phase.Saturation
--------------------------------------------------------------------------------

This section is only relevant to the Richards’ equation cases. All keys relating to this section will be ignored for other cases. The following keys are used to define the saturation-pressure curve.



Phase.Saturation.Type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: string] This key specifies the type of saturation function that will be used on all specified geometries. Note that only one type of saturation may be used for the entire problem. However, parameters may be different for that type in different geometries. For instance, if the problem consists of three geometries, then VanGenuchten may be specified with three different sets of parameters for the three different goemetries. However, once VanGenuchten is specified, one geometry cannot later be specified to have Data as its saturation. The possible values for this key are Constant, VanGenuchten, Haverkamp, Data, Polynomial and PFBFile.


.. note::
    The value must be one of the following options: Constant, VanGenuchten, Haverkamp, Data, Polynomial, PFBFile


Phase.Saturation.GeomNames
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: string] This key specifies the geometries on which saturation will be given. The union of these geometries must cover the entire computational domain.


.. note::
    The value must be a string


Phase.Saturation.VanGenuchten
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^




Phase.Saturation.VanGenuchten.File
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: int] This key specifies whether soil parameters for the VanGenuchten function are specified in a pfb file or by region. The options are either 0 for specification by region, or 1 for specification in a file. Note that either all parameters are specified in files (each has their own input file) or none are specified by files. Parameters specified by files are alpha, N, SRes, and SSat.


:default: 0
.. note::
    The value must be an Integer
      - with a value greater than or equal to 0
      - with a value less than or equal to 1



Type
--------------------------------------------------------------------------------

[Type: string] This key specifies whether density will be a constant value or if it will be given by an equation of state of the form (rd)exp(cP), where P is pressure, rd is the density at atmospheric pressure, and c is the phase compressibility constant. This key must be either Constant or EquationOfState.


.. note::
    The value must be one of the following options: Constant, EquationOfState


Value
--------------------------------------------------------------------------------

[Type: double] This specifies the value of density if this phase was specified to have a constant density value for the phase phase_name.


.. note::
    The value must be an Integer


ReferenceDensity
--------------------------------------------------------------------------------

[Type: double] This key specifies the reference density if an equation of state density function is specified for the phase phase_name.


.. note::
    The value must be an Integer


CompressibilityConstant
--------------------------------------------------------------------------------

[Type: double] This key specifies the phase compressibility constant if an equation of state density function is specified for the phase phase_name.


.. note::
    The value must be an Integer


Type
--------------------------------------------------------------------------------

[Type: string] This key specifies whether viscosity will be a constant value. Currently, the only choice for this key is Constant.


:default: Constant
.. note::
    The value is required
    The value must be one of the following options: Constant


Value
--------------------------------------------------------------------------------

[Type: double] This specifies the value of density if this phase was specified to have a constant density value for the phase phase_name.


.. note::
    The value is required
    The value must be an Integer


Type
--------------------------------------------------------------------------------

[Type: string] This key specifies whether the mobility for phase_name will be a given constant or a polynomial of the form, (S-So)^a, where S is saturation, So is irreducible saturation, and a is some exponent. The possibilities for this key are Constant and Polynomial.


:default: Constant
.. note::
    The value must be one of the following options: Constant, Polynomial


Value
--------------------------------------------------------------------------------

[Type: double] This key specifies the constant mobility value for phase phase_name.


.. note::
    The value must be an Integer


Exponent
--------------------------------------------------------------------------------

[Type: double] This key specifies the exponent used in a polynomial representation of the relative permeability. Currently, only a value of 2.0 is allowed for this key.


:default: 2.0
.. note::
    The value must be an Integer
      - with a value greater than or equal to 2.0
      - with a value less than or equal to 2.0



IrreducibleSaturation
--------------------------------------------------------------------------------

[Type: double] This key specifies the irreducible saturation used in a polynomial representation of the relative permeability. Currently, only a value of 0.0 is allowed for this key.


:default: 0.0
.. note::
    The value must be an Integer
      - with a value greater than or equal to 0.0
      - with a value less than or equal to 0.0



PhaseConcen
================================================================================

Here we define initial concentration conditions for contaminants.



GeomNames
--------------------------------------------------------------------------------

[Type: string] This key specifies the geometries on which an initial condition will be given, if the type was set to Constant. Note that geometries listed later “overlay” geometries listed earlier.


.. note::
    The value must be a string


PredefinedFunction
--------------------------------------------------------------------------------

[Type: string]


.. note::
    The value must be a string


Type
--------------------------------------------------------------------------------

[Type: string] This key specifies the type of initial condition that will be applied to different geometries for given phase, phase_name, and the given contaminant, contaminant_name. The choices for this key are Constant or PFBFile. The choice Constant will apply constants values to different geometries. The choice PFBFile will read values from a “ParFlow Binary” file.


.. note::
    The value must be one of the following options: Constant, PFBFile


FileName
--------------------------------------------------------------------------------

[Type: string] This key specifies the name of the “ParFlow Binary” file which contains the initial condition values if the type was set to PFBFile.


.. note::
    The value must be a string


Value
--------------------------------------------------------------------------------

[Type: double] This key specifies the initial condition value assigned to all points in the named geometry, geom_input_name, if the type was set to Constant.


.. note::
    The value must be an Integer


PhaseSources
================================================================================

The following keys are used to specify phase source terms. The units of the source term are 1=T . So, for example, to specify a region with constant flux rate of L3=T , one must be careful to convert this rate to the proper units by dividing by the volume of the enclosing region. For Richards’ equation input, the source term must be given as a flux multiplied by density.



Type
--------------------------------------------------------------------------------

[Type: string] This key specifies the type of source to use for phase phase_name. Possible values for this key are Constant and PredefinedFunction. Constant type phase sources specify a constant phase source value for a given set of regions. PredefinedFunction type phase sources use a preset function (choices are listed below) to specify the source. Note that the PredefinedFunction type can only be used to set a single source over the entire domain and not separate sources over different regions.


.. note::
    The value must be one of the following options: Constant, PredefinedFunction


GeomNames
--------------------------------------------------------------------------------

[Type: string] This key specifies the names of the geometries on which source terms will be specified. This is used only for Constant type phase sources. Regions listed later “overlay” regions listed earlier.


.. note::
    The value must be a string


PredefinedFunction
--------------------------------------------------------------------------------

[Type: string] This key specifies which of the predefined functions will be used for the source. Possible values for this key are X, XPlusYPlusZ, X3Y2PlusSinXYPlus1, X3Y4PlusX2PlusSinXYCosYPlus1, XYZTPlus1 and XYZTPlus1PermTensor.


.. note::
    The value must be one of the following options: X, XPlusYPlusZ, X3Y2PlusSinXYPlus1, X3Y4PlusX2PlusSinXYCosYPlus1, XYZTPlus1, XYZTPlus1PermTensor


Value
--------------------------------------------------------------------------------

[Type: double] This key specifies the value of a constant source term applied to phase phase _name on geometry geom_name.


.. note::
    The value must be an Integer


Contaminants
================================================================================




Contaminants.Names
--------------------------------------------------------------------------------

[Type: string] This specifies the names of contaminants to be advected.


.. note::
    The value must be a string


Value
--------------------------------------------------------------------------------

[Type: double] This key specifies the half-life decay rate of the named contaminant, contaminant_name. At present only first- order decay reactions are implemented and it is assumed that one contaminant cannot decay into another.


.. note::
    The value must be an Integer


TimingInfo
================================================================================

Setting timing parameters



TimingInfo.BaseUnit
--------------------------------------------------------------------------------

[Type: double] This key is used to indicate the base unit of time for entering time values. All time should be expressed as a multiple of this value. This should be set to the smallest interval of time to be used in the problem. For example, a base unit of “1” means that all times will be integer valued. A base unit of “0.5” would allow integers and fractions of 0.5 to be used for time input values. The rationale behind this restriction is to allow time to be discretized on some interval to enable integer arithmetic to be used when computing/comparing times. This avoids the problems associated with real value comparisons which can lead to events occurring at different timesteps on different architectures or compilers. This value is also used when describing “time cycling data” in, currently, the well and boundary condition sections. The lengths of the cycles in those sections will be integer multiples of this value, therefore it needs to be the smallest divisor which produces an integral result for every “real time” cycle interval length needed.


.. note::
    The value must be an Integer
      - with a value greater than or equal to 0.0



TimingInfo.StartCount
--------------------------------------------------------------------------------

[Type: int] This key is used to indicate the time step number that will be associated with the first advection cycle in a transient problem. The value -1 indicates that advection is not to be done. The value 0 indicates that advection should begin with the given initial conditions. Values greater than 0 are intended to mean “restart” from some previous “checkpoint” time-step, but this has not yet been implemented.


.. note::
    The value must be an Integer
      - with a value greater than or equal to -1
      - with a value less than or equal to 0



TimingInfo.StartTime
--------------------------------------------------------------------------------

[Type: double] This key is used to indicate the starting time for the simulation.


.. note::
    The value is required
    The value must be an Integer


TimingInfo.StopTime
--------------------------------------------------------------------------------

[Type: double] This key is used to indicate the stopping time for the simulation.


.. note::
    The value is required
    The value must be an Integer


TimingInfo.DumpInterval
--------------------------------------------------------------------------------

[Type: double] This key is the real time interval at which time-dependent output should be written. A value of 0 will produce undefined behavior. If the value is negative, output will be dumped out every n time steps, where n is the absolute value of the integer part of the value.


.. note::
    The value is required
    The value must be an Integer


TimingInfo.DumpIntervalExecutionTimeLimit
--------------------------------------------------------------------------------

[Type: int] This key is used to indicate a wall clock time to halt the execution of a run. At the end of each dump interval the time remaining in the batch job is compared with the user supplied value, if remaining time is less than or equal to the supplied value the execution is halted. Typically used when running on batch systems with time limits to force a clean shutdown near the end of the batch job. Time units is seconds, a value of 0 (the default) disables the check. Currently only supported on SLURM based systems, “–with-slurm” must be specified at configure time to enable.


:default: 0
.. note::
    The value must be an Integer


TimeStep
================================================================================

Setting parameters for modeled time steps



TimeStep.Type
--------------------------------------------------------------------------------

[Type: string] This key must be one of: Constant or Growth. The value Constant defines a constant time step. The value Growth defines a time step that starts as dt0 and is defined for other steps as dtnew = gamma*dtold such that dtnew is less than or equal to dtmax and dtnew is greater than or equal to dtmin.


.. note::
    The value is required
    The value must be one of the following options: Constant, Growth


TimeStep.Value
--------------------------------------------------------------------------------

[Type: double] This key is used only if a constant time step is selected and indicates the value of the time step for all steps taken.


.. note::
    The value must be an Integer


TimeStep.InitialStep
--------------------------------------------------------------------------------

[Type: double] This key specifies the initial time step dt0 if the Growth type time step is selected.


.. note::
    The value must be an Integer


TimeStep.GrowthFactor
--------------------------------------------------------------------------------

[Type: double] This key specifies the growth factor gamma by which a time step will be multiplied to get the new time step when the Growth type time step is selected.


.. note::
    The value must be an Integer


TimeStep.MaxStep
--------------------------------------------------------------------------------

[Type: double] This key specifies the maximum time step allowed, dtmax, when the Growth type time step is selected.


.. note::
    The value must be an Integer
      - with a value greater than or equal to 0.0



TimeStep.MinStep
--------------------------------------------------------------------------------

[Type: double] This key specifies the minimum time step allowed, dtmin, when the Growth type time step is selected.


.. note::
    The value must be an Integer
      - with a value greater than or equal to 0.0



Cycle
================================================================================

Setting properties for cycles and intervals within those cycles.



Cycle.Names
--------------------------------------------------------------------------------

[Type: string] This key is used to specify the named time cycles to be used in a simulation. It is a list of names and each name defines a time cycle and the number of items determines the total number of time cycles specified. Each named cycle is described using a number of keys defined under Cycle.


.. note::
    The value must be a string


Wells.{well_name}
--------------------------------------------------------------------------------




Wells.{well_name}.Names
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: string] This key is used to specify the named time intervals for each cycle. It is a list of names and each name defines a time interval when a specific boundary condition is applied and the number of items determines the total number of intervals in that time cycle.


.. note::
    The value must be a string


Wells.{well_name}.Repeat
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[Type: int] This key is used to specify the how many times a named time interval repeats. A positive value specifies a number of repeat cycles a value of -1 specifies that the cycle repeat for the entire simulation.


.. note::
    The value is required
    The value must be an Integer
      - with a value greater than or equal to -1



Wells.{well_name}.{interval_name}
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^




Wells.{well_name}.{interval_name}.Length
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

[Type: int] This key is used to specify the length of a named time intervals. It is an integer multiplier of the value set for the TimingInfo.BaseUnit key described above. The total length of a given time cycle is the sum of all the intervals multiplied by the base unit.


.. note::
    The value must be an Integer
      - with a value greater than or equal to 1



FileVersion
================================================================================

[Type: int] This gives the value of the input file version number that this file fits. As development of the ParFlow code continues, the input file format may vary. We have thus included an input file format number as a way of verifying that the correct format type is being used. The user can check in the parflow/config/file_versions.h file to verify that the format number specified in the input file matches the defined value of PFIN_VERSION.


:default: 4
.. note::
    The value is required
    The value must be an Integer


Gravity
================================================================================

[Type: double] Specifies the gravity constant to be used.


.. note::
    The value is required
    The value must be an Integer
      - with a value greater than or equal to 0.0



OverlandFlowSpinUp
================================================================================

[Type: int] This key specifies that a simplified form of the overland flow boundary condition (Equation 5.17) be used in place of the full equation. This formulation removes lateral flow and drives and ponded water pressures to zero using a SeepageFace boundary condition. While this can be helpful in spinning up the subsurface, this is no longer coupled subsurface-surface flow. If set to zero (the default) this key behaves normally.


:default: 0
.. note::
    The value must be an Integer
      - with a value greater than or equal to 0
      - with a value less than or equal to 1



OverlandFlowSpinUpDampP1
================================================================================

This key sets P1 and provides exponential dampening to the pressure relationship in the overland flow equation by adding the following term: P2*exp[(pressure)*P2]


:default: 0.0
.. note::
    The value must be an Integer
      - with a value greater than or equal to 0.0



OverlandFlowSpinUpDampP2
================================================================================

This key sets P2 and provides exponential dampening to the pressure relationship in the overland flow equation by adding the following term: P2*exp[(pressure)*P2]


:default: 0.0
.. note::
    The value must be an Integer
      - with a value greater than or equal to 0.0



KnownSolution
================================================================================

[Type: string] This specifies the predefined function that will be used as the known solution. Possible choices for this key are No- KnownSolution, Constant, X, XPlusYPlusZ, X3Y2PlusSinXYPlus1, X3Y4PlusX2PlusSinXYCosYPlus1, XYZTPlus1 and XYZTPlus1PermTensor. Choices for this key correspond to solutions as follows: NoKnownSolution: No solution is known for this problem. Constant: p = constant X: p = x XPlusYPlusZ: p = x + y + z X3Y2PlusSinXYPlus1: p = x3y2 + sin(xy) + 1 X3Y4PlusX2PlusSinXYCosYPlus1: p = x3y4 + x2 + sin(xy) cos y + 1 XYZTPlus1: p = xyzt + 1 XYZTPlus1: p = xyzt + 1


.. note::
    The value is required
    The value must be one of the following options: NoKnownSolution, Constant, X, XPlusYPlusZ, X3Y2PlusSinXYPlus1, X3Y4PlusX2PlusSinXYCosYPlus1, XYZTPlus1, XYZTPlus1
