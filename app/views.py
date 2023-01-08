from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('data that has to be responded')


def second(request):
    return HttpResponse('<h1>second data has to be responded</h1>')


def third(request):
    return HttpResponse('<h1><marquee>third data has to be responded</marquee></h1>')


def forth(requet):
    return HttpResponse('<h1>Ganesh</h1>')