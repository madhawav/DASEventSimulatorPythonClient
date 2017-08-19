import random

from DAS4PythonAPI.ObjectMapping.APIObject import APIObject, NotSet
from DAS4PythonAPI.ObjectMapping.FieldMapping import FieldMapping
from DAS4PythonAPI.__Util import decodeField

ran = random


class SimulationProperties(APIObject):
    def __init__(self, simulationName="Simulation_" + str(random.randint(1, 1000)), timestampStartTime=NotSet(),
                 timestampEndTime=NotSet(), noOfEvents=NotSet(), timeInterval=NotSet()):
        self._setup(field_mapping={"simulationName": FieldMapping(str), "timestampStartTime": FieldMapping(int),
                                   "timestampEndTime": FieldMapping(int), "noOfEvents": FieldMapping(int),
                                   "timeInterval": FieldMapping(int)})

        self.simulationName = simulationName
        self.timestampStartTime = timestampStartTime
        self.timestampEndTime = timestampEndTime
        self.noOfEvents = noOfEvents
        self.timeInterval = timeInterval

    @classmethod
    def parse(cls, jsonObject):
        result = SimulationProperties(simulationName=decodeField(jsonObject["simulationName"], str))
        result._parse(jsonObject)
        return result
