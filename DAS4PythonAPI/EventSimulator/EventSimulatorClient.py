import json
import logging

from DAS4PythonAPI.Communication.RestClient import RestClient


class EventSimulatorClient(RestClient):
    def __init__(self, base_url):
        RestClient.__init__(self,base_url)

    def saveSimulationFeedConfiguration(self, simulationConfiguration):
        r = self._sendPostRequest("/feed",data=json.dumps(simulationConfiguration.toRequestObject()))
        if r.status_code == 201:
            return True
        elif r.status_code == 409:
            raise Exception("EventSimulationConfiguration with same name already exists.")
        else:
            raise Exception(str(r.status_code) + ": " + r.text)


    def editSimulationFeedConfiguration(self, simulationName,simulationConfiguration):
        r = self._sendPutRequest("/feed/"+simulationName,data=json.dumps(simulationConfiguration.toRequestObject()))
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
            logging.info("Received: " + r.text)
            result = r.json()
            if result["status"].lower() == "ok":
                data = json.loads(result["message"])
                return data
            else:
                raise Exception("Respose says not ok")
        elif r.status_code == 404:
            raise Exception("EventSimulationConfiguration with specified name does not exist.")
        else:
            raise Exception(str(r.status_code)  + ": " + r.text)

    def simulateSingleEvent(self, singleSimulationConfiguration):
        logging.info("Sending: " + json.dumps(singleSimulationConfiguration.toRequestObject()))
        r = self._sendPostRequest("/single", data=json.dumps(singleSimulationConfiguration.toRequestObject()))
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