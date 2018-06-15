from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect

from .models import Address


def validate_address(request):
    address = request.GET.get('address', None)
    data = {
        'is_saved': Address.objects.filter(address__iexact=address).exists()
    }
    if data['is_saved']:
        data['error_message'] = 'Address already exists in the database and Google Fusion Tables.'
    elif "Unnamed Road" in address:
        data['error_message'] = 'The place you clicked does not have an address.'
    else:
        address = request.GET.get('address')
        lat = request.GET.get('lat')
        lng = request.GET.get('lng')
        Address.create(lat, lng, address)
    return JsonResponse(data)


def home_page(request):
    address_list = Address.objects.all()
    return render(request, 'addresses/index.html', {'address_list': address_list,})


def reset_map(request):
    Address.objects.all().delete()
    return HttpResponseRedirect('index')
