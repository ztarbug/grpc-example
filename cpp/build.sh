#!/bin/bash

set -e
set -x

rm -rf build
mkdir build
cd build

conan install .. --build=missing
cmake .. -DCMAKE_BUILD_TYPE=Release -DBUILD_PYTHON=OFF -DBUILD_EXAMPLES=OFF
cmake --build .
