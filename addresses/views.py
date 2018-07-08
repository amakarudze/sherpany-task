import urllib3, urllib, simplejson, sys, httplib2
from datetime import datetime

from django.views.generic import TemplateView
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
                return JsonResponse(serializer.data, status=201)
            print(serializer.errors)
            return JsonResponse(serializer.errors, status=400)


def reset_map(request):
    Address.objects.all().delete()
    return HttpResponseRedirect('/')
