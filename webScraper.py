# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# Set the URL you want to webscrape from
#url = 'https://ustaboys.com/draws/2019/boys-16-singles/feed-in/round/8/match/0/#body-content'

# Connect to the URL
#response = requests.get(url)

#print(response.text.count("Wo(inj)"))

#data will be indexed by year, each year will have a dictionary with 
data = {}

#looking for
# Ret(inj)
# Def(ns)
# Wo(inj)
# Wo(ill)
for year in range(2000, 2020):
	thisYearData = {"Ret(inj)": 0,
					"Def(ns)": 0,
					 "Wo(inj)": 0,
					 "Wo(ill)": 0}

	#boys 18 singles feed in
	#round 1, loop over matches 0 - 56
	for match in range(0, 56, 8):
		url = 'https://ustaboys.com/draws/' + str(year) + '/boys-18-singles/feed-in/round/1/match/' + str(match) + '/#body-content'
		response = requests.get(url)

		#add to data
		thisYearData["Ret(inj)"] += response.text.count("Ret(inj)");
		thisYearData["Def(ns)"] += response.text.count("Def(ns)");
		thisYearData["Wo(inj)"] += response.text.count("Wo(inj)");
		thisYearData["Wo(ill)"] += response.text.count("Wo(ill)");

	#round 8, match 0
	url = 'https://ustaboys.com/draws/' + str(year) + '/boys-18-singles/feed-in/round/1/match/0/#body-content'
	response = requests.get(url)

	#add to data
	thisYearData["Ret(inj)"] += response.text.count("Ret(inj)");
	thisYearData["Def(ns)"] += response.text.count("Def(ns)");
	thisYearData["Wo(inj)"] += response.text.count("Wo(inj)");
	thisYearData["Wo(ill)"] += response.text.count("Wo(ill)");

	#boys 16 singles feed in
	#round 1, loop over matches 0 - 56
	for match in range(0, 56, 8):
		url = 'https://ustaboys.com/draws/' + str(year) + '/boys-16-singles/feed-in/round/1/match/' + str(match) + '/#body-content'
		response = requests.get(url)

		#add to data
		thisYearData["Ret(inj)"] += response.text.count("Ret(inj)");
		thisYearData["Def(ns)"] += response.text.count("Def(ns)");
		thisYearData["Wo(inj)"] += response.text.count("Wo(inj)");
		thisYearData["Wo(ill)"] += response.text.count("Wo(ill)");

	#round 8, match 0
	url = 'https://ustaboys.com/draws/' + str(year) + '/boys-16-singles/feed-in/round/1/match/0/#body-content'
	response = requests.get(url)

	#add to data
	thisYearData["Ret(inj)"] += response.text.count("Ret(inj)");
	thisYearData["Def(ns)"] += response.text.count("Def(ns)");
	thisYearData["Wo(inj)"] += response.text.count("Wo(inj)");
	thisYearData["Wo(ill)"] += response.text.count("Wo(ill)");

	#add to the data
	data[year] = thisYearData

#print
for year in data:
	print(year)
	for item in data[year]:
		print(item + ": " + str(data[year][item]))


