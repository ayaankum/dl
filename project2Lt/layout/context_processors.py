from django.conf import settings

def global_settings(request):
    return {
        'developer': settings.DEVELOPER_NAME,
        'year': settings.CURRENT_YEAR, 
    }