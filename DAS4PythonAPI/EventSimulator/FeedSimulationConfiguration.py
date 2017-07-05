import json

from DAS4PythonAPI.EventSimulator.SimulationProperties import SimulationProperties
from DAS4PythonAPI.EventSimulator.SimulationSource import SimulationSource
from DAS4PythonAPI.ObjectMapping.APIObject import APIObject
from DAS4PythonAPI.ObjectMapping.FieldMapping import FieldMapping, ListFieldMapping


class FeedSimulationConfiguration(APIObject):
    def __init__(self, simulation_name = None, properties = None):
        self._setup(field_mapping={"properties":FieldMapping(SimulationProperties.parse, SimulationProperties.toRequestObject),"sources":ListFieldMapping(SimulationSource.parse,SimulationSource.toRequestObject)})
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
        result._parse(jsonObject)

        # def sourceListDecode(sourceList):
        #     return_list = []
        #     for source in sourceList:
        #         return_list.append(decodeField(source,SimulationSource.parse))
        #     return return_list
        # decodeObject(jsonObject,result,{"properties":SimulationProperties.parse, "sources": sourceListDecode})
        return result

    #def __eq__(self, other):
    #    return isinstance(other, FeedSimulationConfiguration) and self.properties == other.properties and self.sources == other.sources


    def toRequestObject(self):
        return self.toJSONObject()

        # sources = []
        #
        # for source in self.sources:
        #     sources.append(source.toRequestObject())
        #
        # requestObject = {
        #     "properties": self.properties.toRequestObject(),
        #     "sources": sources
        # }
        #
        # return requestObject

