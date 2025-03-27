import uuid
from datetime import datetime
from config.database import db

class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.UUID, primary_key=True, default=uuid.uuid4)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    published_year = db.Column(db.Integer, nullable=False)
    stock = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.TIMESTAMP, default=datetime.utcnow)
    updated_at = db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)
    isbn = db.Column(db.String(13), unique=True, nullable=False)
