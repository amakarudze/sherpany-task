from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import requires_csrf_token


from .models import Address


def home_page(request):
    address_list = None
    return render(request, 'addresses/index.html', {'address_list': address_list,})


def add_address(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        lat = request.POST.get('lat')
        lng = request.POST.get('lng')
        Address.create(lat, lng, address)

    else:
        data = 'Save failed'
    return JsonResponse(data)


def get_addresses():
    data = Address.objects.all()
    return JsonResponse(data)


def reset_map(request):
    Address.objects.all().delete()
    return HttpResponseRedirect('index')
