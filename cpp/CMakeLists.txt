cmake_minimum_required(VERSION 3.12)
project(sample LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED True)

#set(CMAKE_VERBOSE_MAKEFILE ON)

# this block shall locate protoc binary shipped with Conan dependency to prevent
# version problems, if protoc is installed on your system.
set(CONAN_PROTO_PACKAGE_DIR $ENV{HOME}/.conan/data/protobuf/3.21.1/)
set(FIND_COMMAND "find ${CONAN_PROTO_PACKAGE_DIR} -name protoc ! -type d | grep package")
execute_process(COMMAND bash "-c" "${FIND_COMMAND}" OUTPUT_VARIABLE MY_PROTO_COMPILER)
set(Protobuf_PROTOC_EXECUTABLE ${MY_PROTO_COMPILER} CACHE FILEPATH "The protoc compiler")

find_package(Protobuf REQUIRED)
find_package(gRPC CONFIG REQUIRED)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

# adding all conan libs to include dirs
foreach(PATH ${CONAN_INCLUDE_DIRS})
    include_directories(${PATH})
endforeach()

set(
    PROTO_FILES
    TrafikVerketExample.proto
)

add_library(protos ${PROTO_FILES})
set(gen_cpp_protos) # will hold generated files
protobuf_generate(TARGET protos LANGUAGE cpp OUT_VAR gen_cpp_protos)
get_target_property(grpc_cpp_plugin_location gRPC::grpc_cpp_plugin LOCATION)
set(gen_grpc_protos) # will hold generated files
protobuf_generate(TARGET protos LANGUAGE grpc OUT_VAR gen_grpc_protos GENERATE_EXTENSIONS .grpc.pb.h .grpc.pb.cc PLUGIN "protoc-gen-grpc=${grpc_cpp_plugin_location}")

set(MY_SRC
    "src/sampleClient.hpp"
    "src/sampleClient.cpp"
)

add_executable(sample src/main.cpp ${MY_SRC} ${gen_cpp_protos} ${gen_grpc_protos})

target_link_libraries(sample PUBLIC CONAN_PKG::protobuf)
target_link_libraries(sample PUBLIC CONAN_PKG::grpc)
