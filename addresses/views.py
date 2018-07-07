import json
import urllib3, urllib, simplejson, sys, httplib2
from datetime import datetime

from django.views.generic import TemplateView
from django.http import JsonResponse, HttpResponseRedirect
from rest_framework.parsers import JSONParser

from .models import Address
from .forms import AddressForm
from .serializers import AddressSerializer

api_key = "AIzaSyDA6r1mrmzhCnZVX5gtB_RT45Ab4sKMkBE"
table_id = "1FM7o8dlxWT5BxBoK-UC0-h_oFCuuH9-3wcxh7KM6"


class HomeView(TemplateView):
    template_name = 'addresses/index.html'
    form = AddressForm

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['title'] = 'Home'
        context['year'] = datetime.now().year
        context['address_list'] = Address.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            data = JSONParser().parse(request)
            print(data)
            serializer = AddressSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            print(serializer.errors)
            return JsonResponse(serializer.errors, status=400)


def reset_map(request):
    Address.objects.all().delete()
    return HttpResponseRedirect('/')
