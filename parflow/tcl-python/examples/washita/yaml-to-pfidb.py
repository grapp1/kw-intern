## yaml-to-pfidb.py
## conversion of yaml file to pfidb


import yaml

# function to read the yaml file and convert it to lists of keys and values
def yaml_read(yamlfile):
    
    ## defining traverse function to determine the list of unique key paths
    def traverse(dic, path=None):
        if not path:
            path=[]
        if isinstance(dic,dict):
            for x in dic.keys():
                local_path = path[:]
                local_path.append(x)
                for b in traverse(dic[x], local_path):
                     yield b
        else: 
            yield path,dic
    
    ## reading yaml file
    with open(yamlfile) as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        pf_config = yaml.load(file, Loader=yaml.FullLoader)
        
        #defining list of keys and values
        pf_keys = []
        pf_vals = []
    
        for x in traverse(pf_config):
            pf_keys.append('.'.join(x[0]))
            pf_vals.append(str(x[1]))
    
        return(pf_keys, pf_vals)

# function to convert key and value lists to .pfidb file
def kv_to_pfidb(pf_keys, pf_vals, outfile):

    # setting up empty .pfidb file
    with open(outfile, "w") as file1:
    
        # first line - total number of unique key/value combinations
        file1.write(str(len(pf_keys))+" \n")
    
        # adding key/value pairs to file
        for i in range(len(pf_keys)):
            file1.write(str(len(pf_keys[i]))+" \n")
            file1.write(pf_keys[i]+" \n")
            file1.write(str(len(pf_vals[i]))+" \n")
            file1.write(pf_vals[i]+" \n")
    
        return(file1)
    

yamlfile = "run_LW_config_gr.yaml"
outfile = "LW_test.pfidb"

# execute functions
pf_keys, pf_vals = yaml_read(yamlfile)
kv_to_pfidb(pf_keys, pf_vals, outfile)
    