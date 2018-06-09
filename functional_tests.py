import unittest
import time
import json
import sys
import requests

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_click_on_map_and_address_address(self):
        # Edina has heard about a cool new reverse geocoding address app. She goes
        # to check out its homepage.
        self.browser.get('http://localhost:8000')

        # She notices that the page title and header mentions a map and addresses.
        self.assertIn('Maps & Addresses', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Maps & Addresses', header_text)

        # She is invited to click on the map and get the address of the clicked
        # location.
        my_map = self.browser.find_element_by_id('map')

        # She notices the heading below shows a list of addresses.
        heading_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Addresses of clicked locations', heading_text)

        # She clicks on the map and the app looks up the address of clicked location.
        ActionChains(self.browser).move_to_element(my_map).click(my_map).perform()


        # She notices the page refreshes and the address is listed below on the list
        # of addresses.
        time.sleep(1)

        # She notices a marker appear on the map on the location she clicked.

        # She clicks again on another part of the map. This time the app cannot find
        # the address of the clicked location. The app informs her this and she notices
        # nothing is added to the list of addresses.

        # She again clicks on the map and notices another address added and a marker is
        # also added to the page.

        # She decides to reset the page and start again.

        # Satisfied, she closes the app to re-visit it again later.

if __name__ == '__main__':
    unittest.main(warnings='ignore')