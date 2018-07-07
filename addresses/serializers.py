from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
