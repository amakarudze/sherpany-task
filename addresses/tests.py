from django.test import TestCase

from .models import Address


class HomePageTest(TestCase):

    def test_uses_index_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'addresses/index.html')


class AddressModelTest(TestCase):

    def test_can_add_address_to_database_and_fusion_tables(self):
        address1 = Address()

    def test_does_not_accept_unnamed_address(self):
        address2 = Address()

    def test_does_not_accept_duplicate_address(self):
        address3 = Address()
        address4 = Address()

    def test_can_reset_database_and_fusion_tables(self):
        pass
