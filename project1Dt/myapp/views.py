from django.http import HttpResponse 
from datetime import datetime, timedelta 
  
def current_datetime(request): 
    now = datetime.now() 
    html = f'<html><body><h1>Current Date and Time:</h1><p>{now}</p></body></html>' 
    return HttpResponse(html) 

def hours_ahead(request, offset): 
     offset = int(offset) 
     dt = datetime.now() + timedelta(hours=offset) 
     html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt) 
     return HttpResponse(html)