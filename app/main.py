from operator import index
from turtle import title
from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time

app = FastAPI()


#Class to ensure the content given in the event of a post request is of supported data type.
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

while True:

    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='24462', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Databse connection was successful.")
        break
    except Exception as error:
        print("Connection to database failed")
        print("Error: ", error)
        time.sleep(2)

#an array to store posts with placeholder content
my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 0}, {"title": "title of post 2", "content": "content of post 2", "id": 1}]

#function to iterate through the array of posts (my_posts) to determine if a post is in the array by means of given id
def find_posts(id):
    for a in my_posts:
        if a['id'] == id:
            return a

#function to iterate through the array of posts to determine the index of a post by id using the "enumerate" keyword
def find_index_post(id):
    for i, a in enumerate(my_posts):
        if a['id'] == id:
            return i

#api route handler that defines an endpoint at root path "/" for HTTP GET requests - GET endpoint
@app.get("/") #decorator - @, module - get, path - "/"
def root(): 
    #function to be executed when a get request is made to the root path 
    return {"message": "Hello World!!"}

#defining a GET endpoint at "/posts" 
@app.get("/posts")
def get_posts():
    cursor.execute(""" SELECT * FROM posts """)
    posts = cursor.fetchall()
    #returns to user, the array of posts
    return{"Data": posts}

#defining a POST endpoint at "/posts" and setting a status code 201 
@app.post("/posts", status_code= status.HTTP_201_CREATED)
def create_posts(post: Post):
    cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """,
                   (post.title, post.content, post.published))

    new_post = cursor.fetchone()

    conn.commit()

    return {"data": new_post}

#defining a GET endpoint at "/posts/{id}" where id is given by the user
@app.get("/posts/{id}") # {id} - path parameter
def get_post(id: int, response: Response):

    cursor.execute(""" SELECT * FROM posts WHERE id = %s  """, (str(id)))
    post = cursor.fetchone()
    
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
    
    return {"post details": post}

#defining a DELETE endpoint at "/posts/{id}" path
@app.delete("/posts/{id}")
def delete_post(id: int, status_code= status.HTTP_204_NO_CONTENT):
    
    cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (str(id)))
    deleted_post = cursor.fetchone()
    conn.commit()

    if deleted_post == None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")
    
    return Response(status_code= status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id: int, post: Post):

    cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""", 
                   (post.title, post.content, post.published, str(id)))
    updated_post = cursor.fetchone()
    conn.commit()

    if updated_post == None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")
    
    return{"data": updated_post}
