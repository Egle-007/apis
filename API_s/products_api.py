products = {
    1: {    'name': 't-shirt',   'price': 19.99,    'category': 'clothes'},
    2: {    'name': 'stickers',  'price': 1.99,     'category': 'accessories'},
    3: {    'name': 'mug',       'price': 9.99,     'category': 'kitchenware'},
    4: {    'name': 'hoodie',    'price': 29.99,    'category': 'clothes'},
    5: {    'name': 'cap',       'price': 14.99,    'category': 'accessories'}
}

import fastapi

api = fastapi.FastAPI()
# @api.get('/products/{product_id}')
# def get_product(product_id:int):
#     return products[product_id]

@api.get('/products/by_category/{category}')
def get_product():
    return products[]
