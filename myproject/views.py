#from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html',{})
   # return HttpResponse('Hello welcome home')


def about(request):
    return render(request, 'about.html')
    #return HttpResponse('this is my about page')

def contact(request):
    return render(request, 'contact.html')







#def videos(request):
   # return render(request, 'videos.html')