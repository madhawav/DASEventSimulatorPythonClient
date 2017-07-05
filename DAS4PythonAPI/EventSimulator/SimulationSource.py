from DAS4PythonAPI.EventSimulator.AttributeConfiguration import AttributeConfiguration
from DAS4PythonAPI.Util import encodeField, decodeField, decodeObject


class SimulationSource(object):
    def __init__(self, simulationType=None, streamName=None, siddhiAppName=None, timeStampInterval=5, attributeConfiguration=[]):
        self.simulationType = simulationType
        self.streamName = streamName
        self.siddhiAppName = siddhiAppName
        self.timeStampInterval = timeStampInterval
        self.attributeConfiguration = attributeConfiguration

    def __eq__(self, other):
        return isinstance(other,SimulationSource) and \
               self.simulationType == other.simulationType and \
               self.streamName == other.streamName and \
               self.siddhiAppName == other.siddhiAppName and \
               self.timeStampInterval == other.timeStampInterval and \
               self.attributeConfiguration == other.attributeConfiguration

    @classmethod
    def parse(cls, jsonObject):
        result = SimulationSource()
        # if "simulationType" in jsonObject.keys():
        #     result.simulationType = decodeField(jsonObject["simulationType"],str)
        # if "streamName" in jsonObject.keys():
        #     result.streamName = decodeField(jsonObject["streamName"],str)
        # if "siddhiAppName" in jsonObject.keys():
        #     result.siddhiAppName = decodeField(jsonObject["siddhiAppName"],str)
        # if "timestampInterval" in jsonObject.keys():
        #     result.timeStampInterval = decodeField(jsonObject["timeStampInterval"],int)

        def decodeAttribs(jsonObject):
            return_object = []
            for attrib in jsonObject:
                return_object.append(decodeField(attrib,AttributeConfiguration.parse))
            return return_object
        decodeObject(jsonObject, result,
                     {"simulationType": str, "streamName": str, "siddhiAppName": str, "timeStampInterval": int, "attributeConfiguration":decodeAttribs})
        return result



    def toRequestObject(self):
        attribs = []
        for attrbConfig in self.attributeConfiguration:
            attribs.append(attrbConfig.toRequestObject())
        return {
            "simulationType": encodeField(self.simulationType),
            "streamName": encodeField(self.streamName),
            "siddhiAppName": encodeField(self.siddhiAppName),
            "timeStampInterval": encodeField(self.timeStampInterval),
            "attributeConfiguration": attribs
        }