from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect

from .models import Address


def validate_address(request):
    pass


def home_page(request):
    address_list = Address.objects.all()
    return render(request, 'addresses/index.html', {'address_list': address_list,})


def reset_map(request):
    Address.objects.all().delete()
    return HttpResponseRedirect('index')
