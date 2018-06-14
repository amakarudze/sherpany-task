import sys
import json

from django.shortcuts import render

from .models import Address


def validate_address():
    pass


def home_page(request):
    address_list = Address.objects.all()
    return render(request, 'addresses/index.html', {'address_list': address_list,})


def reset_map():
    pass