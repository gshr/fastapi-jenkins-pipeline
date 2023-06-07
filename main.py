from fastapi import FastAPI
import uvicorn
import datetime
app = FastAPI()


@app.get('/')
def hello():
    return {
        "message":"Hello World",
        "time": datetime.datetime.now()
        }



    