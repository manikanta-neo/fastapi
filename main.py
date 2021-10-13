
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
import uvicorn

app = FastAPI()


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

if __name__ == "__main__":
    uvicorn.run("main:app")



from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/user_id")
async def read_user(user_id: str):
    return {"user_id": user_id}

if __name__ == "__main__":
    uvicorn.run("main:app")

# create Enum class

from enum import Enum
from fastapi import FastAPI
import uvicorn


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW !"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message":"Have some residuals"}

if __name__ == "__main__":
    uvicorn.run("main:app")


from enum import Enum
from fastapi import FastAPI
import uvicorn

class ModelName(str, Enum):
    alexnet = "alexnet"
    lenet = "lenet"
    resnet = "resnet"


app = FastAPI()


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):

    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "welcome to alexnet"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "welcome to lenet"}
    return {"model_name": model_name, "message": "Have some residuals"}

if __name__ == "__main__":
    uvicorn.run("main:app")



from enum import Enum
from fastapi import FastAPI
import uvicorn


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()

@app.get("/model/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep learning FTW "}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LecNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}


if __name__ == "__main__":
    uvicorn.run("main:app")


from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"filepath": file_path}

if __name__ == "__main__":
    uvicorn.run("main:app")
