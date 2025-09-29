import io
from typing import Annotated

import joblib
import numpy as np
import pandas as pd
from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from base_logger import logger


app = FastAPI()

# CORS middleware allowing all origins and methods
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    logger.info("call predict")

    # Validation of file type
    if not file.filename.endswith('.txt'):
        raise HTTPException(400, "File must be txt")

    content = await file.read()

    logger.info(f"File content {content}")

    return


# Health check endpoint
@app.get("/")
async def root():
    return {"message": "LLM Model API is running!"}
