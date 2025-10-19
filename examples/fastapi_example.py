"""
FastAPI example usage of num2words.
"""

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from num2words import num2words

app = FastAPI(title="Number to Words API", version="1.0.0")


class NumberResponse(BaseModel):
    """Response model for number conversion."""
    number: int
    result: str
    language: str
    type: str


@app.get("/convert/{number}", response_model=NumberResponse)
async def convert_number(
    number: int,
    lang: str = Query("en", description="Language code (en, ar)"),
    to: str = Query("cardinal", description="Conversion type (cardinal, ordinal)")
):
    """
    Convert a number to words.
    
    - **number**: The number to convert
    - **lang**: Language code (en, ar, english, arabic)
    - **to**: Conversion type (cardinal, ordinal)
    """
    try:
        result = num2words(number, lang=lang, to=to)
        return NumberResponse(
            number=number,
            result=result,
            language=lang,
            type=to
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except TypeError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "message": "Number to Words API",
        "endpoints": {
            "/convert/{number}": "Convert number to words",
            "/docs": "API documentation"
        },
        "supported_languages": ["en", "ar", "english", "arabic"]
    }


# Run with: uvicorn fastapi_example:app --reload

