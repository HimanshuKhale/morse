# app/schemas.py

from pydantic import BaseModel


class TextInput(BaseModel):
    text: str


class MorseInput(BaseModel):
    morse_code: str


class EncodeResponse(BaseModel):
    original_text: str
    morse_code: str


class DecodeResponse(BaseModel):
    morse_code: str
    decoded_text: str