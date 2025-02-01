from fastapi import FastAPI
import marimo

server = (
    marimo.create_asgi_app()
    .with_app(path="/notebook1", root="./notebooks/notebook1.py")
    .with_app(path="/notebook2", root="./notebooks/notebook2.py")
)


app = FastAPI()


@app.get("/")
def read_main():
    return {"message": "Hello World!"}


app.mount("/notebooks", server.build())
