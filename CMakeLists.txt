cmake_minimum_required(VERSION 3.10)

project(MyProject)

# Set compiler options
set(CMAKE_CXX_FLAGS "-c -g -W -Waggregate-return -Wall -Werror -Wcast-align -Wcast-qual -Wchar-subscripts -Wno-volatile")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wcomment -Wformat -Wmissing-declarations -Wparentheses -Wpointer-arith -Wredundant-decls")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wreturn-type -Wshadow -Wswitch -Wtrigraphs -Wwrite-strings -O")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fPIC -Wuninitialized -Wunused -march=x86-64 -I. -Isrc")

set(CMAKE_C_FLAGS "-Wimplicit -Wmissing-prototypes -Wnested-externs -Wstrict-prototypes -std=gnu99")

if(CMAKE_CXX_COMPILER_ID STREQUAL "Clang")
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wno-address-of-packed-member -Wno-cast-align -Wno-unused-function")
else()
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wno-address-of-packed-member -fno-inline-functions-called-once")
endif()

# Set the output directory for the build artifacts
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/build")

# Include header files
include_directories(src)

# Find all source files
file(GLOB_RECURSE SOURCES "src/*.c" "src/*.cpp")

add_library(sharedhashfile ${SOURCES})
# target_link_libraries(sharedhashfile mylib)
