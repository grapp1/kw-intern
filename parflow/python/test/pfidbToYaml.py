from parflow.utils import sortDict, loadPfidb
import yaml

def searchDict(keyList, existDict, value):
  new_entry = {}
  for i in range(len(keyList)):
    if keyList[i] in existDict.items():
      searchDict(keyList[i+1], existDict.keys())
    elif i == 0:
      existDict[keyList[i]] = {}
      new_entry = existDict[keyList[i]]
    elif i == len(keyList):
      new_entry = new_entry[keyList[i]]

  return new_entry


def pfidbToNestedYaml(dictObj):
  yamlObj = {}
  for key, value in dictObj.items():
    split_keys = key.split('.')
    searchDict(split_keys, yamlObj, value)

  yamlObj = yaml.dump(yamlObj)

  return yamlObj


yamlObj = pfidbToNestedYaml(sortDict(loadPfidb('./test/comparison/test_keys.pfidb')))

print(yamlObj)