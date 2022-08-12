from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import time, asyncio
from .modules.KNN import predict_data

from .routers import classify

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(classify.router)


@app.get("/")
async def root():
    try: 
        result = { "/" : "Bạn đang ở route chính" }
    
    except:
        result = { "Message" : "Sai cú pháp" }
    finally:
        return result

@app.get("/test")
async def test(list_test : Request):
    data = [1,67,0,1,1,1,228,36,0,0,1,0,0,0,1,0,0]
    x = predict_data(data)
    print (x)
    return { "Message" : "Test done" }
