import json
from enum import Enum

from DAS4PythonAPI.__Communication.RestClient import RestClient

class UpdateAppStatusResponse(Enum):
    savedNew=201,
    updated=200

class SiddhiAppManagerClient(RestClient):
    def __init__(self, siddhi_apps_url):
        RestClient.__init__(self,siddhi_apps_url)

    def retrieveSiddhiApp(self, siddhiAppName):
        r = self._sendGetRequest("/" + siddhiAppName)
        if r.status_code == 200:
            result = r.json()
            if "content" in result.keys():
                siddhiApp = result["content"]
                return siddhiApp
            else:
                raise Exception("No content defined in response")
        elif r.status_code == 404:
            raise Exception("Siddhi App with specified name does not exist.")
        else:
            raise Exception(str(r.status_code)  + ": " + r.text)


    def deleteSiddhiApp(self, siddhiAppName):
        r = self._sendDeleteRequest("/" + siddhiAppName)
        if r.status_code == 200:
            return True
        elif r.status_code == 400:
            raise Exception("Siddhi App name provided is invalid.")
        elif r.status_code == 404:
            raise Exception("Siddhi App with specified name does not exist.")
        elif r.status_code == 500:
            raise Exception(str(r.status_code)  + ": " + r.text)
        else:
            raise Exception(str(r.status_code)  + ": " + r.text)


    def retrieveStatusSiddhiApp(self, siddhiAppName):
        r = self._sendGetRequest("/" + siddhiAppName + "/status")
        if r.status_code == 200:
            result = r.json()
            if "status" in result.keys():
                status = result["status"]
                return status
            else:
                raise Exception("No content defined in response")
        elif r.status_code == 404:
            raise Exception("Siddhi App with specified name does not exist.")
        else:
            raise Exception(str(r.status_code)  + ": " + r.text)

    def listSiddhiApps(self, isActive=None):
        params = None
        if isActive is not None:
            params = {"isActive":isActive}
        r = self._sendGetRequest("/",params=params)
        if r.status_code == 200:
            result = r.json()
            return result
        else:
            raise Exception(str(r.status_code) + ": " + r.text)

    def updateSiddhiApp(self, siddhiApp):
        r = self._sendPutRequest("/", data=siddhiApp)
        if r.status_code == 200 or r.status_code == 201:
            result = r.json()
            if result["type"] == "success":
                if r.status_code == 200:
                    return UpdateAppStatusResponse.updated
                elif r.status_code == 201:
                    return UpdateAppStatusResponse.savedNew
            else:
                raise Exception("Result 'type' not 'success'")
        elif r.status_code == 400:
            raise Exception("A validation error occured.")
        elif r.status_code == 500:
            raise Exception("An unexpected error occured.")
        else:
            raise Exception(str(r.status_code) + ": " + r.text)

    def saveSiddhiApp(self, siddhiApp):
        r = self._sendPostRequest("/",data=siddhiApp)
        if r.status_code == 201:
            result = r.json()
            if result["type"] == "success":
                return True
            else:
                raise Exception("Result 'type' not 'success'")
        elif r.status_code == 400:
            raise Exception("A validation error occured.")
        elif r.status_code == 409:
            raise Exception("A Siddhi Application with the given name already exists.")
        elif r.status_code == 500:
            raise Exception("An unexpected error occured.")
        else:
            raise Exception(str(r.status_code) + ": " + r.text)