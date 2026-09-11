from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world!")

def about(request):
    return HttpResponse("This is the about page.")

def contact(request):
    return HttpResponse("This is the contact page.")

def services(request):
    return HttpResponse("This is the services page.")
