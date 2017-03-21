from django.contrib import admin
from  snapp.models import configServiceNow

# Register your models here.
class ConfigServiceAdmin(admin.ModelAdmin):
    list_display = ["host","username","enable"]
    search_fields = ["host" , "username"]

    class Meta:
        model = configServiceNow

admin.site.register(configServiceNow , ConfigServiceAdmin)