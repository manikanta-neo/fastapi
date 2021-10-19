from sqlalchemy import Column, DateTime , Integer, String
from sqlalchemy_utils.types.encrypted.encrypted_type import StringEncryptedType
from sqlalchemy.sql import func

from db_conf  import Base


class Book(Base):
    __tablename__ = "book"

    id = Column(Integer,primary_key=True ,index=True)
    name = Column(String(255),nullable=False)
    author = Column(String(255),nullable=False)
    description = Column(String(255),nullable=False)
    total_copies = Column(Integer,nullable=False)
    available_copies = Column(Integer,nullable=False)
    genre= Column(String(255),nullable=False)
    time_created = Column(DateTime(timezone=True),server_default=func.now())



