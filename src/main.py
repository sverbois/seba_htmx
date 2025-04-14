import os

import fastapi_chameleon
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from . import config
from . import contacts
from . import pages

app = FastAPI(title="A small Hypermedia Driven Application")

template_folder_path = os.path.dirname(__file__)
fastapi_chameleon.global_init(template_folder_path, auto_reload=config.DEVELOPMENT_MODE)

static_folder_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "static"))
app.mount("/static", StaticFiles(directory=static_folder_path), name="static")


@app.get("/")
def index():
    return RedirectResponse("/pages/home")


app.include_router(contacts.router)
app.include_router(pages.router)
