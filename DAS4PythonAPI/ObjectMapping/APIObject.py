from abc import ABCMeta

from DAS4PythonAPI.Util import decodeField, encodeField


class APIObject(metaclass=ABCMeta):
    '''
    Abstract Object representing a model used by Rest API
    '''
    def __new__(cls, *args, **kwargs):
        instance = object.__new__(cls)
        instance._field_mapping = None
        return instance

    def _setup(self, field_mapping):
        '''
        Setup the APIObject using field mapping details provided
        :param field_mapping: details on mappings between JSON object fields and  Python Class (model) fields
        :return: 
        '''
        self._field_mapping = field_mapping
        for k,v in field_mapping.items():
            setattr(self,k,v.default_value)

    def __eq__(self, other):
        '''
        Compare equality between two API Objects
        :param other: 
        :return: 
        '''
        if type(self) != type(other):
            return False
        for k,v in self._field_mapping.items():
            if(getattr(self,k,v.default_value) != getattr(other,k,v.default_value)):
                return False
        return True

    def toJSONObject(self):
        '''
        Obtain JSON object of the APIObject
        :return: 
        '''
        result = {}
        for k,v in self._field_mapping.items():
            if(v.addDefaultField or getattr(self,k,v.default_value) != v.default_value):
                result[k] = encodeField(getattr(self,k,v.default_value),v.encode_function)
        return result

    def _parse(self, jsonObject):
        '''
        Obtain APIObject using JSONObject
        :param jsonObject: 
        :return: 
        '''
        for k,v in self._field_mapping.items():
            if k in jsonObject.keys():
                setattr(self,k,decodeField(jsonObject[k],v.decode_function))
            else:
                setattr(self,k,v.default_value)
