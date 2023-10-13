from fastapi import FastAPI

api = FastAPI(title='My API')

users_db = [
    {
        'user_id': 1,
        'name': 'Alice',
        'subscription': 'free tier'
    },
    {
        'user_id': 2,
        'name': 'Bob',
        'subscription': 'premium tier'
    },
    {
        'user_id': 3,
        'name': 'Clementine',
        'subscription': 'free tier'
    }
]


@api.get('/')
def get_index():
    return {"message":"bonjour"}


@api.get('/users')
def get_all_user():
    return users_db


@api.get('/users/{userid:int}')
def get_all_user(userid):
    user = list (filter(lambda x: x["user_id"] == userid, users_db ))
    return user[0] if len(user) >= 1 else {}

@api.get('/users/{userid:int}/name')
def get_user_name(userid):
    users = list (filter(lambda x: x["user_id"] == userid, users_db ))
    names = list(map(lambda x : x["name"],users))
    return {"name":names[0]} if len(names) >= 1 else {}


@api.get('/users/{userid:int}/subscription')
def get_user_subscription(userid):
    users = list (filter(lambda x: x["user_id"] == userid, users_db ))
    subscriptions = list(map(lambda x : x.get("subscription"),users))
    return {"subscription":subscriptions[0]} if len(subscriptions) >= 1 else {}