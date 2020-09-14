********************************************************************************
Python PFTools Tutorial
********************************************************************************

Introduction
================================================================================

Welcome to the tutorial for the Python pftools. More documentation can be found here: https://pypi.org/project/pftools/

You will need the following to fully follow this tutorial:

- Python >= 3.6
- ParFlow installed and running, with the correct $PARFLOW_DIR environment variable established
  (You can check this by running echo $PARFLOW_DIR in your terminal)

The commands in the tutorial assume that you are running a bash shell in Linux or MacOS.

----

Installation
================================================================================

pftools can be installed with the following command:

.. code-block:: language

    pip install pftools

Or, if you are a developer, you can clone the latest ParFlow repo, which has the source code in the directory *parflow/pftools/python/*:

.. code-block:: language

    git clone https://github.com/parflow/parflow.git

----

Tutorial 1: Converting a TCL File to run in Python
================================================================================
In this first tutorial, we will set up a virtual environment with pftools and its dependencies before importing a TCL file, converting it to Python, and running ParFlow.

First, let's set an environment variable for the newly cloned repo:

.. code-block:: language

    export PARFLOW_SOURCE=/path/to/new/parflow/

Now, set up a virtual environment and install pftools:

.. code-block:: language

    python3 -m venv tutorial-env
    source tutorial-env/bin/activate
    pip install pftools

Test your pftools installation:

.. code-block:: language

    python3 $PARFLOW_SOURCE/test/python/base_3d/default_richards/default_richards.py

The run should execute successfully, printing the message ``ParFlow ran successfully``.

Great, now you have a working ParFlow interface! Next, create a new directory and import a TCL file (example here drawn from the ParFlow TCL tests):

.. code-block:: language

    mkdir -p pftools_tutorial/tcl_to_py
    cd pftools_tutorial/tcl_to_py
    cp $PARFLOW_SOURCE/test/default_richards.tcl .

You can use our ``tcl2py`` tool to convert the TCL script to a Python script using the following command:

.. code-block:: language

   python3 -m parflow.cli.tcl2py -i default_richards.tcl

The converter gets you most of the way there, but there are a few things you'll have to change by hand. Open and edit the new ``.py`` file that you have generated and change the lines that need to be changed. If you are following this example, you will need to edit the ``Process.Topology`` values, the ``GeomInput.Names`` values, and comment out the two ``Solver.Linear.Preconditioner.MGSemi`` keys. Once you have edited your Python script, you can run it like you would any other Python script:

.. code-block:: language

   python3 default_richards.py

Voilà! You have now successfully converted your first ParFlow TCL script to Python. In the next tutorial, we'll get more advanced to leverage the many other features in the Python pftools. Onward!
