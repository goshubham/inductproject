from django.db import models

class configServiceNow(models.Model):
    host = models.CharField(unique= True, max_length=20, null= False , blank= False)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    enable = models.BooleanField(default= False)

    def __str__(self):
        return self.host
