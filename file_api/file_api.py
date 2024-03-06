from fastapi import FastAPI, UploadFile, File
import shutil


file_app = FastAPI()

@file_app.post('/files')
async def get_file(file: bytes = File(...)):
    content = file.decode('utf-8')
    lines = content.split('\n')
    
    return {'content': lines}