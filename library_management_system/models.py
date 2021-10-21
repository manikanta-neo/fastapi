from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy_utils.types.encrypted.encrypted_type import StringEncryptedType
from sqlalchemy.sql import func

from db_conf import Base


class Book(Base):
    _tablename_ = "LibraryManagement"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    total_copies = Column(Integer, nullable=False)
    available_copies = Column(Integer, nullable=False)
    genre = Column(String(255), nullable=False)
    published_on = Column(String, nullable=True)
    time_created = Column(DateTime(timezone=True), server_default=func.now())


class User(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    book = Base.relationship("copy", backref="issue", lazy=True)


class Issue_book(Base):
    id = Column(Integer, primary_key=True)
    date_added = Column(DateTime())
    Issued_to = Column(Integer, Foreign_key="user.id", nullable=False, default=None)
    date_issued = Column(Integer, DateTime(), default=None)
    date_return = Column(DateTime(), default=None)
    book = Column(Integer, Foreign_key="book.id")

