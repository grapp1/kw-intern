********************************************************************************
Python PFTools Introduction
********************************************************************************

Welcome to Python PFTools. This is a Python package that creates a user-friendly
Python interface for ParFlow. This package allows users to run ParFlow directly
from a Python script, leveraging the power and accessibility of Python. More
documentation for this package can be found here: https://pypi.org/project/pftools/

================================================================================
Installation
================================================================================

``pftools`` can be installed with the following command:

.. code-block:: language

    pip install pftools[all]

The ``[all]`` argument will download the dependencies necessary for running ParFlow
and fully employing the other tools within this package. ``[all]`` encompasses the
subsets of dependencies, including:

- ``[pfb]``: installs the ``parflowio`` package for handling ParFlow binary (.pfb) files.
- ``[pfsol]``: installs the ``imageio`` package for handling image processing to assist some workflows to build ParFlow solid (.pfsol) files.

If you would like to set up a virtual environment to install ``pftools``, execute the following commands:

.. code-block:: language

    python3 -m venv py-env
    source py-env/bin/activate
    pip install pftools[all]


================================================================================
Running ParFlow via a Python script - runtime arguments
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
