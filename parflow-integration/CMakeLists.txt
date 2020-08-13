cmake_minimum_required (VERSION 3.14)

# project (PARFLOW LANGUAGES C Fortran CXX)

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

# enable testing
enable_testing ()

#-----------------------------------------------------------------------------
# CMAKE Subdirectories
#-----------------------------------------------------------------------------

# Need to turn on testing so tests in subdirctories are included in test target.
enable_testing ()

# Optionally build the simulator and/or tools.
# This is used on architectures where the login node is a different architecture
# than the compute nodes.   The simulator is built for the compute nodes; tools
# is built for the login node.
set (PARFLOW_ENABLE_SIMULATOR True CACHE BOOL "Enable building of the Parflow simulator")
if ( ${PARFLOW_ENABLE_SIMULATOR} )
  add_subdirectory (pfsimulator)
  add_subdirectory (test)
  add_subdirectory (examples)
endif ()

set (PARFLOW_ENABLE_TOOLS True CACHE BOOL "Enable building of the Parflow tools")
if ( ${PARFLOW_ENABLE_TOOLS} )
  add_subdirectory (pftools)
endif ()

#-----------------------------------------------------------------------------
# Building Python key library and documentation
#-----------------------------------------------------------------------------

if (PARFLOW_USE_PYTHON)
  # testing needs Python interpreter i.e. `PYTHON_EXECUTABLE` without which
  # our `find_python_module` checks to determine which tests to add or exclude
  # will fail. We find it here.
  find_package(Python3 3.3 QUIET REQUIRED COMPONENTS Interpreter)
  set(PYTHON_VERSION_MAJOR "${Python3_VERSION_MAJOR}")
  set(PYTHON_VERSION_MINOR "${Python3_VERSION_MINOR}")
  include(FindPythonModules)

  add_subdirectory(pf-keys/generators/)
  set(PYTHON_GEN_DIR "pf-keys/generators/")

  # adding python test files
  if (${PARFLOW_PYTHON_TESTS})
    set(PYTHON_TEST_DIR "test/python/")
  endif ()

endif()

# CMake command for building (to be moved)
add_test( NAME BuildPFPython
    COMMAND ${CMAKE_COMMAND}
    -DPYTHON_EXECUTABLE:FILEPATH=${PYTHON_EXECUTABLE}
    -DPARFLOW_DIR:PATH=${CMAKE_SOURCE_DIR}
    -DPARFLOW_PYTHON_GEN_LIB=True
    -PARFLOW_PYTHON_GEN_DOC=False
    -PARFLOW_PYTHON_TESTS=False
)
