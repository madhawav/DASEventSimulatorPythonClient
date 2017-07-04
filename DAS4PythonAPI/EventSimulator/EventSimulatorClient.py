import json

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
            raise Exception(r.status + ": " + r.message)

    def deleteSimulationFeedConfiguration(self, simulationName):
        r = self._sendDeleteRequest("/feed/" + simulationName)
        if r.status_code == 200:
            return True
        elif r.status_code == 404:
            raise Exception("EventSimulationConfiguration with specified name does not exist.")
        else:
            raise Exception(r.status + ": " + r.message)