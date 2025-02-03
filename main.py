from fastapi import FastAPI
import marimo

server = marimo.create_asgi_app().with_app(
    path="/notebook1", root="./notebooks/notebook1.py"
)


app = FastAPI()


app.mount("/notebooks", server.build())
