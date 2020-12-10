from django.shortcuts import render
from django.http import HttpResponse
import sys, os, csv


def index(request):
    
    return HttpResponse("Hello world. You're at the library index")


# Create your views here.
