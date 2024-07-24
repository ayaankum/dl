from django.urls import path 
from . import views 
  
urlpatterns = [ 
     path('', views.current_datetime, name='current_datetime'), 
     path('time/plus/<int:offset>/', views.hours_ahead, name='hours_ahead'), 
 ] 