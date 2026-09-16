from flask import Flask, request, jsonify, render_template
import requests
import os

app = Flask(__name__)

#Backend Helper Functions

#-- Function to run the API Query to list all countries
def countrylist():
	response = requests.get(
		'https://api.restcountries.com/countries/v5?limit=100',
		headers={'Authorization': 'Bearer rc_live_819d4a5ec446428a890b8d09546bccb1'}
	)
	data = response.json()
	return data

#Frontend Routes
@app.route("/")
def home():
	data=countrylist()
	country_list=[]

	for country in data["data"]["objects"]:
		country_name=country["names"]["common"]
		country_list.append(country_name)

	return render_template('index.html', country_list=country_list)


if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(debug=True,host='0.0.0.0',port=port)

#include Tests for this code