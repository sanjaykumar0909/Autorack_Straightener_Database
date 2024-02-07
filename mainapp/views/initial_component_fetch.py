import django.http
from django.http import HttpResponse, JsonResponse
from ..models import Component as Cmp
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def handle(request):
    data = request.POST
    print(data)
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
        db_component= Cmp.objects.get(pk= serialnumber) # get data by serial number
        send_components = dict()
        send_components["component_serial_num"]= serialnumber
        send_components["start_time"]= db_component.start_time
        send_components["end_time"]= db_component.end_time
        print([send_components])
        return JsonResponse([send_components], safe=False)
    except Exception as e:
        print(e)
def by_timestamp(data) -> django.http.HttpResponse:
    from datetime import datetime
    # get data requested by user
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
        ersp= HttpResponse("Invalid component data format sent to backend", status=400)
        ersp['Content-Type']= 'text/plain'
        return ersp

    # django ORM query for fetching components by time
    db_components = Cmp.objects.filter(start_time__gt= start_time, end_time__lt= end_time)
    send_components=[]
    for record in db_components:
        add_dict= dict()
        add_dict["component_serial_num"]= record.component_serial_num
        add_dict["start_time"]= record.start_time
        add_dict["end_time"]= record.end_time
        send_components.append(add_dict)
    return JsonResponse(send_components, safe= False)

