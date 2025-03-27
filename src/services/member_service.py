from sqlalchemy.orm import Session
from models.member import Member
from flask import abort
import re

def is_valid_email(email: str):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def create_member(db: Session, name: str, email: str, phone: str, address: str):
    if not is_valid_email(email):
        abort(400, description="Invalid email format")

    existing_member = db.query(Member).filter(Member.email == email).first()
    if existing_member:
        abort(400, description="Email already registered")

    new_member = Member(name=name, email=email, phone=phone, address=address)
    db.add(new_member)
    db.commit()
    db.refresh(new_member)
    return new_member
