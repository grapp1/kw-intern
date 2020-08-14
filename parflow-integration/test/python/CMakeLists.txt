# -----------------------------------------------------------------------------
# Adding test files
# -----------------------------------------------------------------------------

# include(ParflowTest)

option(PARFLOW_TEST "Testing Python scripts" "FALSE")
if (PARFLOW_TEST)

  enable_testing()

  set(TESTS
    ${CMAKE_CURRENT_SOURCE_DIR}/base_3d/default_richards/default_richards.tcl
  )

  foreach(inputfile ${TESTS})
    add_custom_command(
      OUTPUT
        "${PARFLOW_PYTHON}"
      COMMAND
        ${PARFLOW_PYTHON} ${inputfile}
      COMMENT
        "ParFlow Python testing"
      VERBATIM
      )
  endforeach()

endif()

# -----------------------------------------------------------------------------
