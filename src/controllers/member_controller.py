from flask import request, jsonify, abort
from services.member_service import create_member
from config.database import db
from services.borrowing_service import fetch_member_borrowings
class member_controller:

    @staticmethod
    def register_member():
        data = request.get_json()

        if not data:
            abort(400, description="Missing request body")

        required_fields = ["name", "email", "phone", "address"]
        if not all(field in data for field in required_fields):
            abort(400, description="Missing required fields")

        new_member = create_member(
            db.session, data["name"], data["email"], data["phone"], data["address"]
        )

        return jsonify({
            "id": new_member.id,
            "name": new_member.name,
            "email": new_member.email,
            "phone": new_member.phone,
            "address": new_member.address
        }), 201
    def get_member_borrowing_history(member_id):
        try:
            status = request.args.get("status", None)  # Optional
            page = int(request.args.get("page", 1))  # Default to 1
            limit = int(request.args.get("limit", 10))  # Default to 10

            borrowings = fetch_member_borrowings(db.session, member_id, status, page, limit)
            return jsonify(borrowings), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
