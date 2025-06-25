from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Comic(BaseModel):
    id: int
    title: str
    hero: str

comics = []

@app.post("/comics/")
def add_comic(comic: Comic):
    comics.append(comic)
    return comic

@app.get("/comics/")
def list_comics():
    return comics

@app.get("/comics/{comic_id}")
def get_comic(comic_id: int):
    for comic in comics:
        if comic.id == comic_id:
            return comic
    return {"error": "Comic not found"}

@app.delete("/comics/{comic_id}")
def remove_comic(comic_id: int):
    global comics
    comics = [comic for comic in comics if comic.id != comic_id]
    return {"message": "Comic removed"}