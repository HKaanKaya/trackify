import requests
from bs4 import BeautifulSoup

class PriceScrapper():

    def __init__(self):
        self.headers = {"User-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.4 Safari/605.1.15"}

        

    def scrape_product(self,url):
        
        response = requests.get(url, headers=self.headers)
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.text,'html.parser')
        title_element = soup.find("h1")
        raw_title = title_element.text.strip()
        price_element = soup.find(class_="price__item")
        raw_price = float(price_element.text.strip().replace(",","."))
        
        informations = {
            "title" : raw_title,
            "price" : raw_price
        }        

        return informations
        


        
