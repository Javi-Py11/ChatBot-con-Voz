from time import sleep
import speech_recognition as sr
import pyttsx3
import requests
import pywhatkit as rep
from datetime import datetime

# Inicializar el motor de síntesis de voz
engine = pyttsx3.init()

# Función para reproducir videos de YouTube
def play_youtube_video(categoria):
    rep.playonyt(categoria)

# Función para obtener la hora actual
def get_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return f"Son las {current_time}"

# Función para obtener el clima
def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    weather_data = response.json()
    if weather_data.get("cod") != 200:
        return "Lo siento, no puedo obtener el pronostico del tiempo"
    temp = weather_data["main"]["temp"]
    description = weather_data["weather"][0]["description"]
    return f"El clima en la ciudad de {city} es {description} con una temperatura de {temp} grados celcius."

# Función para convertir texto a voz
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Función para reconocer la voz
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            return text.lower()
        except sr.UnknownValueError:
            return "Lo siento, no entendi lo que dijiste"
        except sr.RequestError:
            return "Lo siento mi servicio esta caido"

# API key de OpenWeatherMap
api_key = "2755ae4140ac80b4006f2f8209e8515f"

# Función principal del chatbot
def chatbot():
    speak("Hola me llamo Viernes, Como puedo ayudarte hoy?")
    while True:
        command = recognize_speech()
        print(f"Tu acabas de decir: {command}")
        
        if "viernes" in command:
            speak("Que puedo hacer por ti?")
            while True:
                
                command = recognize_speech()   
            
                sleep(3)
                
                if "hora" in command:
                    time_info = get_time()
                    speak(time_info)
                    break
                elif "clima" in command:
                    speak("Por favor, dame el nombre de la ciudad.")
                    city = recognize_speech()
                    weather_info = get_weather(api_key, city)
                    speak(weather_info)
                    break
                elif "video" in command:
                    speak("Por favor ,dime que quieres buscar en youtube")
                    url = recognize_speech()
                    play_youtube_video(url)
                    speak("Reproduciendo el video.")
                    break
                elif "adios" in command:
                    speak("Nos vemos pronto!")
                    exit()
                #else:
                    #speak("Lo siento, solo estoy programado con el clima , la hora , para reproducir musica y video")

if __name__ == "__main__":
    chatbot()
