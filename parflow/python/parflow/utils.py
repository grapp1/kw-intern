import json

from .database.generated import PFDBObj

def convertValueForStringDict(value):
  if isinstance(value, str):
    return value

  if hasattr(value, '__iter__'):
    return ' '.join([str(v) for v in value])

  return value


def extractKeysFromObject(dictToFill, instance, parentNamespace=''):
  for key in instance.__dict__:
    if key[0] == '_':
      continue

    value = instance.__dict__[key]
    if value == None:
      continue

    fullQualifiedKey = f'{parentNamespace}.{instance.getParFlowKey(key)}' if parentNamespace else key
    if isinstance(value, PFDBObj):
      extractKeysFromObject(dictToFill, value, fullQualifiedKey)
    else:
      dictToFill[fullQualifiedKey] = convertValueForStringDict(value)


def writeDictAsPfidb(dictObj, fileName):
  with open(fileName, 'w') as out:
    out.write(f'{len(dictObj) * 4 + 1}\n')
    for key in dictObj:
      out.write(f'{len(key)}\n')
      out.write(f'{key}\n')
      value = dictObj[key]
      out.write(f'{len(str(value))}\n')
      out.write(f'{str(value)}\n')

def writeDictAsYaml(dictObj, fileName):
  with open(fileName, 'w') as out:
    for key in dictObj:
      out.write(f'{key}:\n')
      value = dictObj[key]
      out.write(f'  {value}\n')


def writeDictAsJson(dictObj, fileName):
  with open(fileName, 'w') as out:
    out.write(json.dumps(dictObj, indent=2))


def writeDict(dictObj, fileName):
  ext = fileName.split('.').pop().lower()
  if ext in ['yaml', 'yml']:
    writeDictAsYaml(dictObj, fileName)
  elif ext == 'pfidb':
    writeDictAsPfidb(dictObj, fileName)
  elif ext == 'json':
    writeDictAsJson(dictObj, fileName)
  else:
    print(f'Could not find writer for {fileName}')
