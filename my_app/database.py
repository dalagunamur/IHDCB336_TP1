from datetime import date
from uuid import uuid4


database = {
    "books": [
        {
            "id": str(uuid4()),
            "isdn_13": "978-0441172719",
            "name": "Dune",
            "author": "Frank Herbert",
            "editor": "Penguin US",
            "entry_date": date(year=2024, month=1, day=21),
        },
        {
            "id": str(uuid4()),
            "isdn_13": "978-0007182367",
            "name": "The Lord of the Rings",
            "author": "John Ronald Reuel Tolkien",
            "editor": "Harper Collins",
            "entry_date": date(year=2022, month=9, day=19),
        },
        {
            "id": str(uuid4()),
            "isdn_13": "978-0008627782",
            "name": "The Hobbit",
            "author": "John Ronald Reuel Tolkien",
            "editor": "Harper Collins",
            "entry_date": date(year=2019, month=7, day=1),
        },
        {
            "id": str(uuid4()),
            "isdn_13": "978-0007477166",
            "name": "A song of ice and fire - complete series",
            "author": "George RR Martin",
            "editor": "Harper Collins",
            "entry_date": date(year=2016, month=3, day=29),
        },
    ]
}
