from django.contrib import admin
from . import models
#from apps.auto.models import Auto
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class AutoCategoria(resources.ModelResource):
    class Meta:
        model = models.Auto
        import_id_fields =('idpbv',)

class DataAuto(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields =['idpbv']
    list_display =('idpbv', 'marca', 'modelo', 'cc', 'especificaciones')
    resource_class = AutoCategoria

admin.site.register(models.Auto, DataAuto)