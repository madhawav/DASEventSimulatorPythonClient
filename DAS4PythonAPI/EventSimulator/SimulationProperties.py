import random

from DAS4PythonAPI.Util import encodeField

ran = random

class SimulationProperties(object):
    def __init__(self, simulationName="Simulation_"+str(random.randint(1,1000)),timestampStartTime=None, timstampEndTime = None, noOfEvents=8, timeInterval=1000):
        self.simulationName = simulationName
        self.timestampStartTime = timestampStartTime
        self.timestampEndTime = timstampEndTime
        self.noOfEvents = noOfEvents
        self.timeInterval = timeInterval

    def toRequestObject(self):
        return {
            "simulationName": encodeField(self.simulationName),
            "timestampStartTime": encodeField(self.timestampStartTime),
            "timestampEndTime": encodeField(self.timestampEndTime),
            "noOfEvents": encodeField(self.noOfEvents),
            "timeInterval": encodeField(self.timeInterval)
        }
