from fastapi import FastAPI
from fastapi.templating import Jinja2Templates


app = FastAPI()
template = Jinja2Templates(directory='templates')
