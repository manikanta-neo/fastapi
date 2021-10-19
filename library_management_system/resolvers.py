from schemas import BookModel
import graphene
from db_conf import db
import sqlalchemy as sa
import models

class Query(graphene.ObjectType):
    all_books = graphene.List(BookModel)
    book_by_id = graphene.Field(BookModel,book_id=graphene.Int(required=True))
    book_by_author = graphene.List(BookModel,book_author=graphene.String(required=True))
    book_by_name = graphene.List(BookModel,book_name=graphene.String(required=True))
    book_by_genre = graphene.List(BookModel,book_genre=graphene.String(required=True))


    def resolve_all_books(self,info):
        query = BookModel.get_query(info)
        return query.all()

    def resolve_book_by_id(self,info,book_id):
        return db.query(models.Book).filter(models.Book.id == book_id).first()

    def resolve_book_by_author(self,info,book_author):
        return db.query(models.Book).filter(models.Book.author.like(book_author)).all()

    def resolve_book_by_name(self,info,book_name):
        return db.query(models.Book).filter(models.Book.name.like(book_name)).all()
    
    def resolve_book_by_genre(self,info,book_genre):
        return db.query(models.Book).filter(models.Book.genre.like(book_genre)).all()
