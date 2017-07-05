from DAS4PythonAPI.EventSimulator.AttributeConfiguration import AttributeConfiguration
from DAS4PythonAPI.ObjectMapping.APIObject import APIObject
from DAS4PythonAPI.ObjectMapping.FieldMapping import FieldMapping, ListFieldMapping


class SimulationSource(APIObject):
    def __init__(self, simulationType=None, streamName=None, siddhiAppName=None, timeStampInterval=5, attributeConfiguration=[]):
        self._setup(field_mapping={"simulationType": FieldMapping(str), "streamName": FieldMapping(str),
                                   "siddhiAppName": FieldMapping(str), "timeStampInterval": FieldMapping(int),
                                   "attributeConfiguration": ListFieldMapping(AttributeConfiguration.parse,AttributeConfiguration.toJSONObject)})
        self.simulationType = simulationType
        self.streamName = streamName
        self.siddhiAppName = siddhiAppName
        self.timeStampInterval = timeStampInterval
        self.attributeConfiguration = attributeConfiguration

    @classmethod
    def parse(cls, jsonObject):
        result = SimulationSource()
        result._parse(jsonObject)
        return result