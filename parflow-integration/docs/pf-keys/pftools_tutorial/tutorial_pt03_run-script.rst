********************************************************************************
Tutorial 2: Python PFTools run scripts
********************************************************************************

================================================================================
Calling methods on a ``Run`` object
================================================================================

Recall in the Python scripts we used to run ParFlow in the first tutorial. At the top of the script, there were the following lines:

.. code-block:: language

    from parflow import Run
    default_richards = Run("default_richards", __file__)

These lines import the ``Run`` method from the ``parflow`` module and create a new ``Run`` object called ``default_richards``. All the key/value pairs are set on this object. Finally, once all the key/value pairs are set, the ``run()`` method is called on the object using ``default_richards.run()``. This is one of the methods that can be called on a ``Run`` object. These methods are explained below:

1. ``runobj.clone(name)`` - clones the object ``runobj`` to a new object ``name``. This makes it easy to develop ensembles of runs without having to reset all the keys and values.
2. ``runobj.dist(pfb_file)`` - distributes a given ParFlow binary file using the ``parflowio`` library with the given ``Process.Topology.[P/Q/R]``  values. The topology that the ``dist()`` method uses can be overwritten as in the following example:

    .. code-block:: language

        LWvdz.dist('lw.1km.slope_x.10x.pfb', 'P': 2, 'Q': 2)

  This will be covered in more detail in the next part of the tutorial.

3. ``runobj.run(working_directory=None, skip_validation=False)`` - this calls the ``write()`` method to write the set of key/value pairs to a ParFlow binary file. It also calls the ``validate()`` method if ``skip_validation=False``. If ``skip_validation=True``, it will skip the validation. Finally, the method will attempt to execute ParFlow. If ``working_directory`` is not given, ``run()`` defaults to writing all files in the directory of the Python script.

4. ``runobj.validate()`` - validates the values set to each key. Validation checks for:

  - Data type (int, float, string)
  - Appropriate range of value (e.g. saturation can’t be less than zero!)
  - File availability
  - Duplicate values

5. ``runobj.write(file_name=None, file_format='pfidb')`` - this will write the set of key/value pairs associated with the ``runobj`` in a specified format. The default ``file_name`` is the name of the ``Run`` object, and the default format is the ParFlow databse format. Other supported formats include *.yaml*, *.yml*, and *.json*.

----

================================================================================
Runtime arguments
================================================================================
Some of these methods can be called as arguments in the command line when executing the Python script defining your ParFlow run. These arguments include:

- ``--parflow-directory [/path/to/dir]``: User-specified path to the ParFlow directory (will override $PARFLOW_DIR)
- ``--parflow-version [3.6.0]``: Overrides the detected Parflow version
- ``--working-directory [/path/to/dir]``: Overrides the working directory. This is equivalent to the ``working_directory`` argument in the ``run()`` method.
- ``--skip-validation``: Disables validation. This is equivalent to setting the ``skip_validation`` argument in the ``run()`` method to ``True``.
- ``--show-line-error``: Changes the run settings to show the line(s) where an error occurs.
- ``--exit-on-error``: Changes the run settings to exit on error.
- ``--write-yaml``: Will write out the key/value pairs into a YAML file.
- ``-p [int]``: Overrides the value set to ``Process.Topology.P``.
- ``-q [int]``: Overrides the value set to ``Process.Topology.Q``.
- ``-r [int]``: Overrides the value set to ``Process.Topology.R``.

----

================================================================================
Try it out!
================================================================================
With the ``default_richards.py`` script that you created in the first tutorial, try calling the various methods within the script or add the runtime arguments to get familiar with them.
