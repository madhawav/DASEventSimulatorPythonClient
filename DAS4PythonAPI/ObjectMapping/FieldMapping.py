from DAS4PythonAPI.Util import encodeField, decodeField


class FieldMapping(object):
    def __init__(self, decode_function,encode_function=str, default_value=None):
        self.encode_function = encode_function
        self.decode_function = decode_function
        self.default_value = default_value

class ListFieldMapping(FieldMapping):
    def __init__(self, decode_function, encode_function, default_value=[]):
        def encode_func(input_object):
            result_object = []
            for item in input_object:
                result_object.append(encodeField(item,encode_function))
            return result_object

        def decode_func(input_object):
            result_object = []
            for item in input_object:
                result_object.append(decodeField(item,decode_function))
            return result_object
        super().__init__(decode_func,encode_func,default_value)
