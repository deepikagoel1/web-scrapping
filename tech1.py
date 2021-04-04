#Begin by importing the Requests module:

import requests

#Now, let’s try to get a webpage. For this example, let’s get GitHub’s public timeline:

r = requests.get('https://developer.nrel.gov/api/alt-fuel-stations/v1.json?fuel_type=E85,ELEC&state=CA&limit=2&api_key=PhBVDryNz4oi6VV7HtCePOda2AfIiwThurI410FI')

#Get the status code...returns an integer on success

r.status_code

#Get the data

r.text

#Get the data in the json format

r.json