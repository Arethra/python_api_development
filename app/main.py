from operator import index
from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
app = FastAPI()


#Class to ensure the content given in the event of a post request is of supported data type.
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

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
    #returns to user, the array of posts
    return{"Data": my_posts}

#defining a POST endpoint at "/posts" and setting a status code 201 
@app.post("/posts", status_code= status.HTTP_201_CREATED)
def create_posts(post: Post):
    #converts the post given to a dictionary 
    post_dict = post.model_dump()
    #randomly generates an id for the given post
    post_dict['id'] = randrange(0, 100000)
    #appends the dictionary created to the array
    my_posts.append(post_dict)
    #returns the created post dictionary to the user
    return {"data": post_dict}

#defining a GET endpoint at "/posts/{id}" where id is given by the user
@app.get("/posts/{id}") # {id} - path parameter
def get_post(id: int, response: Response):
    #a variable to store a post if the id is found by the find_posts function in the my_posts array
    post = find_posts(int(id))
    #throw an error with a message if the post with the provided id is not found in the my_posts array
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
    #return post to the user 
    return {"post details": post}

#defining a DELETE endpoint at "/posts/{id}" path
@app.delete("/posts/{id}")
def delete_post(id: int, status_code= status.HTTP_204_NO_CONTENT):
    #deleting post
    # find index in array with that id and pop the index.
    index = find_index_post(id)
    
    if index == None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")
    
    my_posts.pop(index)
    return Response(status_code= status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id: int, post: Post):

    #finds the index of the post with the given id
    index = find_index_post(id)
    
    #throw error if the id isn't found
    if index == None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")
    
    #convert the post given to a dictionary
    post_dict = post.model_dump()
    #get the id given in the post from the post's dictionary created
    post_dict['id'] = id
    #at the index in the my_posts array where posts are stored, the content from post dictionary is put in place of the content present
    my_posts[index] = post_dict
    return{"data": post_dict}
