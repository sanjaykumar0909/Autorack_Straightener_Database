from ..models import Component as Cmp
from django.http import HttpResponse
from datetime import datetime
# handles component trigger inputs
def handle(request):
    trigger= int(request.GET["id"]) # gets trigger input
    try:
        latest= Cmp.objects.latest("component_serial_num") # last component entry based on component_serial_num
    except Exception as e:
        latest= None
        print(e)
    if (trigger==1): # handles start trigger
        if latest is None or latest.end_time is not None:
            Cmp(start_time= datetime.now()).save()
        else:
            return HttpResponse("successive start_time trigger", status=400)
    else:# handles end trigger
        if latest is None or latest.end_time is not None:
            return HttpResponse("successive end_time trigger", status=400)
        else:
            latest.end_time= datetime.now()

