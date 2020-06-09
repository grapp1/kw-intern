## yaml-to-pfidb.py
## conversion of yaml file to pfidb


import yaml

yamlfile = "run_LW_config_pt.yaml"
outfile = "LW_test.pfidb"

def yaml_to_pfidb(yamlfile, outfile):
    
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
    
        # print(pf_keys) to check if you want
        # print(pf_vals)
        
    # setting up empty .pfidb file
    file1 = open(outfile,"w")
    
    # first line - total number of unique key/value combinations
    file1.write(str(len(pf_keys))+" \n")
    
    # adding key/value pairs to file
    for i in range(1, len(pf_keys)):
        file1.write(str(len(pf_keys[i]))+" \n")
        file1.write(pf_keys[i]+" \n")
        file1.write(str(len(pf_vals[i]))+" \n")
        file1.write(pf_vals[i]+" \n")
    
    file1.close() 
    

yaml_to_pfidb(yamlfile, outfile)
    