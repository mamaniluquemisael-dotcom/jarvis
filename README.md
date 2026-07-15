# 🤖 JARVIS - Asistente IA Personal + Gestor de Tareas

JARVIS es un proyecto completo que incluye un asistente de voz inteligente con IA y una aplicación web de gestión de tareas con almacenamiento local.

## 📦 Lo que Incluye

### 1. 🎤 Asistente JARVIS (CLI)
- Reconocimiento de voz en español
- Síntesis de voz natural
- IA conversacional con Groq
- Información útil (hora, fecha, clima)
- Búsquedas en Google
- Control de aplicaciones

**Archivo:** `jarvis.py`

```bash
python jarvis.py
```

### 2. 📝 Gestor de Tareas (CLI)
- Almacenamiento local en JSON
- Gestión completa de tareas
- Filtrado y estadísticas
- Exportación/importación

**Archivo:** `todo_app.py`

```bash
python todo_app.py
```

### 3. 🌐 Gestor de Tareas Web (Flask)
- Interfaz moderna y responsiva
- API REST completa
- Estadísticas en tiempo real
- Exportación de datos
- Diseño hermoso con gradientes

**Archivo:** `app.py`

```bash
python app.py
# Abre http://localhost:5000
```

## 🛠️ Instalación Rápida

### 1. Clona el repositorio
```bash
git clone https://github.com/mamaniluquemisael-dotcom/jarvis.git
cd jarvis
```

### 2. Crea entorno virtual (opcional)
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Instala dependencias
```bash
# Para CLI JARVIS
pip install -r requirements.txt

# Para versión web (adicional)
pip install -r requirements_web.txt
```

### 4. Configura API Key de Groq
```bash
# Copia el archivo de configuración
cp .env.example .env

# Edita .env y añade tu API key
# Obtén la key en: https://console.groq.com
```

## 🚀 Uso Rápido

### Opción 1: JARVIS (Asistente de Voz)
```bash
python jarvis.py
# Di: "Hola", "¿Qué hora es?", "Busca Python", etc.
```

### Opción 2: Gestor de Tareas (Terminal)
```bash
python todo_app.py
# Menú interactivo para gestionar tareas
```

### Opción 3: Gestor de Tareas Web
```bash
python app.py
# Abre http://localhost:5000 en tu navegador
```

## 📊 Estructura del Proyecto

```
jarvis/
├── jarvis.py                # Asistente de voz IA
├── todo_app.py             # Gestor de tareas CLI
├── app.py                  # Servidor Flask web
├── requirements.txt        # Dependencias CLI
├── requirements_web.txt    # Dependencias web
├── .env.example           # Plantilla de configuración
├── .gitignore             # Archivos a ignorar
├── README.md              # Este archivo
├── templates/
│   └── index.html         # Página web
├── static/
│   ├── css/
│   │   └── style.css      # Estilos web
│   └── js/
│       └── app.js         # Lógica JavaScript
└── todos.json             # Almacenamiento de tareas
```

## 🎯 Funcionalidades Detalladas

### 🗣️ JARVIS - Comandos
| Comando | Resultado |
|---------|----------|
| "Hola" | Saluda y pregunta cómo ayudar |
| "¿Qué hora es?" | Dice la hora actual |
| "¿Cuál es la fecha?" | Muestra la fecha |
| "¿Cómo está el clima?" | Clima actual |
| "Busca Python en Google" | Abre búsqueda |
| "Abre Chrome" | Abre navegador |
| "Cuéntame un chiste" | Cuenta un chiste |
| Cualquier pregunta | Responde con IA |

### 📋 Tareas - Funciones
- ➕ Crear tareas con prioridad (low, medium, high)
- 📋 Listar todas, pendientes o completadas
- ✔️ Marcar como completada/pendiente
- ✏️ Editar tareas
- 🗑️ Eliminar tareas
- 📊 Ver estadísticas
- 🧹 Limpiar completadas
- 📤 Exportar a JSON
- 📥 Importar desde JSON

### 🌐 Web - Características
- Interfaz moderna con gradientes
- Responsive (funciona en móvil)
- Estadísticas en tiempo real
- Filtros (todas, pendientes, completadas)
- Exportación de tareas
- API REST completa
- Almacenamiento local (JSON)

## ⚙️ Configuración Avanzada

### Personalizar JARVIS
```python
# En jarvis.py
engine.setProperty('rate', 150)        # Velocidad de habla
engine.setProperty('volume', 0.9)      # Volumen
self.user_name = "Sir"                  # Tu nombre
```

### Cambiar Puerto Web
```python
# En app.py
if __name__ == '__main__':
    app.run(debug=True, port=8000)  # Cambiar puerto aquí
```

## 🔐 Seguridad

⚠️ **IMPORTANTE:**
- Nunca compartas tu `.env` o API Key
- El archivo `.env` está en `.gitignore`
- Usa variables de entorno para credenciales

## 📱 Requisitos

### Para JARVIS (Voz)
- Python 3.8+
- 🎤 Micrófono
- 🔊 Altavoces/Auriculares
- 🌐 Conexión a internet
- API Key de Groq (gratis)

### Para Web
- Python 3.8+
- Navegador moderno
- 🌐 Conexión a internet (solo para IA)

## 🆘 Solución de Problemas

### "No reconoce mi voz"
- Verifica que el micrófono esté conectado
- Acércate al micrófono
- Habla claro en español

### "No tiene sonido"
- Verifica altavoces encendidos
- Aumenta volumen: `engine.setProperty('volume', 1.0)`

### "Error de API Key"
- Verifica que `.env` existe
- Comprueba que la key es correcta
- Obtén nueva key en https://console.groq.com

### "Puerto 5000 en uso"
- Cambia puerto en `app.py`: `port=8000`
- O cierra la aplicación usando el puerto

## 📝 Ejemplos de Uso

### Crear una tarea en web
1. Abre http://localhost:5000
2. Escribe título: "Aprender Python"
3. Descripción: "Estudiar listas y diccionarios"
4. Prioridad: "Alta"
5. Click en "Añadir Tarea"

### Usar JARVIS para búsquedas
```
Tú: "Busca recetas de pasta en Google"
JARVIS: "Abriendo Google..."
```

### Exportar tareas
- Desde CLI: opción 11
- Desde Web: botón "Exportar"
- Genera archivo: `tareas_YYYY-MM-DD.json`

## 🤝 Contribuciones

¿Quieres mejorar JARVIS?
1. Fork el repositorio
2. Crea una rama: `git checkout -b feature/mifeature`
3. Commit: `git commit -am 'Add mifeature'`
4. Push: `git push origin feature/mifeature`
5. Abre un Pull Request

## 📚 Tecnologías Utilizadas

- **Backend:** Flask, Groq API
- **Frontend:** HTML5, CSS3, JavaScript
- **Voz:** pyttsx3, SpeechRecognition
- **Almacenamiento:** JSON local
- **APIs:** Google Search, wttr.in (clima)

## 📄 Licencia

Este proyecto es de código abierto. Úsalo libremente.

## 👨‍💻 Autor

Creado por **mamaniluquemisael-dotcom**

---

**¡Disfruta usando JARVIS! 🚀**

Tienes preguntas? Abre un [issue](https://github.com/mamaniluquemisael-dotcom/jarvis/issues)
