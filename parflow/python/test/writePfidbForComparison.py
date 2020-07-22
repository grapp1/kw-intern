from parflow.utils import sortDict, loadPfidb, writeDictAsYaml

writeDictAsYaml(
    sortDict(loadPfidb('./test/comparison/water_balance.pfidb')),
    './output/ref_water_balance_x.yaml'
)

writeDictAsYaml(
    sortDict(loadPfidb('./output/water_balance_x.pfidb')),
    './output/py_water_balance_x.yaml'
)
