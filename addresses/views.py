import urllib3, urllib.parse, httplib2
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
                http = httplib2.Http()
                url = 'https://www.googleapis.com/fusiontables/v2/tables/1FM7o8dlxWT5BxBoK-UC0-h_oFCuuH9-3wcxh7KM6'
                body = serializer.data
                headers = {'Content-type': 'application/json'}
                response, content = http.request(url, 'POST', headers=headers, body=urllib.parse.urlencode(body))
                return JsonResponse(serializer.data, status=201)
            print(serializer.errors)
            return JsonResponse(serializer.errors, status=400)


def reset_map(request):
    Address.objects.all().delete()
    return HttpResponseRedirect('/')
