add_custom_target(Name [ALL]
  ${PYTHON_EXECUTABLE} pf-python.py
  WORKING_DIRECTORY
    ${CMAKE_CURRENT_SOURCE_DIR}/../pf-keys/generators/
  COMMENT
    "Generate ParFlow keys for Python"
)

