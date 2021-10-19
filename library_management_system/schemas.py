from pydantic import BaseModel
from models import Book
from graphene_sqlalchemy import SQLAlchemyObjectType

class BookAdd(BaseModel):
    name:str
    author:str
    description: str
    total_copies: int
    genre:str
    available_copies:int

class BookModel(SQLAlchemyObjectType):
    class Meta:
        model = Book

class BookDel(BaseModel):
    id:int