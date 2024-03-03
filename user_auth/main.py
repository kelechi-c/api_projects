from fastapi import FastAPI
from config import settings
from session import engine
from base_class import User

def create_table():
    User.metadata.create_all(bind=engine)
    
def start_app():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    create_table()
    return app

app = start_app()

@app.get('/')
def home():
    return "It works!!!"