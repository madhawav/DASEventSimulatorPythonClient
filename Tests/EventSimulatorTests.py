import unittest

import logging
import os
from time import sleep

from DAS4PythonAPI.EventSimulator.AttributeConfiguration import AttributeConfiguration
from DAS4PythonAPI.EventSimulator.EventSimulatorClient import EventSimulatorClient
from DAS4PythonAPI.EventSimulator.FeedSimulationConfiguration import FeedSimulationConfiguration
from DAS4PythonAPI.EventSimulator.SimulationProperties import SimulationProperties
from DAS4PythonAPI.EventSimulator.SimulationSource import SimulationSource
from DAS4PythonAPI.EventSimulator.SingleSimulationConfiguration import SingleSimulationConfiguration

logging.basicConfig(level=logging.INFO)

resources_path = os.path.dirname(__file__) + "/resources/"

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

    def testCSVUploadAndDelete(self):
        logging.info("Test: Uploading and Deleting a CSV.")
        eventSimulatorClient = EventSimulatorClient(self.simulationUrl)

        self.assertTrue(eventSimulatorClient.uploadCSV("sample.csv",path=resources_path+"sample.csv"))
        logging.info("Successfully Uploaded CSV")

        sleep(5)

        self.assertTrue(eventSimulatorClient.deleteCSV("sample.csv"))
        logging.info("Successfully Deleted CSV")


    def testCSVUpdate(self):
        logging.info("Test: Uploading, Updating and Deleting a CSV.")
        eventSimulatorClient = EventSimulatorClient(self.simulationUrl)

        self.assertTrue(eventSimulatorClient.uploadCSV("sample.csv",path=resources_path+"sample.csv"))
        logging.info("Successfully Uploaded CSV")

        sleep(5)

        self.assertTrue(eventSimulatorClient.updateCSV("sample.csv","sample2.csv", path=resources_path + "sample.csv"))
        logging.info("Successfully Uploaded CSV")

        sleep(5)

        self.assertTrue(eventSimulatorClient.deleteCSV("sample2.csv"))
        logging.info("Successfully Deleted CSV")


    def testSaveDeleteSimulationFeedConfiguration(self):
        logging.info("Test1: Saving and Deleting simulation feed configuration")
        eventSimulatorClient = EventSimulatorClient(self.simulationUrl)

        svr = FeedSimulationConfiguration("simulationPrimitive")
        svr.properties.timestampStartTime = 1488615136958
        svr.properties.timestampEndTime = None
        svr.properties.noOfEvents = 8
        svr.properties.timeInterval = 1000

        sm1 = SimulationSource(simulationType=SimulationSource.Type.RANDOM_DATA_SIMULATION, streamName="FooStream", siddhiAppName="TestSiddhiApp", timestampInterval=5)

        sm1.attributeConfiguration.append(AttributeConfiguration(AttributeConfiguration.Type.PRIMITIVE_BASED, length=10))
        sm1.attributeConfiguration.append(AttributeConfiguration(AttributeConfiguration.Type.PRIMITIVE_BASED, min=35000, max=30000, precision=2))
        sm1.attributeConfiguration.append(AttributeConfiguration(AttributeConfiguration.Type.PRIMITIVE_BASED, min=150, max=300))

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

        sm1 = SimulationSource(simulationType=SimulationSource.Type.RANDOM_DATA_SIMULATION, streamName="FooStream", siddhiAppName="TestSiddhiApp", timestampInterval=5)

        sm1.attributeConfiguration.append(AttributeConfiguration(AttributeConfiguration.Type.PRIMITIVE_BASED, length=10))
        sm1.attributeConfiguration.append(AttributeConfiguration(AttributeConfiguration.Type.PRIMITIVE_BASED, min=35000, max=30000, precision=2))
        sm1.attributeConfiguration.append(AttributeConfiguration(AttributeConfiguration.Type.PRIMITIVE_BASED, min=150, max=300))

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

        sm1 = SimulationSource(simulationType=SimulationSource.Type.RANDOM_DATA_SIMULATION, streamName="FooStream", siddhiAppName="TestSiddhiApp", timestampInterval=5)

        sm1.attributeConfiguration.append(AttributeConfiguration(AttributeConfiguration.Type.PRIMITIVE_BASED, length=10))
        sm1.attributeConfiguration.append(AttributeConfiguration(AttributeConfiguration.Type.PRIMITIVE_BASED, min=35000, max=30000, precision=2))
        sm1.attributeConfiguration.append(AttributeConfiguration(AttributeConfiguration.Type.PRIMITIVE_BASED, min=150, max=300))

        svr.sources.append(sm1)

        self.assertTrue(eventSimulatorClient.saveSimulationFeedConfiguration(svr), "Unable to Save "
                                                                                   "SimulationConfiguration")

        sleep(5)
        retrieveObject = eventSimulatorClient.retrieveSimulationFeedConfiguration("simulationPrimitive")
        self.assertTrue(retrieveObject == svr, "Retrieved SimulationConfigurations does not match")

        sleep(5)
        self.assertTrue(eventSimulatorClient.deleteSimulationFeedConfiguration("simulationPrimitive"),"Unable to delete"
                                                                                            "SimulationConfiguration")


    def testRandomSimulationCustomList(self):
        logging.info("Test: Random Simulation using Custom List")
        eventSimulatorClient = EventSimulatorClient(self.simulationUrl)

        svr = FeedSimulationConfiguration("sim")
        svr.properties.timestampStartTime = 1488615136958
        svr.properties.timestampEndTime = 1488615136998
        svr.properties.noOfEvents = 5
        svr.properties.timeInterval = 1000

        s1 = SimulationSource(simulationType=SimulationSource.Type.RANDOM_DATA_SIMULATION)
        s1.streamName = "FooStream"
        s1.siddhiAppName = "TestSiddhiApp"
        s1.timestampInterval = 5
        svr.sources.append(s1)

        s1.attributeConfiguration.append(
            AttributeConfiguration(type=AttributeConfiguration.Type.CUSTOM_DATA_BASED,list=["WSO2,AAA","DDD","IBM"]))
        s1.attributeConfiguration.append(
            AttributeConfiguration(type=AttributeConfiguration.Type.CUSTOM_DATA_BASED, list=[1.0,2.0,3.0]))
        s1.attributeConfiguration.append(
            AttributeConfiguration(type=AttributeConfiguration.Type.CUSTOM_DATA_BASED, list=[10, 20, 30]))

        self.assertTrue(eventSimulatorClient.saveSimulationFeedConfiguration(svr))
        logging.info("Successfully Saved Simulation Feed Configuration")

        sleep(5)

        self.assertTrue(eventSimulatorClient.deleteSimulationFeedConfiguration(svr.properties.simulationName))
        logging.info("Successfully Deleted Simulation Feed Configuration")

    def testCSVSimulationSingleSource(self):
        logging.info("Test: CSV Simulation - One Source")
        eventSimulatorClient = EventSimulatorClient(self.simulationUrl)

        svr = FeedSimulationConfiguration("simulation1")
        svr.properties.timestampStartTime = None
        svr.properties.timeInterval = 8000

        s1 = SimulationSource(simulationType=SimulationSource.Type.CSV_SIMULATION)
        s1.streamName = "FooStream"
        s1.siddhiAppName = "TestSiddhiApp"
        s1.fileName = "sample.csv"
        s1.timestampInterval = 1000
        s1.isOrdered = True
        s1.delimiter = ","
        svr.sources.append(s1)

        self.assertTrue(eventSimulatorClient.uploadCSV("sample.csv", path=resources_path + "sample.csv"))
        logging.info("Successfully Uploaded CSV")

        sleep(5)

        self.assertTrue(eventSimulatorClient.saveSimulationFeedConfiguration(svr))
        logging.info("Successfully Saved Simulation Feed Configuration")

        sleep(5)

        self.assertTrue(eventSimulatorClient.deleteSimulationFeedConfiguration(svr.properties.simulationName))
        logging.info("Successfully Deleted Simulation Feed Configuration")

        self.assertTrue(eventSimulatorClient.deleteCSV("sample.csv"))
        logging.info("Successfully Deleted CSV")


    def testCSVSimulationTwoSource(self):
        logging.info("Test: CSV Simulation - Two Source")
        eventSimulatorClient = EventSimulatorClient(self.simulationUrl)

        svr = FeedSimulationConfiguration("simCSV2")
        svr.properties.timestampStartTime = 1488615136957
        svr.properties.timestampEndTime = 1488615136973
        svr.properties.noOfEvents = 7
        svr.properties.timeInterval = 1000

        s1 = SimulationSource(simulationType=SimulationSource.Type.CSV_SIMULATION)
        s1.streamName = "FooStream"
        s1.siddhiAppName = "TestSiddhiApp"
        s1.fileName = "sample.csv"
        s1.timestampAttribute=0
        s1.isOrdered = True
        s1.delimiter = ","
        svr.sources.append(s1)

        s2 = SimulationSource(simulationType=SimulationSource.Type.CSV_SIMULATION)
        s2.streamName = "FooStream"
        s2.siddhiAppName = "TestSiddhiApp"
        s2.fileName = "sample.csv"
        s2.timestampAttribute = 0
        s2.isOrdered = True
        s2.delimiter = ","
        svr.sources.append(s2)

        self.assertTrue(eventSimulatorClient.uploadCSV("sample.csv", path=resources_path + "sample.csv"))
        logging.info("Successfully Uploaded CSV")

        sleep(5)

        self.assertTrue(eventSimulatorClient.saveSimulationFeedConfiguration(svr))
        logging.info("Successfully Saved Simulation Feed Configuration")

        sleep(5)

        self.assertTrue(eventSimulatorClient.deleteSimulationFeedConfiguration(svr.properties.simulationName))
        logging.info("Successfully Deleted Simulation Feed Configuration")

        self.assertTrue(eventSimulatorClient.deleteCSV("sample.csv"))
        logging.info("Successfully Deleted CSV")



    def testDBSimulationOneSource(self):
        logging.info("Test: DB Simulation - One Source")

        target = {
          "properties": {
            "simulationName": "simDb",
            "timestampStartTime": "1488615136958",
            "timestampEndTime": None,
            "noOfEvents" : None,
            "timeInterval": "1000"
          },
          "sources": [
            {
              "simulationType": "DATABASE_SIMULATION",
              "streamName": "FooStream",
              "siddhiAppName": "TestSiddhiApp",
              "dataSourceLocation": "jdbc:mysql:\/\/localhost:3306\/DatabaseFeedSimulation",
              "driver" : "com.mysql.jdbc.Driver",
              "username": "root",
              "password": "root",
              "tableName": "foostream3",
              "timestampInterval": "1000",
              "columnNamesList": None
            }
          ]
        }

        eventSimulatorClient = EventSimulatorClient(self.simulationUrl)

        svr = FeedSimulationConfiguration("simDb")
        svr.properties.timestampStartTime = 1488615136958
        svr.properties.timestampEndTime = None
        svr.properties.noOfEvents = None
        svr.properties.timeInterval = 1000

        s1 = SimulationSource(simulationType=SimulationSource.Type.DATABASE_SIMULATION)
        s1.streamName = "FooStream"
        s1.siddhiAppName = "TestSiddhiApp"
        s1.dataSourceLocation = "jdbc:mysql:\/\/localhost:3306\/DatabaseFeedSimulation"
        s1.driver="com.mysql.jdbc.Driver"
        s1.username="root"
        s1.password="root"
        s1.tableName="foostream3"
        s1.timestampInterval=1000
        s1.columnNamesList=None
        svr.sources.append(s1)

        match = svr.toJSONObject()

        self.assertDictEqual(target,match)

        self.assertTrue(eventSimulatorClient.saveSimulationFeedConfiguration(svr))
        logging.info("Successfully Saved Simulation Feed Configuration")

        sleep(5)

        self.assertTrue(eventSimulatorClient.deleteSimulationFeedConfiguration(svr.properties.simulationName))
        logging.info("Successfully Deleted Simulation Feed Configuration")



if __name__ == '__main__':
    unittest.main()
