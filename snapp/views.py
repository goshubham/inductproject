from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json
import requests
from .services import ConnDet
import logging
from .services import *

# Standard Logger for project
stdlogg = logging.getLogger(name= 'mylog')
stdlogg2 = logging.getLogger(name= 'mylogfordebug')
stdlogg2.debug(msg='-------------------------------------------------------------------------------')

# Create your views here.
@login_required(login_url="login/")
def logi(request):
    try:
        configServiceNowInstance()
        stdlogg.info('Viewing Dashboard')
        return render(request, "home.html")
    except Exception as e:
        stdlogg.info('Unsuccessful attempt (check logs)')
        stdlogg2.debug(e.__str__())
        return render(request , "error.html")


########################################################################################################################
@login_required(login_url="login/")
def listall(request):
    try:
        #logging.error('hey there') worked
        dictOfList = getConnectSnList()
        #stdlogg2.debug(msg="Not working debug")
        stdlogg.info(msg= 'Listing all incidents')

        #stdlogg.warning(msg= 'isuue with listing')
        return render(request, "list.html", {'instancelist': dictOfList})
    except requests.ConnectionError as e:
        stdlogg2.debug(e.__str__())
        #stdlogg.warning(msg= 'isuue with listing')
        return render(request, "error.html", {'error': 'ConnectionError'})


#######################################################################################################################


@login_required(login_url="login/")
def incidentdet(request, sys_id):
    try:
        dictOfDetails = getConnectDetail(sys_id)
        stdlogg.info(msg= 'Getting information about incident')
        return render(request, 'incidet.html', {'instancedetaildict': dictOfDetails})

    except requests.ConnectionError as e:
        stdlogg2.debug(e.strerror)
        stdlogg.info(msg='Failed to get information about incident')
        return render(request, 'error.html', {'error': 'ConnectionError'})


######################################################################################################################
@login_required(login_url="login/")
def createinc(request):
    stdlogg.info(msg='Need some info to create your incident')
    return render(request, 'createinc.html')


@login_required(login_url="login/")
def createdinc(request):
    try:
        name = request.POST['nameinci']
        describe = request.POST['descriptioninci']
        butt = request.POST['buttcreate']
        #print(butt)
        #print(describe)
        stdlogg.info(msg='got the info to create incident')
        createincident(name, describe)
        stdlogg.info(msg='Incident creation completed...')
        return render(request, 'creation.html')

    except Exception as e:
        stdlogg2.debug(msg= e.__str__())
        stdlogg.info(msg='creation failed...')
        return render(request, "error.html", {'error': 'ConnectionError'})

######################################################################################################################
@login_required(login_url="login/")
def updateinc(request):
    try:
        dictOfList = getConnectSnList()
        stdlogg.info('Select incident to update...')
        return render(request, "update.html", {'instancelist': dictOfList})
    except Exception as e:
        stdlogg2.debug('updation failed...'+ e.__str__())
        stdlogg.info('worng while selecting incident to update')
        return render(request, "error.html", {'error': 'ConnectionError'})


@login_required(login_url="login/")
def getUpdateDetail(request):
    try:
        name = request.POST['nameinci']
        idofinci = request.POST['idinci']
        describe = request.POST['descriptioninci']

        stdlogg.info(msg='processing info for updation')
        finalupdate(idofinci, describe, name)
        stdlogg.info(msg='updation completed sucessfully')
        dictOfList = getConnectSnList()
        return render(request, 'list.html', {'instancelist': dictOfList})

    except Exception as e:
        stdlogg2.debug('failed to update or retrieving info after updation '+ e.__str__())
        stdlogg.info('worng while upadting')
        return render(request, "error.html", {'error': 'ConnectionError'})

@login_required(login_url="login/")
def update_select(request, number):
    sys_id = request.POST['but']
    stdlogg.info(msg='getting upadtion info from user')
    return render(request, 'updateform.html', {'sys_id': sys_id, 'name': number})


#######################################################################################################################
@login_required(login_url="login/")
def deleteinc(request):
    try:
        dictOfList = getConnectSnList()
        stdlogg.info(msg='selecting incident to be deleted')
        return render(request, "delete.html", {'instancelist': dictOfList})

    except Exception as e:
        stdlogg2.debug('failed to delete'+ e.__str__())
        stdlogg.info(msg='problem while deletion')
        return render(request, "error.html", {'error': 'ConnectionError'})


@login_required(login_url="login/")
def delete_select(request):
    try:
        sys_id = request.POST['but']
        stdlogg.info(msg='got the sys_id and deletion started')
        finaldelete(sys_id)
        dictOfList = getConnectSnList()
        stdlogg.info(msg='Deletion completed')
        return render(request, "delete.html", {'instancelist': dictOfList})

    except Exception as e:
        stdlogg2.debug('failed to delete selected'+e.__str__())
        stdlogg.info('failed to delete selected incident')
        return render(request, "error.html", {'error': 'ConnectionError'})

