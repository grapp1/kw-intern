********************************************************************************
Tutorial 2: Python PFTools run scripts
********************************************************************************

================================================================================
Calling methods on a ``Run`` object
================================================================================

Recall in the Python scripts we used to run ParFlow in the first tutorial. At the top of the script, there were the following lines:

.. code-block:: python3

    from parflow import Run
    default_richards = Run("default_richards", __file__)

These lines import the ``Run`` class from the ``parflow`` module and create a new ``Run`` object called ``default_richards``. All the key/value pairs are set on this object. Finally, once all the key/value pairs are set, the ``run()`` method is called on the object using ``default_richards.run()``. This is one of the methods that can be called on a ``Run`` object. These methods are shown below:

.. code-block:: python3

   from parflow import Run

   # Instantiate a Run object
   test_run = Run("test_run", __file__)

   # Clone the Run object
   test_run_2 = test_run.clone('test_run_2')

   # Distribute a ParFlow binary file associated with a run
   # 'P', 'Q', and 'R' optional arguments will override the Process.Topology values set to the Run object.
   test_run.dist('test_slopes.pfb', 'P'=2, 'Q'=2)

   # Validate the values set to the keys of the Run object
   test_run.validate()

   # Write out key/value pairs to a file
   test_run.write(file_format='pfidb')
   test_run.write(file_format='yaml')
   test_run.write(file_format='json')

   # Write pfidb file and run ParFlow in the same directory as the script, skipping validation
   test_run.run(skip_validation=True)

================================================================================
Full API
================================================================================


1. ``runobj.clone(name)`` - clones the object ``runobj`` to a new object ``name``. This makes it easy to develop ensembles of runs without having to reset all the keys and values.

2. ``runobj.dist(pfb_file)`` - distributes a given ParFlow binary file using the ``parflowio`` library with the given ``Process.Topology.[P/Q/R]``  values. The topology that the ``dist()`` method uses can be overwritten as in the above example. This will be covered in more detail in Tutorial 4.

3. ``runobj.run(working_directory=None, skip_validation=False)`` - this calls the ``write()`` method to write the set of key/value pairs to a ParFlow binary file. It also calls the ``validate()`` method if ``skip_validation=False``. If ``skip_validation=True``, it will skip the validation. This is equivalent to the ``--skip-validation`` runtime argument. Finally, the method will attempt to execute ParFlow. If ``working_directory`` is not given, ``run()`` defaults to writing all files in the directory of the Python script. The ``working_directory`` argument is equivalent to the ``--working-directory`` runtime argument.

4. ``runobj.validate()`` - validates the values set to each key. Validation checks for:

  - Data type (int, float, string)
  - Appropriate range of value (e.g. saturation can’t be less than zero!)
  - File availability
  - Duplicate values

5. ``runobj.write(file_name=None, file_format='pfidb')`` - this will write the set of key/value pairs associated with the ``runobj`` in a specified format. The default ``file_name`` is the name of the ``Run`` object, and the default format is the ParFlow databse format. Other supported formats include *.yaml*, *.yml*, and *.json*.


================================================================================
Try it out!
================================================================================
With the ``default_richards.py`` script that you created in the first tutorial, try calling the various methods within the script or add the runtime arguments (see "Usage" in the PFTools introduction) to get familiar with them.
