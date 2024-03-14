import os
import sys
from typing import List

from fastapi import FastAPI

# API Gateway
from fastapi.middleware.cors import CORSMiddleware

# This schema is crucial for API Gateway to understand your API and handle requests appropriately.
from fastapi.openapi.utils import get_openapi

# This class from the pydantic library simplifies data modeling for API requests and responses.
# It allows you to define the expected data structure, including data types and validation rules.
# This makes your code more readable, maintainable, and helps prevent errors in data exchange.
from pydantic import BaseModel

# This function helps generate the API schema, which describes the structure and functionalities of your API.
app = FastAPI()

MODEL_SERVE = os.environ.get("MODEL_SERVE", "None")

@app.get("/")
async def root():
    return {"message": f"Ok {MODEL_SERVE}"}

# Schema for API Gateway
class RequestItem(BaseModel):
    instances: List[str]

class ResponseItem(BaseModel):
    predictions: List[str] 
    
def gen_model(text: str):
    return f"gen: {text}"

@app.post("/predictions", response_model=ResponseItem)
def model_serve(input: RequestItem):
    """
    The model serving route.
    """
    if not os.getenv("MODEL_SERVE"):
        print("You need to set the MODEL_SERVE env variable to true", file=sys.stderr)

    result = gen_model(input.instances[0])
    return {"predictions": [result]}


@app.get("/api/health", status_code=200)
def health_check():
    return {"api_healthy": True}