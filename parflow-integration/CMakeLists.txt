cmake_minimum_required (VERSION 3.14)

project (PARFLOW)

set (CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_SOURCE_DIR}/cmake/modules/")

#-----------------------------------------------------------------------------
# Version number
#-----------------------------------------------------------------------------
include (Version)
#
# Make a version file containing the current version from git.
#

include(GetGitRevisionDescription)
git_describe(PARFLOW_VERSION --tags)

# If not building with git then get version from file
if (NOT PARFLOW_VERSION)
  file (STRINGS "VERSION" PARFLOW_VERSION)
endif ()

message("Configuring version : ${PARFLOW_VERSION}")
version_create_variables (PARFLOW)

#-----------------------------------------------------------------------------
# CMAKE Subdirectories
#-----------------------------------------------------------------------------

# Need to turn on testing so tests in subdirctories are included in test target.
enable_testing ()

#-----------------------------------------------------------------------------
# Building Python key library and documentation if required
#-----------------------------------------------------------------------------

option(PARFLOW_USE_PYTHON "Build python module for running ParFlow" "FALSE")
if (PARFLOW_USE_PYTHON)
  find_package(Python3 3.3 QUIET REQUIRED COMPONENTS Interpreter)
  set(PARFLOW_PYTHON ${Python3_EXECUTABLE})
  set(PARFLOW_PYTHON_DEPENDS)

  option(USE_VIRTUAL_ENV "Use local Python virtual environment" "FALSE")
  if (USE_VIRTUAL_ENV)
    set(PARFLOW_PYTHON "${CMAKE_CURRENT_BINARY_DIR}/py-env/bin/python")
    add_custom_command(
      WORKING_DIRECTORY
        "${CMAKE_CURRENT_BINARY_DIR}"
      OUTPUT
        "${PARFLOW_PYTHON}"
      COMMAND
        ${Python3_EXECUTABLE} -m venv py-env
      COMMAND
        "${CMAKE_CURRENT_BINARY_DIR}/py-env/bin/pip3" install -r "${CMAKE_CURRENT_SOURCE_DIR}/pftools/python/requirements.txt"
      COMMAND
        "${CMAKE_CURRENT_BINARY_DIR}/py-env/bin/pip3" install -r "${CMAKE_CURRENT_SOURCE_DIR}/docs/pf-keys/requirements.txt"
      COMMENT
        "Generate virtual environment for building Python components"
      VERBATIM
    )
    add_custom_target(
      BuildVirtualEnv
      DEPENDS
        "${PARFLOW_PYTHON}"
    )
    set(PARFLOW_PYTHON_DEPENDS BuildVirtualEnv)
  endif()

  add_subdirectory(pf-keys)
  add_subdirectory(pftools/python)

  # Only enable Key Documentation if we enable Python
  option(PARFLOW_KEY_DOCUMENTATION "Build key documentation for ParFlow" "FALSE")
  if (PARFLOW_KEY_DOCUMENTATION)
    add_subdirectory(docs/pf-keys)
  endif()
endif()
