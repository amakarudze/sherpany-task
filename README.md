# maps-addresses
This is an app that enables you to get addresses of clicked places and saves
them to an sqlite database and Google Fusion Table.

## Tutorial
This section of the documentation is aimed at a newcomer to [maps-addresses](https://github.com/amakarudze/sherpany-task).
It is designed to help one get started quickly. The tutorial will take you step-by-step through some key aspects of
this work. It is not intended to explain the topics in depth but provide you with a good idea of what it’s possible
to achieve in just a few steps, and how to go about it.

Once you’re familiar with the basics presented in the tutorial, you will find the more in-depth coverage of the
same topics in the **How-to** section.

The tutorials follow a logical progression, starting from installation so it is recommended to work through them in
the order presented here.

### Prerequisites
This is app requires the following to run:
 - Python 3.6+
 - Django 1.9
 - Google Developer Account
 - Google Maps API Key
 - Google Fusion Tables API Key
 - Geckodriver for running functional tests with Selenium and Mozilla Firefox browser.

### Installation
Clone or download this repository, create and activate a virtual environment. Install required packages
in your virtual environment using the command:

 `pip install -r requirements.txt`

If you are new to Django, you can learn  more on Python and Django installation from the
  [Django Girls Tutorial](https://tutorial.djangogirls.org/en/installation/).

### Setting up the project
The project is designed to run with one model `Address` which is in `models.py` of `addresses` module. To have this
 model working, you need to run migrations by running these commands:

 `python manage.py makemigrations`

 `python manage.py migrate`

### Adding Google Maps and Google Fusion Table API Keys
Create API keys for [Google Maps](https://developers.google.com/maps/documentation/javascript/get-api-key) and
[Google Fusion Tables](https://developers.google.com/fusiontables/docs/v1/using#APIKey) and update
`YOUR_KEY` values in `templates/addresses/index.html` file.

If you do not have a separate developer account with [Google](https://mail.google.com), it maybe necessary that
you sign up for one that you will use to work with Google Fusion Tables so that you do not risk losing your data.
Visit [this link](https://support.google.com/fusiontables/answer/184641?hl=en) for more information on how to get started with
[Google Fusion Tables](https://support.google.com/fusiontables/answer/184641?hl=en) if you are new to them.

### Testing
To check that the project is properly run tests by running the functional tests in `functional_tests.py` and units tests
in `addresses/tests.py`. To run functional tests, [Mozilla Firefox](https://www.mozilla.org/firefox/) and
[Geckodriver](https://github.com/mozilla/geckodriver/releases) driver for Mozilla Firefox are required.
To install in your project, follow the instructions
[here](https://www.obeythetestinggoat.com/book/pre-requisite-installations.html#_installing_django_and_selenium).

To run first activate your virtualenv and run the following commands:

- To run functional tests, run:

`python functional_tests.py`

- To run unit tests, run:

`python manage.py test`


## How-to Guides
### Create a Google Fusion Table
To create a Google Fusion Table, follow the [Google Fusion Tables tutorial](https://support.google.com/fusiontables/answer/184641?hl=en). Rename your fields in the table to `latitude`,
 `longitude` and `location` and hide the `date` field as it is not necesary for the project. Set the following
 data types for the fields:
 - `longitude` - `Number`.
 - `latitude` -  set Type to `Location` and check `Two-column location`. Set the values of `Latitude` to `latitude`
 and `Longitude` to `longitude`.
 - `location` - set type to `Text`.

### Customise model

### Customise JSON data to be saved from map

### Save location data to sqlite database

### Save location data to Google Fusion Table

### Reset database and Google Fusion Table

### Testing

## Explanation
### How the app works

## Reference

