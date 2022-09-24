from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse("<h1>heloo world</h1>")
    return render(request, 'pages/index.html')


def about(request):
    #return HttpResponse("About Us") 
    x = 10
    y = -20
    foods = ['tea', 'coffee', 'maggi', 'Roll'] 
    students = {
        'Tom': 80,
        'Jerry': 45,
        'Casper' : 47,
        'spike' : 75,

    }
    context = {
        'var' : x,
        'y' : y,
        'foods' : foods,
        'students' : students
    }  
    return render(request, 'pages/about.html', context)

def contact(request):
    return render(request, 'pages/contact.html')