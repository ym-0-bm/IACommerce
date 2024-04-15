from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime


def base(request):
    return render(request, "test.html")
