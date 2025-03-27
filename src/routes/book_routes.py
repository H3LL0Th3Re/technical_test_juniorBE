
from flask import Blueprint
from controllers.book_controller import book_controller

book_bp = Blueprint("books", __name__)


book_bp.add_url_rule("/", view_func=book_controller.list_books, methods=["GET"])
book_bp.add_url_rule("/", view_func=book_controller.create_book, methods=["POST"])
