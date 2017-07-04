import json

from Communication.RestClient import RestClient


class EventSimulatorClient(RestClient):
    def __init__(self, base_url):
        RestClient.__init__(self,base_url)

    def saveSimulationConfiguration(self, simulationConfiguration):
        r = self._sendPostRequest("/feed",data=json.dumps(simulationConfiguration.toRequestObject()))
        if r.status_code == 201:
            return True
        elif r.status_code == 409:
            raise Exception("EventSimulationConfiguration with same name already exists.")
        else:
            raise Exception(r.status + ": " + r.message)