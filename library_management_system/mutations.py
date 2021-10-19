from schemas import BookDel,BookAdd
from db_conf import db
import models
import graphene

class DeleteBook(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required = True)
    isDeleted = graphene.Boolean()
    @staticmethod
    def mutate(root, info, id):
        delBook = BookDel(id = id)
        if db.query(models.Book).filter(models.Book.id == delBook.id).delete():
            db.commit()
            db.flush()
            isDeleted = True
            return DeleteBook(isDeleted = isDeleted)
        else:
            isDeleted = False
            return DeleteBook(isDeleted = isDeleted)

class CreateNewBook(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        author = graphene.String(required=True)
        description = graphene.String(required=True)
        total_copies = graphene.Int(required=True)
        genre = graphene.String(required=True)
        available_copies = graphene.Int(required=True)
    ok = graphene.Boolean()
    @staticmethod
    def mutate(root, info, name, author, description, total_copies,genre, available_copies):
        post = BookAdd(name=name, author=author, description=description, total_copies=total_copies, genre=genre,
                available_copies=available_copies)
        db_post = models.Book(name=post.name, author=post.author, description=post.description, total_copies=post.total_copies,
                    genre=post.genre, available_copies=post.available_copies)
        db.add(db_post)
        db.commit()
        db.refresh(db_post)
        ok = True
        return CreateNewBook(ok="successfullycreated")

class BookMutations(graphene.ObjectType):
        create_new_book = CreateNewBook.Field()
        delete_book = DeleteBook.Field()
