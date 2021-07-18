from django.http import HttpResponse

from datetime import datetime
import json

def server_time(request):
    now = datetime.now()
    current_time = '{}{}'.format('Current server time is ',now)
    return HttpResponse(current_time)

def numbers(request):
    sorted_numbers = sorted([int(i) for i in request.GET['numbers'].split(',')])  
    data = {
        'status': 'ok',
        'numbers': sorted_numbers,
        'message': 'Integers sorted successfully'
    }
    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')

def say_hi(request, name, age):
    if age<12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello, {}! Welcome to PyBook'.format(name)
    return HttpResponse(message)
    