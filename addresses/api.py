# API endpoint
from rest_framework.viewsets import ModelViewSet

from .serializers import AddressSerializer
from .models import Address


class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
