from fastapi import FastAPI
from routes import routing
from config.database import db_engine
from config.models import Base
import uvicorn


app = FastAPI()
routing(app)
db_engine.connect()
Base.metadata.create_all(db_engine)


@app.get("/")
def home():
    return "/students"

if __name__ == "__main__":
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)