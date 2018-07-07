import json
from datetime import datetime

from django.views.generic import TemplateView
from django.http import JsonResponse, HttpResponseRedirect
from rest_framework.parsers import JSONParser

from .models import Address
from .forms import AddressForm
from .serializers import AddressSerializer


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
            data = dict(data)
            serializer = AddressSerializer(data=data, many=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            print(serializer.errors)
            return JsonResponse(serializer.errors, status=400)

def reset_map(request):
    Address.objects.all().delete()
    return HttpResponseRedirect('/')
