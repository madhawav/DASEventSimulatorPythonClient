import time

from DAS4PythonAPI.Util import encodeField


class SingleSimulationConfiguration(object):
    def __init__(self, siddhiAppName, streamName, data):
        self.siddhiAppName = siddhiAppName
        self.streamName = streamName
        self.data = data
        self.timestamp = millis = int(round(time.time() * 1000))

    def toRequestObject(self):
        req_data = []

        for datum in self.data:
            req_data.append(encodeField(datum))

        requestObject = {
            "siddhiAppName": encodeField(self.siddhiAppName),
            "streamName": encodeField(self.streamName),
            "data": req_data,
            "timestamp": encodeField(self.timestamp)
        }

        return requestObject

