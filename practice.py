'''

# query parameters : when you declare other function parameters that are not part of the path parameters , they are
automatically interpreted as "query parameters"

all the same process that applied for path parameters also aplies for quey parameters:
Editor support
data parsing
Data Validation
Automatic documentation
Both urls would be same
http://127.0.0.1:8000/items/
http://127.0.0.1:8000/items/?skip=0&limit=10

optional Parameters
The same way , you can declare optional query parameters, by setting their default to None:
'''
import uvicorn

'''
from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": 'foo'}, {"item_name": 'bar'}, {"item_name": 'baz'}]

@app.get('/')
def home():
    return "home page"

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]


from typing import Optional
from fastapi import FastAPI
app = FastAPI()

@app.get('/')
def homepage():
    return "homepage"

@app.get('/items/')
async def read_item(item_id: str, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item,_id": item_id}
# item_id is path parameter but, q is a query parameter so code showing error
# fastapi used only str , but Optional[str] = None is query parameter

# query parameter type conversion

from fastapi import FastAPI
from typing import Optional
import uvicorn
app = FastAPI()


@app.get('/')
def index_page():
    return "index page"


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "This is amazing item that has long description"})
    return item

if __name__ == "__main__":
    uvicorn.run("practice:app")

    
# http://127.0.0.1:8000/items/foo?short=1
http://127.0.0.1:8000/items/foo?&short=True
http://127.0.0.1:8000/items/foo?&short=true
http://127.0.0.1:8000/items/foo?&short=on
http://127.0.0.1:8000/items/foo?&short=yes

http://127.0.0.1:8000/items/foo?&short=no returns
{"item_id":"foo",
"description":"This is amazing item that has long description"}


or any other case variation (uppercase, first letter in uppercase, etc), your function will see the parameter short 
with a bool value of True. Otherwise as False.

# multiple path parameters and query parameters

from typing import Optional
from fastapi import FastAPI
app = FastAPI()


@app.get('/')
def homepage():
    return "Home page"

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
        user_id:int, item_id:str, q: Optional[str] = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "this is amazing long"})
    return item

# required query parameters
from fastapi import FastAPI
app = FastAPI()

@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy":needy}
    return item

# http://127.0.0.1:8000/items/foo-item?needy=soneedy

from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/items/{item_id}")
async def read_user_item(
        item_id:str, needy:str, skip: int = 0, limit: Optional[int] = None
):
    item = {"Item_id": item_id, "needy": needy, "skip": skip,"limit": limit}
    return item
# Request body

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    return item
    
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] =None

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    item.name + item.price
    return item

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import uvicorn

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = FastAPI()

@app.post("/items")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


from typing import Optional

from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


class User(BaseModel):
    username: str
    full_name: Optional[str] = None


@app.put("/items/{item_id}")
async def update_item(

    item_id: int, item: Item, user: User, importance: int = Body(...)

):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return results

if __name__ == "__main__":
    uvicorn.run("practice:app")
'''
# path and numeric vaidations gt, ge, lt, le

from typing import Optional
from fastapi import FastAPI, Path, Query
app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(
    item_id: int = Path(..., title="The ID of the item to get"),
    q: Optional[str] = Query(None, alias="item-query"),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
