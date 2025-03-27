make virtual env to avoid conflicts then install these:
pip install psycopg2-binary
pip install flask
pip install flask sqlalchemy
pip install flask_migrate

then flask db init
flask db migrate -m "migration name"
flask db upgrade.
this will create the tables in db

sample testing

to return books simply use the put method
http://127.0.0.1:5000/api/borrowings/{borrow_id}/return

to borrow simply use post method
{
     "book_id": "1c95551b-29bc-464d-89fd-c371e4bd0ba5",
     "member_id": "e01e4c06-41a4-41e3-a55f-d0d74bcd150c"
}

to register a member simply use post method
{
     "name": "Theo",
     "email": "theo@mail.com",
     "phone": "+622131311123",
     "address": "queen street"
}

to create a book simply use post method
{
   "title": "The Art of AI",
   "author": "John Doe",
   "published_year": 2023,
   "stock": 5,
   "isbn": "9781234"
}

to get all books simply use get method
http://127.0.0.1:5000/api/books/

to get all borrow history use get method
http://127.0.0.1:5000/api/members/e01e4c06-41a4-41e3-a55f-d0d74bcd150c/borrowings?status=BORROWED&page=1&limit=10




