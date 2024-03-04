from fastapi import FastAPI
from pydantic import BaseModel
from bs4 import BeautifulSoup
import requests


news_api = FastAPI() 

class WebScraper:
    def __init__(self, url):
        self.url = url
        self.soup = None
    
    def get_page(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            
            self.soup = BeautifulSoup(response.content, 'lxml')
            
        except requests.exceptions.RequestException as e:
            print(f'Error in scraping: {e}')
                    
    def find_element(self, tag, class_selector):
        if not self.soup:
            self.get_page()
            
        return self.soup.select(f'{tag}', class_=f'{class_selector}')
    
    def extract_text(self, elements, attributes=None):
        if not elements:
            return []
        
        if attributes:
            return [element[attributes] for element in elements]
        else:
             return [element.get_text(strip=True) for element in elements]
        
    


@news_api.get('/')
async def main():
    return 'Testing the API'

@news_api.get('/cryptofxnews')
async def fxnews():
    return 'Crypto/Forex news endpoint'