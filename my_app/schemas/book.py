from datetime import date

from pydantic import BaseModel, Field


class Book(BaseModel):
    id: str
    isdn_13: str
    name: str = Field(min_length=3, max_length=50)
    author: str = Field(min_length=3, max_length=50)
    editor: str = Field(min_length=3, max_length=50)
    entry_date: date
