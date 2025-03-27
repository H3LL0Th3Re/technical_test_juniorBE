from flask import Blueprint
from controllers.member_controller import member_controller

member_bp = Blueprint("members", __name__)


member_bp.add_url_rule("/", view_func=member_controller.register_member, methods=["POST"])
member_bp.add_url_rule(
    "/<uuid:member_id>/borrowings",
    view_func=member_controller.get_member_borrowing_history,
    methods=["GET"]
)