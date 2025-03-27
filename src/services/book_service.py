# from sqlalchemy.orm import Session
# from models.book import Book
# from fastapi import HTTPException
# from sqlalchemy import or_

# def get_books(db: Session, title: str = None, author: str = None, page: int = 1, limit: int = 10):
#     query = db.query(Book)
    
#     # Apply filters if provided
#     if title:
#         query = query.filter(Book.title.ilike(f"%{title}%"))
#     if author:
#         query = query.filter(Book.author.ilike(f"%{author}%"))
    
#     total = query.count()
#     books = query.offset((page - 1) * limit).limit(limit).all()

#     return {
#         "data": books,
#         "pagination": {
#             "total": total,
#             "page": page,
#             "limit": limit,
#             "totalPages": (total + limit - 1) // limit
#         }
#     }


from sqlalchemy.orm import Session
from models.book import Book

def get_books(db: Session, title: str = None, author: str = None, page: int = 1, limit: int = 10):
    query = db.query(Book)

    if title:
        query = query.filter(Book.title.ilike(f"%{title}%"))
    if author:
        query = query.filter(Book.author.ilike(f"%{author}%"))

    total = query.count()
    books = query.offset((page - 1) * limit).limit(limit).all()

    return {
        "data": [{"id": book.id, "title": book.title, "author": book.author} for book in books],
        "pagination": {
            "total": total,
            "page": page,
            "limit": limit,
            "totalPages": (total + limit - 1) // limit
        }
    }

def create_book(db: Session, title: str, author: str, published_year: int, stock: int, isbn: str):
    new_book = Book(title=title, author=author, published_year=published_year, stock=stock, isbn=isbn)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    
    return {"id": new_book.id, "title": new_book.title, "author": new_book.author}
