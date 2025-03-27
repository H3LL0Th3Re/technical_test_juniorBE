# from fastapi import APIRouter
# from controllers.borrowing_controller import router as borrowing_router

# borrowing_bp = APIRouter()
# borrowing_bp.include_router(borrowing_router, prefix="/api", tags=["Borrowings"])


from flask import Blueprint
from controllers.borrowing_controller import borrowing_controller

borrowing_bp = Blueprint("borrowings", __name__)

# Define borrowing routes
borrowing_bp.add_url_rule("/", view_func=borrowing_controller.borrow, methods=["POST"])
borrowing_bp.add_url_rule("/<string:borrowing_id>/return", view_func=borrowing_controller.return_borrowed_book, methods=["PUT"])
