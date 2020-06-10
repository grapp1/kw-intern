# pf_key_checking
# function to cross-check keys values between ParFlow and manual

manual_file = '/Users/grapp/ParF/parflow/docs/manuals/files.tex'
parflow_folder = '~/ParF/parflow/pfsimulator/parflow_lib/'

with open(manual_file, 'r') as f:
    for line in f.readlines():
        if '\pfkey' in line:
            print(line)
            
import os
import re

def findfiles(path, regex):
    regObj = re.compile(regex)
    res = []
    for root, dirs, fnames in os.walk(path):
        for fname in fnames:
            if regObj.match(fname):
                res.append(os.path.join(root, fname))
    return res

print findfiles('.', r'my?(reg|ex)')

def grep(filepath, regex):
    regObj = re.compile(regex)
    res = []
    with open(filepath) as f:
        for line in f:
            if regObj.match(line):
                res.append(line)
    return res