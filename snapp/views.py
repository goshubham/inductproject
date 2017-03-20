from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json
import requests
from .services import ConnDet
import logging
from .services import *

# Standard Logger for project
stdlogg = logging.getLogger(name= 'mylog')

# Create your views here.
@login_required(login_url="login/")
def logi(request):
    try:
        stdlogg.info('Login Successful')
        return render(request, "home.html")
    except Exception as e:
        stdlogg.info('Login Unsuccessful')
        stdlogg.debug(e.__str__())
        return render(request , "error.html")


########################################################################################################################
@login_required(login_url="login/")
def listall(request):
    try:
        #logging.error('hey there')
        dictOfList = getConnectSnList()
        stdlogg.debug(msg= 'Listing all incidents')
        return render(request, "list.html", {'instancelist': dictOfList})
    except Exception as e:
        stdlogg.debug(e.__str__())
        return render(request, "error.html", {'error': 'ConnectionError'})


#######################################################################################################################


@login_required(login_url="login/")
def incidentdet(request, sys_id):
    try:
        dictOfDetails = getConnectDetail(sys_id)
        return render(request, 'incidet.html', {'instancedetaildict': dictOfDetails})
    except Exception as e:
        print(e.__str__())
        return render(request, "error.html", {'error': 'ConnectionError'})


######################################################################################################################
@login_required(login_url="login/")
def createinc(request):
    return render(request, 'createinc.html')


@login_required(login_url="login/")
def createdinc(request):
    try:
        name = request.POST['nameinci']
        describe = request.POST['descriptioninci']
        butt = request.POST['buttcreate']
        print(butt)
        print(describe)
        createincident(name, describe)
        return render(request, 'creation.html')

    except Exception as e:
        print(e.__str__())
        return render(request, "error.html", {'error': 'ConnectionError'})

######################################################################################################################
@login_required(login_url="login/")
def updateinc(request):
    try:
        dictOfList = getConnectSnList()
        return render(request, "update.html", {'instancelist': dictOfList})
    except Exception as e:
        print(e.__str__())
        return render(request, "error.html", {'error': 'ConnectionError'})


@login_required(login_url="login/")
def getUpdateDetail(request):
    try:
        name = request.POST['nameinci']
        idofinci = request.POST['idinci']
        describe = request.POST['descriptioninci']

        finalupdate(idofinci, describe, name)
        dictOfList = getConnectSnList()
        return render(request, 'list.html', {'instancelist': dictOfList})

    except Exception as e:
        print(e.__str__())
        return render(request, "error.html", {'error': 'ConnectionError'})

@login_required(login_url="login/")
def update_select(request, number):
    sys_id = request.POST['but']
    return render(request, 'updateform.html', {'sys_id': sys_id, 'name': number})


#######################################################################################################################
@login_required(login_url="login/")
def deleteinc(request):
    try:
        dictOfList = getConnectSnList()
        return render(request, "delete.html", {'instancelist': dictOfList})

    except Exception as e:
        print(e.__str__())
        return render(request, "error.html", {'error': 'ConnectionError'})


@login_required(login_url="login/")
def delete_select(request):
    try:
        sys_id = request.POST['but']
        finaldelete(sys_id)
        dictOfList = getConnectSnList()
        return render(request, "delete.html", {'instancelist': dictOfList})

    except Exception as e:
        print(e.__str__())
        return render(request, "error.html", {'error': 'ConnectionError'})

