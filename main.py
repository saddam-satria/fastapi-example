from fastapi import FastAPI
from routes import routing
import uvicorn

app = FastAPI()

routing(app)

@app.get("/")
def home():
    return "/students"

if __name__ == "__main__":
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)