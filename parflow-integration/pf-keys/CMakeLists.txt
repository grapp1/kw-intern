cmake_minimum_required (VERSION 3.14)

# project (PARFLOW LANGUAGES C Fortran CXX)

set (CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_SOURCE_DIR}/cmake/modules/")

#-----------------------------------------------------------------------------
# Building Python key library and documentation
#-----------------------------------------------------------------------------

# generating python library
if (${PARFLOW_PYTHON_GEN_LIB})
  COMMAND ${PYTHON_EXECUTABLE}
          "${PYTHON_GEN_DIR}/pf-python.py"
endif ()

# generating documentation of python library
if (${PARFLOW_PYTHON_GEN_DOC})
  COMMAND ${PYTHON_EXECUTABLE}
          "${PYTHON_GEN_DIR}/read_the_doc_rst.py"
endif ()