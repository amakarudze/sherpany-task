from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect

from .models import Address


def add_address(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        lat = request.POST.get('lat')
        lng = request.POST.get('lng')
        Address.create(lat, lng, address)

    else:
        data = 'Save failed'
    return JsonResponse(data)


def home_page(request):
    address_list = Address.objects.all()
    return render(request, 'addresses/index.html', {'address_list': address_list,})


def reset_map(request):
    Address.objects.all().delete()
    return HttpResponseRedirect('index')
