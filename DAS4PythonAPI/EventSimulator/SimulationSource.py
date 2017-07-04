from DAS4PythonAPI.Util import encodeField


class SimulationSource(object):
    def __init__(self, simulationType=None, streamName=None, siddhiAppName=None, timeStampInterval=5, attributeConfiguration=[]):
        self.simulationType = simulationType
        self.streamName = streamName
        self.siddhiAppName = siddhiAppName
        self.timeStampInterval = timeStampInterval
        self.attributeConfiguration = attributeConfiguration

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