from DAS4PythonAPI.ObjectMapping.APIObject import APIObject
from DAS4PythonAPI.ObjectMapping.FieldMapping import FieldMapping
from DAS4PythonAPI.Util import decodeField, decodeObject


class AttributeConfiguration(APIObject):
    def __init__(self, type, min=None, max=None, length=None, precision=None):
        self._setup(field_mapping={"type":FieldMapping(str),"length":FieldMapping(int),
                                   "min":FieldMapping(int), "max":FieldMapping(int),
                                   "precision":FieldMapping(int)})
        self.type = type
        self.length = length
        self.min = min
        self.max = max
        self.precision = precision

    @classmethod
    def parse(cls, jsonObject):
        result = AttributeConfiguration(type=decodeField(jsonObject["type"],str))
        result._parse(jsonObject)
        return result