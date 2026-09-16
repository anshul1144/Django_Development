from django.http import HttpResponse

from django.shortcuts import render

def home(request):
    user={
        'name': 'Anshul',
        'id ': 103 ,
        'qulification': 'B.Tech',
        'Profession': 'Software Engineer',
        'project': 'Django Development'
    }
    
    
    return render(request, 'home.html', {'name': user['name'], 'id ': user['id '], 'qulification': user['qulification'], 'Profession': user['Profession'], 'project': user['project']})
def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')