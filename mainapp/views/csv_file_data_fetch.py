import django.http
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from ..models import CsvFileData as Cfd
import json

def index(request: django.http.HttpRequest)-> HttpResponse:
    csv_file_serial_num= int(request.GET["id"])
    db_data= Cfd.objects.get(pk= csv_file_serial_num).bend_data
    return render(request, "csv_file_data.html", {"db_data": [db_data]})
