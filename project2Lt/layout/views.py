from django.shortcuts import render
def home(request):
    return render(request, 'events/home.html')
def about_us(request):
    return render(request, 'events/about_us.html')
def contact_us(request):
    return render(request, 'events/contact_us.html')