import speech_recognition as sr
import sys, pyjokes, pyttsx3, pyautogui, subprocess, random, pywhatkit
import win32gui, win32con


class RubiPayasa:

    SALUDO = [
        "¿Que tal señor? ¿Como se encuentra hoy?",
        "Buenas! Espero que este teniendo una excelente tarde",
        "Camara mi todo licenciado, ¿Que pedo, como andamos? ",
        "Hola señor, hoy esta mas guapo de lo normal",
        "Encendida y listo para el servicio"
    ]
    WIDGET_PATH = "Rubi_Widget.py"

    def __init__(self):
        self.oidos = sr.Recognizer()
        self.widget = subprocess.Popen(["python", self.WIDGET_PATH])
        self.estado = "llamado"
        saludo_random = random.choice(self.SALUDO)
        pyttsx3.speak(saludo_random)

    # --- Órdenes ---

    def broma(self):
        bromilla = pyjokes.get_joke(language="es", category="all")
        pyttsx3.speak(bromilla)

    def cierre(self):
        DESPEDIDA = [
            "Hasta la proxima, señor",
            "Nos vemos guapo...",
            "Ha sido un gusto, adios",
            "NO OLVIDEIS DEJAR UN LIKE, COMENTAR Y SUSCRIBIRSE"
        ]
        despedida_random = random.choice(DESPEDIDA)
        pyttsx3.speak(despedida_random)
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
        siguiente_random = random.choice(SIGUIENTE)
        pyttsx3.speak(siguiente_random)
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
        ventana = win32gui.FindWindow(None, "Rubi")
        if ventana:
            pyttsx3.speak("Chao")
            win32gui.ShowWindow(ventana, win32con.SW_HIDE)
        else:
            pyttsx3.speak("No puedo esconderme, señor")

    def aparecer(self):
        ventana = win32gui.FindWindow(None, "Rubi")
        if ventana:
            win32gui.ShowWindow(ventana, win32con.SW_SHOW)
            pyttsx3.speak("Hola otra vez!!!!")

    def cancelar(self):
        Cancelada = [
                "Saquese pues",
                "ash",
                "entonces no estes chingando"
                ]
        siguiente_random = random.choice(Cancelada)
        pyttsx3.speak(siguiente_random)

    def mensaje(self):
        texto = "pilin"
        contacto = "+5215624907455"
        hora = 23
        minuto = 10
        pyttsx3.speak("conectando con la madre nodrisa")
        pywhatkit.sendwhatmsg(contacto, texto, hora, minuto)
        
    
    # --- Lógica principal ---

    def realizar_orden(self, orden):
        orden = orden.lower()
        comandos = {
            "bromilla": self.broma,
            "adiós": self.cierre,
            "pausa": self.pausa,
            "siguiente": self.siguiente,
            "anterior": self.anterior,
            "abajo": self.esconderse,
            "ven": self.aparecer,
            "repítela": self.Repetir,
            "bloquear": self.Bloquear,
            "súbele": self.VolumenMaximo,
            "cállate": self.VolumenMinimo,
            "mensaje": self.mensaje,
            "olvídalo": self.cancelar,
        }
        for clave, accion in comandos.items():
            if clave in orden:
                accion()
                break


    # --- Estado de la IA ---

    def estado_orden(self):
        with sr.Microphone() as source:
            self.oidos.adjust_for_ambient_noise(source)
            audio = self.oidos.listen(source)
        try:
            orden = self.oidos.recognize_google(audio, language="es-ES")
            print("orden", orden)
            self.realizar_orden(orden)
        except sr.UnknownValueError:
            pass
        finally:
            self.estado = "llamado"

    def estado_invocacion(self):
        with sr.Microphone() as source:
            self.oidos.adjust_for_ambient_noise(source)
            audio = self.oidos.listen(source)
        try:
            invocacion = self.oidos.recognize_google(audio, language="es-ES")
            print("invocacion", invocacion)
            if invocacion == "Rubí":
                FrasesInvocacion = [
                    "cocha pacha?",
                    "Mandeme?",
                    "Que quieres Buuuey?",
                    "Huh?",
                    "En que puedo ayudarte?",
                    "Que necesitas Señor?",
                    "Para que soy buena?",
                    ]
                frase_invocacion_random = random.choice(FrasesInvocacion)
                pyttsx3.speak(frase_invocacion_random)
                self.estado = "orden"
        except sr.UnknownValueError:
            pass

    def cambiar_estado(self):
        while True:
            if self.estado == "llamado":
                self.estado_invocacion()
            elif self.estado == "orden":
                self.estado_orden()


if __name__ == "__main__":
    rubi = RubiPayasa()
    rubi.cambiar_estado()