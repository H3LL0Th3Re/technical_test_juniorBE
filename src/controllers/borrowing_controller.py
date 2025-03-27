from flask import request, jsonify, abort
from services.borrowing_service import borrow_book, return_book
from config.database import db

class borrowing_controller:

    @staticmethod
    def borrow():
        data = request.get_json()

        if not data:
            abort(400, description="Missing request body")

        required_fields = ["book_id", "member_id"]
        if not all(field in data for field in required_fields):
            abort(400, description="Missing required fields")

        borrowing = borrow_book(db.session, data["book_id"], data["member_id"])

        return jsonify({
            "id": borrowing.id,
            "book_id": borrowing.book_id,
            "member_id": borrowing.member_id,
            "borrow_date": borrowing.borrow_date,
            "status": borrowing.status
        }), 201

    @staticmethod
    def return_borrowed_book(borrowing_id):
        borrowing = return_book(db.session, borrowing_id)

        return jsonify({
            "id": borrowing.id,
            "book_id": borrowing.book_id,
            "member_id": borrowing.member_id,
            "borrow_date": borrowing.borrow_date,
            "return_date": borrowing.return_date,
            "status": borrowing.status
        }), 200
