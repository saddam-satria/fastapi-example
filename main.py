from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def rootAPI():
    return {"message" : "Hello"}