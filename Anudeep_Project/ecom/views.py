from django.http import HttpResponse

from django.shortcuts import render

def home(request):
    user = {
        'name':'jos', 
        'id':101,
        'qualification':'MCA',
        'projects':['video player', 'gps', 'find nearest blood bank']
    }
    return render(request, "home.html", user)

def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "services.html")

