import json
import sys
import requests

from django.test import TestCase

from .models import Address


class HomePageTest(TestCase):

    def test_uses_index_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'addresses/index.html')
