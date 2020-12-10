from django.shortcuts import render
from django.http import HttpResponse
import sys, os, csv


def index(request):
    dictionary = {"books": [{"book1" : "page1"}, {"book2": "page2"}]}
    return render(request, 'library.html', dictionary)


# Create your views here.
