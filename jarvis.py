import pyttsx3
import speech_recognition as sr
import os
import turtle

# Initialize the speech engine
engine = pyttsx3.init()

# Change the voice to a female voice
def change_voice():
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Female voice, adjust index if needed

# Speak function with custom voice and speed
def speak(text):
    change_voice()  # Set to female voice
    engine.say(text)
    engine.runAndWait()
    update_gui(text)  # Update GUI with the spoken text

# Function to update the turtle window with the latest response
def update_gui(text):
    # Clear the turtle screen
    turtle.clearscreen()

    # Set up the turtle window and write the text
    turtle.bgcolor("lightblue")
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()
    pen.goto(0, 0)
    pen.color("black")
    pen.write(f"Jarvis: {text}", align="center", font=("Arial", 14, "normal"))
    pen.goto(0, -50)
    pen.write("Say 'Hey Jarvis' to interact", align="center", font=("Arial", 12, "italic"))
    turtle.update()

# Function to listen for commands
def listen():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"Command received: {command}")
        return command
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        speak("Sorry, there was an issue with the speech recognition service.")
        return ""

# Function to open system applications
def open_application(app_name):
    app_path = None
    if app_name == "notepad":
        app_path = "notepad.exe"
    elif app_name == "chrome":
        app_path = "chrome.exe"  # Modify based on your Chrome installation path
    elif app_name == "vscode":
        app_path = "code.exe"
    elif app_name == "android studio":
        app_path = "studio.exe"
    elif app_name == "email":
        app_path = "outlook.exe"  # Assuming Outlook is the default email client

    if app_path and os.path.exists(app_path):
        os.system(app_path)
        speak(f"{app_name} is opening.")
        update_gui(f"Jarvis: {app_name} is opening.")
    else:
        speak(f"Sorry, I couldn't find {app_name}.")
        update_gui(f"Jarvis: Sorry, I couldn't find {app_name}.")

# Main function to start Jarvis
def start_jarvis():
    speak("Hey Sir, I am Jarvis. Say 'Hey Jarvis' to start the assistant.")
    update_gui("Jarvis: Hey Sir, I am Jarvis. Say 'Hey Jarvis' to start the assistant.")
    
    while True:
        command = listen()
        if "hey jarvis" in command:
            speak("Yes Sir, how can I help you?")
            update_gui("Jarvis: Yes Sir, how can I help you?")
            command = listen()

            if "open notepad" in command:
                speak("Opening Notepad.")
                update_gui("Jarvis: Opening Notepad.")
                open_application("notepad")

            elif "open chrome" in command:
                speak("Opening Chrome.")
                update_gui("Jarvis: Opening Chrome.")
                open_application("chrome")

            elif "open vscode" in command:
                speak("Opening Visual Studio Code.")
                update_gui("Jarvis: Opening Visual Studio Code.")
                open_application("vscode")

            elif "open android studio" in command:
                speak("Opening Android Studio.")
                update_gui("Jarvis: Opening Android Studio.")
                open_application("android studio")

            elif "open email" in command:
                speak("Opening Email client.")
                update_gui("Jarvis: Opening Email client.")
                open_application("email")

            else:
                speak("Sorry, I didn't recognize that command. Please try again.")
                update_gui("Jarvis: Sorry, I didn't recognize that command. Please try again.")

# Setup the turtle screen
def setup_turtle():
    turtle.setup(800, 600)  # Set up the window size
    turtle.bgcolor("lightblue")
    turtle.tracer(0)  # Disable auto-update
    turtle.hideturtle()
    turtle.listen()
    turtle.mainloop()

# Run the Jarvis assistant with turtle graphics
setup_turtle()
start_jarvis()