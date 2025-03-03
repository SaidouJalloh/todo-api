from flask import Blueprint, jsonify, request
from app.models import Task
from app.utils import find_task_by_id

main = Blueprint('main', __name__)

# In-memory database
tasks = []
next_id = 1

@main.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify([task.to_dict() for task in tasks])

@main.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = find_task_by_id(tasks, task_id)
    if task:
        return jsonify(task.to_dict())
    return jsonify({"error": "Task not found"}), 404

@main.route('/tasks', methods=['POST'])
def create_task():
    global next_id
    data = request.json
    
    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400
    
    task = Task(next_id, data["title"], data.get("description", ""))
    tasks.append(task)
    next_id += 1
    
    return jsonify(task.to_dict()), 201

@main.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.json
    task = find_task_by_id(tasks, task_id)
    
    if not task:
        return jsonify({"error": "Task not found"}), 404
    
    task.update(data)
    return jsonify(task.to_dict())

@main.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    task = find_task_by_id(tasks, task_id)
    
    if not task:
        return jsonify({"error": "Task not found"}), 404
    
    tasks = [t for t in tasks if t.id != task_id]
    return jsonify({"message": "Task deleted successfully"})

@main.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"})