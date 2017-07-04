class AttributeConfiguration(object):
    def __init__(self, type, min=None, max=None, length=None, precision=None):
        self.type = type
        self.length = length
        self.min = max
        self.max = max
        self.precision = precision

    def _putField(self, requestObject, fieldName, value):
        if value is not None:
            requestObject[fieldName] = str(value)

    def toRequestObject(self):
        requestObject = {
            "type": self.type
        }
        self._putField(requestObject, "length",self.length)
        self._putField(requestObject, "min", self.min)
        self._putField(requestObject, "max", self.max)
        self._putField(requestObject, "precision", self.precision)
        return requestObject