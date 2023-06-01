import requests
from bs4 import BeautifulSoup

url = ("https://www.btkakademi.gov.tr/portal/catalog?sf=popular")
get = requests.get(url)
soup = BeautifulSoup(get.content, 'html.parser')

isim = soup.find_all("div",{"class":"font-medium text-base"})

for i in isim:
    i = i.text
    print(i)
#Efekan Acar
