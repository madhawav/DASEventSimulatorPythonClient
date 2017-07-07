from enum import Enum

from DAS4PythonAPI.EventSimulator.AttributeConfiguration import AttributeConfiguration
from DAS4PythonAPI.ObjectMapping.APIObject import APIObject, NotSet
from DAS4PythonAPI.ObjectMapping.FieldMapping import FieldMapping, ListFieldMapping


class SimulationSource(APIObject):
    class Type(Enum):
        RANDOM_DATA_SIMULATION="RANDOM_DATA_SIMULATION"
        CSV_SIMULATION = "CSV_SIMULATION"
        DATABASE_SIMULATION = "DATABASE_SIMULATION"
        @classmethod
        def encode(cls, v):
            return v.value

        @classmethod
        def decode(cls, v):
            return SimulationSource.Type(v)

    def __init__(self, simulationType=Type.RANDOM_DATA_SIMULATION, streamName=NotSet(), siddhiAppName=NotSet(), timestampInterval=NotSet(), attributeConfiguration=[],
                 fileName=NotSet(), isOrdered=NotSet(), delimiter=NotSet(), timestampAttribute = NotSet(), dataSourceLocation=NotSet(),driver=NotSet(),
                 username=NotSet(), password=NotSet(), tableName=NotSet(),columnNamesList=NotSet()):
        self._setup(field_mapping={"simulationType": FieldMapping(SimulationSource.Type.decode, SimulationSource.Type.encode), "streamName": FieldMapping(str),
                                   "siddhiAppName": FieldMapping(str), "timestampInterval": FieldMapping(int),
                                   "attributeConfiguration": ListFieldMapping(AttributeConfiguration.parse,AttributeConfiguration.toJSONObject),
                                   "fileName":FieldMapping(str), "isOrdered":FieldMapping(bool), "delimiter":FieldMapping(str),
                                   "timestampAttribute":FieldMapping(int), "dataSourceLocation":FieldMapping(str),"driver":FieldMapping(str),
                                   "username":FieldMapping(str),"password":FieldMapping(str),"tableName":FieldMapping(str),
                                   "columnNamesList":ListFieldMapping(str,str,NotSet())})
        self.simulationType = simulationType
        self.streamName = streamName
        self.siddhiAppName = siddhiAppName
        self.timestampInterval = timestampInterval
        self.attributeConfiguration = attributeConfiguration
        self.fileName=fileName
        self.isOrdered = isOrdered
        self.delimiter = delimiter
        self.timestampAttribute = timestampAttribute
        self.dataSourceLocation=dataSourceLocation
        self.driver=driver
        self.username=username
        self.password=password
        self.tableName=tableName
        self.columnNamesList=columnNamesList

    @classmethod
    def parse(cls, jsonObject):
        result = SimulationSource()
        result._parse(jsonObject)
        return result