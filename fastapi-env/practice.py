'''
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import uvicorn
app = FastAPI()


@app.get('/blogs')  # path operator decorator ?limit=10&published=true
def home(limit):    # path operator function
    return {'data': f'{limit} blogs from db'}


@app.get('/blog/{id}')
def show(id: int):
    # fetch blog with id = id
    return {"data": id}


@app.get(('blog/unpublished'))
def unpublished():
    return {'data': 'all unpublished blogs'}


@app.get('/')
def home():
    return {'data':'home page'}


@app.get('/blog')
def index(limit=10, published: bool = True, sort: Optional[str] = None):

    if published:
        return {'data': f'{limit} published blogs from db'}
    else:
        return {'data': f'{limit} blogs from db'}


@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    return {'data': {'1','2'}}

# Request body

class Blog(BaseModel):
    title: str
    body: str
    published_at: Optional[bool]

@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': 'Blog is created with title as {request.title}'}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.5', port=9000)


# sql Relational Databases SQL Alchemy
# pydantic models


@app.post('/blog')
def create(title, body):
    return {'title': title, 'body': body}
'''

from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Blog(BaseModel):
    title: str
    body: str

@app.post('/blog')
def create(request: Blog):
    return 'request'









