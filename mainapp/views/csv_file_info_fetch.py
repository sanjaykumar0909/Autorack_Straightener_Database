import django.http
from django.http import HttpResponse, JsonResponse, HttpResponseServerError
from ..models import CsvFileInfo as Cfi
from django.views.decorators.csrf import csrf_exempt

comp_serial_num= None

@csrf_exempt
def handle(request):
    data= request.POST
    print('a',data)
    try:
        csv_file_serial_num= data['SerialNo'].strip()
        print('b',csv_file_serial_num)
        if (len(csv_file_serial_num)!=0):
            return by_serialnumber(csv_file_serial_num)
        else:
            return by_timestamp(data)
    except Exception as e:
        print('error occured', e)
        return HttpResponseServerError(str(e).encode())

def by_serialnumber(serialnumber: int)-> django.http.HttpResponse:
    try:
        db_csv_file= Cfi.objects.get(pk=serialnumber)
        send_csv_file_info= dict()
        send_csv_file_info['csv_file_serial_num']= serialnumber
        send_csv_file_info['creation_time']= db_csv_file.creation_time
        send_csv_file_info['x_distance']= db_csv_file.x_distance
        send_csv_file_info['servo_angle']= db_csv_file.servo_angle
        send_csv_file_info['max_deflection']= db_csv_file.max_deflection
        print('c',send_csv_file_info)
        return JsonResponse([send_csv_file_info], safe=False)
    except Exception as e:
        print(e)

def by_timestamp(data)-> django.http.HttpResponse:
    from datetime import datetime
    cmp_serial_num= data['cmpserialno']
    date_from = data['DateFrom']
    date_to = data['DateTo']
    time_from = data['TimeFrom']
    time_to = data['TimeTo']

    # form handling
    if (len(date_from) != 0 or len(date_to) != 0):
        if (len(time_from) == 0):
            start_time = datetime.strptime(f"{date_from}", "%Y-%m-%d")
            end_time = datetime.strptime(f"{date_to}", "%Y-%m-%d")
        else:
            start_time = datetime.strptime(f"{date_from} {time_from}", "%Y-%m-%d %H:%M")
            end_time = datetime.strptime(f"{date_to} {time_to}", "%Y-%m-%d %H:%M")
    else:
        ersp = HttpResponse("Invalid data format for csv_file_info sent to backend", status=400)
        ersp['Content-Type'] = 'text/plain'
        return ersp

    db_csv_files= Cfi.objects\
        .filter(component_serial_num=cmp_serial_num)\
        .filter(creation_time__gt= start_time, creation_time__lt= end_time)
    send_components=[]
    for record in db_csv_files:
        add_dict= dict()
        add_dict["csv_file_serial_num"]= record.csv_file_serial_num
        add_dict["creation_time"]= record.creation_time
        add_dict["x_distance"]= record.x_distance
        add_dict["servo_angle"]= record.servo_angle
        add_dict["max_deflection"]= record.max_deflection
        send_components.append(add_dict)
    print(send_components)
    return JsonResponse(send_components, safe= False)