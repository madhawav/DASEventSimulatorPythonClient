import unittest

import logging
from time import sleep

from DAS4PythonAPI.EventSimulator.AttributeConfiguration import AttributeConfiguration
from DAS4PythonAPI.EventSimulator.EventSimulatorClient import EventSimulatorClient
from DAS4PythonAPI.EventSimulator.FeedSimulationConfiguration import FeedSimulationConfiguration
from DAS4PythonAPI.EventSimulator.SimulationSource import SimulationSource
from DAS4PythonAPI.EventSimulator.SingleSimulationConfiguration import SingleSimulationConfiguration

logging.basicConfig(level=logging.INFO)


class EventSimulatorTests(unittest.TestCase):
    def setUp(self):
        self.hostUrl = "http://localhost:9090"
        self.simulationUrl = self.hostUrl + "/simulation"
        logging.info("Prior to launching tests, make sure DAS 4 is running at " + self.hostUrl)

    def testSingleSimulation(self):
        logging.info("Test: Simulating a Single Event")
        eventSimulatorClient = EventSimulatorClient(self.simulationUrl)

        singleSimulationConfiguration = SingleSimulationConfiguration("TestSiddhiApp","FooStream",[None, 9, 45])

        self.assertTrue(eventSimulatorClient.simulateSingleEvent(singleSimulationConfiguration))
        logging.info("Successfully Simulated Single Event")


    def testSaveDeleteSimulationFeedConfiguration(self):
        logging.info("Test1: Saving and Deleting simulation feed configuration")
        eventSimulatorClient = EventSimulatorClient(self.simulationUrl)

        svr = FeedSimulationConfiguration("simulationPrimitive")
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

    def testEditSimulationFeedConfiguration(self):
        logging.info("Test1: Saving, Editing and Deleting simulation feed configuration")
        eventSimulatorClient = EventSimulatorClient(self.simulationUrl)

        svr = FeedSimulationConfiguration("simulationPrimitive")
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
        sleep(5)

        svr.properties.simulationName = "simulationNewName"
        self.assertTrue(eventSimulatorClient.editSimulationFeedConfiguration("simulationPrimitive",svr))
        logging.info("Successfully Editted Simulation Feed Configuration")
        sleep(5)

        self.assertTrue(eventSimulatorClient.deleteSimulationFeedConfiguration("simulationNewName"))
        logging.info("Successfully Deleted Simulation Feed Configuration")


    def testRetrieveSimulationFeedConfiguration(self):
        logging.info("Test1: Saving, Retrieving and Deleting simulation feed configuration")
        eventSimulatorClient = EventSimulatorClient(self.simulationUrl)

        svr = FeedSimulationConfiguration("simulationPrimitive")
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

        sleep(5)
        response = eventSimulatorClient.retrieveSimulationFeedConfiguration("simulationPrimitive")
        # NOTE: Unable to proceed since JSON Response sent from DAS has an invalid message field
        # {"status":"OK","message":"Simulation configuration : {\"sources\":[{\"timeStampInterval\":\"5\",\"simulationType\":\"RANDOM_DATA_SIMULATION\",\"attributeConfiguration\":[{\"length\":\"10\",\"type\":\"PRIMITIVE_BASED\"},{\"min\":\"30000\",\"max\":\"30000\",\"precision\":\"2\",\"type\":\"PRIMITIVE_BASED\"},{\"min\":\"300\",\"max\":\"300\",\"type\":\"PRIMITIVE_BASED\"}],\"streamName\":\"FooStream\",\"siddhiAppName\":\"TestSiddhiApp\"}],\"properties\":{\"timestampStartTime\":\"1488615136958\",\"simulationName\":\"simulationPrimitive\",\"timeInterval\":\"1000\",\"timestampEndTime\":null,\"noOfEvents\":\"8\"}}"}
        # Simulation configuration should be placed within inverted commas

        sleep(5)
        self.assertTrue(eventSimulatorClient.deleteSimulationFeedConfiguration("simulationPrimitive"))
        logging.info("Successfully Deleted Simulation Feed Configuration")


if __name__ == '__main__':
    unittest.main()
