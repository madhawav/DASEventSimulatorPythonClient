import os
import unittest

import logging
from time import sleep

from debian.debian_support import readLinesSHA1

from DAS4PythonAPI.SiddhiAppManagement.SiddhiAppManagerClient import SiddhiAppManagerClient

logging.basicConfig(level=logging.INFO)


resources_path = os.path.dirname(__file__) + "/resources/"


class EventSimulatorTests(unittest.TestCase):
    def setUp(self):
        self.hostUrl = "http://localhost:9090"
        self.simulationUrl = self.hostUrl + "/siddhi-apps"
        logging.info("Prior to launching tests, make sure DAS 4 is running at " + self.hostUrl)

    def testRetrieveSiddhiAppStatus(self):
        logging.info("Test1: Retrieving a Siddhi App Status")
        siddhiAppManagerClient = SiddhiAppManagerClient(self.simulationUrl)

        status = siddhiAppManagerClient.retrieveStatusSiddhiApp("TestSiddhiApp")

        self.assertEqual(status,"active")

    def testRetrieveSiddhiApp(self):
        logging.info("Test1: Retrieving a Siddhi App")
        siddhiAppManagerClient = SiddhiAppManagerClient(self.simulationUrl)

        app = siddhiAppManagerClient.retrieveSiddhiApp("TestSiddhiApp")

        lines = []
        with open(resources_path + "/TestSiddhiApp.siddhi","rb") as f:
            lines = [line.decode() for line in f.readlines()]

        target_app = "".join(lines)

        logging.info(target_app)

        logging.info(app)
        self.assertEqual(app,target_app)


    def testListSiddhiApps(self):
        logging.info("Test1: Save, List Siddhi Apps and Delete")
        siddhiAppManagerClient = SiddhiAppManagerClient(self.simulationUrl)

        lines = []
        with open(resources_path + "/TestSiddhiApp1.siddhi", "rb") as f:
            lines = [line.decode() for line in f.readlines()]

        siddhiApp = "".join(lines)

        result = siddhiAppManagerClient.saveSiddhiApp(siddhiApp)
        self.assertTrue(result)

        sleep(5)

        apps = siddhiAppManagerClient.listSiddhiApps()
        self.assertTrue("TestSiddhiApp1" in apps)
        logging.info(apps)

        apps = siddhiAppManagerClient.listSiddhiApps(isActive=True)
        self.assertTrue("TestSiddhiApp1" in apps)
        logging.info(apps)

        apps = siddhiAppManagerClient.listSiddhiApps(isActive=False)
        self.assertTrue("TestSiddhiApp1" not in apps)
        logging.info(apps)

        siddhiAppManagerClient = SiddhiAppManagerClient(self.simulationUrl)

        result = siddhiAppManagerClient.deleteSiddhiApp("TestSiddhiApp1")
        self.assertTrue(result)




    def testSaveAndDeleteSiddhiApp(self):
        logging.info("Test1: Save and Delete Siddhi App")
        siddhiAppManagerClient = SiddhiAppManagerClient(self.simulationUrl)

        lines = []
        with open(resources_path + "/TestSiddhiApp1.siddhi", "rb") as f:
            lines = [line.decode() for line in f.readlines()]

        siddhiApp = "".join(lines)

        result = siddhiAppManagerClient.saveSiddhiApp(siddhiApp)
        self.assertTrue(result)


        sleep(5)

        siddhiAppManagerClient = SiddhiAppManagerClient(self.simulationUrl)

        result = siddhiAppManagerClient.deleteSiddhiApp("TestSiddhiApp1")
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
