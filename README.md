# Introduction
In today's software landscapes multiple development stacks for different components are nothing unusal. So technologies are necessary to create sound 
bridges, to connect those components (feel free to add random BS here, how wonderful micro services are...).
In order to provide an interesting example use case, some function from Sweden's TrafikVerket API is being used. API doc can be found here: https://api.trafikinfo.trafikverket.se/API/Model

All the stuff here is developed on Linux. It is most certainly possible to build and run on Windows, but that is somebody else's project...

# Goal of this repo
This is an educational repo showing how to use ProtoBuf and gRPC. So no production use is intended. If you want to use it, you'll do so without 
any warranty. It's goal is to demonstrate how to use these technologies to let components written in different languages communicate with each other. 

# How to use
Client is written in C++ and server in Python. 

## Build and run Python part

Installation
* python3 -m pip install --user grpcio-tools

Generate gRPC & ProtoBuf

    python3 -m grpc_tools.protoc -I. --python_out=python/ --grpc_python_out=python/ TrafikVerketExample.proto

Run server

    python3 sampleServer.py

Run client

    python3 sampleClient.py 
    
## Build and run C++ part

Installation
* CMake https://cmake.org/
* python3 -m pip install --user conan https://docs.conan.io/en/latest/installation.html
* apt-get install libprotobuf-dev protobuf-compiler
* clone and build grpc 
* add compiler.libcxx=libstdc++11 to ~/.conan/profiles/default

Running

In folder cpp bash script build.sh should do everything necessary. However all steps will be explained here anyhow.

With CMake it is convention, to create a folder build in which all action takes place. Do not check in this folder to git. In short you need following commands:
* conan install .. --build=missing
* cmake .. -DCMAKE_BUILD_TYPE=Release
* cmake --build .