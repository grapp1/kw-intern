********************************************************************************
Tutorial 3: Files!
********************************************************************************
Files in ParFlow are like sand at the beach: everywhere. Fortunately, Python PFTools has some helpful functions to read, write, move, and reference files that take some of the headache out of working with the many input and output files necessary for a given run.

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
