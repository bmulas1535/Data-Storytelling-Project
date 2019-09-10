import requests
from bs4 import BeautifulSoup
import pandas as pd

template = 'https://www.cars.com/for-sale/searchresults.action/?dealerType=all&page=&perPage=100&rd=30&searchSource=PAGINATION&sort=relevance&stkTypId=28881&zc=93955'
data_array = []
for x in range(1,100):
	url = template[:72] + str(x) + template[72:]
	response = requests.get(url, timeout=5)
	content = BeautifulSoup(response.content, "html.parser")
	# Begin Looking through page for these items
	for item in content.findAll('div', {'class':'shop-srp-listings__listing-container'}):
		carObjects= {
		"Price": item.find('span', attrs={"class": "listing-row__price"}).text.strip(),
		"Mileage": item.find('span', attrs={"class": "listing-row__mileage"}).text.strip(),
		"Make and Model": item.find('h2', attrs={"class": "listing-row__title"}).text.strip(),
		"Meta": item.find('ul', attrs={'class': 'listing-row__meta'}).text.strip()
		}
		data_array.append(carObjects)
df = pd.DataFrame(data_array)
df.to_csv('cars.data', index=False)