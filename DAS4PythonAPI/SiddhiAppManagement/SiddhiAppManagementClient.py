from enum import Enum

from DAS4PythonAPI.__Communication.RestClient import RestClient

class UpdateAppStatusResponse(Enum):
    '''
    Response from WSO2 DAS on updateSidhdiApp call of SiddhiAppManagementClient.
    '''
    savedNew=201,
    updated=200

class SiddhiAppManagementClient(RestClient):
    '''
    Client for Siddhi App Management (publish, edit, list, retrieve etc.) in WSO2 DAS.
    '''
    def __init__(self, siddhi_apps_url):
        '''
        Instantiates SiddhiAppMangementClient. 
        :param siddhi_apps_url: url to siddhi_apps endpoint (e.g. root_url + '/siddhi-apps')
        '''
        RestClient.__init__(self,siddhi_apps_url)

    def retrieveSiddhiApp(self, siddhiAppName):
        '''
        Retrieve siddhiApp stored in WSO2 DAS.
        :param siddhiAppName: 
        :return: 
        '''
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
        '''
        Deletes a SiddhiApp stored in WSO2 DAS.
        :param siddhiAppName: 
        :return: 
        '''
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
        '''
        Retrieve the status of a SiddhiApp in WSO2 DAS.
        :param siddhiAppName: 
        :return: 
        '''
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
        '''
        Obtains the list of Siddhi Apps in WSO2 DAS.
        :param isActive: 
        :return: 
        '''
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
        '''
        Updates a Siddhi App in WSO2 DAS.
        :param siddhiApp: 
        :return: 
        '''
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
        '''
        Saves a Siddhi App to WSO2 DAS.
        :param siddhiApp: 
        :return: 
        '''
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