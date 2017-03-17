from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json
import requests
from .services import ConnDet
from .services import *


# Create your views here.
@login_required(login_url="login/")
def logi(request):
    try:
        return render(request, "home.html")
    except Exception:
        return render(request , "error.html")


########################################################################################################################

# print('Status:', response.status_code, 'Headers:', response.headers, 'Response:', response.json())


@login_required(login_url="login/")
def listall(request):
    try:
        dictOfList = getConnectSnList()
        return render(request, "list.html", {'instancelist': dictOfList})
    except Exception as e:
        print("donnn")
        return render(request, "error.html")


#######################################################################################################################


@login_required(login_url="login/")
def incidentdet(request, sys_id):
    dictOfDetails = getConnectDetail(sys_id)
    return render(request, 'incidet.html', {'instancedetaildict': dictOfDetails})


######################################################################################################################
@login_required(login_url="login/")
def createinc(request):
    return render(request, 'createinc.html')


@login_required(login_url="login/")
def createdinc(request):
    name = request.POST['nameinci']
    describe = request.POST['descriptioninci']
    butt = request.POST['buttcreate']
    print(butt)
    print(describe)

    createincident(name, describe)
    return render(request, 'creation.html')


######################################################################################################################
@login_required(login_url="login/")
def updateinc(request):
    dictOfList = getConnectSnList()
    return render(request, "update.html", {'instancelist': dictOfList})


@login_required(login_url="login/")
def getUpdateDetail(request):
    name = request.POST['nameinci']
    idofinci = request.POST['idinci']
    describe = request.POST['descriptioninci']

    finalupdate(idofinci, describe, name)
    dictOfList = getConnectSnList()
    return render(request, 'list.html', {'instancelist': dictOfList})


@login_required(login_url="login/")
def update_select(request, number):
    sys_id = request.POST['but']
    return render(request, 'updateform.html', {'sys_id': sys_id, 'name': number})


#######################################################################################################################
@login_required(login_url="login/")
def deleteinc(request):
    dictOfList = getConnectSnList()
    return render(request, "delete.html", {'instancelist': dictOfList})


@login_required(login_url="login/")
def delete_select(request):
    sys_id = request.POST['but']
    finaldelete(sys_id)
    dictOfList = getConnectSnList()
    return render(request, "delete.html", {'instancelist': dictOfList})
