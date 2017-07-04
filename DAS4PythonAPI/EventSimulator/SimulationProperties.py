from DAS4PythonAPI.Util import encodeField


class SimulationProperties(object):
    def __init__(self, simulationName):
        self.simulationName = simulationName
        self.timestampStartTime = None
        self.timestampEndTime = None
        self.noOfEvents = 8
        self.timeInterval = 1000

    def toRequestObject(self):
        return {
            "simulationName": encodeField(self.simulationName),
            "timestampStartTime": encodeField(self.timestampStartTime),
            "timestampEndTime": encodeField(self.timestampEndTime),
            "noOfEvents": encodeField(self.noOfEvents),
            "timeInterval": encodeField(self.timeInterval)
        }
