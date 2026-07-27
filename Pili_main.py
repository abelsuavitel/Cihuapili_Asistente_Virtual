import speech_recognition as sr
import sys, pyjokes, pyttsx3, pyautogui, subprocess, random
import win32gui, win32con


class CihuapiliPayasa:

    SALUDO = [
        "¿Que tal señor? ¿Como se encuentra hoy?",
        "Buenas! Espero que este teniendo un excelente dia",
        "Camara mi todo licenciado, ¿Que pedo, como andamos? ",
        "Hola señor, hoy esta mas guapo de lo normal",
        "Encendido y listo para el servicio"
    ]
    SALUDORANDOM = random.choice(SALUDO)
    WIDGET_PATH = "Pili_Widget.py"

    def __init__(self):
        self.oidos = sr.Recognizer()
        self.widget = subprocess.Popen(["python", self.WIDGET_PATH])
        pyttsx3.speak(self.SALUDORANDOM)

    # --- Órdenes ---

    def broma(self):
        bromilla = pyjokes.get_joke(language="es", category="all")
        pyttsx3.speak(bromilla)

    def cierre(self):
        DESPEDIDA = [
            "Hasta la proxima, señor",
            "Nos vemos guapo...,"
            "Ha sido un gusto, adios",
            "NO OLVIDEIS DEJAR UN LIKE, COMENTAR  Y SUSCRIBIRSE"
        ]
        DESPEDIDARANDOM = random.choice(DESPEDIDA)
        pyttsx3.speak(DESPEDIDARANDOM)
        self.widget.terminate()
        sys.exit()

    def pausa(self):
        pyttsx3.speak("Pausa")
        pyautogui.press("playpause")

    def siguiente(self):
        SIGUIENTE = [
            "Cambiando de ritmo",
            "¿Que te parece esta?",
            "Deleitate con esta cancion",
            "Espero que la siguiente rola te encante tanto como a mi"
        ]
        SIGUIENTERANDOM = random.choice(SIGUIENTE)
        pyttsx3.speak(SIGUIENTERANDOM)
        pyautogui.press("nexttrack")

    def anterior(self):
        pyttsx3.speak("Regresando")
        pyautogui.press("prevtrack")
        pyautogui.press("prevtrack")

    def Repetir(self):
        pyttsx3.speak("Otra, Otra, Otra")
        pyautogui.press("prevtrack")

    def VolumenMaximo(self):
        pyttsx3.speak("QUE SE ESCUCHE BIEN FUERTEEEEEE")
        for _ in range(50):
            pyautogui.press("volumeup")


    def VolumenMinimo(self):
        pyttsx3.speak("si, ok, entiendo...")
        for _ in range(50):
            pyautogui.press("volumedown")


    def Bloquear(self):
        pyttsx3.speak("Bloqueo, Bloqueo, Bloqueo")
        pyautogui.hotkey("win", "l")

    def esconderse(self):
        ventana = win32gui.FindWindow(None, "Cihuapilli")
        if ventana:
            pyttsx3.speak("Chao")
            win32gui.ShowWindow(ventana, win32con.SW_HIDE)
        else:
            pyttsx3.speak("No puedo esconderme, señor")

    def aparecer(self):
        ventana = win32gui.FindWindow(None, "Cihuapilli")
        if ventana:
            win32gui.ShowWindow(ventana, win32con.SW_SHOW)
            pyttsx3.speak("Hola otra vez!!!!")

    # --- Lógica principal ---

    def realizar_orden(self, orden):
        orden = orden.lower()
        comandos = {
            "pili bromilla": self.broma,
            "adiós":         self.cierre,
            "pili pausa":    self.pausa,
            "pili siguiente": self.siguiente,
            "pili anterior": self.anterior,
            "pili abajo":    self.esconderse,
            "pili ven":      self.aparecer,
            "pili repítela": self.Repetir,
            "pili bloquear": self.Bloquear,
            "pili súbele":   self.VolumenMaximo,
            "pili cállate": self.VolumenMinimo,
        }
        for clave, accion in comandos.items():
            if clave in orden:
                accion()
                break

    def escuchar_orden(self):
        with sr.Microphone() as source:
            self.oidos.adjust_for_ambient_noise(source)
            audio = self.oidos.listen(source)
        try:
            orden = self.oidos.recognize_google(audio, language="es-ES")
            print(orden)
            self.realizar_orden(orden)
        except sr.UnknownValueError:
            pass

    def iniciar(self):
        while True:
            self.escuchar_orden()


if __name__ == "__main__":
    CihuapiliPayasa().iniciar()