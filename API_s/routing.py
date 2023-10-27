import fastapi
import uvicorn

bookshop = fastapi.FastAPI()

@bookshop.get('/')
def index():
    return 'Welcome to the bookshop!'

@bookshop.get('/author/all/')
def get_all_authors():
    return 'Here is a list of all the authors we stock!'

@bookshop.get('/book/all')
def get_all_books():
    return 'Here is a list of all the books we stock!'

@bookshop.get('/book/{book_id}')
def get_book(book_id: int):
    return f'Here is the book with id {book_id}'
    
if __name__ == '__main__':
    uvicorn.run(api, port=8000, host='127.0.0.1')

## or do this:

import fastapi
router = fastapi.APIRouter()


@router.get('/')
def index():
    return 'Welcome to the bookshop!'

# This would be our book.py script:

import fastapi
router = fastapi.APIRouter()

@router.get('/book/all')
def get_all_books():
    return 'Here is a list of all the books we stock!'

@router.get('/book/{book_id}')
def get_book(book_id: int):
    return f'Here is the book with id {book_id}'

# and this would be our author.py script:
import fastapi
router = fastapi.APIRouter()

@router.get('/author/all/')
def get_all_authors():
    return 'Here is a list of all the authors we stock!'

# main.py
import fastapi
import uvicorn
import store_api.author
import store_api.book
import store_api.home

api = fastapi.FastAPI()

def configure_routing():
    api.include_router(store_api.home.router)
    api.include_router(store_api.author.router)
    api.include_router(store_api.book.router)



if __name__ == '__main__':
    configure_routing()
    uvicorn.run(api, port=8000, host='127.0.0.1')