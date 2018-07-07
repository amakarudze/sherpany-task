import json
from datetime import datetime

from django.views.generic import TemplateView
from django.http import JsonResponse, HttpResponseRedirect

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
        addresses = Address.objects.all()
        serializer = AddressSerializer(addresses, many=True)
        context['address_list'] = JsonResponse(serializer.data, safe=False)
        return context

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            data = json.loads(request.body)
            serializer = AddressSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)

def reset_map(request):
    Address.objects.all().delete()
    return HttpResponseRedirect('/')
