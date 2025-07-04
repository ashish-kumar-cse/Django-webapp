# views.py

from django.http import HttpResponse
from django.shortcuts import render

print("=== Loaded views.py ===")

def home(request):
    print("Rendering home view")
    return render(request,'index.html')
 #   return HttpResponse("Welcome to the Home page!")

def about(request):
    return render(request,'about.html')
    #return HttpResponse("About Us")
def contact(request):
    return render (request,'contact.html')
    #return HttpResponse("Contact Us")
