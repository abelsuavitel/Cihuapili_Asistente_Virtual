import speech_recognition as sr
import sys, pyjokes, pyttsx3, pyautogui, subprocess
import win32gui, win32con


#Saludo
Saludo = "Hola Señor Cruz, un gusto estar aqui para servirle"
OidosCihuapili = sr.Recognizer()

# Ordenes para Cihuapili:
def broma():
        bromilla = pyjokes.get_joke(language="es", category="all")
        pyttsx3.speak(bromilla)

def Cierre():
    pyttsx3.speak("Hasta la proxima, señor")
    Widget.terminate()
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

def Esconderse():
    EsconderWidget = win32gui.FindWindow(None, "Cihuapilli")
    if EsconderWidget:
        pyttsx3.speak("Chao")
        win32gui.ShowWindow(EsconderWidget, win32con.SW_HIDE)
    else:
        pyttsx3.speak("No puedo esconderme, señor")

def AbrirWidget():
    AparecerWodget = win32gui.FindWindow(None, "Cihuapilli")
    if AparecerWodget:
        win32gui.ShowWindow(AparecerWodget, win32con.SW_SHOW)
        pyttsx3.speak("Hola otra vez!!!!")

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
    elif "pili abajo" in peronomegrites:
        Esconderse()
    elif "pili ven" in peronomegrites:
        AbrirWidget()

def escuchar_orden():
    with sr.Microphone() as source:
        OidosCihuapili.adjust_for_ambient_noise(source)
        audio = OidosCihuapili.listen(source)
    try:
        orden = OidosCihuapili.recognize_google(audio, language="es-ES")
        print(orden)
        realizar_orden(orden)
    except sr.UnknownValueError:
        pass

Widget = subprocess.Popen(["python", r"C:\Users\Abel\Desktop\+Ultra\Cihuapilli\Cihuapili_Widget.py"])
pyttsx3.speak(Saludo)
while True:
    escuchar_orden()