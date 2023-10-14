from fastapi import FastAPI

users=[]



@api.get('/')
def get_index(argument1):
    return {
        'data': argument1
    }


@api.get('/typed')
def get_typed(argument1: int):
    return {
        'data': argument1 + 1
    }
    

from typing import Optional

@api.get('/addition')
def get_addition(a: int, b: Optional[int]=None):
    if b:
        result = a + b
    else:
        result = a + 1
    return {
        'addition_result': result
    }


