
from fastapi import FastAPI
import uvicorn


app = FastAPI()

@app.get("/")
def app_root():
    return "Hello:world"

if __name__ == "__main__":
    uvicorn.run("main:app")

from typing import Optional
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.price, "item_id": item_id}

if __name__ == "__main__":
    uvicorn.run("main:app")

from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
async def root():
    return {"message": "welcome to fastapi"}

if __name__ == "__main__":
    uvicorn.run("main:app")

from fastapi import FastAPI
import uvicorn
app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id:int):
    return {"item_id": item_id}

if __name__ == "__main__":
    uvicorn.run("main:app")

from fastapi import FastAPI
app = FastAPI()


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}



