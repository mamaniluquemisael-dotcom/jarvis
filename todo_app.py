import json
import os
from datetime import datetime
from pathlib import Path

class TodoApp:
    def __init__(self, storage_file="todos.json"):
        """Inicializa la aplicación de tareas con almacenamiento local"""
        self.storage_file = storage_file
        self.todos = []
        self.load_todos()
    
    def load_todos(self):
        """Carga las tareas del archivo local"""
        try:
            if os.path.exists(self.storage_file):
                with open(self.storage_file, 'r', encoding='utf-8') as f:
                    self.todos = json.load(f)
                print(f"✅ Se cargaron {len(self.todos)} tareas")
            else:
                self.todos = []
                print("📝 Archivo de tareas nuevo creado")
        except Exception as e:
            print(f"❌ Error al cargar tareas: {e}")
            self.todos = []
    
    def save_todos(self):
        """Guarda las tareas en el archivo local"""
        try:
            with open(self.storage_file, 'w', encoding='utf-8') as f:
                json.dump(self.todos, f, indent=2, ensure_ascii=False)
            print("💾 Tareas guardadas correctamente")
        except Exception as e:
            print(f"❌ Error al guardar tareas: {e}")
    
    def add_todo(self, title, description="", priority="normal"):
        """Añade una nueva tarea"""
        if not title.strip():
            print("⚠️  El título no puede estar vacío")
            return False
        
        todo = {
            "id": len(self.todos) + 1,
            "title": title.strip(),
            "description": description.strip(),
            "priority": priority.lower(),
            "completed": False,
            "created_at": datetime.now().isoformat(),
            "completed_at": None
        }
        
        self.todos.append(todo)
        self.save_todos()
        print(f"✨ Tarea añadida: '{title}' (ID: {todo['id']})")
        return True
    
    def list_todos(self, filter_type="all"):
        """Lista todas las tareas"""
        if not self.todos:
            print("\n📭 No hay tareas aún. ¡Añade una!")
            return
        
        filtered = self.todos
        if filter_type == "pending":
            filtered = [t for t in self.todos if not t["completed"]]
        elif filter_type == "completed":
            filtered = [t for t in self.todos if t["completed"]]
        
        if not filtered:
            print(f"\n📭 No hay tareas {filter_type}.")
            return
        
        print("\n" + "="*70)
        print(f"📋 TAREAS ({filter_type.upper()})")
        print("="*70)
        
        for todo in filtered:
            status = "✅" if todo["completed"] else "⏳"
            priority_emoji = self._get_priority_emoji(todo["priority"])
            
            print(f"\n{status} [{todo['id']}] {todo['title']}")
            print(f"   {priority_emoji} Prioridad: {todo['priority'].upper()}")
            
            if todo["description"]:
                print(f"   📝 {todo['description']}")
            
            created = datetime.fromisoformat(todo["created_at"]).strftime("%d/%m/%Y %H:%M")
            print(f"   📅 Creada: {created}")
            
            if todo["completed_at"]:
                completed = datetime.fromisoformat(todo["completed_at"]).strftime("%d/%m/%Y %H:%M")
                print(f"   ✔️ Completada: {completed}")
        
        print("\n" + "="*70)
    
    def mark_completed(self, todo_id):
        """Marca una tarea como completada"""
        for todo in self.todos:
            if todo["id"] == todo_id:
                if todo["completed"]:
                    print(f"⚠️  La tarea ya estaba completada")
                    return False
                
                todo["completed"] = True
                todo["completed_at"] = datetime.now().isoformat()
                self.save_todos()
                print(f"✅ Tarea '{todo['title']}' marcada como completada")
                return True
        
        print(f"❌ No se encontró tarea con ID {todo_id}")
        return False
    
    def mark_pending(self, todo_id):
        """Marca una tarea como pendiente"""
        for todo in self.todos:
            if todo["id"] == todo_id:
                if not todo["completed"]:
                    print(f"⚠️  La tarea ya estaba pendiente")
                    return False
                
                todo["completed"] = False
                todo["completed_at"] = None
                self.save_todos()
                print(f"⏳ Tarea '{todo['title']}' marcada como pendiente")
                return True
        
        print(f"❌ No se encontró tarea con ID {todo_id}")
        return False
    
    def delete_todo(self, todo_id):
        """Elimina una tarea"""
        for i, todo in enumerate(self.todos):
            if todo["id"] == todo_id:
                title = todo["title"]
                self.todos.pop(i)
                self.save_todos()
                print(f"🗑️  Tarea '{title}' eliminada")
                return True
        
        print(f"❌ No se encontró tarea con ID {todo_id}")
        return False
    
    def edit_todo(self, todo_id, title=None, description=None, priority=None):
        """Edita una tarea existente"""
        for todo in self.todos:
            if todo["id"] == todo_id:
                if title:
                    todo["title"] = title.strip()
                if description is not None:
                    todo["description"] = description.strip()
                if priority:
                    todo["priority"] = priority.lower()
                
                self.save_todos()
                print(f"✏️  Tarea {todo_id} actualizada")
                return True
        
        print(f"❌ No se encontró tarea con ID {todo_id}")
        return False
    
    def get_statistics(self):
        """Devuelve estadísticas de las tareas"""
        total = len(self.todos)
        completed = len([t for t in self.todos if t["completed"]])
        pending = total - completed
        
        high_priority = len([t for t in self.todos if t["priority"] == "high" and not t["completed"]])
        
        print("\n" + "="*70)
        print("📊 ESTADÍSTICAS")
        print("="*70)
        print(f"📌 Total de tareas: {total}")
        print(f"✅ Completadas: {completed}")
        print(f"⏳ Pendientes: {pending}")
        print(f"🔴 De alta prioridad sin completar: {high_priority}")
        
        if total > 0:
            percentage = (completed / total) * 100
            print(f"📈 Progreso: {percentage:.1f}%")
        
        print("="*70)
    
    def _get_priority_emoji(self, priority):
        """Devuelve emoji según la prioridad"""
        emojis = {
            "high": "🔴",
            "medium": "🟡",
            "low": "🟢"
        }
        return emojis.get(priority, "⚪")
    
    def clear_completed(self):
        """Elimina todas las tareas completadas"""
        initial_count = len(self.todos)
        self.todos = [t for t in self.todos if not t["completed"]]
        removed = initial_count - len(self.todos)
        
        if removed > 0:
            self.save_todos()
            print(f"🗑️  Se eliminaron {removed} tareas completadas")
        else:
            print("⚠️  No hay tareas completadas para eliminar")
    
    def export_todos(self, filename="todos_export.json"):
        """Exporta las tareas a un archivo JSON"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.todos, f, indent=2, ensure_ascii=False)
            print(f"📤 Tareas exportadas a '{filename}'")
            return True
        except Exception as e:
            print(f"❌ Error al exportar: {e}")
            return False
    
    def import_todos(self, filename):
        """Importa tareas desde un archivo JSON"""
        try:
            if not os.path.exists(filename):
                print(f"❌ El archivo '{filename}' no existe")
                return False
            
            with open(filename, 'r', encoding='utf-8') as f:
                imported = json.load(f)
            
            self.todos.extend(imported)
            self.save_todos()
            print(f"📥 Se importaron {len(imported)} tareas")
            return True
        except Exception as e:
            print(f"❌ Error al importar: {e}")
            return False


def interactive_menu():
    """Menú interactivo para la aplicación de tareas"""
    app = TodoApp()
    
    while True:
        print("\n" + "="*70)
        print("📝 APLICACIÓN DE TAREAS")
        print("="*70)
        print("1. ➕ Añadir nueva tarea")
        print("2. 📋 Ver todas las tareas")
        print("3. ⏳ Ver tareas pendientes")
        print("4. ✅ Ver tareas completadas")
        print("5. ✔️  Marcar como completada")
        print("6. ⏳ Marcar como pendiente")
        print("7. ✏️  Editar tarea")
        print("8. 🗑️  Eliminar tarea")
        print("9. 📊 Ver estadísticas")
        print("10. 🧹 Limpiar completadas")
        print("11. 📤 Exportar tareas")
        print("12. 📥 Importar tareas")
        print("0. 🚪 Salir")
        print("="*70)
        
        choice = input("\n¿Qué deseas hacer? (0-12): ").strip()
        
        if choice == "1":
            title = input("Título de la tarea: ").strip()
            description = input("Descripción (opcional): ").strip()
            priority = input("Prioridad (low/medium/high) [default: normal]: ").strip() or "normal"
            app.add_todo(title, description, priority)
        
        elif choice == "2":
            app.list_todos("all")
        
        elif choice == "3":
            app.list_todos("pending")
        
        elif choice == "4":
            app.list_todos("completed")
        
        elif choice == "5":
            app.list_todos("all")
            try:
                todo_id = int(input("\nID de la tarea a completar: "))
                app.mark_completed(todo_id)
            except ValueError:
                print("❌ ID inválido")
        
        elif choice == "6":
            app.list_todos("completed")
            try:
                todo_id = int(input("\nID de la tarea a marcar como pendiente: "))
                app.mark_pending(todo_id)
            except ValueError:
                print("❌ ID inválido")
        
        elif choice == "7":
            app.list_todos("all")
            try:
                todo_id = int(input("\nID de la tarea a editar: "))
                new_title = input("Nuevo título (dejar en blanco para no cambiar): ").strip()
                new_description = input("Nueva descripción (dejar en blanco para no cambiar): ").strip()
                new_priority = input("Nueva prioridad (dejar en blanco para no cambiar): ").strip()
                
                app.edit_todo(
                    todo_id,
                    new_title if new_title else None,
                    new_description if new_description else None,
                    new_priority if new_priority else None
                )
            except ValueError:
                print("❌ ID inválido")
        
        elif choice == "8":
            app.list_todos("all")
            try:
                todo_id = int(input("\nID de la tarea a eliminar: "))
                app.delete_todo(todo_id)
            except ValueError:
                print("❌ ID inválido")
        
        elif choice == "9":
            app.get_statistics()
        
        elif choice == "10":
            app.clear_completed()
        
        elif choice == "11":
            filename = input("Nombre del archivo (default: todos_export.json): ").strip() or "todos_export.json"
            app.export_todos(filename)
        
        elif choice == "12":
            filename = input("Nombre del archivo a importar: ").strip()
            app.import_todos(filename)
        
        elif choice == "0":
            print("\n👋 ¡Hasta luego!")
            break
        
        else:
            print("❌ Opción inválida. Por favor, intenta de nuevo.")


if __name__ == "__main__":
    interactive_menu()
