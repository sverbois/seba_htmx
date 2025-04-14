from typing import Annotated

from fastapi import APIRouter
from fastapi import Query
from fastapi_chameleon import template

router = APIRouter()


@router.get("/pages/home")
@template("pages/home.pt")
def page_home():
    return {}


@router.get("/pages/contacts")
@template("pages/contacts.pt")
def page_contacts(
    q: Annotated[str, Query()] = "",
):
    return {"q": q}
