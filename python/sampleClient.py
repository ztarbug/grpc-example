import logging
import grpc
import time

import TrafikVerketExample_pb2
import TrafikVerketExample_pb2_grpc

def run():
    with grpc.insecure_channel('127.0.0.1:50051') as channel:
        stub = TrafikVerketExample_pb2_grpc.WeatherServiceStub(channel)
        req = TrafikVerketExample_pb2.WeatherMeasurepointRequest(ids = [1,2])
        
        for i in range(15):
            resp = stub.GetWeatherMeasurepoint(req)
            print(resp)
            time.sleep(0.8)

if __name__ == '__main__':
    logging.basicConfig()
    run()