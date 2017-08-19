from enum import Enum

from DAS4PythonAPI.EventSimulator.AttributeConfiguration import AttributeConfiguration
from DAS4PythonAPI.ObjectMapping.APIObject import APIObject, NotSet
from DAS4PythonAPI.ObjectMapping.FieldMapping import FieldMapping, ListFieldMapping, strOrInt


class SimulationSource(APIObject):
    '''
    SimulationSource APIObject which can be added to sources of FeedSimulationConfiguration
    '''

    class Type(Enum):
        '''
        Type of SimulationSource
        '''
        RANDOM_DATA_SIMULATION = "RANDOM_DATA_SIMULATION"
        CSV_SIMULATION = "CSV_SIMULATION"
        DATABASE_SIMULATION = "DATABASE_SIMULATION"

        @classmethod
        def encode(cls, v):
            return v.value

        @classmethod
        def decode(cls, v):
            return SimulationSource.Type(v)

    def __init__(self, simulationType=Type.RANDOM_DATA_SIMULATION, streamName=NotSet(), siddhiAppName=NotSet(),
                 timestampInterval=NotSet(), attributeConfiguration=[],
                 fileName=NotSet(), isOrdered=NotSet(), delimiter=NotSet(), timestampAttribute=NotSet(),
                 dataSourceLocation=NotSet(), driver=NotSet(),
                 username=NotSet(), password=NotSet(), tableName=NotSet(), columnNamesList=NotSet()):
        '''
        Instantiates Simulation Source. Refer DAS4 Documentation for details on parameters
        :param simulationType: Type of SimulationSource
        :param streamName: 
        :param siddhiAppName: 
        :param timestampInterval: 
        :param attributeConfiguration: 
        :param fileName: for File Access
        :param isOrdered: 
        :param delimiter: 
        :param timestampAttribute: 
        :param dataSourceLocation: 
        :param driver: for DB Access
        :param username: for DB access
        :param password: for DB Access
        :param tableName: for DB Access
        :param columnNamesList: for DB Access
        '''
        self._setup(
            field_mapping={"simulationType": FieldMapping(SimulationSource.Type.decode, SimulationSource.Type.encode),
                           "streamName": FieldMapping(str),
                           "siddhiAppName": FieldMapping(str), "timestampInterval": FieldMapping(int),
                           "attributeConfiguration": ListFieldMapping(AttributeConfiguration.parse,
                                                                      AttributeConfiguration.toJSONObject),
                           "fileName": FieldMapping(str), "isOrdered": FieldMapping(bool),
                           "delimiter": FieldMapping(str),
                           "timestampAttribute": FieldMapping(strOrInt), "dataSourceLocation": FieldMapping(str),
                           "driver": FieldMapping(str),
                           "username": FieldMapping(str), "password": FieldMapping(str), "tableName": FieldMapping(str),
                           "columnNamesList": FieldMapping(str)})

        self.simulationType = simulationType
        self.streamName = streamName
        self.siddhiAppName = siddhiAppName
        self.timestampInterval = timestampInterval
        self.attributeConfiguration = attributeConfiguration
        self.fileName = fileName
        self.isOrdered = isOrdered
        self.delimiter = delimiter
        self.timestampAttribute = timestampAttribute
        self.dataSourceLocation = dataSourceLocation
        self.driver = driver
        self.username = username
        self.password = password
        self.tableName = tableName
        self.columnNamesList = columnNamesList

    @classmethod
    def parse(cls, jsonObject):
        '''
        Converts a Python Class Object (from JSON) to SimulationSource Object.
        :param jsonObject: 
        :return: 
        '''
        result = SimulationSource()
        result._parse(jsonObject)
        return result
