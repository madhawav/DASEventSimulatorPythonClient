from DAS4PythonAPI.Util import decodeField, decodeObject


class AttributeConfiguration(object):
    def __init__(self, type, min=None, max=None, length=None, precision=None):
        self.type = type
        self.length = length
        self.min = min
        self.max = max
        self.precision = precision

    def __eq__(self, other):
        return isinstance(other,AttributeConfiguration) and \
               self.type == other.type and \
               self.length == other.length and \
               self.min == other.min and \
               self.max == other.max and \
               self.precision == other.precision

    def _putField(self, requestObject, fieldName, value):
        if value is not None:
            requestObject[fieldName] = str(value)

    @classmethod
    def parse(cls, jsonObject):
        result = AttributeConfiguration(type=decodeField(jsonObject["type"],str))
        decodeObject(jsonObject,result,{"type":str,"length":int, "min":int, "max":int, "precision":int})
        return result

    def toRequestObject(self):
        requestObject = {
            "type": self.type
        }
        self._putField(requestObject, "length",self.length)
        self._putField(requestObject, "min", self.min)
        self._putField(requestObject, "max", self.max)
        self._putField(requestObject, "precision", self.precision)
        return requestObject