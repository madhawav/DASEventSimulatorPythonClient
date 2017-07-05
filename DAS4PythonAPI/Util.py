def encodeField(value, encode_function=str):
    if value is None:
        return None
    return encode_function(value)

def decodeField(value, type):
    if value is None:
        return None
    return type(value)

def decodeObject(jsonObject,target, decodeMap):
    for (key,value) in jsonObject.items():
        setattr(target, key,decodeField(value, decodeMap[key]))
    return target