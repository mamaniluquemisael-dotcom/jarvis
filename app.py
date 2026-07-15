from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_cors import CORS
import json
import os
from datetime import datetime
from pathlib import Path

app = Flask(__name__)
CORS(app)

# Configuración
app.config['JSON_SORT_KEYS'] = False
TODO_FILE = 'todos.json'

# Funciones auxiliares
def load_todos():
    """Carga las tareas del archivo JSON"""
    try:
        if os.path.exists(TODO_FILE):
            with open(TODO_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
    except Exception as e:
        print(f"Error al cargar: {e}")
    return []

def save_todos(todos):
    """Guarda las tareas en el archivo JSON"""
    try:
        with open(TODO_FILE, 'w', encoding='utf-8') as f:
            json.dump(todos, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error al guardar: {e}")
        return False

def get_next_id(todos):
    """Obtiene el siguiente ID disponible"""
    if not todos:
        return 1
    return max([t.get('id', 0) for t in todos]) + 1

# Rutas principales
@app.route('/')
def index():
    """Página principal"""
    return render_template('index.html')

@app.route('/api/todos', methods=['GET'])
def get_todos():
    """Obtiene todas las tareas"""
    todos = load_todos()
    filter_type = request.args.get('filter', 'all')
    
    if filter_type == 'pending':
        todos = [t for t in todos if not t.get('completed', False)]
    elif filter_type == 'completed':
        todos = [t for t in todos if t.get('completed', False)]
    
    return jsonify(todos)

@app.route('/api/todos', methods=['POST'])
def create_todo():
    """Crea una nueva tarea"""
    data = request.get_json()
    
    if not data or not data.get('title'):
        return jsonify({'error': 'Título requerido'}), 400
    
    todos = load_todos()
    new_todo = {
        'id': get_next_id(todos),
        'title': data.get('title', '').strip(),
        'description': data.get('description', '').strip(),
        'priority': data.get('priority', 'normal').lower(),
        'completed': False,
        'created_at': datetime.now().isoformat(),
        'completed_at': None
    }
    
    todos.append(new_todo)
    save_todos(todos)
    
    return jsonify(new_todo), 201

@app.route('/api/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    """Obtiene una tarea específica"""
    todos = load_todos()
    todo = next((t for t in todos if t.get('id') == todo_id), None)
    
    if not todo:
        return jsonify({'error': 'Tarea no encontrada'}), 404
    
    return jsonify(todo)

@app.route('/api/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    """Actualiza una tarea"""
    data = request.get_json()
    todos = load_todos()
    
    todo = next((t for t in todos if t.get('id') == todo_id), None)
    if not todo:
        return jsonify({'error': 'Tarea no encontrada'}), 404
    
    # Actualizar campos
    if 'title' in data:
        todo['title'] = data['title'].strip()
    if 'description' in data:
        todo['description'] = data['description'].strip()
    if 'priority' in data:
        todo['priority'] = data['priority'].lower()
    if 'completed' in data:
        todo['completed'] = data['completed']
        if data['completed']:
            todo['completed_at'] = datetime.now().isoformat()
        else:
            todo['completed_at'] = None
    
    save_todos(todos)
    return jsonify(todo)

@app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    """Elimina una tarea"""
    todos = load_todos()
    todo = next((t for t in todos if t.get('id') == todo_id), None)
    
    if not todo:
        return jsonify({'error': 'Tarea no encontrada'}), 404
    
    todos = [t for t in todos if t.get('id') != todo_id]
    save_todos(todos)
    
    return jsonify({'message': 'Tarea eliminada'})

@app.route('/api/todos/<int:todo_id>/complete', methods=['PUT'])
def complete_todo(todo_id):
    """Marca una tarea como completada"""
    todos = load_todos()
    todo = next((t for t in todos if t.get('id') == todo_id), None)
    
    if not todo:
        return jsonify({'error': 'Tarea no encontrada'}), 404
    
    todo['completed'] = True
    todo['completed_at'] = datetime.now().isoformat()
    save_todos(todos)
    
    return jsonify(todo)

@app.route('/api/todos/<int:todo_id>/pending', methods=['PUT'])
def pending_todo(todo_id):
    """Marca una tarea como pendiente"""
    todos = load_todos()
    todo = next((t for t in todos if t.get('id') == todo_id), None)
    
    if not todo:
        return jsonify({'error': 'Tarea no encontrada'}), 404
    
    todo['completed'] = False
    todo['completed_at'] = None
    save_todos(todos)
    
    return jsonify(todo)

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Obtiene estadísticas de las tareas"""
    todos = load_todos()
    
    total = len(todos)
    completed = len([t for t in todos if t.get('completed', False)])
    pending = total - completed
    high_priority = len([t for t in todos if t.get('priority') == 'high' and not t.get('completed', False)])
    
    progress = (completed / total * 100) if total > 0 else 0
    
    return jsonify({
        'total': total,
        'completed': completed,
        'pending': pending,
        'high_priority': high_priority,
        'progress': round(progress, 1)
    })

@app.route('/api/todos/clear-completed', methods=['DELETE'])
def clear_completed():
    """Limpia todas las tareas completadas"""
    todos = load_todos()
    initial_count = len(todos)
    todos = [t for t in todos if not t.get('completed', False)]
    removed = initial_count - len(todos)
    
    save_todos(todos)
    
    return jsonify({
        'message': f'{removed} tareas eliminadas',
        'removed': removed
    })

@app.route('/api/todos/export', methods=['GET'])
def export_todos():
    """Exporta las tareas"""
    todos = load_todos()
    
    response = {
        'data': todos,
        'export_date': datetime.now().isoformat(),
        'total_tasks': len(todos)
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
