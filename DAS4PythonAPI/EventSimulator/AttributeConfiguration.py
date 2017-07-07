from enum import Enum

from DAS4PythonAPI.ObjectMapping.APIObject import APIObject
from DAS4PythonAPI.ObjectMapping.FieldMapping import FieldMapping, ListFieldMapping
from DAS4PythonAPI.Util import decodeField, decodeObject


class AttributeConfiguration(APIObject):
    class Type(Enum):
        CUSTOM_DATA_BASED = "CUSTOM_DATA_BASED"
        PRIMITIVE_BASED = "PRIMITIVE_BASED"

        @classmethod
        def encode(cls, v):
            return v.value

        @classmethod
        def decode(cls, v):
            return AttributeConfiguration.Type(v)

    def __init__(self, type, min=None, max=None, length=None, precision=None, list=None):
        self._setup(field_mapping={"type":FieldMapping(AttributeConfiguration.Type.decode,AttributeConfiguration.Type.encode),"length":FieldMapping(int),
                                   "min":FieldMapping(int), "max":FieldMapping(int),
                                   "precision":FieldMapping(int), "list":ListFieldMapping(str,str)})
        self.type = type
        self.length = length
        self.min = min
        self.max = max
        self.precision = precision
        self.list = list

    @classmethod
    def parse(cls, jsonObject):
        result = AttributeConfiguration(type=decodeField(jsonObject["type"],str))
        result._parse(jsonObject)
        return result