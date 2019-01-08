cmake_minimum_required( VERSION 3.0 )

project(cs1010_template)

add_compile_options( -g -Wall -Wextra -Wpedantic -Wdocumentation )

#set( CMAKE_RUNTIME_OUTPUT_DIRECTORY ~/tutorial/bin)

include_directories(include)

# set( CMAKE_BUILD_FILES_DIRECTORY  "${CMAKE_CURRENT_SOURCE_DIR}/build" )
# set( CMAKE_BUILD_DIRECTORY  "${CMAKE_CURRENT_SOURCE_DIR}/build" )


set( CMAKE_EXPORT_COMPILE_COMMANDS ON )

file(GLOB SOURCES "*.cpp")

foreach( testsourcefile ${SOURCES} )
  #string( REPLACE ".cpp" "" testname ${testsourcefile} )
  get_filename_component( testname ${testsourcefile} NAME_WE)
  add_executable( ${testname} ${testsourcefile} )
  target_link_libraries( ${testname} m )
endforeach( testsourcefile ${SOURCES} )



