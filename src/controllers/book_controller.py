from flask import request, jsonify
from services.book_service import get_books, create_book
from config.database import db

class book_controller:

    @staticmethod
    def list_books():
        title = request.args.get("title")
        author = request.args.get("author")
        page = int(request.args.get("page", 1))
        limit = int(request.args.get("limit", 10))

        books = get_books(db.session, title, author, page, limit)
        return jsonify(books), 200

    @staticmethod
    def create_book():
        data = request.get_json()

        if not data or "title" not in data or "author" not in data:
            return jsonify({"error": "Title and author are required"}), 400

        new_book = create_book(db.session, data["title"], data["author"], data["published_year"], data["stock"], data["isbn"])
        return jsonify(new_book), 201
