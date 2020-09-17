********************************************************************************
Run script
********************************************************************************

================================================================================
Calling methods on a ``Run`` object
================================================================================

At the top of all the Python test scripts (located in $PARFLOW_SOURCE/test/python/) are something similar to the following lines:

.. code-block:: python3

    from parflow import Run
    test_run = Run("test_run", __file__)

These lines import the ``Run`` class from the ``parflow`` module and create a new ``Run`` object called ``test_run`` (or whatever you want the run name to be). All the key/value pairs are set on this object. The methods that can be called on a ``Run`` object are shown below:

.. code-block:: python3

   from parflow import Run

   # Instantiate a Run object
   test_run = Run("test_run", __file__)

   # Distribute a ParFlow binary file associated with a run
   # P, Q, and R optional arguments override Process.Topology values
   test_run.dist('test_slopes.pfb')

   # Validate the values set to the keys of the Run object
   test_run.validate()

   # Write out key/value pairs to a file
   test_run.write(file_format='pfidb')
   test_run.write(file_format='yaml')
   test_run.write(file_format='json')

   # Write pfidb file and run ParFlow in the same directory as the script, skipping validation
   test_run.run(skip_validation=True)

   # Clone the run into a new Run object
   cloned_run = test_run.clone('cloned_run')

================================================================================
Full API
================================================================================

1. ``runobj.validate()`` - validates the values set to each key. Validation checks for:

  - Data type (int, float, string)
  - Appropriate range of value (e.g. saturation can’t be less than zero!)
  - File availability
  - Duplicate values
  - Necessary module(s) installed
  - Key exists in working version of ParFlow

2. ``runobj.write(file_name=None, file_format='pfidb')`` - this will write the set of key/value pairs associated with the ``runobj`` in a specified format. The default ``file_name`` is the name of the ``Run`` object, and the default format is the ParFlow databse format. Other supported formats include *.yaml*, *.yml*, and *.json*.

3. ``runobj.run(working_directory=None, skip_validation=False)`` - this calls the ``write()`` method to write the set of key/value pairs to a ParFlow binary file. It also calls the ``validate()`` method if ``skip_validation=False``. If ``skip_validation=True``, it will skip the validation. This is equivalent to the ``--skip-validation`` runtime argument. Finally, the method will attempt to execute ParFlow. If ``working_directory`` is not given, ``run()`` defaults to writing all files in the directory of the Python script. The ``working_directory`` argument is equivalent to the ``--working-directory`` runtime argument.

4. ``runobj.dist(pfb_file)`` - distributes a given ParFlow binary file using the ``parflowio`` library with the given ``Process.Topology.[P/Q/R]``  values. The topology that the ``dist()`` method uses can be overwritten as in the above example. This will be covered in more detail in Tutorial 4.

5. ``runobj.clone(name)`` - clones the object ``runobj`` to a new object ``name``. This makes it easy to develop ensembles of runs without having to reset all the keys and values.

================================================================================
Setting keys
================================================================================

The basic way to set keys in a Python script is assigning a variable to the ``Run`` object that you initialize at the beginning of your model, like shown:

.. code-block:: python3

   from parflow import Run
   test_run = Run("test_run", __file__)

   # Now that the Run object is initialized, you can set keys:
   test_run.Process.Topology.P = 1
   test_run.Process.Topology.Q = 1
   test_run.Process.Topology.R = 1

Pretty simple! You can also create your user-defined keys, as shown below. Note that the following excerpts of code assume that you have already instantiated the ``Run`` object ``test_run``.

.. code-block:: python3

   test_run.GeomInput.Names = 'domain_input background_input'

   # Defining the InputType and GeomName of the 'domain_input' that you already defined:
   test_run.GeomInput.domain_input.InputType = 'Box'
   test_run.GeomInput.domain_input.GeomName = 'domain'

Python PFTools requires that you define the user-defined input names (e.g., ``GeomInput.Names``, ``Cycle.Names``, ``Phase.Names``) *before* you use them as part of a key name.

================================================================================
Valid key names
================================================================================

As a general rule, each "token" within a key name (e.g. ``GeomInput`` or ``domain_input`` in the prior example) must be a valid Python variable name. Information about valid Python variable names is `here
<https://www.w3schools.com/python/python_variables.asp>`_. This means that you can't use hyphens in your user-defined variables or use integers as tokens. However, if you absolutely *must* use non-Pythonic key names, there is a way. You can specify the token in brackets without the preceding decimal, as in the following example:

.. code-block:: python3

   test_run.Patch['x-lower'].BCPressure.Type = 'FluxConst'

Specifying integer tokens (e.g., setting ``Cell.0.dzScale.Value``) can be done in multiple ways. The preferred method is to use the token's "prefix", which is a character (alphanumeric or "_") that will always prefix that token. Right now, the prefixes for all the integer tokens is an underscore ("_").
However, as shown in the following example, these integer tokens can be set in multiple ways:

.. code-block:: python3

   prefix.dzScale.nzListNumber = 6

   # Here are four different ways to set integer values as part of a key name:
   # 1) no bracket, no quotes, underscore
   prefix.Cell._3.dzScale.Value = 1.000

   # 2) bracket, quotes, underscore, no preceding decimal
   prefix.Cell['_0'].dzScale.Value = 1.0

   # 3) bracket, quotes, no underscore, no preceding decimal
   prefix.Cell['1'].dzScale.Value = 1.00

   # 4) bracket, no quotes, no underscore, no preceding decimal
   prefix.Cell[2].dzScale.Value = 1.000

These will all write the key in the ParFlow database file in the correct format.

================================================================================
Setting keys that aren't in the library with with ``pfset()``
================================================================================

If you want to set a key in the Python script that's not already in the library, you have two options: 1) add the key to the library (see the documentation on "Contributing keys") or 2) using the ``pfset(key, value)`` method.
``pfset(key, value)`` allows the user to set a key (or token) ``name`` at any level with any ``value``. Here are some examples from the test file ``$PARFLOW_SOURCE/test/python/new_features/pfset_test/pfset_test.py``:

.. code-block:: python3

   # Sets A.New.Key.Test = 'SomeSuperContent'
   pfset_test.pfset(key='A.New.Key.Test', value='SomeSuperContent')

   # Sets Process.Topology.Random.Path = 5
   pfset_test.pfset(key='Process.Topology.Random.Path', value=5)

   # Sets Process.Topology.Random.PathFromTopology = 6
   pfset_test.Process.Topology.pfset(key='Random.PathFromTopology', value=6)

   # Sets Process.Topology.P = 2
   pfset_test.pfset(key='Process.Topology.P', value=2)

   # Sets Process.Topology.Q = 2
   pfset_test.Process.pfset(key='Topology.Q', value=3)

   # Sets Process.Topology.R = 2
   pfset_test.Process.Topology.pfset(key='R', value=4)

   # Sets Process.Topology.Seb = 2
   pfset_test.Process.Topology.pfset(key='Seb', value=5)

As you can see from the many examples here, you can use ``pfset(key, value)`` at any level of token within your key, and even set keys that already exist.

================================================================================
Setting keys and values with ``pfset()``
================================================================================
The ``pfset()`` method does more than just allow you to set an individual key. You can set groups of keys at a time using the ``hierarchical_map``, ``flat_map``, or ``yamlContent`` arguments in the ``pfset`` method, as shown in the test file ``$PARFLOW_SOURCE/test/python/new_features/pfset_test/pfset_test.py``:

.. code-block:: python3

   #-----------------------------------------------------------------------------
   # pfset: hierarchical_map
   #-----------------------------------------------------------------------------

   pfset_test.pfset(hierarchical_map={
       'SpecificStorage': {
           'Type': 'Constant',
           'GeomNames': 'domain',
    }
   })

   constOne = {'Type': 'Constant', 'Value': 1.0}

   pfset_test.Phase.water.Density.pfset(hierarchical_map=constOne)
   pfset_test.Phase.water.Viscosity.pfset(flat_map=constOne)

   #-----------------------------------------------------------------------------
   # pfset: flat_map
   #-----------------------------------------------------------------------------

   pfset_test.pfset(flat_map={
       'Phase.Saturation.Type': 'VanGenuchten',
       'Phase.Saturation.GeomNames': 'domain',
   })

   pfset_test.Phase.pfset(flat_map={
       'RelPerm.Type': 'VanGenuchten',
       'RelPerm.GeomNames': 'domain',
   })

   #---------------------------------------------------------
   # pfset: yamlContent
   #---------------------------------------------------------

   pfset_test.Geom.source_region.pfset(yamlContent='''
   Lower:
       X: 65.56
       Y: 79.34
       Z: 4.5
   Upper:
       X: 74.44
       Y: 89.99
       Z: 5.5
   ''')

   pfset_test.Geom.concen_region.pfset(yamlContent='''
   Lower:
       X: 60.0
       Y: 80.0
       Z: 4.0
   Upper:
       X: 80.0
       Y: 100.0
       Z: 6.0
   ''')

Or, if you have a yaml file, you can use the ``yamlFile`` argument to read in a yaml file to set the keys:

.. code-block:: python3

   #---------------------------------------------------------
   # pfset: yamlFile
   #---------------------------------------------------------

   pfset_test.pfset(yamlFile='./BasicSettings.yaml')
   pfset_test.pfset(yamlFile='./ComputationalGrid.yaml')
   pfset_test.Geom.pfset(yamlFile='./GeomChildren.yaml')

This can make your run scripts more compact and readable.

===================================================
Key validation
===================================================

An objective of the Python PFTools is to improve the error messages before and during a ParFlow run. The first step of this is validation.
If you call the ``validate()`` method on your ``Run`` object with incorrect values set to a key, you will get a range of error messages like the following:

.. image:: error_1.png
   :width: 684

.. image:: error_2.png
   :width: 377

You will also get a warning if you set a key multiple times, as shown:

.. image:: duplicate.png
   :width: 256

Here, ``Process.Topology.P`` was set three times: first to 1, then to 4, and finally to 2. Note: if you use the ``pfset()`` method to define a new key name, it
will not throw an error in the validation.

===================================================
Executing ParFlow
===================================================

When executing ParFlow via the Python script using ``run()``, you will get the following message if the ParFlow run succeeds:

.. image:: PF_success.png
   :width: 696

Or if it fails:

.. image:: PF_fail.png
   :width: 809

This will be followed by the contents of the *runname.out.txt* file.
