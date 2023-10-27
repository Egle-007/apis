import fastapi
import order
import menu

api = fastapi.FastAPI()

def configure_routing():
    api.include_router(menu.router)
    api.include_router(order.router)

# if __name__ = '__main__':
# configure_routing()
# uvicorn.run()~~