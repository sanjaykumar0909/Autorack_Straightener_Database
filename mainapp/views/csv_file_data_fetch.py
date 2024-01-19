import django.http
from django.http import JsonResponse
from ..models import CsvFileData as Cfd
import json

def index(request: django.http.HttpRequest)-> JsonResponse:
    csv_file_serial_num= int(request.GET["id"])
    db_data= Cfd.objects.get(pk= csv_file_serial_num).bend_data
    result= json.loads(db_data)
    return JsonResponse([result], safe= False)
