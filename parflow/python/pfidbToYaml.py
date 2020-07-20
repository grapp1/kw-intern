from parflow.utils import sortDict, loadPfidb
import yaml

def searchDict(keyList, existDict, value):
  for i in range(len(keyList)):
    if len(existDict) and keyList[i] in existDict.keys():
      print(f'{keyList[i]} already exists')
      searchDict(keyList[i+1], existDict.keys(), value)
    elif i == len(keyList):
      existDict[keyList[i]] = value
    else:
      existDict[keyList[i]] = {}

  return existDict


def pfidbToNestedYaml(dictObj):
  yamlObj = {}
  for key, value in dictObj.items():
    split_keys = key.split('.')
    yamlObj = searchDict(split_keys, yamlObj, value)

  yamlObj = yaml.dump(yamlObj)

  return yamlObj


yamlObj = pfidbToNestedYaml(sortDict(loadPfidb('./test/comparison/test_keys.pfidb')))

print(yamlObj)