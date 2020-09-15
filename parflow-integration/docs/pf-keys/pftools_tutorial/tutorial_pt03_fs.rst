********************************************************************************
Tutorial 3: Files!
********************************************************************************
Files in ParFlow are like sand at the beach: everywhere. Fortunately, Python PFTools has some helpful functions to read, write, move, and reference files that take some of the headache out of working with the many input and output files necessary for a given run. You can import these functions into your Python environment with the command ``from parflow.tools.fs import [function1, function2, ...]``. The available functions in this module are below.

================================================================================
Functions
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
Let's start from the ``pftools_tutorial`` directory that you made in the first tutorial, and copy in one of the Python script examples from the ParFlow repo:

.. code-block:: language

    mkdir -p ~/path/pftools_tutorial/fs
    cd ~/path/pftools_tutorial/fs
    cp $PARFLOW_SOURCE/test/python/clm/clm/clm.py .

Now, open ``clm.py``. You'll see that it imports and uses the ``mkdir`` and ``cp`` functions from ``parflow.tools.fs``. The syntax and usage is more compact than the ``os`` and ``shutil`` methods commonly used in Python. If you don't provide an absolute path to the file name, these functions will use ``get_absolute_path`` to find the absolute path based on your working directory (which again defaults to the directory where your Python script lives).

----

Try to run this script (``python3 clm.py``). It should fail. Towards the top of the printout, you should see several messages stating ``Error occurred while copying file``. These error messages can be helpful for troubleshooting failing runs. Open up the script again and replace the ``$PF_SRC`` calls with the ``$PARFLOW_SOURCE`` environment variable you made in the first tutorial. Now, try running again. As long as you have CLM compiled, it should work! Add some of the other functions to this script to exercise more of the options in the ``parflow.tools.fs`` toolbox.
