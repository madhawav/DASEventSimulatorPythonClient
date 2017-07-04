from DAS4PythonAPI.Util import encodeField


class SimulationSource(object):
    def __init__(self):
        self.simulationType = "RANDOM_DATA_SIMULATION"
        self.streamName = "FooStream"
        self.siddhiAppName = "TestSiddhiApp"
        self.timeStampInterval = 5
        self.attributeConfiguration = []

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