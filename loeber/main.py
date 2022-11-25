from fastapi import FastAPI
from typing import Union

app = FastAPI()

@app.get("/")
# can be async 
# async def read_root():
def read_root():
    # dictionary auto converted to json 
    return {"Hello": "World"}


#? run with:
#* uvicorn main:app --reload

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# http://localhost:8000/items/5?q=hello-world