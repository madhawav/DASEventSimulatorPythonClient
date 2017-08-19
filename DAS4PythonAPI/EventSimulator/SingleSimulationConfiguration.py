from DAS4PythonAPI.ObjectMapping.APIObject import APIObject
from DAS4PythonAPI.ObjectMapping.FieldMapping import FieldMapping, ListFieldMapping


class SingleSimulationConfiguration(APIObject):
    def __init__(self, siddhiAppName, streamName, data):
        self._setup(field_mapping={"siddhiAppName":FieldMapping(str),"streamName":FieldMapping(str),
                                   "data":ListFieldMapping(int,str), "timestamp":FieldMapping(int)})
        self.siddhiAppName = siddhiAppName
        self.streamName = streamName
        self.data = data
        self.timestamp = None

