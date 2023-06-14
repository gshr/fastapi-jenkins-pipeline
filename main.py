from fastapi import FastAPI
import uvicorn
import datetime
app = FastAPI()


@app.get('/')
def hello():
    return {
        "message":"Hello World",
        "status": "200",
        "event": "Testing Webhook github event"
        }



    