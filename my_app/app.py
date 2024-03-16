from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from my_app.routes.books import router as book_router


app = FastAPI(title="David's books")
app.mount("/static", StaticFiles(directory="static"))
app.include_router(book_router)
