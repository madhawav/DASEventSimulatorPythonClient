import unittest

import logging

from DAS4PythonAPI.EventSimulator.AttributeConfiguration import AttributeConfiguration
from DAS4PythonAPI.EventSimulator.EventSimulatorClient import EventSimulatorClient
from DAS4PythonAPI.EventSimulator.SimulationFeedConfiguration import SimulationFeedConfiguration
from DAS4PythonAPI.EventSimulator.SimulationSource import SimulationSource

logging.basicConfig(level=logging.INFO)


class EventSimulatorTests(unittest.TestCase):
    def setUp(self):
        self.hostUrl = "http://localhost:9090"
        self.simulationUrl = self.hostUrl + "/simulation"
        logging.info("Prior to launching tests, make sure DAS 4 is running at " + self.hostUrl)

    def testSaveDeleteSimulationFeedConfiguration(self):
        logging.info("Test1: Saving and Deleting simulation feed configuration")
        eventSimulatorClient = EventSimulatorClient(self.simulationUrl)

        svr = SimulationFeedConfiguration("simulationPrimitive")
        svr.properties.timestampStartTime = 1488615136958
        svr.properties.timestampEndTime = None
        svr.properties.noOfEvents = 8
        svr.properties.timeInterval = 1000

        sm1 = SimulationSource(simulationType="RANDOM_DATA_SIMULATION", streamName="FooStream", siddhiAppName="TestSiddhiApp", timeStampInterval=5)

        sm1.attributeConfiguration.append(AttributeConfiguration("PRIMITIVE_BASED", length=10))
        sm1.attributeConfiguration.append(AttributeConfiguration("PRIMITIVE_BASED", min=35000, max=30000, precision=2))
        sm1.attributeConfiguration.append(AttributeConfiguration("PRIMITIVE_BASED", min=150, max=300))

        svr.sources.append(sm1)

        self.assertTrue(eventSimulatorClient.saveSimulationFeedConfiguration(svr))
        logging.info("Successfully Saved Simulation Feed Configuration")
        self.assertTrue(eventSimulatorClient.deleteSimulationFeedConfiguration("simulationPrimitive"))
        logging.info("Successfully Deleted Simulation Feed Configuration")


if __name__ == '__main__':
    unittest.main()
