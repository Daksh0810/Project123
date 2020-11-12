from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hi(request):
    return render(request, 'Projectapp/hi.html')


def Statistics(request):
    return render(request, 'Projectapp/Statistics.html')


def Summary(request):
    return render(request, 'Projectapp/Summary.html')
