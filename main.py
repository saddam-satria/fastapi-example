from fastapi import FastAPI
from routes import routing
from config.database import db_engine
from fastapi_sqlalchemy import DBSessionMiddleware
import os
import uvicorn
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
routing(app)
db_engine.connect()
app.add_middleware(DBSessionMiddleware,db_url=os.environ["DATABASE_URL"])

@app.get("/")
def home():
    return "/students"

if __name__ == "__main__":
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)