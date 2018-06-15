from django.test import TestCase

from .models import Address


class HomePageTest(TestCase):

    def test_uses_index_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'addresses/index.html')


class AddressModelTest(TestCase):

    def test_can_add_address_to_database_and_fusion_tables(self):
        address1 = Address(lat=-17.8251657, lng=31.033510000000003, address="Herbert Chitepo Ave, Harare, Zimbabwe")

    def test_does_not_accept_unnamed_address(self):
        address2 = Address(lat=-17.957160658802813, lng=31.12964037109373, address="Unnamed Road, Zimbabwe")


    def test_does_not_accept_duplicate_address(self):
        address3 = Address(lat=-17.8251657, lng=31.033510000000003, address="Herbert Chitepo Ave, Harare, Zimbabwe")
        address4 = Address(lat=-17.8251657, lng=31.033510000000003, address="Herbert Chitepo Ave, Harare, Zimbabwe")

    def test_can_reset_database_and_fusion_tables(self):
        pass
