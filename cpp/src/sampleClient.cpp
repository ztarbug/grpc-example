#include <iostream>

#include <grpc/grpc.h>
#include <grpcpp/channel.h>
#include <grpcpp/create_channel.h>
#include <grpcpp/client_context.h>

#include "google/protobuf/util/time_util.h"

#include "sampleClient.hpp"

#include "../build/TrafikVerketExample.pb.h"
#include "../build/TrafikVerketExample.grpc.pb.h"

using namespace std;
using namespace sampleclient;
using namespace trafikverket;

using google::protobuf::util::TimeUtil;

void MyClient::callAPI() {
    cout << "start gRPC call " << std::endl;

    string host = "localhost:50051";
    auto creds = grpc::InsecureChannelCredentials();
    auto channel = grpc::CreateChannel(host, creds);
    std::unique_ptr<trafikverket::WeatherService::Stub> stub = WeatherService::NewStub(channel);

    grpc::ClientContext context;

    WeatherMeasurepointRequest req;
    WeatherMeasurepointList resp;
    stub->GetWeatherMeasurepoint(&context, req, &resp);
    auto points = resp.points();
    for(::google::protobuf::RepeatedPtrField<WeatherMeasurepoint>::const_iterator it = points.begin() ; it != points.end(); ++it ) {
        string data = "";
        data += std::to_string(it->id());
        data += " " + it->name();
        data += " " + std::to_string(it->observation_air_temperature());
        data += " " +  TimeUtil::ToString(it->last_update());
        cout << data << std::endl;
    }
    

}