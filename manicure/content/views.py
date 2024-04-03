from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def masters(request):
    return render(request, 'masters.html')