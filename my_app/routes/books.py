from typing import Annotated
from uuid import uuid4
from datetime import date

from fastapi import APIRouter, HTTPException, status, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import ValidationError

from my_app.schemas import Book
import my_app.services.books as service


router = APIRouter(prefix="/books", tags=["Books"])
templates = Jinja2Templates(directory="templates")


@router.get('/all')
def get_all_books(request: Request):
    books = service.get_all_books()
    return templates.TemplateResponse(
        "books.html",
        context={'request': request, 'books': books}
    )


@router.get('/new')
def ask_to_create_new_book(request: Request):
    return templates.TemplateResponse(
        "new_book.html",
        context={'request': request}
    )


@router.post('/new')
def create_new_book(name: Annotated[str, Form()], author: Annotated[str, Form()], editor: Annotated[str, Form()], isdn_13: Annotated[str, Form()]):
    new_book_data = {
        "id": str(uuid4()),
        "isdn_13": isdn_13,
        "name": name,
        "author": author,
        "editor": editor,
        "entry_date": date.today(),
    }
    try:
        new_book = Book.model_validate(new_book_data)
    except ValidationError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid name or description for the book.",
        )
    service.save_book(new_book)
    return RedirectResponse(url="/books/all", status_code=302)


@router.post('/remove')
def ask_to_remove_book(book_id: Annotated[str, Form()]):
    service.remove_book_by_id(book_id)
    return RedirectResponse(url="/books/all", status_code=302)


@router.get('/update')
def ask_to_create_new_book(request: Request):
    return templates.TemplateResponse(
        "new_book.html",
        context={'request': request}
    )


@router.post('/update')
def create_new_book(name: Annotated[str, Form()], author: Annotated[str, Form()], editor: Annotated[str, Form()], isdn_13: Annotated[str, Form()]):
    new_book_data = {
        "id": str(uuid4()),
        "isdn_13": isdn_13,
        "name": name,
        "author": author,
        "editor": editor,
        "entry_date": date.today(),
    }
    try:
        new_book = Book.model_validate(new_book_data)
    except ValidationError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid name or description for the book.",
        )
    service.save_book(new_book)
    return RedirectResponse(url="/books/all", status_code=302)
