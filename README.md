# Introduction
In today's software landscapes multiple development stacks for different components are nothing unusal. So technologies are necessary to create sound 
bridges, to connect those components (feel free to add random BS here, how wonderful micro services are...).
In order to provide an interesting example use case, some function from Sweden's TrafikVerket API is being used. API doc can be found here: https://api.trafikinfo.trafikverket.se/API/Model

# Goal of this repo
This is an educational repo showing how to use ProtoBuf and gRPC. So no production use is intended. If you want to use it, you'll do so without 
any warranty. It's goal is to demonstrate how to use these technologies to let components written in different languages communicate with each other. 

# How to use
Client is written in C++ and server in Python. 

## Build and run Python part
Generate gRPC & ProtoBuf

    python3 -m grpc_tools.protoc -I. --python_out=python/ --grpc_python_out=python/ TrafikVerketExample.proto

Run server

    python3 sampleServer.py

Run client

    python3 sampleClient.py 
    
## Build and run C++ part
TODO
