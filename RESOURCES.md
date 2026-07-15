📦 JARVIS - Recursos Útiles

## 🔗 Enlaces Importantes

- **Groq API:** https://console.groq.com
  - Obtén tu API Key gratis
  - 10,000 requests/día

- **Repositorio:** https://github.com/mamaniluquemisael-dotcom/jarvis

## 📚 Documentación

### Librerías Utilizadas

**Voz y Audio:**
- `pyttsx3` - Síntesis de texto a voz
  https://pyttsx3.readthedocs.io/
- `SpeechRecognition` - Reconocimiento de voz
  https://github.com/Uberi/speech_recognition

**Web:**
- `Flask` - Framework web
  https://flask.palletsprojects.com/
- `Flask-CORS` - CORS para Flask
  https://flask-cors.readthedocs.io/

**APIs:**
- `Groq` - IA conversacional
  https://console.groq.com/docs
- `requests` - HTTP client
  https://requests.readthedocs.io/

**Datos:**
- `python-dotenv` - Manejo de variables de entorno
  https://python-dotenv.readthedocs.io/

## 🎓 Tutoriales

### Crear tu primer JARVIS
1. Clona el repo
2. Instala dependencias
3. Configura .env
4. Ejecuta `python jarvis.py`

### Personalizar JARVIS
- Edita `jarvis.py`
- Cambia velocidad: `engine.setProperty('rate', 150)`
- Añade nuevos comandos en `process_command()`

### Desplegar Web en Producción
1. Usa Gunicorn: `pip install gunicorn`
2. Ejecuta: `gunicorn -w 4 app:app`
3. Usa Nginx como reverse proxy

## 🐛 Debugging

### Ver logs de JARVIS
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Probar API REST
```bash
curl http://localhost:5000/api/todos
curl -X POST http://localhost:5000/api/todos -d '{"title":"Test"}' -H 'Content-Type: application/json'
```

## 💡 Tips

1. **Mejorar reconocimiento de voz:**
   - Habla en ambiente silencioso
   - Acércate al micrófono
   - Habla lentamente

2. **Usar JARVIS como servicio:**
   - Crea un archivo .bat/.sh
   - Programa ejecución automática

3. **Sincronizar tareas:**
   - Exporta desde CLI
   - Importa en Web
   - Usa JSON como intermediario

## ❓ Preguntas Frecuentes

**¿Necesito internet?**
Solo para la IA (Groq) y búsquedas. Las tareas funcionan offline.

**¿Qué SO soporta?**
Windows, macOS, Linux

**¿Es gratis?**
Sí, con límites de Groq (10k requests/día)

**¿Puedo añadir base de datos?**
Sí, edita `save_todos()` y `load_todos()`

## 🚀 Roadmap

- [ ] Autenticación de usuarios
- [ ] Base de datos PostgreSQL
- [ ] App móvil
- [ ] Notificaciones por email
- [ ] Temas personalizados
- [ ] Compartir tareas
- [ ] Historial de voz
- [ ] Integración con calendario

---

¡Gracias por usar JARVIS! 💜
