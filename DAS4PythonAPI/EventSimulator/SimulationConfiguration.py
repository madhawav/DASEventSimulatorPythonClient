import json

from DAS4PythonAPI.Communication.RestClient import RestClient
from DAS4PythonAPI.EventSimulator.AttributeConfiguration import AttributeConfiguration
from DAS4PythonAPI.EventSimulator.SimulationProperties import SimulationProperties
from DAS4PythonAPI.EventSimulator.SimulationSource import SimulationSource

class SimulationConfiguration(object):
    def __init__(self, simulation_name):
        self.properties = SimulationProperties(simulation_name)
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

