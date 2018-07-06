import json
from pdb import set_trace

from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse, HttpResponseRedirect
from django.core import serializers

from .models import Address
from .forms import AddressForm


class HomeView(TemplateView):
    template_name = 'addresses/index.html'
    form = AddressForm

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            location_data = json.loads(request.body)
            print(location_data)

            obj = Address()
            obj.lat = location_data[1]
            obj.lng = location_data[2]
            obj.location = location_data[0]
            obj.save()
            data = {
                'message': "Successfully submitted form data."
            }
            return JsonResponse(data)
        else:

            return JsonResponse({"nothing to see": "this isn't happening"})


"""def home_page(request):
    address_list = Address.objects.all()

    return render(request, 'addresses/index.html', {'address_list': address_list,})"""


def add_address(request):
    # set_trace()
    if request.method == 'POST':
        place = request.POST.get('postdata')
        for deserialized_object in serializers.deserialize("json", place):
            data = {
                'is_duplicate': Address.objects.filter(location__iexact=deserialized_object[0]).exists(),
                'has_no_address': 'Unnamed Road' in deserialized_object.address
            }
            if data['is_duplicate']:
                data['error_message'] = 'The address has already been saved. Duplicates are not allowed.'
            elif data['has_no_address']:
                data['error_message'] = 'Location does not have an address and cannot be saved.'
            else:
                Address.objects.create(location=deserialized_object[0],
                                       lat=float(deserialized_object[1]),
                                       lng=float(deserialized_object[2]))
        return JsonResponse(data)
    else:
        return JsonResponse({"nothing to see": "this isn't happening"})


def reset_map(request):
    Address.objects.all().delete()
    return HttpResponseRedirect('index')
