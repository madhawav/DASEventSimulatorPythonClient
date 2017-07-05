from abc import ABCMeta

from DAS4PythonAPI.Util import decodeField, encodeField


class APIObject(metaclass=ABCMeta):
    def __new__(cls, *args, **kwargs):
        '''Factory method for base/subtype creation. Simply creates an
        (new-style class) object instance and sets a base property. '''
        instance = object.__new__(cls)
        instance._field_mapping = None
        return instance

    def _setup(self, field_mapping):
        self._field_mapping = field_mapping
        for k,v in field_mapping.items():
            setattr(self,k,v.default_value)

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        for k,v in self._field_mapping.items():
            if(getattr(self,k,v.default_value) != getattr(other,k,v.default_value)):
                return False
        return True

    def toJSONObject(self):
        result = {}
        for k,v in self._field_mapping.items():
            result[k] = encodeField(getattr(self,k,v.default_value),v.encode_function)
        return result

    def _parse(self, jsonObject):
        for k,v in self._field_mapping.items():
            if k in jsonObject.keys():
                setattr(self,k,decodeField(jsonObject[k],v.decode_function))
            else:
                setattr(self,k,v.default_value)
