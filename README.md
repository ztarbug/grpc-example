# Introduction
In today's software landscapes multiple development stacks for different components are nothing unusal. So technologies are necessary to create sound bridges, to connect those components (feel free to add random BS here, how wonderful micro services are...).
In order to provide an interesting example use case, some function from Sweden's TrafikVerket API is being used. API doc can be found here: https://api.trafikinfo.trafikverket.se/API/Model

All the stuff here is developed on Linux. It is most certainly possible to build and run on Windows, but that is somebody else's project...

# Goal of this repo
This is an educational repo showing how to use ProtoBuf and gRPC. So no production use is intended. If you want to use it, you'll do so without any warranty. It's goal is to demonstrate how to use these technologies to let components written in different languages communicate with each other.

You can support this repo by adding more clients in your prefered language. Pull requests are very much appreciated :) However please note, that it is super important to write good documentation how to build/run things in your language/runtime. As this is for education purposes students shall be able to get everything running here. 

# How to use
This repo contains so far clients in Python, Rust and C++. To keep things easy sample server is done in Python. One in Rust will follow. See following sections how to run individual clients.

## Build and run Python part

If you are familiar with virtual environments, it is highly recommended to use those.

Installation
* python3 -m pip install --user grpcio-tools

Generate gRPC & ProtoBuf

    python3 -m grpc_tools.protoc -I. --python_out=python/ --grpc_python_out=python/ TrafikVerketExample.proto

Run server

    python3 sampleServer.py

Run client

    python3 sampleClient.py 
    
## Build and run Rust part
Good news with Rust is, that it ships with a build and dependency management system called Cargo. Which is awesome, because with that you can focus on learning the language instead of investing many hours to build code. So install Rust on your Linux system like described here: https://www.rust-lang.org/tools/install

Then just enter Rust folder and run

    cargo run

First run will download and compile dependencies, which may take a while. 


## Build and run C++ part
As building in C++ isn't particular easy to reproduce, please have patiences to get this example running on your environment.

Installation
* CMake https://cmake.org/
* python3 -m pip install --user conan https://docs.conan.io/en/latest/installation.html
* apt-get install libprotobuf-dev protobuf-compiler
* clone and build grpc 
* add compiler.libcxx=libstdc++11 to ~/.conan/profiles/default

Running

In folder cpp bash script build.sh should do everything necessary. However all steps will be explained here anyhow. Note that ProtoBuf and gRPC code is generated by CMake. So no separate command is necessary. Generated code is located in build folder.

With CMake it is convention, to create a folder build in which all action takes place. Do not check in this folder to git. In short you need following commands:
* conan install .. --build=missing
* cmake .. -DCMAKE_BUILD_TYPE=Release
* cmake --build .

## Build and run C# part
Install DotNet SDK on your selected operating system. All necessary dependencies are already in project config file. To build and run just enter folder dotnet/grpc-sample and use dotnet commend:

    dotnet run