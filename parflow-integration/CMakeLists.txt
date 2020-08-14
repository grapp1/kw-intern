cmake_minimum_required (VERSION 3.14)

project (PARFLOW LANGUAGES C Fortran CXX)

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
# Building Python key library and documentation
#-----------------------------------------------------------------------------

option(PARFLOW_USE_PYTHON "Build python module for running ParFlow" "FALSE")
if (PARFLOW_USE_PYTHON)
  find_package(Python3 3.3 QUIET REQUIRED COMPONENTS Interpreter)
  set(PARFLOW_PYTHON ${Python3_EXECUTABLE})
  set(PYTHON_DEPENDS)

  option(USE_PYTHON_VENV "Use local virtual environment" "FALSE")
  if (USE_PYTHON_VENV)
    set(PARFLOW_PYTHON "${CMAKE_CURRENT_BINARY_DIR}/py-env/bin/python")
    add_custom_command(
      OUTPUT
        "${PARFLOW_PYTHON}"
      COMMAND
        ${Python3_EXECUTABLE} -m venv "${CMAKE_CURRENT_BINARY_DIR}/py-env"
      COMMAND
        source "${CMAKE_CURRENT_BINARY_DIR}/py-env/bin/activate"
      COMMAND
        pip install -r "${CMAKE_CURRENT_SOURCE_DIR}/pf-python/requirements.txt"
      COMMAND
        pip install -r "${CMAKE_CURRENT_SOURCE_DIR}/pf-keys/documentation/requirements.txt"
      COMMENT
        "Generate virtual environment for building Python components"
      VERBATIM
    )
    add_custom_target(
      BuildVirtualEnv
      DEPENDS
        "${PARFLOW_PYTHON}"
    )
    set(PYTHON_DEPENDS BuildVirtualEnv)
  endif()

  add_subdirectory(pf-keys)
  add_subdirectory(pf-python)
endif()
