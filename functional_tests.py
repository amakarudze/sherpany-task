from selenium import webdriver
import unittest

browser = webdriver.Firefox()

# Edina has heard about a cool new reverse geocoding address app. She goes
# to check out its homepage.
browser.get('http://localhost:8000')

# She notices that the page title and header mentions a map and addresses.
assert 'Maps & Addresses' in browser.title

# She is invited to click on the map and get the address of the clicked
# location.

# She clicks on the map and the app looks up the address of clicked location.

# She notices the page refreshes and the address is listed below on the list
# of addresses.

# She notices a marker appear on the map on the location she clicked.

# She clicks again on another part of the map. This time the app cannot find
# the address of the clicked location. The app informs her this and she notices
# nothing is added to the list of addresses.

# She again clicks on the map and notices another address added and a marker is
# also added to the page.

# She decides to reset the page and start again.

# Satisfied, she closes the app to re-visit it again later.

browser.quit()
