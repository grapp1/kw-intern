********************************************************************************
Tutorial 3: Files!
********************************************************************************
Files in ParFlow are like sand at the beach: everywhere.
Python native modules offers plenty of methods to handle files and directories
but they are not necessarily convenient when dealing with a ParFlow runs.
Fortunately, Python PFTools has some helpful functions to deal with the ParFlow
run working directory.

For example, lets pretend you want to automatically create a sub-directory for
your run while copying some data files into it at run time based on where your
run script lives.

You can simply do the following to achieve exactly that while using environment
variable interpolation to dynamically adapt your run script at runtime without
keep editing your script.

.. code-block:: python3

   from parflow.tools.fs import mkdir, cp

   mkdir('input-data')
   cp('$PF_SRC/test/input/*.pfb', './input-data/')


The working directory used to resolved your relative path get automatically set
when you initialize your run instance by doing ``myRun = Run("demo", __file__)``.
This means, that you should only use the ``fs`` methods after that initialization line.

The ``parflow.tools.fs`` module offer the following set of methods which all allow usage
of environment variable and relative path to your run script:

.. code-block:: python3

   from parflow.tools.fs import get_absolute_path, exists, mkdir, chdir, cp, rm, get_text_file_content

   # Create directory in your current run script directory
   mkdir('input')
   mkdir('tmp')

   # Copy if file missing
   if not exists('data.pfb'):
       # Use environment variable to resolve location of PF_DATA
       cp('$PF_DATA/data.pfb')

   # Read data using Python tools
   full_path = get_absolute_path('data.cvs')
   with open(full_path) as file:
       pass

   # Or use python working directory
   chdir('.')
   with open('data.csv') as file:
       pass

   # Or use the text file content helper
   txt = get_text_file_content('data.csv')

   # Clean behind yourself
   rm('tmp')


================================================================================
Full API
================================================================================

1. ``get_absolute_path(file_path)``: Returns the absolute file path of the relative file location argument ``file_path``.
2. ``exists(file_path)``: Returns ``True`` or ``False`` as to whether the file at ``file_path`` exists.
3. ``mkdir(dir_name)``: Makes a new directory ``dir_name``. This works recursively, so it will also create intermediate directories if they do not exist.
4. ``chdir(directory_path)``: Changes the working directory to ``directory_path``.
5. ``cp(source, target_path='.')``: Copies the file specified in the ``source`` argument to the location and/or file name specified in the ``target_path`` argument.
6. ``rm(path)``: Removes the file or directory located at ``path``.
7. ``get_text_file_content(file_path)``: Reads a text file located at ``file_path`` and returns its content.

================================================================================
Example
================================================================================

If you want more examples on how to leverage those helper functions,
you can look at ``$PARFLOW_SOURCE/test/python/clm/clm/clm.py``

The syntax and usage is more compact than the ``os`` and ``shutil`` methods commonly used in Python.
If you don't provide an absolute path to the file name, these functions will use ``get_absolute_path``
to find the absolute path based on your working directory which defaults to the directory where your
Python script lives.
