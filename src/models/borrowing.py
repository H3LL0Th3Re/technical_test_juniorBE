import uuid
from datetime import datetime
from config.database import db

class Borrowing(db.Model):
    __tablename__ = "borrowings"

    id = db.Column(db.UUID, primary_key=True, default=uuid.uuid4)
    book_id = db.Column(db.UUID, db.ForeignKey('books.id'), nullable=False)
    member_id = db.Column(db.UUID, db.ForeignKey('members.id'), nullable=False)
    borrow_date = db.Column(db.Date, nullable=False)
    return_date = db.Column(db.Date, nullable=True)
    status = db.Column(db.Enum('BORROWED', 'RETURNED', name='borrow_status'), default='BORROWED')

    created_at = db.Column(db.TIMESTAMP, default=datetime.utcnow)
    updated_at = db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    book = db.relationship("Book", backref="borrowings")
    member = db.relationship("Member", backref="borrowings")
