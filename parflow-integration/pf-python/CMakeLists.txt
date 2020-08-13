
message("Generate ParFlow keys for Python ${Python3_EXECUTABLE}")

add_custom_target(Name [ALL]
  ${Python3_EXECUTABLE} pf-python.py
  WORKING_DIRECTORY
    ${CMAKE_CURRENT_SOURCE_DIR}/../pf-keys/generators/
  COMMENT
    "Generate ParFlow keys for Python"
)

