import requests
from bs4 import BeautifulSoup

url = "https://www.btkakademi.gov.tr/portal/catalog?categoryId=353"
get = requests.get(url)
soup = BeautifulSoup(get.content, 'html.parser')

isimler = soup.find_all("div", {"class": "font-medium text-base"})

with open("btk_kurslar.txt", "w") as file:
    for i in isimler:
        i = i.text
        file.write(i + "\n")
#Efekan Acar
