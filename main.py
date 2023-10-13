from fastapi import FastAPI

api = FastAPI(title='My API')

@api.get('/')
def get_index():
    return {'data': 'hello world'}


@api.get('/item/{itemid:int}')
def get_item(itemid):
    return {
        'route': 'dynamic',
        'itemid': itemid
    }


@api.get('/item/{itemid}/description/{language}')
def get_item_language(itemid, language):
    if language == 'fr':
        return {
            'itemid': itemid,
            'description': 'un objet',
            'language': 'fr'
        }
    else:
        return {
            'itemid': itemid,
            'description': 'an object',
            'language': 'en'
        }
