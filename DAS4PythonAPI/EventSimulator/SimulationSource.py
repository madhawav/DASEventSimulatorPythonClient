from DAS4PythonAPI.EventSimulator.AttributeConfiguration import AttributeConfiguration
from DAS4PythonAPI.ObjectMapping.APIObject import APIObject
from DAS4PythonAPI.ObjectMapping.FieldMapping import FieldMapping, ListFieldMapping


class SimulationSource(APIObject):
    def __init__(self, simulationType=None, streamName=None, siddhiAppName=None, timeStampInterval=5, attributeConfiguration=[]):
        self._setup(field_mapping={"simulationType": FieldMapping(str), "streamName": FieldMapping(str),
                                   "siddhiAppName": FieldMapping(str), "timeStampInterval": FieldMapping(int),
                                   "attributeConfiguration": ListFieldMapping(AttributeConfiguration.parse,AttributeConfiguration.toRequestObject)})
        self.simulationType = simulationType
        self.streamName = streamName
        self.siddhiAppName = siddhiAppName
        self.timeStampInterval = timeStampInterval
        self.attributeConfiguration = attributeConfiguration

    @classmethod
    def parse(cls, jsonObject):
        result = SimulationSource()
        result._parse(jsonObject)
        return result

        # if "simulationType" in jsonObject.keys():
        #     result.simulationType = decodeField(jsonObject["simulationType"],str)
        # if "streamName" in jsonObject.keys():
        #     result.streamName = decodeField(jsonObject["streamName"],str)
        # if "siddhiAppName" in jsonObject.keys():
        #     result.siddhiAppName = decodeField(jsonObject["siddhiAppName"],str)
        # if "timestampInterval" in jsonObject.keys():
        #     result.timeStampInterval = decodeField(jsonObject["timeStampInterval"],int)

        # def decodeAttribs(jsonObject):
        #     return_object = []
        #     for attrib in jsonObject:
        #         return_object.append(decodeField(attrib,AttributeConfiguration.parse))
        #     return return_object
        # decodeObject(jsonObject, result,
        #              {"simulationType": str, "streamName": str, "siddhiAppName": str, "timeStampInterval": int, "attributeConfiguration":decodeAttribs})
        # return result



    def toRequestObject(self):
        return self.toJSONObject()
        # attribs = []
        # for attrbConfig in self.attributeConfiguration:
        #     attribs.append(attrbConfig.toRequestObject())
        # return {
        #     "simulationType": encodeField(self.simulationType),
        #     "streamName": encodeField(self.streamName),
        #     "siddhiAppName": encodeField(self.siddhiAppName),
        #     "timeStampInterval": encodeField(self.timeStampInterval),
        #     "attributeConfiguration": attribs
        # }