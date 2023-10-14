from pydantic import BaseModel
from typing import Optional
from fastapi import FastAPI, HTTPException,Header


class User(BaseModel):
    id: int
    name: str
    age: Optional[str] = None
        
        
api = FastAPI()

users = []

@api.get('/users')
def get_users():
    return users if users else {}


@api.post("/users")
def post_user(user: User):
    userid_list = list(filter(lambda x: x.id==user.id,users))
    if len (userid_list) >= 1 :
         raise HTTPException(status_code=409, detail=f"The id {user.id} already exist")
    users.append(user)
    return {"result":"ok"}


@api.post("/users/{userid:int}")
def update_user(user: User,userid):
    userid_list = []
    for i,u in enumerate(users):
        if u.id == userid:
           userid_list.append(i)
           break
    if len (userid_list) == 0 :
         raise HTTPException(status_code=404, detail=f"The id {user.id} has not been find to update it")
    users[i]=user
    return users[i]


@api.delete("/users/{userid:int}")
def delete_user(userid):
    userid_list = []
    for i,u in enumerate(users):
        if u.id == userid:
           userid_list.append(i)
           break
    if len (userid_list) == 0:
         raise HTTPException(status_code=404, detail=f"The id {userid} has not been find to delete")
    users.pop(i)
    return {"result":"ok"}


@api.get("/header")
def get_header(usr=Header(),pwd=Header()):
    return {usr:pwd }