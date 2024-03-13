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

MODEL_SERVE = os.environ.get("MODEL_SERVE")

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


def custom_openapi():
    """
    A function that generates the OpenAPI schema for the FastAPI application.
    If the app already has an OpenAPI schema, it returns that.
    Otherwise, it creates a new schema, adds some custom Google Cloud Run backend configuration,
    sets a specific path option, updates the app's OpenAPI schema, and returns it.

    https://fastapi.tiangolo.com/how-to/extending-openapi/
    """
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(title="Custom FastAPI", version="0.1.0", routes=app.routes)

    openapi_schema["x-google-backend"] = {
        "address": "${CLOUD_RUN_URL}",
        "deadline": "${TIMEOUT}",
    }

    openapi_schema["paths"]["/predictions"]["options"] = {
        "operationId": "corsHelloWorld",
        "responses": {"200": {"description": "Successful response"}},
    }

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
