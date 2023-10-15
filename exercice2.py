from pydantic import BaseModel
from typing import Optional
from fastapi import FastAPI, HTTPException,Header


class User(BaseModel):
    """A user avaible un the application
    """
    id: Optional[int]
    name: str
    age: Optional[str] = None
    def get_id():
        User.id += 1
        return User.id-1
    
User.id = 0        
        
api = FastAPI()

users = []

@api.get('/users',name='All existing users')
def get_users():
    "return all user existing in the application"
    return users if users else {}


@api.post("/users",name="Create a new user",responses={200: {"description": "OK"},409: {"description": "User id already exist"}})
async def post_user(user: User):
    """Create a new user in the application"""
    userid_list = list(filter(lambda x: x.id==user.id,users))
    if len (userid_list) >= 1 :
         raise HTTPException(status_code=409, detail=f"The id {user.id} already exist")
    if user.id is None:
       user.id = User.get_id()
    users.append(user)
    return {"result":"ok","id":user.id}


@api.post("/users/{userid:int}",name="Update a user",responses={200: {"description": "OK"},404: {"description": "User id not found"}})
async def update_user(user: User,userid):
    """Update a existing user with it existing id"""
    userid_list = []
    for i,u in enumerate(users):
        if u.id == userid:
           userid_list.append(i)
           break
    if len (userid_list) == 0 :
         raise HTTPException(status_code=404, detail=f"The id {user.id} has not been find to update it")
    users[i]=user
    return users[i]


@api.delete("/users/{userid:int}",name="Delete user",responses={200: {"description": "OK"},404: {"description": "User id not found"}})
async def delete_user(userid):
    """Delete a existing user with it existing id"""
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
async def get_header(usr=Header(),pwd=Header()):
    return {usr:pwd }