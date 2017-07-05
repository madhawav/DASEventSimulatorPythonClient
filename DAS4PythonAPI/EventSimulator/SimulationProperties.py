import random

from DAS4PythonAPI.Util import encodeField, decodeField, decodeObject

ran = random

class SimulationProperties(object):
    def __init__(self, simulationName="Simulation_"+str(random.randint(1,1000)),timestampStartTime=None, timestampEndTime = None, noOfEvents=8, timeInterval=1000):
        self.simulationName = simulationName
        self.timestampStartTime = timestampStartTime
        self.timestampEndTime = timestampEndTime
        self.noOfEvents = noOfEvents
        self.timeInterval = timeInterval

    @classmethod
    def parse(cls, jsonObject):
        # result = SimulationProperties(simulationName=jsonObject["simulationName"])
        # if "timestampStartTime" in jsonObject.keys():
        #     result.timestampStartTime = decodeField(jsonObject["timestampStartTime"],type=int)
        # if "timestampEndTime" in jsonObject.keys():
        #     result.timestampEndTime = decodeField(jsonObject["timestampEndTime"],type=int)
        # if "noOfEvents" in jsonObject.keys():
        #     result.noOfEvents = decodeField(jsonObject["noOfEvents"],type=int)
        # if "timeInterval" in jsonObject.keys():
        #     result.timeInterval = decodeField(jsonObject["timeInterval"],type=int)
        # return result
        result = SimulationProperties(simulationName=decodeField(jsonObject["simulationName"],str))
        decodeObject(jsonObject,result,{"simulationName":str,"timestampStartTime":int, "timestampEndTime":int, "noOfEvents":int, "timeInterval":int  })
        return result

    def __eq__(self, other):
        return isinstance(other,SimulationProperties) and \
               self.simulationName == other.simulationName and \
               self.timestampEndTime == other.timestampEndTime and \
               self.timestampStartTime == other.timestampStartTime and \
               self.noOfEvents == other.noOfEvents and \
               self.timeInterval == other.timeInterval


    def toRequestObject(self):
        return {
            "simulationName": encodeField(self.simulationName),
            "timestampStartTime": encodeField(self.timestampStartTime),
            "timestampEndTime": encodeField(self.timestampEndTime),
            "noOfEvents": encodeField(self.noOfEvents),
            "timeInterval": encodeField(self.timeInterval)
        }
