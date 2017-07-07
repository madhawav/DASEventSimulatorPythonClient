import json
import logging

from DAS4PythonAPI.Communication.RestClient import RestClient
from DAS4PythonAPI.EventSimulator.FeedSimulationConfiguration import FeedSimulationConfiguration


class EventSimulatorClient(RestClient):
    def __init__(self, base_url):
        RestClient.__init__(self,base_url)

    def saveSimulationFeedConfiguration(self, simulationConfiguration):
        r = self._sendPostRequest("/feed",data=json.dumps(simulationConfiguration.toJSONObject()))
        if r.status_code == 201:
            return True
        elif r.status_code == 409:
            raise Exception("EventSimulationConfiguration with same name already exists.")
        else:
            raise Exception(str(r.status_code) + ": " + r.text)


    def runSimulationFeedConfiguration(self, simulationConfiguration):
        r = self._sendPostRequest("/feed/" + simulationConfiguration.properties.simulationName + "/?action=run",data=json.dumps(simulationConfiguration.toJSONObject()))
        if r.status_code == 200:
            return True
        elif r.status_code == 404:
            raise Exception("EventSimulationConfiguration with given name does not exist.")
        else:
            raise Exception(str(r.status_code) + ": " + r.text)

    def pauseSimulationFeedConfiguration(self, simulationName):
        r = self._sendPostRequest("/feed/" + simulationName + "/?action=pause")
        if r.status_code == 200:
            return True
        elif r.status_code == 404:
            raise Exception("EventSimulationConfiguration with given name does not exist.")
        else:
            raise Exception(str(r.status_code) + ": " + r.text)

    def resumeSimulationFeedConfiguration(self, simulationName):
        r = self._sendPostRequest("/feed/" + simulationName + "/?action=resume")
        if r.status_code == 200:
            return True
        elif r.status_code == 404:
            raise Exception("EventSimulationConfiguration with given name does not exist.")
        else:
            raise Exception(str(r.status_code) + ": " + r.text)

    def stopSimulationFeedConfiguration(self, simulationName):
        r = self._sendPostRequest("/feed/" + simulationName + "/?action=stop")
        if r.status_code == 200:
            return True
        elif r.status_code == 404:
            raise Exception("EventSimulationConfiguration with given name does not exist.")
        elif r.status_code == 409:
            raise Exception("EventSimulation is already stopped.")
        else:
            raise Exception(str(r.status_code) + ": " + r.text)

    def editSimulationFeedConfiguration(self, simulationName,simulationConfiguration):
        r = self._sendPutRequest("/feed/"+simulationName,data=json.dumps(simulationConfiguration.toJSONObject()))
        if r.status_code == 200:
            return True
        elif r.status_code == 404:
            raise Exception("EventSimulationConfiguration with specified name does not exist.")
        else:
            raise Exception(str(r.status_code) + ": " + r.text)

    def deleteSimulationFeedConfiguration(self, simulationName):
        r = self._sendDeleteRequest("/feed/" + simulationName)
        if r.status_code == 200:
            return True
        elif r.status_code == 404:
            raise Exception("EventSimulationConfiguration with specified name does not exist.")
        else:
            raise Exception(str(r.status_code) + ": " + r.text)

    def retrieveSimulationFeedConfiguration(self, simulationName):
        r = self._sendGetRequest("/feed/" + simulationName)
        if r.status_code == 200:
            result = r.json()
            if result["status"].lower() == "ok":
                jsonObject = json.loads(result["message"])["Simulation configuration"]
                return FeedSimulationConfiguration.parse(jsonObject)
            else:
                raise Exception("Respose says not ok")
        elif r.status_code == 404:
            raise Exception("EventSimulationConfiguration with specified name does not exist.")
        else:
            raise Exception(str(r.status_code)  + ": " + r.text)

    def simulateSingleEvent(self, singleSimulationConfiguration):
        logging.info("Sending: " + json.dumps(singleSimulationConfiguration.toJSONObject()))
        r = self._sendPostRequest("/single", data=json.dumps(singleSimulationConfiguration.toJSONObject()))
        if r.status_code == 200:
            logging.info("Received: " + r.text)
            result = r.json()
            if result["status"].lower() == "ok":
                return True
            else:
                raise Exception("Respose says not ok")
        elif r.status_code == 409:
            raise Exception("EventSimulationConfiguration with same name already exists.")
        else:
            raise Exception(str(r.status_code) + ": " + r.text)

    def uploadCSV(self, fileName, raw=None, path=None):
        files = {}
        if raw is not None:
            files = {"file" : (fileName,raw)}
        else:
            files = {"file" : (fileName,open(path,"rb"))}
        r = self._sendPostRequest("/files",files=files)

        logging.info(r)

        if r.status_code == 201:
            return True
        else:
            raise Exception(str(r.status_code) + ": " + r.text)

    def updateCSV(self, uploadedFileName, newFileName,raw = None, path=None):
        files = {}
        if raw is not None:
            files = {"file": (newFileName, raw)}
        else:
            files = {"file": (newFileName, open(path, "rb"))}
        r = self._sendPutRequest("/files/" + uploadedFileName, files=files)

        logging.info(r)

        if r.status_code == 200:
            return True
        else:
            raise Exception(str(r.status_code) + ": " + r.text)

    def deleteCSV(self, fileName):
        r = self._sendDeleteRequest("/files/" + fileName)
        logging.info(r)

        if r.status_code == 200:
            return True
        else:
            raise Exception(str(r.status_code) + ": " + r.text)






