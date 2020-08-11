from parflow.utils import sortDict, loadPfidb
import yaml

def getContainer(root, keyList):
  currentContainer = root
  for i in range(len(keyList)):
    if keyList[i] not in currentContainer:
      currentContainer[keyList[i]] = {}
    currentContainer = currentContainer[keyList[i]]

  return currentContainer


def pfidbToNestedYaml(dictObj):
  yamlObj = {}
  for key, value in dictObj.items():
    split_keys = key.split('.')
    getContainer(yamlObj, split_keys[:-1])[split_keys[-1]] = value

  yamlObj = yaml.dump(yamlObj)

  return yamlObj


yamlObj = pfidbToNestedYaml(sortDict(loadPfidb('./test/comparison/test_keys.pfidb')))

print(yamlObj)
