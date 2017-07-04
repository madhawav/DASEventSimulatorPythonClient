import json

from DAS4PythonAPI.Communication.RestClient import RestClient
from DAS4PythonAPI.EventSimulator.AttributeConfiguration import AttributeConfiguration
from DAS4PythonAPI.EventSimulator.SimulationProperties import SimulationProperties
from DAS4PythonAPI.EventSimulator.SimulationSource import SimulationSource

class SimulationFeedConfiguration(object):
    def __init__(self, simulation_name = None, properties = None):
        if properties is not None:
            self.properties = properties
        elif simulation_name is not None:
            self.properties = SimulationProperties(simulationName=simulation_name)
        else:
            self.properties = SimulationProperties()
        self.sources = []

    def toRequestObject(self):
        sources = []

        for source in self.sources:
            sources.append(source.toRequestObject())

        requestObject = {
            "properties": self.properties.toRequestObject(),
            "sources": sources
        }

        return requestObject

