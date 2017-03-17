import requests
import json


########################################################################################################################
# Connection details
class ConnDet:
    url = 'https://dev20632.service-now.com/api/now/table/incident'
    user = 'admin'
    pwd = 'Qazwsx@123'


def getConnectDetail(sys_id):
    url = ConnDet.url + '/' + sys_id
    user = ConnDet.user
    pwd = ConnDet.pwd

    # Set proper headers
    headers = {"Accept": "application/json"}

    # Do the HTTP request
    response = requests.get(url, auth=(user, pwd), headers=headers)

    # Check for HTTP codes other than 200
    if response.status_code != 200:
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.json())
        exit()

    # Decode the JSON response into a dictionary and use the data
    if response.status_code == 200:
        print('Status:', response.status_code)

    resData = json.dumps(response.json())
    resDataJson = json.loads(resData)

    parseRes = resDataJson['result']
    print('#################')
    # print(resDataJson)
    return parseRes


# Get the list of all
def getConnectSnList():
    # Set the request parameters
    url = ConnDet.url + "g"
    user = ConnDet.user
    pwd = ConnDet.pwd

    # Set proper headers
    headers = {"Accept": "application/json"}
    try:
        # Do the HTTP request
        response = requests.get(url, auth=(user, pwd), headers=headers)
        if (response.status_code != 200):
            raise requests.ConnectionError
    except ConnectionError as c:
        print('*************')

    # Check for HTTP codes other than 200
    if response.status_code != 200:
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.json())
        exit()

    # Decode the JSON response into a dictionary and use the data
    if response.status_code == 200:
        print('Status:', response.status_code)

    # print(str(response.json()))
    resData = json.dumps(response.json())
    resDataJson = json.loads(resData)  # result in string error solved

    parseRes = resDataJson['result']
    # print('**************')
    # print(parseRes)
    # print(resDataJson)
    return parseRes


# creating new incident
def createincident(name, desc):
    url = ConnDet.url
    user = ConnDet.user
    pwd = ConnDet.pwd

    # Set proper headers
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    postBody = "{'short_description':'" + desc + "','number':'" + name + "'}"

    response = requests.post(url, auth=(user, pwd), headers=headers, data=postBody)
    print(response.status_code)


def finalupdate(idofinci, desc, name):
    url = ConnDet.url + '/' + idofinci
    user = ConnDet.user
    pwd = ConnDet.pwd

    # Set proper headers
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    postBody = "{'short_description':'" + desc + "','number':'" + name + "'}"

    response = requests.put(url, auth=(user, pwd), headers=headers, data=postBody)
    print(url)
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print(response.status_code)


def finaldelete(idofinci):
    url = ConnDet.url + '/' + idofinci
    user = ConnDet.user
    pwd = ConnDet.pwd

    # Set proper headers
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    # postBody = "{'short_description':'" + desc + "','number':'" + name + "'}"

    response = requests.delete(url, auth=(user, pwd), headers=headers)
    print(url)
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print(response.status_code)
