from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hi(request):
    return render(request, 'Projectapp1/hi.html')


def Statistics(request):
    return render(request, 'Projectapp1/Statistics.html')


def Summary(request):
    return render(request, 'Projectapp1/Summary.html')
