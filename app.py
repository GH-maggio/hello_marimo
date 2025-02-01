from litestar import Litestar, get, asgi
import marimo

server = (
    marimo.create_asgi_app()
    .with_app(path="/notebook1", root="./notebooks/notebook1.py")
    .with_app(path="/notebook2", root="./notebooks/notebook2.py")
)


@get(path="/")
async def get_root() -> dict[str, str]:
    return {"message": "Hello World!"}


get_notebook = asgi(path="/notebooks", is_mount=True)(server.build())


app = Litestar(
    route_handlers=[
        get_root,
        get_notebook,
    ]
)
