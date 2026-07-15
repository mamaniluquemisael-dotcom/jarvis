# 🤖 JARVIS - Asistente IA Personal

JARVIS es un asistente de voz inteligente inspirado en Iron Man, con capacidades de reconocimiento y síntesis de voz, integrado con IA de Groq.

## ✨ Características

- 🎤 **Reconocimiento de voz** en español
- 🔊 **Síntesis de voz** natural
- 🤖 **IA conversacional** con Groq
- ⏰ **Información útil** (hora, fecha, clima)
- 🌐 **Búsquedas en Google**
- 🎮 **Control de aplicaciones** (Chrome, Spotify)
- 😄 **Entretenimiento** (chistes, etc)

## 📋 Requisitos Previos

- Python 3.8+
- 🎤 Micrófono en tu computadora
- 🔊 Altavoces o auriculares
- 🌐 Conexión a internet
- API Key de Groq (gratuita)

## 🚀 Instalación

### 1. Clona el repositorio
```bash
git clone https://github.com/tu-usuario/jarvis.git
cd jarvis
```

### 2. Crea un entorno virtual (opcional pero recomendado)
```bash
python -m venv venv

# En Windows
venv\Scripts\activate

# En macOS/Linux
source venv/bin/activate
```

### 3. Instala las dependencias
```bash
pip install -r requirements.txt
```

### 4. Configura tu API Key de Groq

1. Ve a https://console.groq.com
2. Crea una cuenta (gratis)
3. Genera una nueva API Key
4. Copia el archivo `.env.example` a `.env`:
   ```bash
   cp .env.example .env
   ```
5. Edita `.env` y pega tu API Key:
   ```
   GROQ_API_KEY=tu-api-key-aqui
   ```

### 5. Ejecuta JARVIS
```bash
python jarvis.py
```

## 💬 Comandos de Ejemplo

| Comando | Resultado |
|---------|----------|
| "Hola" | Saluda y pregunta cómo ayudarte |
| "¿Qué hora es?" | Te dice la hora actual |
| "¿Cuál es la fecha?" | Te muestra la fecha |
| "¿Cómo está el clima?" | Muestra el clima actual |
| "Busca Python en Google" | Abre una búsqueda en Google |
| "Abre Chrome" | Abre el navegador |
| "Cuéntame un chiste" | Cuenta un chiste |
| "Adiós" | Se despide y cierra |
| Cualquier otra pregunta | Usa IA para responder |

## ⚙️ Configuración

Puedes personalizar JARVIS editando `jarvis.py`:

- **Velocidad de habla**: Cambia `engine.setProperty('rate', 150)`
- **Volumen**: Cambia `engine.setProperty('volume', 0.9)`
- **Idioma**: Modifica `language='es-ES'` en la función `listen()`
- **Nombre**: Cambia `self.name = "JARVIS"`

## 🔒 Seguridad

⚠️ **NUNCA** compartas tu `.env` o API Key públicamente.

El archivo `.env` está en `.gitignore` para proteger tus credenciales.

## 🐛 Solución de Problemas

### "No reconoce mi voz"
- Verifica que el micrófono esté conectado
- Aumenta el volumen
- Habla más cerca del micrófono

### "No tiene sonido"
- Verifica que los altavoces estén encendidos
- Aumenta el volumen en `engine.setProperty('volume', 1.0)`

### "Error de API Key"
- Verifica que la `.env` tenga tu API Key correcta
- Comprueba que tengas conexión a internet

## 📝 Licencia

Este proyecto es de código abierto. Úsalo libremente.

## 🤝 Contribuciones

¿Quieres mejorar JARVIS? ¡Haz un fork y envía un pull request!

---

**Hecho con ❤️ por Misael**