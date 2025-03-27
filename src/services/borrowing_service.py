from sqlalchemy.orm import Session
from models.borrowing import Borrowing
from models.book import Book
from models.member import Member
from flask import abort
from datetime import datetime
from sqlalchemy.exc import IntegrityError

def borrow_book(db: Session, book_id: str, member_id: str):
    # Check book stock
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        abort(404, description="Book not found")
    if book.stock <= 0:
        abort(400, description="Book out of stock")

    # Check member borrowing count
    active_borrowings = db.query(Borrowing).filter(
        Borrowing.member_id == member_id,
        Borrowing.status == 'BORROWED'
    ).count()

    if active_borrowings >= 3:
        abort(400, description="Member cannot borrow more than 3 books")

    # Create borrowing record within a transaction
    try:
        borrowing = Borrowing(book_id=book_id, member_id=member_id, borrow_date=datetime.utcnow())
        db.add(borrowing)
        book.stock -= 1  # Reduce stock
        db.commit()
        db.refresh(borrowing)
    except IntegrityError:
        db.rollback()
        abort(400, description="Error creating borrowing record")

    return borrowing

def return_book(db: Session, borrowing_id: str):
    borrowing = db.query(Borrowing).filter(Borrowing.id == borrowing_id).first()
    if not borrowing:
        abort(404, description="Borrowing record not found")

    if borrowing.status == "RETURNED":
        abort(400, description="Book already returned")

    # Process return
    borrowing.status = "RETURNED"
    borrowing.return_date = datetime.utcnow()

    # Increase book stock
    book = db.query(Book).filter(Book.id == borrowing.book_id).first()
    if book:
        book.stock += 1

    db.commit()
    db.refresh(borrowing)
    return borrowing


def fetch_member_borrowings(db: Session, member_id, status, page, limit):
    query = db.query(Borrowing).join(Book, Borrowing.book_id == Book.id).filter(Borrowing.member_id == member_id)

    if status:
        query = query.filter(Borrowing.status == status)

    # Pagination using offset and limit
    borrowings = query.offset((page - 1) * limit).limit(limit).all()

    result = []
    for borrowing in borrowings:
        result.append({
            "borrowing_id": borrowing.id,
            "book": {
                "id": borrowing.book.id,
                "title": borrowing.book.title,
                "author": borrowing.book.author,
                "published_year": borrowing.book.published_year
            },
            "status": borrowing.status,
            "borrow_date": borrowing.borrow_date.isoformat(),
            "return_date": borrowing.return_date.isoformat() if borrowing.return_date else None
        })

    return result