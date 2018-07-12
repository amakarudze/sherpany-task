import urllib3, urllib.parse, httplib2
import requests
from datetime import datetime

from django.views.generic.list import ListView
from django.http import JsonResponse, HttpResponseRedirect
from rest_framework.parsers import JSONParser

from .models import Address
from .forms import AddressForm
from .serializers import AddressSerializer


class HomeView(ListView):
    template_name = 'addresses/index.html'
    queryset = Address.objects.all()
    form = AddressForm

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['title'] = 'Home'
        context['year'] = datetime.now().year
        return context

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            data = JSONParser().parse(request)
            serializer = AddressSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                requests.post(
                    'https://www.google.com/fusiontables/query?sql=INSERT INTO 1FM7o8dlxWT5BxBoK-UC0-h_oFCuuH9-3wcxh7KM6'
                    '({lat, lon, address}) VALUES (serializer.data)&key=AIzaSyDA6r1mrmzhCnZVX5gtB_RT45Ab4sKMkBE')
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)


def reset_map(request):
    Address.objects.all().delete()
    return HttpResponseRedirect('/')
