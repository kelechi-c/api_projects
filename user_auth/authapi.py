from fastapi import FastAPI, HTTPException
import typing

user_auth = FastAPI()

@user_auth.get('/')
async def main():
    return 'Here we go @FastAPI'