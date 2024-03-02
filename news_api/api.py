from fastapi import FastAPI
from pydantic import BaseModel
from bs4 import BeautifulSoup
# import schedule

news_app = FastAPI() 

@news_app.get('/')
async def main():
    return 'Testing the API'

@news_app.get('/cryptofxnews')
async def fxnews():
    return 'Crypto/Forex news endpoint'