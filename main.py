from fastapi import FastAPI
from routes import routing
from config.database import db_engine

import uvicorn


app = FastAPI()
routing(app)
db_engine.connect()

@app.get("/")
def home():
    return "/students"

if __name__ == "__main__":
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)