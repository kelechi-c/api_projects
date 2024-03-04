from fastapi import FastAPI
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

opts = Options()
opts.add_argument('--headless')
opts.add_argument('--disable-gpu')



news_api = FastAPI() 

class WebScraper:
    def __init__(self, url):
        self.url = url
        self.soup = None
    
    def get_page(self):
        try:
            driver = webdriver.Firefox()
            driver.get(self.url)
    
            response = driver.page_source
            driver.quit()
            
            self.soup = BeautifulSoup(response.content, 'lxml')
            
        except:
            print('Error in scraping:')
            
                    
    def find_element(self, tag, class_selector):
        if not self.soup:
            self.get_page()
        
        text = self.soup.select(f'{tag}', class_=f'{class_selector}')
        
        return text



@news_api.get('/')
async def main():
    return 'Testing the API'

@news_api.get('/cryptofxnews')
async def fxnews():
    return 'Crypto/Forex news endpoint'