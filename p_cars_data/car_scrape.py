import requests
from bs4 import BeautifulSoup
import pandas as pd

sedan= 20211
reg_cab_pickup= 20210
suv= 20217
body_types= [sedan,reg_cab_pickup,suv]

template = 'https://www.cars.com/for-sale/searchresults.action/?'
data_array = []

for i in body_types:
    url1= template + 'bsId=' + str(i)
    
    for x in range(1,50):
        url2= url1 + '&page=' + str(x) + '&perPage=100&rd=100&searchSource=PAGINATION&sort=relevance&stkTypId=28881&zc=93955'
        response = requests.get(url2, timeout=5)
        content = BeautifulSoup(response.content, "html.parser")
        
        # Begin Looking through page for these items
        for item in content.findAll('div', {'class':'shop-srp-listings__listing-container'}):
            carObjects= {
            "Price": item.find('span', attrs={"class": "listing-row__price"}).text.strip(),
            "Mileage": item.find('span', attrs={"class": "listing-row__mileage"}).text.strip(),
            "Make and Model": item.find('h2', attrs={"class": "listing-row__title"}).text.strip(),
            "Meta": item.find('ul', attrs={'class': 'listing-row__meta'}).text.strip(),
            "body_code": i,
            }
            data_array.append(carObjects)
            
df = pd.DataFrame(data_array)

df['Meta']= df['Meta'].replace(r'\s+|\\n', ' ', regex=True)
df= df[~df.Mileage.str.contains('--')]
df= df[~df.Price.str.contains('Not Priced')]

def removeS(string):
    string= string.replace('$', '')
    string= string.replace('mi.', '')
    string= string.replace(',', '')
    return string

def get_year(string):
    return string.split()[0]

def get_maker(string):
    return string.split()[1]

def get_model(string):
    return ' '.join(string.split()[2:])

def get_color(string):
    color= string.split()[2]
    return color

def get_trans(string):
    trans= string.split()[7]
    return trans

def get_drivet(string):
    drivet= string.split()[9]
    return drivet

df['Price']= df['Price'].apply(removeS).astype(int)
df['Mileage']= df['Mileage'].apply(removeS).astype(int)
df['year']= df['Make and Model'].apply(get_year)
df['maker']= df['Make and Model'].apply(get_maker)
df['model']= df['Make and Model'].apply(get_model)
df['color']= df['Meta'].apply(get_color)
df['trans']= df['Meta'].apply(get_trans)
df['drivet']= df['Meta'].apply(get_drivet)
df= df[['year','maker','model','color','trans','drivet','Mileage','Price','body_code']]
df= df.rename(columns={'Mileage':'mileage', 'Price':'price'})

df.to_csv('cars.data', index=False)