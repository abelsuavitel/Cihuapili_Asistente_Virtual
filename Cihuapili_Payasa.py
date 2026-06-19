import speech_recognition as sr
import sys
import pyjokes
import pyttsx3
import pyautogui

OidosCihuapili = sr.Recognizer()

# Ordenes para Cihuapili:
def broma():
        bromilla = pyjokes.get_joke(language="es", category="all")
        pyttsx3.speak(bromilla)

def Cierre():
    pyttsx3.speak("Adios Licenciado, hasta mañana")
    sys.exit()

def Pausa():
    pyttsx3.speak("Pausa")
    pyautogui.press("playpause")

def Siguiente():
    pyttsx3.speak("¿que te parece esta?")
    pyautogui.press("nexttrack")

def Anterior():
    pyttsx3.speak("Regresando")
    pyautogui.press("prevtrack")
    pyautogui.press("prevtrack")


# Funcion para realizar las ordenes:
def realizar_orden(orden):
    peronomegrites = orden.lower()
    if "pili bromilla" in peronomegrites:
        broma()
    elif "adiós" in peronomegrites:
        Cierre()
    elif "pili pausa" in peronomegrites:
        Pausa()
    elif "pili siguiente" in peronomegrites:
        Siguiente()
    elif "pili anterior" in peronomegrites:
        Anterior()

def escuchar_orden():
    with sr.Microphone() as source:
        OidosCihuapili.adjust_for_ambient_noise(source)
        audio = OidosCihuapili.listen(source)
    try:
        orden = OidosCihuapili.recognize_google(audio, language="es-ES")
        realizar_orden(orden)
    except sr.UnknownValueError:
        pass

while True:
    escuchar_orden()