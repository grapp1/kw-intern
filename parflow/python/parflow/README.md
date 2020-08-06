# ParFlow/python/parflow

This directory contains the necessary files to build the ParFlow library in Python.

## So you want to add a key to the library...

You've come to the right place. First, navigate to the ./database/definitions folder.

1. Select the yaml file that most closely matches the key that you want to add. If your key is nested within an 
existing key, be sure to find which yaml file includes the parent key(s). For example, if you wanted to add the key
*Solver.Linear.NewKey*, you would add it within the file *solver.yaml*.

2. Open the yaml file and navigate to the level within the hierarchy where you want to put your key. The structure of
the yaml files is designed to be easy to follow, so it should be easy to find the level where you'd like to add your
key. The indentation of these files is two spaces. Using our *Solver.Linear.NewKey* example, *Solver* is at the far
left, *Linear* is two spaces (one tab) in, and you would add *NewKey* two more spaces in (two tabs). I suggest copying
and pasting an existing key from the same level to make sure it's correct.

3. Fill in the details of your key. Again, this format is designed to be readable, so please refer to examples in the 
yaml files to guide you. The details that you can add are the following:

    - **__class__**: This is for adding dynamically defined key names. If the key you want to add is something that the
        user defines in the run script, make sure the key name is in the format *.{geom_name}*. The "__class__" name
        will only be used within the library generator. 
        
    - **__rst__**: This contains details to support the documentation. Subkeys for this include:
        - **name: {string}**: This argument will change the name of the key as it appears in the documentation. 
        - **skip: {no arguments}**: This will cause the key to not print in the documentation. This does not affect 
            nested keys.
        - **warning: {string}**: This argument will add a special warning message to the documentation. This should be
            used for special cases, such as when a key must be set differently in Python as opposed to a TCL script.
            
    - **help/__doc__**: This contains the documentation for the key. **help:** should be used for a field, and 
        **__doc__** should be used for a container or class.


