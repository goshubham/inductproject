import requests
import json
import logging
from snapp.models import configServiceNow

########################################################################################################################
# Connection details
loghttp = logging.getLogger(name='mylogfordebug')

class ConnDet:
    url = 'https://dev20632.service-now.com/api/now/table/incident'
    user = 'admin'
    pwd = 'Qazwsx@123'


def configServiceNowInstance():
    conObj = configServiceNow.objects.get(enable = True)
    ConnDet.url = 'https://' + conObj.host + '.service-now.com/api/now/table/incident'
    ConnDet.user = conObj.username
    ConnDet.pwd = conObj.password
    loghttp.debug('Service Now instance configured successfully with host ' + conObj.host)

def getConnectDetail(sys_id):
    url = ConnDet.url + '/' + sys_id
    user = ConnDet.user
    pwd = ConnDet.pwd

    # Set proper headers
    headers = {"Accept": "application/json"}

    # Do the HTTP request
    response = requests.get(url, auth=(user, pwd), headers=headers)
    if response.status_code != 200:
        loghttp.debug('Response other than 200 in getConnectDetail(sysid) '+ str(response.status_code))
        raise requests.ConnectionError

    # Check for HTTP codes other than 200
    if response.status_code != 200:
        #print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.json())
        exit()

    # Decode the JSON response into a dictionary and use the data
    if response.status_code == 200:
        loghttp.debug('Connection is okk...\n getConnectDetail(sysid)' + str(response.status_code))

    resData = json.dumps(response.json())
    resDataJson = json.loads(resData)

    parseRes = resDataJson['result']
    loghttp.debug('JSON is returned backed from getConnectDetail(sysid)' + str(response.status_code))
    # print(resDataJson)
    return parseRes


# Get the list of all
def getConnectSnList():
    # Set the request parameters
    url = ConnDet.url
    user = ConnDet.user
    pwd = ConnDet.pwd

    # Set proper headers
    headers = {"Accept": "application/json"}
    # Do the HTTP request
    response = requests.get(url, auth=(user, pwd), headers=headers)
    if response.status_code != 200:
        loghttp.debug('Response other than 200 in getConnectSnList()' + str(response.status_code))
        raise requests.ConnectionError

    if response.status_code != 200:
        #print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.json())
        exit()

    # Decode the JSON response into a dictionary and use the data
    if response.status_code == 200:
        loghttp.debug('Connection is okk.... \n getConnectSnList()' + str(response.status_code))
        #print('Status:', response.status_code)

    #print(response.json())
    resData = json.dumps(response.json())
    resDataJson = json.loads(resData)  # result in string error solved

    parseRes = resDataJson['result']
    loghttp.debug('JSON is returned backed from getConnectSnList()' + str(response.status_code))

    return parseRes


# creating new incident
def createincident(name, desc, urgency, catag, state):
    url = ConnDet.url
    user = ConnDet.user
    pwd = ConnDet.pwd

    # Set proper headers
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    postBody = "{'short_description':'" + desc + "','number':'" + name + "','urgency':'"+ urgency +"', 'catagory':'"+ catag +"', 'state':'"+ state +"'}"

    response = requests.post(url, auth=(user, pwd), headers=headers, data=postBody)
    if response.status_code != 201:
        loghttp.debug('failed to create incident check createincident(name, desc)' + str(response.status_code))
        raise requests.ConnectionError

    loghttp.debug('Incident is creating createincident(name, desc)' + str(response.status_code))


def finalupdate(idofinci, desc, name,urgency,catag,state):
    url = ConnDet.url + '/' + idofinci
    user = ConnDet.user
    pwd = ConnDet.pwd

    # Set proper headers
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    postBody = "{'short_description':'" + desc + "','number':'" + name + "','urgency':'"+ urgency +"', 'catagory':'"+ catag +"', 'state':'"+ state +"'}"

    response = requests.put(url, auth=(user, pwd), headers=headers, data=postBody)

    if response.status_code != 200:
        loghttp.debug('Failed to update in finalupdate(idofinci, desc, name)' + str(response.status_code))
        raise requests.ConnectionError

    loghttp.debug('Upadted successfully... finalupdate(idofinci, desc, name)' + str(response.status_code))


def finaldelete(idofinci):
    url = ConnDet.url + '/' + idofinci
    user = ConnDet.user
    pwd = ConnDet.pwd

    # Set proper headers
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    # postBody = "{'short_description':'" + desc + "','number':'" + name + "'}"

    response = requests.delete(url, auth=(user, pwd), headers=headers)
    if response.status_code != 204:
        loghttp.debug('Failed to delete in finaldelete(idofinci)' + str(response.status_code))
        raise requests.ConnectionError
