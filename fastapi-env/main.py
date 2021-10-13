from fastapi import FastAPI
import schemas
import uvicorn
app = FastAPI()


@app.post('/blog')
def create(result: schemas.Blog):
    return result


if __name__ == '__main__':
    uvicorn.run('main:app')