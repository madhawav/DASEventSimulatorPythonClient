import unittest

import logging

from DAS4PythonAPI.EventSimulator.AttributeConfiguration import AttributeConfiguration
from DAS4PythonAPI.EventSimulator.EventSimulatorClient import EventSimulatorClient
from DAS4PythonAPI.EventSimulator.SimulationConfiguration import SimulationConfiguration
from DAS4PythonAPI.EventSimulator.SimulationSource import SimulationSource

logging.basicConfig(level=logging.INFO)


class EventSimulatorTests(unittest.TestCase):
    def setUp(self):
        self.hostUrl = "http://localhost:9090"
        self.simulationUrl = self.hostUrl + "/simulation"
        logging.info("Prior to launching tests, make sure DAS 4 is running at " + self.hostUrl)

    def testSaveSimulationConfiguration(self):
        logging.info("Test1: Saving simulation configuration")
        eventSimulatorClient = EventSimulatorClient(self.simulationUrl)

        svr = SimulationConfiguration("simulationPrimitive")
        svr.properties.timestampStartTime = 1488615136958
        svr.properties.timestampEndTime = None
        svr.properties.noOfEvents = 8
        svr.properties.timeInterval = 1000

        sm1 = SimulationSource()
        sm1.simulationType = "RANDOM_DATA_SIMULATION"
        sm1.streamName = "FooStream"
        sm1.siddhiAppName = "TestSiddhiApp"
        sm1.timeStampInterval = 5

        sm1.attributeConfiguration.append(AttributeConfiguration("PRIMITIVE_BASED", length=10))
        sm1.attributeConfiguration.append(AttributeConfiguration("PRIMITIVE_BASED", min=35000, max=30000, precision=2))
        sm1.attributeConfiguration.append(AttributeConfiguration("PRIMITIVE_BASED", min=150, max=300))

        svr.sources.append(sm1)

        self.assertTrue(eventSimulatorClient.saveSimulationConfiguration(svr))


if __name__ == '__main__':
    unittest.main()
