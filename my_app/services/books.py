from my_app.schemas import Book
from my_app.database import database


def save_book(new_book: Book) -> Book:
    database["books"].append(new_book)
    return new_book


def get_all_books() -> list[Book]:
    books_data = database["books"]
    books = [Book.model_validate(data) for data in books_data]
    return books

# TO DO - analyse why the remove does not work in case of an entry created via the app?
# Error reported is >> TypeError: 'Book' object is not subscriptable    
def remove_book_by_id(id_to_del: str):
    for book in database["books"]:
        if book["id"] == id_to_del:
            database["books"].remove(book)
  