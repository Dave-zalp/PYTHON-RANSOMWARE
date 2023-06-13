import speech_recognition as sr
import pyttsx3
import pyaudio

def execute_command(command):
    if "open telegram" in command:
        # Execute the command to open Notepad
        import os
        os.startfile("Telegram.exe ")
        print("Opening Telegram...")
    elif "open calculator" in command:
        # Execute the command to open the Calculator
        import os
        os.startfile("calc.exe")
        print("Opening Calculator...")
    else:
        # Command not recognized
        print("Command not recognized.")

# Create an instance of the recognizer
r = sr.Recognizer()

# Create an instance of the speech synthesis engine
engine = pyttsx3.init()

# Use the default system microphone as the audio source
mic = sr.Microphone()

# Function to listen for voice commands
def listen_for_commands():
    with mic as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        command = r.recognize_google(audio)
        print("You said:", command)
        execute_command(command)
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Function to generate speech from text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Say "open notepad"
speak("What do you want to open?")

# Listen for commands
listen_for_commands()
