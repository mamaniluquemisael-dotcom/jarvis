class TodoApp {
    constructor() {
        this.todos = [];
        this.currentFilter = 'all';
        this.init();
    }

    async init() {
        this.setupEventListeners();
        await this.loadTodos();
        await this.updateStats();
    }

    setupEventListeners() {
        // Form
        document.getElementById('addTodoForm').addEventListener('submit', (e) => this.handleAddTodo(e));

        // Filters
        document.querySelectorAll('.filter-btn').forEach(btn => {
            btn.addEventListener('click', (e) => this.handleFilter(e));
        });

        // Action buttons
        document.getElementById('clearCompletedBtn').addEventListener('click', () => this.clearCompleted());
        document.getElementById('exportBtn').addEventListener('click', () => this.exportTodos());
    }

    async loadTodos() {
        try {
            const response = await fetch(`/api/todos?filter=${this.currentFilter}`);
            this.todos = await response.json();
            this.render();
        } catch (error) {
            console.error('Error al cargar tareas:', error);
        }
    }

    async handleAddTodo(e) {
        e.preventDefault();

        const title = document.getElementById('todoTitle').value.trim();
        const description = document.getElementById('todoDescription').value.trim();
        const priority = document.getElementById('todoPriority').value;

        if (!title) {
            alert('Por favor, ingresa un título');
            return;
        }

        try {
            const response = await fetch('/api/todos', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ title, description, priority })
            });

            if (response.ok) {
                document.getElementById('addTodoForm').reset();
                await this.loadTodos();
                await this.updateStats();
                this.showNotification('✨ Tarea añadida correctamente');
            }
        } catch (error) {
            console.error('Error al añadir tarea:', error);
            this.showNotification('❌ Error al añadir la tarea', 'error');
        }
    }

    async handleFilter(e) {
        const filterType = e.target.dataset.filter;
        this.currentFilter = filterType;

        document.querySelectorAll('.filter-btn').forEach(btn => {
            btn.classList.remove('active');
        });
        e.target.classList.add('active');

        await this.loadTodos();
    }

    async toggleTodo(todoId, completed) {
        try {
            const endpoint = completed ? 'complete' : 'pending';
            const response = await fetch(`/api/todos/${todoId}/${endpoint}`, {
                method: 'PUT'
            });

            if (response.ok) {
                await this.loadTodos();
                await this.updateStats();
            }
        } catch (error) {
            console.error('Error al actualizar tarea:', error);
        }
    }

    async deleteTodo(todoId) {
        if (!confirm('¿Estás seguro de que deseas eliminar esta tarea?')) return;

        try {
            const response = await fetch(`/api/todos/${todoId}`, {
                method: 'DELETE'
            });

            if (response.ok) {
                await this.loadTodos();
                await this.updateStats();
                this.showNotification('🗑️ Tarea eliminada');
            }
        } catch (error) {
            console.error('Error al eliminar tarea:', error);
        }
    }

    async clearCompleted() {
        if (!confirm('¿Eliminar todas las tareas completadas?')) return;

        try {
            const response = await fetch('/api/todos/clear-completed', {
                method: 'DELETE'
            });

            if (response.ok) {
                const data = await response.json();
                await this.loadTodos();
                await this.updateStats();
                this.showNotification(`🧹 ${data.removed} tareas eliminadas`);
            }
        } catch (error) {
            console.error('Error al limpiar:', error);
        }
    }

    async updateStats() {
        try {
            const response = await fetch('/api/stats');
            const stats = await response.json();

            document.getElementById('stat-total').textContent = stats.total;
            document.getElementById('stat-completed').textContent = stats.completed;
            document.getElementById('stat-pending').textContent = stats.pending;
            document.getElementById('stat-high-priority').textContent = stats.high_priority;
            document.getElementById('progress-percent').textContent = stats.progress;
            document.getElementById('progress-fill').style.width = stats.progress + '%';
        } catch (error) {
            console.error('Error al cargar estadísticas:', error);
        }
    }

    async exportTodos() {
        try {
            const response = await fetch('/api/todos/export');
            const data = await response.json();

            const jsonString = JSON.stringify(data, null, 2);
            const blob = new Blob([jsonString], { type: 'application/json' });
            const url = URL.createObjectURL(blob);

            const link = document.createElement('a');
            link.href = url;
            link.download = `tareas_${new Date().toISOString().split('T')[0]}.json`;
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
            URL.revokeObjectURL(url);

            this.showNotification('📤 Tareas exportadas correctamente');
        } catch (error) {
            console.error('Error al exportar:', error);
            this.showNotification('❌ Error al exportar', 'error');
        }
    }

    render() {
        const todosList = document.getElementById('todosList');

        if (this.todos.length === 0) {
            todosList.innerHTML = '<li class="empty-state"><p>📭 No hay tareas. ¡Añade una para empezar!</p></li>';
            return;
        }

        todosList.innerHTML = this.todos.map(todo => this.createTodoElement(todo)).join('');
    }

    createTodoElement(todo) {
        const createdDate = new Date(todo.created_at).toLocaleDateString('es-ES');
        const priorityEmoji = this.getPriorityEmoji(todo.priority);

        return `
            <li class="todo-item ${todo.completed ? 'completed' : ''}">
                <input 
                    type="checkbox" 
                    class="todo-checkbox" 
                    ${todo.completed ? 'checked' : ''}
                    onchange="app.toggleTodo(${todo.id}, this.checked)"
                >
                <div class="todo-content">
                    <div class="todo-title">${this.escapeHtml(todo.title)}</div>
                    ${todo.description ? `<div class="todo-description">${this.escapeHtml(todo.description)}</div>` : ''}
                    <div class="todo-meta">
                        <span class="priority-badge priority-${todo.priority}">${priorityEmoji} ${todo.priority.toUpperCase()}</span>
                        <span>📅 ${createdDate}</span>
                        ${todo.completed_at ? `<span>✔️ Completada</span>` : ''}
                    </div>
                </div>
                <div class="todo-actions">
                    <button class="delete-btn" onclick="app.deleteTodo(${todo.id})">🗑️</button>
                </div>
            </li>
        `;
    }

    getPriorityEmoji(priority) {
        const emojis = {
            'high': '🔴',
            'medium': '🟡',
            'low': '🟢'
        };
        return emojis[priority] || '⚪';
    }

    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    showNotification(message, type = 'success') {
        console.log(message);
        // Aquí puedes implementar un sistema de notificaciones visual
    }
}

// Inicializar la aplicación
let app;
document.addEventListener('DOMContentLoaded', () => {
    app = new TodoApp();
});
