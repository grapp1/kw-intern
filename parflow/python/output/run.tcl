lappend auto_path $env(PARFLOW_DIR)/bin
package require parflow
namespace import Parflow::*

set runname "default_richards"
puts $runname
pfwritedb    $runname
