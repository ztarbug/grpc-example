import logging
import grpc

import TrafikVerketExample_pb2
import TrafikVerketExample_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = TrafikVerketExample_pb2_grpc.WeatherServiceStub(channel)
        req = TrafikVerketExample_pb2.WeatherMeasurepointRequest(ids = [1,2])
        
        resp = stub.GetWeatherMeasurepoint(req)
        print(resp)

if __name__ == '__main__':
    logging.basicConfig()
    run()