from  rest_framework import serializers
from .models import configServiceNow

class ConfigSNSerializer(serializers.ModelSerializer):

    class Meta:
        model = configServiceNow
        fields = ('host' , 'username' , 'enable')
