from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Annotated


class FileMaterial(BaseModel):
    name: str
    file_type: str
    size: str


file_app = FastAPI()

@file_app.get('/')
async def check_home():
    return 'Status: Active'


@file_app.post('/files/')
async def get_file(files: Annotated[list[bytes], File(description='Multi file as bytes')]):
    
    return {'content_length': [len(file) for file in files]}


@file_app.post('/upload/')
async def upload_file(
    files: Annotated[
        list[UploadFile], File(description='Multi-file upload')
    ]
):
    # return {'filename': files.content_type}
    return {'files': [file.filename for file in files]}


@file_app.get('/html')
async def main():
    content = """
     <body>
        <form action="/files/" enctype="multipart/form-data" method="post">
        <input name="files" type="file" multiple>
        <input type="submit">
        </form>
        <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
        <input name="files" type="file" multiple>
        <input type="submit">
        </form>
     </body>
    """
    
    return HTMLResponse(content=content)