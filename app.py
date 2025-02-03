from litestar import Litestar, asgi
import marimo

server = marimo.create_asgi_app().with_app(
    path="/notebook1", root="./notebooks/notebook1.py"
)


get_notebook = asgi(path="/notebooks", is_mount=True)(server.build())


app = Litestar(
    route_handlers=[
        get_notebook,
    ]
)
