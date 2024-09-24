from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models, schemas, utils
from .database import engine, get_db  # type: ignore
from sqlalchemy.orm import Session
from . routers import post, user

models.Base.metadata.create_all(bind=engine)


app = FastAPI()


while True:
    try:
        conn = psycopg2.connect(
            host='localhost', database='fastapi', user='postgres', password='anirudh2005',
            cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print('Database connection was successful')
        break
    except Exception as error:
        print('Connecting to database failed')
        print('Error: ', error)
        time.sleep(2)


app.include_router(post.router)
app.include_router(user.router)


@app.get("/")
def root():
    return {"message": "Welcome to my api!!"}
