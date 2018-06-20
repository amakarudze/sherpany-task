from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.core import serializers

from .models import Address


def home_page(request):
    address_list = Address.objects.all()
    return render(request, 'addresses/index.html', {'address_list': address_list,})


def add_address(request):
    location = request.POST.get('postdata')
    for deserialized_object in serializers.deserialize("json", location):
        data = {
            'is_duplicate': Address.objects.filter(address__iexact=deserialized_object.address).exists(),
            'has_no_address': 'Unnamed Road' in deserialized_object.address
        }
        if data['is_duplicate']:
            data['error_message'] = 'The address has already been saved. Duplicates are not allowed.'
        elif data['has_no_address']:
            data['error_message'] = 'Location does not have an address and cannot be saved.'
        else:
            Address.objects.create(address=deserialized_object.address,
                                   lat=float(deserialized_object.lat),
                                   lng=float(deserialized_object.lng))
    return JsonResponse(data)


def reset_map(request):
    Address.objects.all().delete()
    return HttpResponseRedirect('index')
