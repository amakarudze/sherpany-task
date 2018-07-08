from django.test import TestCase
from django.core.exceptions import ValidationError

from .models import Address


class HomePageTest(TestCase):

    def test_uses_index_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'addresses/index.html')

    def test_can_add_address_to_database(self):
        address1 = Address.objects.create(lat=-17.8251657, lon=31.033510000000003,
                                          address="Herbert Chitepo Ave, Harare, Zimbabwe")
        response = self.client.get('/')
        self.assertContains(response, address1.address)
        self.assertContains(response, address1.lat)
        self.assertContains(response, address1.lon)


class AddressModelTest(TestCase):
    def test_string_representation(self):
        address5 = Address.objects.create(lat=-17.8251657, lon=31.033510000000003,
                                          address="Herbert Chitepo Ave, Harare, Zimbabwe")
        self.assertEqual(str(address5), address5.address)

    def test_does_not_accept_unnamed_address(self):
        with self.assertRaises(ValidationError):
            address2 = Address.objects.create(lat=-17.957160658802813, lon=31.12964037109373,
                                              address="Unnamed Road, Zimbabwe")

    def test_does_not_accept_duplicate_address(self):
        address3 = Address.objects.create(lat=-17.8251657, lon=31.033510000000003,
                                          address="Herbert Chitepo Ave, Harare, Zimbabwe")
        with self.assertRaises(Exception) as raised:
            address4 = Address.objects.create(lat=-17.8251657, lon=31.033510000000003,
                                              address="Herbert Chitepo Ave, Harare, Zimbabwe")

    def test_can_reset_database(self):
        address1 = Address.objects.create(lat=-17.8251657, lon=31.033510000000003,
                                          address="Herbert Chitepo Ave, Harare, Zimbabwe")
        Address.objects.all().delete()
        response = self.client.get('/')
        self.assertNotContains(response, address1.address)

