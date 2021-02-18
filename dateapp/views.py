from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.
import datetime as dt
date=dt.datetime.now()
def dateview(request):
    x='The current Date and time is {}'.format(date)
    return HttpResponse(x)

