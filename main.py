from fastapi import FastAPI

# app instance from fastapi
app = FastAPI()


# index home
@app.get('/')
def index():
    return "Hello into Mini Sales  System"
