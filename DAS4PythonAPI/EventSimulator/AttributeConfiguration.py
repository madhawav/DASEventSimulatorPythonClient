from enum import Enum

from DAS4PythonAPI.ObjectMapping.APIObject import APIObject, NotSet
from DAS4PythonAPI.ObjectMapping.FieldMapping import FieldMapping, ListFieldMapping
from DAS4PythonAPI.__Util import decodeField, decodeObject


class AttributeConfiguration(APIObject):
    class Type(Enum):
        CUSTOM_DATA_BASED = "CUSTOM_DATA_BASED"
        PRIMITIVE_BASED = "PRIMITIVE_BASED"
        REGEX_BASED = "REGEX_BASED"
        PROPERTY_BASED = "PROPERTY_BASED"

        @classmethod
        def encode(cls, v):
            return v.value

        @classmethod
        def decode(cls, v):
            return AttributeConfiguration.Type(v)


    class PrimitiveType(Enum):
        LONG = "LONG"
        INT = "INT"
        STRING = "STRING"
        FLOAT = "FLOAT"
        DOUBLE = "DOUBLE"

        @classmethod
        def encode(cls, v):
            return v.value

        @classmethod
        def decode(cls, v):
            return AttributeConfiguration.Type(v)

    def __init__(self, type, min=NotSet(), max=NotSet(), length=NotSet(), precision=NotSet(), list=NotSet(), pattern=NotSet(),
                 primitiveType=NotSet(), property=NotSet()):
        self._setup(field_mapping={"type":FieldMapping(AttributeConfiguration.Type.decode,AttributeConfiguration.Type.encode),"length":FieldMapping(int),
                                   "min":FieldMapping(int), "max":FieldMapping(int),
                                   "precision":FieldMapping(int), "list":ListFieldMapping(str,str,NotSet()),
                                   "pattern":FieldMapping(str),"property": FieldMapping(str) ,
                                   "primitiveType":FieldMapping(AttributeConfiguration.PrimitiveType.decode,AttributeConfiguration.PrimitiveType.encode)})
        self.type = type
        self.length = length
        self.min = min
        self.max = max
        self.precision = precision
        self.list = list
        self.pattern = pattern
        self.primitiveType = primitiveType
        self.property = property

    @classmethod
    def parse(cls, jsonObject):
        result = AttributeConfiguration(type=decodeField(jsonObject["type"],str))
        result._parse(jsonObject)
        return result