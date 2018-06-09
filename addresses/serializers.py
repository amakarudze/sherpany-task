# serializer class for Address to make it available through the Rest API.

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Address


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = '__all__'
        # validate and ensure an address is entered only once
        validators = [
            UniqueTogetherValidator(
                queryset=Address.objects.all(),
                fields=('long_name', 'formatted_address', 'location')
            )
        ]