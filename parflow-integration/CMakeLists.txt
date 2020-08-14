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
  add_subdirectory(pf-keys)
  add_subdirectory(pf-python)
endif()
