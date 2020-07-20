from parflow.utils import sortDict, loadPfidb

def searchDict(keyList, existDict):
  for i in range(len(keyList)):
    if keyList[i] in existDict.items():
      print(keyList[i])
      searchDict(keyList[i+1], existDict.keys())
    else:
      new_entry = existDict[keyList[i]]

  return new_entry

def pfidbToNestedYaml(dictObj):
  yamlObj = {}
  for key, value in dictObj.items():
    split_keys = key.split('.')
    new_key = searchDict(split_keys, yamlObj)
    print(new_key)

  return yamlObj


yamlObj = pfidbToNestedYaml(sortDict(loadPfidb('./test/comparison/test_keys.pfidb')))

print(yamlObj)