import sys
import json

from django.shortcuts import render


def reverse_geolocation():
    pass


def home_page(request):
    return render(request, 'addresses/index.html')


