import os
import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia

wikipedia.set_lang("pt")
engine = pyttsx3.init("sapi5")
engine.setProperty('voice', engine.getProperty("voices")[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def get_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ouvindo...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Reconhecendo...")
        command = r.recognize_google(audio, language='pt-br')
        print("Usuário falou:" + command + "\n")
    except Exception as e:
        print(e)
        speak("Eu não entendo")
        return "None"
    return command

if __name__ == '__main__':
    speak("Amigo foi ativado ")
    speak("Como eu posso te ajudar?")
    while True:
        command = get_command().lower()
        if 'wikipédia' in command:
            speak("Procurando na Wikipedia ...")
            command = command.replace("wikipédia", '')
            command = command.replace("Procure na", '')
            results = wikipedia.summary(command, sentences=2)
            speak("De acordo com a Wikipédia")
            speak(results)
        elif 'como você vai' in command:
            speak("Olá amigo, eu vou bem, obrigado por perguntar")
        elif 'abrir youtube' in command:
            speak("Abrindo o Navegador com o youtube")
            webbrowser.open("youtube.com")
        elif 'abrir o google' in command:
            speak("Abrindo o google")
            webbrowser.open("google.com")
        elif 'abrir github' in command:
            speak("Abrindo o github")
            webbrowser.open("github.com")
        elif 'abrir o stackoverflow' in command:
            speak("Abrindo o stackoverflow")
            webbrowser.open("stackoverflow.com")
        elif 'abrir o spotify' in command:
            speak("Abrindo o spotify")
            webbrowser.open("spotify.com")
        elif 'abrir a calculadora' in command:
            speak("Abrindo a calculadora")
            loc = "C:\\Windows\\System32\\calc.exe"
            os.startfile(loc)
        elif 'abrir pasta c:' in command:
            speak("Abrindo o C:")
            webbrowser.open("D://")
        elif 'tchau' in command:
            speak("Tchau Tchau")
            exit(0)
