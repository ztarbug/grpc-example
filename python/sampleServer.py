from concurrent import futures
import logging
import grpc
from google.protobuf.timestamp_pb2 import Timestamp
import pprint

import TrafikVerketExample_pb2
import TrafikVerketExample_pb2_grpc

class WeatherServiceServicer(TrafikVerketExample_pb2_grpc.WeatherServiceServicer):
    
    def __init__(self):
        logging.info("server created")


    def GetWeatherMeasurepoint(self, request, context):
        print("server called")
        pprint.pprint(request.ids)
        context.set_code(grpc.StatusCode.OK)
        context.set_details('Executed')
        timestamp = Timestamp()
        wmpList = []
        wmp1 = TrafikVerketExample_pb2.WeatherMeasurepoint(id=1, name="station01", Observation_Air_Temperature=20.0, last_update=timestamp.GetCurrentTime())
        wmp2 = TrafikVerketExample_pb2.WeatherMeasurepoint(id=2, name="station02", Observation_Air_Temperature=20.1, last_update=timestamp.GetCurrentTime())
        wmpList.append(wmp1)
        wmpList.append(wmp2)
        
        return TrafikVerketExample_pb2.WeatherMeasurepointList(points = wmpList)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    TrafikVerketExample_pb2_grpc.add_WeatherServiceServicer_to_server(WeatherServiceServicer(), server)
    server.add_insecure_port('127.0.0.1:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()