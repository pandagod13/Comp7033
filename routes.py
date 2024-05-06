from flask import Blueprint, request, jsonify
from app import db

main_routes = Blueprint('main_routes', __name__)


@main_routes.route('/exercises', methods=['POST'])
def create_exercise():
    from models import Assignment
    data = request.get_json()
    new_exercise = Assignment(
        title=data['title'],
        description=data['description'],
        due_date=data['due_date'],
        type=data['type']
    )
    db.session.add(new_exercise)
    db.session.commit()
    return jsonify({'message': 'Exercise created successfully', 'exercise': data}), 201


@main_routes.route('/exercises', methods=['GET'])
def get_exercises():
    from models import Assignment
    exercises = Assignment.query.all()
    return jsonify([
        {'id': ex.id, 'title': ex.title, 'description': ex.description, 'due_date': ex.due_date.isoformat(),
         'type': ex.type}
        for ex in exercises
    ]), 200
