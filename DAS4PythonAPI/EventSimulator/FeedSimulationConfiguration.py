import json

from DAS4PythonAPI.Communication.RestClient import RestClient
from DAS4PythonAPI.EventSimulator.AttributeConfiguration import AttributeConfiguration
from DAS4PythonAPI.EventSimulator.SimulationProperties import SimulationProperties
from DAS4PythonAPI.EventSimulator.SimulationSource import SimulationSource
from DAS4PythonAPI.Util import decodeObject, decodeField


class FeedSimulationConfiguration(object):
    def __init__(self, simulation_name = None, properties = None):
        if properties is not None:
            self.properties = properties
        elif simulation_name is not None:
            self.properties = SimulationProperties(simulationName=simulation_name)
        else:
            self.properties = SimulationProperties()
        self.sources = []

    @classmethod
    def parse(cls,jsonObject):
        result = FeedSimulationConfiguration(simulation_name=jsonObject["properties"]["simulationName"])
        def sourceListDecode(sourceList):
            return_list = []
            for source in sourceList:
                return_list.append(decodeField(source,SimulationSource.parse))
            return return_list
        decodeObject(jsonObject,result,{"properties":SimulationProperties.parse, "sources": sourceListDecode})
        return result

    def __eq__(self, other):
        return isinstance(other, FeedSimulationConfiguration) and self.properties == other.properties and self.sources == other.sources


    def toRequestObject(self):
        sources = []

        for source in self.sources:
            sources.append(source.toRequestObject())

        requestObject = {
            "properties": self.properties.toRequestObject(),
            "sources": sources
        }

        return requestObject

