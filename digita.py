import os
import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia

engine = pyttsx3.init("sapi5")
engine.setProperty('voice', engine.getProperty("voices")[0].id)
wikipedia.set_lang("pt")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def getCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ouvindo")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Reconhecendo")
        command = r.recognize_google(audio, language='pt-br')
        print("usuário falou: " + command + "\n")
    except Exception as e:
        print(e)
        speak("Não entendi")
        return ""
    return command

if __name__ == "__main__":
    speak("Assistente Digita foi ativada")
    speak("Como eu posso te ajudar?")

    while(True):
        command = getCommand().lower()
        if 'wikipédia' in command:
            command = command.replace("wikipédia","")
            command = command.replace("procure na","")
            command = command.replace("pesquise na","")

            results = wikipedia.summary(command, sentences=2)
            speak("De Acordo com a Wikipédia")
            speak(results)
        elif 'youtube' in command:
            speak("Abrindo o Youtube")
            webbrowser.open("youtube.com")
            exit(0)
        elif 'google' in command:
            speak("Abrindo o Google")
            webbrowser.open("google.com")
            exit(0)
        elif 'c2 pontos' in command:
            speak("Abrindo o C:")
            webbrowser.open("C://")
        elif 'calculadora' in command:
            speak("Abrindo a Calculadora")
            loc = "C:\\Windows\\System32\\calc.exe"
            os.startfile(loc)
        elif 'tchau' in command:
            speak("Tchau Tchau")
            exit(0)
