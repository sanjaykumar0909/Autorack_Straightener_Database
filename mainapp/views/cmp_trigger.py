from ..models import Component as Cmp
from django.http import HttpResponse
from datetime import datetime
def handle(request):
    trigger= int(request.GET["id"])
    try:
        latest= Cmp.objects.latest("component_serial_num")
    except Exception as e:
        latest= None
        print(e)
    if (trigger==1):
        if latest is None or latest.end_time is not None:
            Cmp(start_time= datetime.now()).save()
        else:
            return HttpResponse("successive start_time trigger", status=400)
    else:
        if latest is None or latest.end_time is not None:
            return HttpResponse("successive end_time trigger", status=400)
        else:
            latest.end_time= datetime.now()

