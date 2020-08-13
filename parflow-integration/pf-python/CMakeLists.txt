# -----------------------------------------------------------------------------
# Build generated python file for key definitions
# -----------------------------------------------------------------------------

add_custom_command(
  OUTPUT
    "${CMAKE_CURRENT_SOURCE_DIR}/parflow/tools/database/generated.py"
  COMMAND
    ${Python3_EXECUTABLE} pf-python.py
  DEPENDS
    "${CMAKE_CURRENT_SOURCE_DIR}/../pf-keys/generators/pf-python.py"
    "${CMAKE_CURRENT_SOURCE_DIR}/../pf-keys/definitions/wells.yaml"
    "${CMAKE_CURRENT_SOURCE_DIR}/../pf-keys/definitions/timing.yaml"
    "${CMAKE_CURRENT_SOURCE_DIR}/../pf-keys/definitions/bconditions.yaml"
    "${CMAKE_CURRENT_SOURCE_DIR}/../pf-keys/definitions/core.yaml"
    "${CMAKE_CURRENT_SOURCE_DIR}/../pf-keys/definitions/geom.yaml"
    "${CMAKE_CURRENT_SOURCE_DIR}/../pf-keys/definitions/netcdf.yaml"
    "${CMAKE_CURRENT_SOURCE_DIR}/../pf-keys/definitions/phase.yaml"
    "${CMAKE_CURRENT_SOURCE_DIR}/../pf-keys/definitions/run.yaml"
    "${CMAKE_CURRENT_SOURCE_DIR}/../pf-keys/definitions/solver.yaml"
  WORKING_DIRECTORY
    "${CMAKE_CURRENT_SOURCE_DIR}/../pf-keys/generators/"
  COMMENT
    "Generate ParFlow keys for Python"
  VERBATIM
)

# -----------------------------------------------------------------------------

add_custom_target(
  GeneratePythonKeys ALL
  DEPENDS
    ${CMAKE_CURRENT_SOURCE_DIR}/parflow/tools/database/generated.py
)

# -----------------------------------------------------------------------------
# Generate Pypy package
# -----------------------------------------------------------------------------

# TODO
