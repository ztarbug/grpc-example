import logging
import grpc
import time
import base64

from google.protobuf.timestamp_pb2 import Timestamp

import TrafikVerketExample_pb2
import TrafikVerketExample_pb2_grpc

def run():
    with grpc.insecure_channel('127.0.0.1:50051') as channel:
        stub = TrafikVerketExample_pb2_grpc.WeatherServiceStub(channel)
        req = TrafikVerketExample_pb2.WeatherMeasurepointRequest(ids = [1,2])

        camReq = TrafikVerketExample_pb2.CameraRequest(id = 1)

        resp = stub.GetCameraData(camReq)
        image_string = base64.b64decode(resp.image)
        fh = open("imageToSave.png", "wb")
        fh.write(image_string)
        fh.close()

        print("got image " + str(resp.image))

        timestamp = Timestamp()
        wmpList = []
        wmp1 = TrafikVerketExample_pb2.WeatherMeasurepoint(id=1, name="station01", Observation_Air_Temperature=20.0, last_update=timestamp.GetCurrentTime())
        wmp2 = TrafikVerketExample_pb2.WeatherMeasurepoint(id=2, name="station02", Observation_Air_Temperature=20.1, last_update=timestamp.GetCurrentTime())
        wmpList.append(wmp1)
        wmpList.append(wmp2)

        resp = stub.AddWeatherMeasurepoint(TrafikVerketExample_pb2.WeatherMeasurepointList(points = wmpList))
        print("added measurement points " + str(resp.successful))
        
        for i in range(5):
            resp = stub.GetWeatherMeasurepoint(req)
            print(resp)
            time.sleep(0.8)            

if __name__ == '__main__':
    logging.basicConfig()
    run()