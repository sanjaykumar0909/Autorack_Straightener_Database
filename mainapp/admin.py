from django.contrib import admin

# Register your models here.
from .models import Component, CsvFileData, CsvFileInfo
admin.site.register(Component)
admin.site.register(CsvFileInfo)
admin.site.register(CsvFileData)