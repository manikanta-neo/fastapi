from pydantic import BaseModel
from models import Book
from graphene_sqlalchemy import SQLAlchemyObjectType


class BookAdd(BaseModel):
    name: str
    author: str
    description: str
    total_copies: int
    genre: str
    available_copies: int


class BookModel(SQLAlchemyObjectType):
    class Meta:
        model = Book


class BookDel(BaseModel):
    id: int


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str
    book: str


class Issue_book(BaseModel):
    id: int
    date_added: str
    issued_to: str
    date_issued: str
    date_return: str
    book: str