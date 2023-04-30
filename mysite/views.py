from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render


def index(request):
    return render(request, 'mysite/index.html')