import django.http
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from ..models import Component as Cmp
test_response = JsonResponse([
        {
            "name": "1",
            "description": "31/07/2023",
            "price": "29/09/2023"
        },
        {
            "name": "2",
            "description": "31/07/2023",
            "price": "29/09/2023"
        }
    ], safe=False)

def index(request):
    return render(request, 'index.html')

def handle(request):
    data = request.POST

    try:
        serialnumber = data['serialnumber'].strip()
        if (len(serialnumber) != 0):
            return by_serialnumber(int(serialnumber))
        else:
            return by_timestamp(data)
    except Exception as e:
        print(e)
        return HttpResponse("Invalid serial number input")

def by_serialnumber(serialnumber: int) -> django.http.HttpResponse:
    try:
        db_component= Cmp.objects.get(pk= serialnumber)
        send_components = dict()
        send_components["component_serial_num"]= serialnumber
        send_components["start_time"]= db_component.start_time
        send_components["end_time"]= db_component.end_time
        return JsonResponse([send_components], safe=False)
    except Exception as e:
        print(e)
def by_timestamp(data) -> django.http.HttpResponse:
    from datetime import datetime
    date_from= data['datefrom']
    date_to= data['dateto']
    time_from= data['timefrom']
    time_to= data['timeto']

    # form handling
    if (len(date_from) !=0 or len(date_to) !=0):
        if (len(time_from)==0):
            start_time = datetime.strptime(f"{date_from}", "%Y-%m-%d")
            end_time = datetime.strptime(f"{date_to}", "%Y-%m-%d")
        else:
            start_time = datetime.strptime(f"{date_from} {time_from}", "%Y-%m-%d %H:%M")
            end_time = datetime.strptime(f"{date_to} {time_to}", "%Y-%m-%d %H:%M")
    else:
        return HttpResponse("<script>alert('Enter date if you didn't entered serial number')</script>")

    db_components = Cmp.objects.filter(start_time__gt= start_time, end_time__lt= end_time)
    send_components=[]
    for record in db_components:
        add_dict= dict()
        add_dict["component_serial_num"]= record.component_serial_num
        add_dict["start_time"]= record.start_time
        add_dict["end_time"]= record.end_time
        send_components.append(add_dict)
    return JsonResponse(send_components, safe= False)

