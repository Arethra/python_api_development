from operator import index
from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 0}, {"title": "title of post 2", "content": "content of post 2", "id": 1}]


def find_posts(id):
    for a in my_posts:
        if a['id'] == id:
            return a


def find_index_post(id):
    for i, a in enumerate(my_posts):
        if a['id'] == id:
            return i

@app.get("/") #decorator - @, modeule - get, path - "/"
def root():
    return {"message": "Hello World!!"}

@app.get("/posts")
def get_posts():
    return{"Data": my_posts}

@app.post("/posts", status_code= status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict = post.model_dump()
    post_dict['id'] = randrange(0, 100000)
    my_posts.append(post_dict)
    return {"data": post_dict}

@app.get("/posts/{id}") # {id} - path parameter
def get_post(id: int, response: Response):
    post = find_posts(int(id))
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
    return {"post details": post}

@app.delete("/posts/{id}")
def delete_post(id: int, status_code= status.HTTP_204_NO_CONTENT):
    #deleting post
    # find index in array wiht that id and pop the index.
    index = find_index_post(id)
    
    if index == None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")
    
    my_posts.pop(index)
    return Response(status_code= status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id: int, post: Post):

    index = find_index_post(id)
    
    if index == None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")
    
    post_dict = post.model_dump()
    post_dict['id'] = id
    my_posts[index] = post_dict
    return{"data": post_dict}
