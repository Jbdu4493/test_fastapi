from fastapi import FastAPI
from fastapi import Header
from pydantic import BaseModel
from typing import Optional

class Computer(BaseModel):
    computerid: int
    cpu: Optional[str]
    gpu: Optional[str]
    price: float

api = FastAPI(
    title="My API",
    description="My own API powered by FastAPI.",
    version="1.0.1")




@api.get('/',name="Hello World")
def get_index():
    """Returns greetings
    """
    return {'greetings': 'welcome'}


@api.put('/computer', name='Create a new computer')
def get_computer(computer: Computer):
    """Creates a new computer within the database
    """
    return computer

@api.get('/custom', name='Get custom header')
def get_content(custom_header: Optional[str] = Header(None, description='My own personal header')):
    return {
        'Custom-Header': custom_header
    }