from django.http import HttpResponse

from datetime import datetime

def server_time(request):
    now = datetime.now()
    current_time = '{}{}'.format('Current server time is ',now)
    return HttpResponse(current_time)