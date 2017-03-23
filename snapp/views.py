from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
import json
import requests
from .services import ConnDet
import logging
from .services import *
from .models import configServiceNow
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ConfigSNSerializer

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


@login_required(login_url="login/")
def listall(request):
    try:
        #logging.error('hey there') worked
        dictOfList = getConnectSnList()
        #stdlogg2.debug(msg="Not working debug")
        stdlogg.info(msg= 'Listing all incidents')

        #stdlogg.warning(msg= 'isuue with listing')
        return render(request, "list.html", {'instancelist': dictOfList})
    except Exception as e:
        stdlogg2.debug(str(e))
        #stdlogg.warning(msg= 'isuue with listing')
        return render(request, "error.html", {'error': str(e)})




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



@login_required(login_url="login/")
def createinc(request):
    stdlogg.info(msg='Need some info to create your incident')
    return render(request, 'createinc.html')




@login_required(login_url="login/")
def createdinc(request):
    try:
        name = request.POST['nameinci']
        short_describe = request.POST['descriptioninci']
        urgency = request.POST['urgencyin']
        catag = request.POST['catainc']
        state = request.POST['stateinc']
        butt = request.POST['buttcreate']
        #print(butt)
        #print(describe)
        stdlogg.info(msg='got the info to create incident')
        createincident(name, short_describe, urgency, catag, state)
        stdlogg.info(msg='Incident creation completed...')
        return render(request, 'creation.html')

    except Exception as e:
        stdlogg2.debug(msg= e.__str__())
        stdlogg.info(msg='creation failed...')
        return render(request, "error.html", {'error': 'ConnectionError'})




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
        urgency = request.POST['urgencyin']
        catag = request.POST['catainc']
        state = request.POST['stateinc']

        stdlogg.info(msg='processing info for updation')
        finalupdate(idofinci, describe, name, urgency, catag, state)
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




# Commit is made before implementing REST framework
#to list all configured instances of Service Now



class SNInstanceConfiguredList(APIView):

    def get(self , request):
        confObjects = configServiceNow.objects.all()
        serial = ConfigSNSerializer(confObjects, many = True)
        stdlogg.info(msg= 'GET request is made to get list of configured SN instances')
        stdlogg2.debug(msg= 'GET request for listing configured SN instances')
        return Response(serial.data)

    def post(self , request):
        serial = ConfigSNSerializer(data= request.data)
        if serial.is_valid():
            serial.save()
            stdlogg.info(msg='POST request to store new SN configurations')
            stdlogg2.debug(msg='POST request to store new SN configurations')
            return Response(serial.data, status= status.HTTP_201_CREATED)

        stdlogg2.debug(msg='POST request failed to store')
        return Response(serial.errors, status= status.HTTP_400_BAD_REQUEST)
