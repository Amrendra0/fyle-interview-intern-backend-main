from flask import Blueprint, jsonify, request
from core.models.assignment import Assignment
from core.models import db

teacher_views = Blueprint("teacher_views", __name__)

@teacher_views.route("/assignments", methods=["GET"])
def list_assignments():
    # Get teacher ID from headers
    teacher_id = request.headers.get("X-Principal", {}).get("teacher_id")

    if not teacher_id:
        return jsonify({"error": "Unauthorized"}), 401

    assignments = Assignment.query.filter_by(teacher_id=teacher_id, state="SUBMITTED").all()
    return jsonify({"data": [assignment.to_dict() for assignment in assignments]})

@teacher_views.route("/assignments/grade", methods=["POST"])
def grade_assignment():
    data = request.json
    assignment_id = data.get("id")
    grade = data.get("grade")

    # Retrieve assignment
    assignment = Assignment.query.get(assignment_id)
    if not assignment or assignment.state != "SUBMITTED":
        return jsonify({"error": "Invalid assignment ID or state"}), 400

    assignment.grade = grade
    assignment.state = "GRADED"
    db.session.commit()

    return jsonify({"message": "Assignment graded successfully", "assignment": assignment.to_dict()})
