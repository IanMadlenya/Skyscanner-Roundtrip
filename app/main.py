from flask import *
# Import the app object from the main app module
from app import app
import json
import requests

API_KEY = "ca462265583925016847853845313477"

jsonSample = {
	'from_list': False, # or True + cities=Europe
	'cities': ['London', 'Paris', 'Barcelona'], # or Europe
	'date_from': 1475912855,
	'date_to': 1475998855,
	'price': 400 # or none
}

@app.route('/')
def index():
	return "<code> POST /trip <br> - with parameter 'params'=jsonData<br>jsonData = {}</code>".format(json.dumps(jsonSample, indent=4))


@app.route('/trip', methods=['POST'])
def getTrip():
	params = request.form["params"]
	params = json.loads(params)

	from_list = params["fromList"]
	cities = params["cities"]
	if (from_list):
		cities = select_from_list(cities)

	date_from = params["date_from"]
	date_to = params["date_to"]
	budget = params["budget"]

@app.route('/debug')
def debug():
	#find_flights_ab("", "")
	get_map("", "")
	return "ok"
	
def select_from_list(name):
	if (name == "Europe"):
		return ["Paris", "London"]
	print("invalid list-name")
	return []


def find_flights_ab(a, b):
	a = "LON"
	b = "JFK"
	year = "2016"
	month = "11"
	url = "http://partners.api.skyscanner.net/apiservices/browsegrid/v1.0/GB/GBP/en-GB/{}/{}/{}-{}?apiKey={}".format(a, b, year, month, API_KEY)
	r = requests.get(url, headers={"Accept": "application/json"})
	print(r.text)

def get_map(lat, lng):
	lat = "40.71"
	lng = "-73.998"
	for z in [18, 16, 14, 12]:
		url = "https://maps.googleapis.com/maps/api/staticmap?center={},{}&zoom={}&size=500x500&key=AIzaSyD7_mdKB-fGg-O9axsu_wIsvW6XjeTs0YI".format(lat, lng, str(z))
		r = requests.get(url)
		f = open("map-{}.png".format(z), 'wb')
		f.write(r.content)
		f.close()
