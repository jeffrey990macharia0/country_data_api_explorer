from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import requests
import os

app = Flask(__name__)

#get api credentials as environment variables
load_dotenv()

#Backend Helper Functions

#-- Function to run the API Query to list all countries
def countrylist():
	api_key=os.getenv('API_KEY')
	response = requests.get(
		'https://api.restcountries.com/countries/v5?limit=100',
		headers={'Authorization': api_key}
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

@app.route("/search",methods=['POST'])
def search():
	data=countrylist()
	country_list=[]

	for country in data["data"]["objects"]:
		country_name=country["names"]["common"]
		country_list.append(country_name)

	#get the form data
	country=request.form.get("country","")
	capitals=request.form.get("capitals","")
	region=request.form.get("region","")
	flag=request.form.get("flag.url_png","")

	

	#construct the query
	api_key=os.getenv('API_KEY')
	response = requests.get(
		'https://api.restcountries.com/countries/v5/names.common/{}'.format(country),
		headers={'Authorization': api_key}
	)

	data = response.json()

	capitals_list=[]
	region_string=""
	flag_url=""


	if capitals:
		for attribute in data["data"]["objects"][0]["capitals"]:
			capitals_list.append(attribute["name"])


	if region:
		region_string=data["data"]["objects"][0]["region"]

	if flag:
		flag_url=data["data"]["objects"][0]["flag"]["url_png"]


	return render_template('index.html', country_list=country_list,country=country,capitals_list=capitals_list,region_string=region_string,flag_url=flag_url)


if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(debug=True,host='0.0.0.0',port=port)

#include Tests for this code