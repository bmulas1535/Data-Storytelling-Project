import requests
from bs4 import BeautifulSoup
import pandas as pd

url1 = 'https://www.cars.com/for-sale/searchresults.action/?dealerType=all&page=1&perPage=100&rd=30&searchSource=GN_BREADCRUMB&sort=relevance&stkTypId=28881&zc=93955'
url2 = 'https://www.cars.com/for-sale/searchresults.action/?dealerType=all&page=2&perPage=100&rd=30&searchSource=PAGINATION&sort=relevance&stkTypId=28881&zc=93955'
url3 = 'https://www.cars.com/for-sale/searchresults.action/?dealerType=all&page=3&perPage=100&rd=30&searchSource=PAGINATION&sort=relevance&stkTypId=28881&zc=93955'
url4 = 'https://www.cars.com/for-sale/searchresults.action/?dealerType=all&page=4&perPage=100&rd=30&searchSource=PAGINATION&sort=relevance&stkTypId=28881&zc=93955'
url5 = 'https://www.cars.com/for-sale/searchresults.action/?dealerType=all&page=5&perPage=100&rd=30&searchSource=PAGINATION&sort=relevance&stkTypId=28881&zc=93955'
url6 = 'https://www.cars.com/for-sale/searchresults.action/?dealerType=all&page=6&perPage=100&rd=30&searchSource=PAGINATION&sort=relevance&stkTypId=28881&zc=93955'
url7 = 'https://www.cars.com/for-sale/searchresults.action/?dealerType=all&page=7&perPage=100&rd=30&searchSource=PAGINATION&sort=relevance&stkTypId=28881&zc=93955'
url8 = 'https://www.cars.com/for-sale/searchresults.action/?dealerType=all&page=8&perPage=100&rd=30&searchSource=PAGINATION&sort=relevance&stkTypId=28881&zc=93955'
url9 = 'https://www.cars.com/for-sale/searchresults.action/?dealerType=all&page=9&perPage=100&rd=30&searchSource=PAGINATION&sort=relevance&stkTypId=28881&zc=93955'
url10 = 'https://www.cars.com/for-sale/searchresults.action/?dealerType=all&page=10&perPage=100&rd=30&searchSource=PAGINATION&sort=relevance&stkTypId=28881&zc=93955'
url11 = 'https://www.cars.com/for-sale/searchresults.action/?dealerType=all&page=11&perPage=100&rd=30&searchSource=PAGINATION&sort=relevance&stkTypId=28881&zc=93955'
url12 = 'https://www.cars.com/for-sale/searchresults.action/?dealerType=all&page=12&perPage=100&rd=30&searchSource=PAGINATION&sort=relevance&stkTypId=28881&zc=93955'
url13 = 'https://www.cars.com/for-sale/searchresults.action/?dealerType=all&page=13&perPage=100&rd=30&searchSource=PAGINATION&sort=relevance&stkTypId=28881&zc=93955'
url14 = 'https://www.cars.com/for-sale/searchresults.action/?dealerType=all&page=14&perPage=100&rd=30&searchSource=PAGINATION&sort=relevance&stkTypId=28881&zc=93955'
url15 = 'https://www.cars.com/for-sale/searchresults.action/?dealerType=all&page=15&perPage=100&rd=30&searchSource=PAGINATION&sort=relevance&stkTypId=28881&zc=93955'
url16 = 'https://www.cars.com/for-sale/searchresults.action/?dealerType=all&page=16&perPage=100&rd=30&searchSource=PAGINATION&sort=relevance&stkTypId=28881&zc=93955'
url17 = 'https://www.cars.com/for-sale/searchresults.action/?dealerType=all&page=17&perPage=100&rd=30&searchSource=PAGINATION&sort=relevance&stkTypId=28881&zc=93955'
url18 = 'https://www.cars.com/for-sale/searchresults.action/?dealerType=all&page=18&perPage=100&rd=30&searchSource=PAGINATION&sort=relevance&stkTypId=28881&zc=93955'
url19 = 'https://www.cars.com/for-sale/searchresults.action/?dealerType=all&page=19&perPage=100&rd=30&searchSource=PAGINATION&sort=relevance&stkTypId=28881&zc=93955'
url20 = 'https://www.cars.com/for-sale/searchresults.action/?dealerType=all&page=20&perPage=100&rd=30&searchSource=PAGINATION&sort=relevance&stkTypId=28881&zc=93955'

test_dict= {'URL': [url1,url2,url3,url4,url5,url6,url7,url6,url8,url9,url6,url10,
                    url11,url12,url13,url14,url15,url16,url17,url18,url19,url20]}
data_array = []
for key, value in test_dict.items():
    for x in value:
        url = x
        response = requests.get(url, timeout=5)
        content = BeautifulSoup(response.content, "html.parser")
        
        # Begin Looking through page for these items
        for item in content.findAll('div', {'class':'shop-srp-listings__listing-container'}):
            carObjects= {
                "Price": item.find('span', attrs={"class": "listing-row__price"}).text.strip(),
                "Mileage": item.find('span', attrs={"class": "listing-row__mileage"}).text.strip(),
                "Make and Model": item.find('h2', attrs={"class": "listing-row__title"}).text.strip()
            }
            data_array.append(carObjects)
            
df = pd.DataFrame(data_array)
df.to_csv('cars.data', index=False)