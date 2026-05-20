# app/main.py

from fastapi import FastAPI, HTTPException
from app.schemas import TextInput, MorseInput, EncodeResponse, DecodeResponse
from app.morse import encode_to_morse, decode_from_morse

app = FastAPI(
    title="Morse Code Translator API",
    description="An API that converts text to Morse code and Morse code back to text.",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to the Morse Code Translator API",
        "endpoints": {
            "encode": "POST /encode",
            "decode": "POST /decode",
            "docs": "/docs"
        }
    }


@app.post("/encode", response_model=EncodeResponse)
def encode_text(data: TextInput):
    try:
        morse_code = encode_to_morse(data.text)
        return {
            "original_text": data.text,
            "morse_code": morse_code
        }
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@app.post("/decode", response_model=DecodeResponse)
def decode_morse(data: MorseInput):
    try:
        decoded_text = decode_from_morse(data.morse_code)
        return {
            "morse_code": data.morse_code,
            "decoded_text": decoded_text
        }
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))