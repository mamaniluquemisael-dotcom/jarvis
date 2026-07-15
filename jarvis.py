import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
from dotenv import load_dotenv
from groq import Groq
import requests

# Cargar variables de entorno
load_dotenv()

# Inicializar el motor de texto a voz
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Velocidad de habla
engine.setProperty('volume', 0.9)  # Volumen

# Inicializar el reconocedor de voz
recognizer = sr.Recognizer()

# Inicializar cliente de Groq para IA conversacional
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

class Jarvis:
    def __init__(self):
        self.name = "JARVIS"
        self.user_name = "Sir"
        
    def speak(self, text):
        """Convierte texto a voz"""
        print(f"🎤 {self.name}: {text}")
        engine.say(text)
        engine.runAndWait()
    
    def listen(self):
        """Escucha y reconoce voz del usuario"""
        try:
            with sr.Microphone() as source:
                print("🎧 Escuchando...")
                recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = recognizer.listen(source, timeout=5)
            
            print("🔍 Procesando audio...")
            text = recognizer.recognize_google(audio, language='es-ES')
            print(f"👤 Tú: {text}")
            return text.lower()
        
        except sr.UnknownValueError:
            self.speak("Disculpe, no entendí lo que dijo.")
            return None
        except sr.RequestError:
            self.speak("No tengo acceso a internet en este momento.")
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def get_weather(self, city="Madrid"):
        """Obtiene el clima actual"""
        try:
            response = requests.get(f"https://wttr.in/{city}?format=3")
            return response.text
        except:
            return "No pude obtener el clima."
    
    def get_time(self):
        """Devuelve la hora actual"""
        now = datetime.datetime.now()
        return now.strftime("%H:%M:%S")
    
    def get_date(self):
        """Devuelve la fecha actual"""
        today = datetime.datetime.now()
        return today.strftime("%d de %B de %Y")
    
    def search_web(self, query):
        """Busca en Google"""
        search_url = f"https://www.google.com/search?q={query}"
        webbrowser.open(search_url)
        self.speak(f"Buscando {query} en Google")
    
    def ask_groq(self, prompt):
        """Usa la IA de Groq para responder preguntas"""
        try:
            message = client.messages.create(
                model="mixtral-8x7b-32768",
                max_tokens=1024,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )
            return message.content[0].text
        except Exception as e:
            return f"Error al conectar con la IA: {e}"
    
    def process_command(self, command):
        """Procesa comandos del usuario"""
        if not command:
            return
        
        # Comandos de saludo
        if any(word in command for word in ['hola', 'buenos días', 'buenas noches', 'buenas tardes']):
            self.speak(f"Buenos días {self.user_name}. ¿Cómo puedo ayudarle?")
        
        # Preguntar la hora
        elif any(word in command for word in ['hora', 'qué hora es']):
            time = self.get_time()
            self.speak(f"Son las {time}")
        
        # Preguntar la fecha
        elif any(word in command for word in ['fecha', 'qué día es', 'cuál es la fecha']):
            date = self.get_date()
            self.speak(f"Hoy es {date}")
        
        # Clima
        elif 'clima' in command or 'tiempo' in command:
            weather = self.get_weather()
            self.speak(f"El clima actual es: {weather}")
        
        # Búsqueda web
        elif 'busca' in command or 'google' in command:
            query = command.replace('busca', '').replace('en google', '').strip()
            self.search_web(query)
        
        # Abrir aplicaciones
        elif 'abre' in command:
            if 'chrome' in command or 'navegador' in command:
                if os.name == 'nt':
                    os.startfile('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')
                else:
                    os.system('open -a "Google Chrome"')
                self.speak("Abriendo Chrome")
            elif 'spotify' in command:
                if os.name == 'nt':
                    os.startfile('spotify:')
                else:
                    os.system('open -a Spotify')
                self.speak("Abriendo Spotify")
        
        # Chiste
        elif 'cuéntame un chiste' in command:
            self.speak("¿Por qué los libros de matemáticas están siempre tristes? Porque tienen muchos problemas.")
        
        # Despedida
        elif any(word in command for word in ['adiós', 'hasta luego', 'apágate', 'desconecta']):
            self.speak(f"Adiós {self.user_name}. Ha sido un placer servir.")
            exit()
        
        # Para cualquier otra pregunta, usa IA
        else:
            self.speak("Consultando con la IA...")
            response = self.ask_groq(command)
            self.speak(response)
    
    def run(self):
        """Inicia el asistente"""
        self.speak("Buenos días. Soy JARVIS, su asistente personal. ¿Cómo puedo ayudarle?")
        
        while True:
            command = self.listen()
            if command:
                self.process_command(command)

if __name__ == "__main__":
    jarvis = Jarvis()
    jarvis.run()