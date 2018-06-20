# Maps & Addresses API
This is an app that enables you to get addresses of clicked places and saves
them to an Sqlite database and Google Fusion Table.

## Tutorial
### Prerequisites
This is app requires the following to run:
 - Python 3.6+
 - Django 1.9
 - Google Maps API Key
 - Google Fusion Tables API Key

### Installation
Clone or download this repository, create and activate a virtual environment and install required packages
 in your virtual environment using `pip install -r requirements.txt`. If you are new to Django, you can learn
 more on Python and Django installation from the [Django Girls Tutorial.](https://tutorial.djangogirls.org/en/installation/)
Create API keys for [Google Maps](https://developers.google.com/maps/documentation/javascript/get-api-key) and
[Google Fusion Tables](https://developers.google.com/fusiontables/docs/v1/using#APIKey) and update
`YOUR_KEY` values in `templates/addresses/index.html` file.

If you do not have a separate developer account with [Google](https://mail.google.com), it maybe necessary that
you sign up for one that you will use to work with Google Fusion Tables so that you do not risk losing your data.
Visit [this link](https://support.google.com/fusiontables/answer/184641?hl=en) for more information on how to get started with
[Google Fusion Tables](https://support.google.com/fusiontables/answer/184641?hl=en) if you are new to them.


## How-to Guides
### Create a Google Fusion Table
To create a Google Fusion Table, follow the [Google Fusion Tables tutorial](https://support.google.com/fusiontables/answer/184641?hl=en). Rename your fields in the table to `latitude`,
 `longitude` and `location` and hide the `date` field as it is not necesary for the project. Set the following
 data types for the fields:
 - `longitude` - `Number`.
 - `latitude` -  set Type to `Location` and check `Two-column location`. Set the values of `Latitude` to `latitude`
 and `Longitude` to `longitude`.
 - `location` - set type to `Text`.


## Explanation


## References

