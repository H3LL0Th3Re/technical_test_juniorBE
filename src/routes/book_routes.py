# from fastapi import APIRouter, HTTPException
# from controllers.book_controller import router as book_router

# # Define the main router for books
# book_bp = APIRouter()

# # Include the book controller router inside the main router
# book_bp.include_router(book_router, prefix="/api/books", tags=["Books"])


from flask import Blueprint
from controllers.book_controller import book_controller

book_bp = Blueprint("books", __name__)

# Register routes from the book controller
book_bp.add_url_rule("/", view_func=book_controller.list_books, methods=["GET"])
book_bp.add_url_rule("/", view_func=book_controller.create_book, methods=["POST"])
