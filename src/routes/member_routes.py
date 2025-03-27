# from fastapi import APIRouter
# from controllers.member_controller import router as member_router

# member_bp = APIRouter()
# member_bp.include_router(member_router, prefix="/api", tags=["Members"])


from flask import Blueprint
from controllers.member_controller import member_controller

member_bp = Blueprint("members", __name__)

# Define member routes
member_bp.add_url_rule("/", view_func=member_controller.register_member, methods=["POST"])
member_bp.add_url_rule(
    "/<uuid:member_id>/borrowings",
    view_func=member_controller.get_member_borrowing_history,
    methods=["GET"]
)