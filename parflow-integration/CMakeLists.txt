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
  add_subdirectory(pf-python/generators/)
  set(PYTHON_GEN_DIR "pf-python/generators/")
endif()

# generating python library
if (${PARFLOW_PYTHON_GEN_LIB})
  add_subdirectory(test/python/)
  set(PYTHON_TEST_DIR "test/python/")
  COMMAND $<TARGET_FILE:python>
          "${PYTHON_GEN_DIR}/pf-python.py"
endif ()

# generating documentation of python library
if (${PARFLOW_PYTHON_GEN_DOC})
  COMMAND $<TARGET_FILE:python>
          "${PYTHON_GEN_DIR}/read_the_doc_rst.py"
endif ()

# adding python test files
if (${PARFLOW_PYTHON_TESTS})
  add_subdirectory(test/python/)
  set(PYTHON_TEST_DIR "test/python/")
endif ()

# maybe necessary for adding Python modules?
adding_python_dependencies(
    MODULES         ${python_modules}
    INSTALL_EXPORT  ParaViewPython
    INSTALL_HEADERS "${PARAVIEW_INSTALL_DEVELOPMENT_FILES}"
    PYTHON_PACKAGE  "paraview.modules"
    MODULE_DESTINATION  "${PARAVIEW_PYTHON_SITE_PACKAGES_SUFFIX}"
    CMAKE_DESTINATION   "${paraview_cmake_destination}"
    LIBRARY_DESTINATION "${CMAKE_INSTALL_LIBDIR}"
    WRAPPED_MODULES paraview_python_wrapped_modules
    TARGET          ParaView::pvpythonmodules
    DEPENDS         VTK::vtkpythonmodules)

# CMake command for building
add_test( NAME BuildPFPython
    COMMAND ${CMAKE_COMMAND}
    -DPYTHON_EXECUTABLE:FILEPATH=${PYTHON_EXECUTABLE}
    -DPARFLOW_DIR:PATH=${CMAKE_SOURCE_DIR}
    -DPARFLOW_PYTHON_GEN_LIB=True
    -PARFLOW_PYTHON_GEN_DOC=False
    -PARFLOW_PYTHON_TESTS=False
)
