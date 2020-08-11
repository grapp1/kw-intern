from parflow.utils import sortDict, loadPfidb, writeDictAsYaml

writeDictAsYaml(
    sortDict(loadPfidb('./test/comparison/default_richards.pfidb')),
    './output/ref_default_richards.yaml'
)

writeDictAsYaml(
    sortDict(loadPfidb('./output/default_richards.pfidb')),
    './output/py_default_richards.yaml'
)
