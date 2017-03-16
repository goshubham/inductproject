from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json
import requests

# Create your views here.
@login_required(login_url="login/")
def logi(request):
    return render(request,"home.html")

##################################################################################################################################################
# Connection details
class ConnDet:
    url = 'https://dev20632.service-now.com/api/now/table/incident'
    user = 'admin'
    pwd = 'Qazwsx@123'

# Get Connection
def getConnectSnList():
    # Set the request parameters
    url = 'https://dev20632.service-now.com/api/now/table/incident'
    user = 'admin'
    pwd = 'Qazwsx@123'

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

    # print(str(response.json()))
    resData = json.dumps(response.json())
    resDataJson = json.loads(resData) # result in string error solved

    parseRes = resDataJson['result']
    #print('**************')
    #print(parseRes)
    #print(resDataJson)
    return parseRes

    # print('Status:', response.status_code, 'Headers:', response.headers, 'Response:', response.json())


@login_required(login_url="login/")
def listall(request):
    dictOfList = getConnectSnList()
    return render(request, "list.html", { 'instancelist': dictOfList })

#######################################################################################################################
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
        #print('*************')

    resData = json.dumps(response.json())
    resDataJson = json.loads(resData)

    parseRes = resDataJson['result']
    print('#################')
    #print(resDataJson)
    return parseRes

@login_required(login_url="login/")
def incidentdet(request,sys_id):
    dictOfDetails = getConnectDetail(sys_id)
    return render(request, 'incidet.html',{ 'instancedetaildict': dictOfDetails })