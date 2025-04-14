from typing import Annotated

from fastapi import APIRouter
from fastapi import Form
from fastapi import Path
from fastapi import Query
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi_chameleon import template

from .. import db

router = APIRouter()


@router.post("/contacts")
@template("contacts/row.pt")
def create_contact(
    firstname: Annotated[str, Form()],
    lastname: Annotated[str, Form()],
    email: Annotated[str, Form()],
):
    searcheable = lambda s: s.replace(" ", "").lower()
    id = firstname.lower()[0] + lastname.lower()[:7]
    infos = {
        "id": id,
        "firstname": firstname,
        "lastname": lastname,
        "email": email,
        "SearchableText": f"{searcheable(firstname)}{searcheable(lastname)}{searcheable(email)}",
    }
    db.CONTACTS[id] = infos
    return {"contact": db.CONTACTS[id]}


@router.get("/contacts")
@template("contacts/rows.pt")
def read_contacts(
    request: Request,
    q: Annotated[str | None, Query()] = None,
):
    import time

    # time.sleep(1)
    q = q.strip().lower() if q else ""
    return {
        "contacts": [item for item in db.CONTACTS.values() if q in item["SearchableText"]],
    }


@router.get("/contacts/{contact_id}")
@template("contacts/row.pt")
def read_contact(contact_id: Annotated[str, Path()]):
    contact = db.CONTACTS.get(contact_id)
    return {"contact": contact}


@router.delete("/contacts/{contact_id}", response_class=HTMLResponse)
def delete_contact(contact_id: Annotated[str, Path()]):
    if contact_id in db.CONTACTS:
        del db.CONTACTS[contact_id]
    return ""
