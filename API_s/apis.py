import fastapi
import uvicorn

# let's create an instance of the FastAPI class, which will represent your FastAPI application:
api = fastapi.FastAPI()

# decorators specify the URL path and associate it with a corresponding function that handles the request.
@api.get('/test/calculate')
def calculate(x=int, y=int):
    return x + y

uvicorn.run(api, port=8000, host='127.0.0.1')