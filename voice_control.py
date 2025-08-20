import speech_recognition as sr
import pyttsx3
import webbrowser
import os
from datetime import datetime

# Initialize Text-to-Speech engine once
engine = pyttsx3.init()
engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # male voice

# Speak function
def speak(text):
    print("🤖 Assistant:", text)
    engine.say(text)
    engine.runAndWait()   # make sure speech is spoken fully

# Listen function
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=7)

    try:
        print("⏳ Recognizing...")
        command = r.recognize_google(audio, language="en-in")
        print(f"👉 You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        speak("Speech service is down, check your internet.")
        return ""
    except Exception as e:
        print("Error:", e)
        return ""

# Main Loop
def run_assistant():
    speak("Hello, I am your assistant. How can I help you?")
    while True:
        command = listen()

        if not command:
            continue

        # Commands
        if "your name" in command:
             speak(f"My name is  Voice assistant. How can I help you?")

        elif "time" in command:
            time = datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {time}")

        elif "date" in command:
            date = datetime.now().strftime("%d %B %Y")
            speak(f"Today's date is {date}")

        elif "open google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif "open youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif "open notepad" in command:
            speak("Opening Notepad")
            os.system("notepad.exe")

        elif "joke" in command:
            speak("Why don’t programmers like nature? Because it has too many bugs.")

        elif "exit" in command or "quit" in command or "stop" in command:
            speak("Goodbye! Have a nice day.")
            break

        else:
            speak("Sorry, I don’t know that command.")

# Run
if __name__ == "__main__":
    run_assistant()
