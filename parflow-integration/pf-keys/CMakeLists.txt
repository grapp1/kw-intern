# -----------------------------------------------------------------------------
# Build Documentation if required
# -----------------------------------------------------------------------------

option(PARFLOW_KEY_DOCUMENTATION "Build key documentation for ParFlow" "FALSE")
if (PARFLOW_KEY_DOCUMENTATION)
  add_subdirectory(documentation)
endif()


# -----------------------------------------------------------------------------
# Make sure our Python has the module that we need
# -----------------------------------------------------------------------------

find_python_module("yaml" yaml_found)
if (NOT yaml_found AND NOT USE_PYTHON_VENV)
  message(STATUS
    "Please install yaml to generate ParFlow keys for Python module or use the VirtualEnv option.")
  return()
endif()

# -----------------------------------------------------------------------------
# Build generated python file for key definitions
# -----------------------------------------------------------------------------

add_custom_command(
  OUTPUT
    "${CMAKE_CURRENT_SOURCE_DIR}/../pf-python/parflow/tools/database/generated.py"
  COMMAND
    ${PARFLOW_PYTHON} pf-python.py
  DEPENDS
    "${CMAKE_CURRENT_SOURCE_DIR}/generators/pf-python.py"
    "${CMAKE_CURRENT_SOURCE_DIR}/definitions/wells.yaml"
    "${CMAKE_CURRENT_SOURCE_DIR}/definitions/timing.yaml"
    "${CMAKE_CURRENT_SOURCE_DIR}/definitions/bconditions.yaml"
    "${CMAKE_CURRENT_SOURCE_DIR}/definitions/core.yaml"
    "${CMAKE_CURRENT_SOURCE_DIR}/definitions/geom.yaml"
    "${CMAKE_CURRENT_SOURCE_DIR}/definitions/netcdf.yaml"
    "${CMAKE_CURRENT_SOURCE_DIR}/definitions/phase.yaml"
    "${CMAKE_CURRENT_SOURCE_DIR}/definitions/run.yaml"
    "${CMAKE_CURRENT_SOURCE_DIR}/definitions/solver.yaml"
  WORKING_DIRECTORY
    "${CMAKE_CURRENT_SOURCE_DIR}/generators/"
  COMMENT
    "Generate ParFlow keys for Python"
  VERBATIM
)

# -----------------------------------------------------------------------------

add_custom_target(
  GeneratePythonKeys
  DEPENDS
    ${PYTHON_DEPENDS}
    "${CMAKE_CURRENT_SOURCE_DIR}/../pf-python/parflow/tools/database/generated.py"
)
