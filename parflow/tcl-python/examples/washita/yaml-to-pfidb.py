# yaml-to-pfidb.py
# conversion of yaml file to pfidb

import yaml


# function to read the yaml file and convert it to lists of keys and values
def yaml_read(yamlfile):

    ## defining traverse function to determine the list of unique key paths
    def traverse(dic, path=None):
        if path is None:
            path = []
        if isinstance(dic, dict):
            for key, val in dic.items():
                local_path = path.copy() + [key]
                for b in traverse(val, local_path):
                     yield b
        else:
            yield path, dic

    ## reading yaml file
    with open(yamlfile) as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        pf_config = yaml.load(file, Loader=yaml.FullLoader)

        #defining list of keys and values
        pf_keys = []
        pf_vals = []

        for path, val in traverse(pf_config):
            pf_keys.append('.'.join(path))
            pf_vals.append(str(val))

        return pf_keys, pf_vals


# function to convert key and value lists to .pfidb file
def kv_to_pfidb(pf_keys, pf_vals, outfile):

    # setting up empty .pfidb file
    with open(outfile, "w") as file1:

        # first line - total number of unique key/value combinations
        file1.write(str(len(pf_keys)) + " \n")

        # adding key/value pairs to file
        for key, val in zip(pf_keys, pf_vals):
            file1.write(str(len(key)) + "\n")
            file1.write(key + "\n")
            file1.write(str(len(val)) + "\n")
            file1.write(val + "\n")

        return file1


yamlfile = "run_LW_config_gr.yaml"
outfile = "LW_test.pfidb"

# execute functions
pf_keys, pf_vals = yaml_read(yamlfile)
kv_to_pfidb(pf_keys, pf_vals, outfile)
    