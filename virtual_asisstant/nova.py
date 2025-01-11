import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import os
import psutil  # This library helps in killing processes by name
import subprocess

# Define the function to take voice commands
def takeCommand():
    r = sr.Recognizer()

    # Adjust the recognizer sensitivity to ambient noise
    with sr.Microphone() as source:
        print('Listening...')

        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 0.7  # Time in seconds of silence before recognizing end of speech
        audio = r.listen(source)

        try:
            print("Recognizing...")
            Query = r.recognize_google(audio, language='en-in')
            print("The command is printed =", Query)

        except sr.UnknownValueError:
            print("Sorry, I couldn't understand the audio")
            return "None"
        except sr.RequestError:
            print("Sorry, there seems to be an issue with the speech service.")
            return "None"

        return Query

# Define the function to run the virtual mouse in the background
def run_virtual_mouse():
    speak("Running Virtual Mouse Application")
    process = subprocess.Popen(['python', 'E:/machine/virtual_mouse_using_hand_gesture/virtualmouse.py'], 
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # Open the URL in the browser
    webbrowser.open("http://127.0.0.1:5000/")
    return process

# Define the function to close the virtual mouse
def close_virtual_mouse(process):
    speak("Closing Virtual Mouse Application")
    process.terminate()  # Terminate the virtual mouse process
    close_browser_tab()  # Close the browser tab associated with the virtual mouse

# Define the function to run the virtual keyboard in the background
def run_virtual_keyboard():
    speak("Running Virtual Keyboard Application")
    process = subprocess.Popen(['python', 'E:/machine/virtual_keyboard/main.py'], 
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return process

# Define the function to close the virtual keyboard
def close_virtual_keyboard(process):
    speak("Closing Virtual Keyboard Application")
    process.terminate()  # Terminate the virtual keyboard process

# Function to speak text aloud
def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Set to male voice
    engine.say(audio)
    engine.runAndWait()

# Function to tell the day of the week
def tellDay():
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)

# Function to tell the current time
def tellTime():
    time = str(datetime.datetime.now())
    hour = time[11:13]
    min = time[14:16]
    speak("The time is sir " + hour + " Hours and " + min + " Minutes")

# Function to greet the user
def Hello():
    speak("Hello sir! I am nova. Tell me how may I help you")

# Function to close an application by its name
def close_application(app_name):
    """
    Closes the application by killing its process name.
    """
    for proc in psutil.process_iter():
        try:
            if app_name.lower() in proc.name().lower():
                proc.terminate()
                print(f"Closed {app_name}")
                speak(f"{app_name} has been closed.")
                break
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

# Function to close the browser tab that opened the virtual mouse application
def close_browser_tab():
    speak("Closing the browser tab.")
    
    # Loop through all running processes to find the browser process
    for proc in psutil.process_iter():
        try:
            # Check if the process is a browser (Chrome, Firefox, etc.)
            if 'chrome' in proc.name().lower():  # You can change this to 'firefox' or 'msedge' based on the browser
                for conn in proc.connections(kind='inet'):
                    # Check if the connection is on the specific URL we opened (http://127.0.0.1:5000/)
                    if conn.laddr.ip == '127.0.0.1' and conn.laddr.port == 5000:
                        proc.terminate()  # Close the browser process
                        speak("The browser tab has been closed.")
                        print(f"Closed browser process {proc.name()} with PID {proc.pid}")
                        return
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    speak("Could not find the browser tab to close.")

# Main function to handle queries
def Take_query():
    Hello()
    virtual_mouse_process = None  # Variable to store the virtual mouse process
    virtual_keyboard_process = None  # Variable to store the virtual keyboard process

    while(True):
        query = takeCommand().lower()

        if query == "none":
            continue

        print(f"Recognized Query: {query}")  # Debugging print

        # Running virtual mouse
        if "run virtual mouse" in query:
            if virtual_mouse_process is None:  # If virtual mouse is not already running
                virtual_mouse_process = run_virtual_mouse()
            else:
                speak("Virtual Mouse is already running")
            continue

        # Closing virtual mouse
        if "close virtual mouse" in query:
            if virtual_mouse_process is not None:  # If virtual mouse is running
                close_virtual_mouse(virtual_mouse_process)
                virtual_mouse_process = None  # Reset the process variable
            else:
                speak("Virtual Mouse is not running")
            continue

        # Running virtual keyboard
        if "run virtual keyboard" in query:
            if virtual_keyboard_process is None:  # If virtual keyboard is not already running
                virtual_keyboard_process = run_virtual_keyboard()
            else:
                speak("Virtual Keyboard is already running")
            continue

        # Closing virtual keyboard
        if "close virtual keyboard" in query:
            if virtual_keyboard_process is not None:  # If virtual keyboard is running
                close_virtual_keyboard(virtual_keyboard_process)
                virtual_keyboard_process = None  # Reset the process variable
            else:
                speak("Virtual Keyboard is not running")
            continue

        # Match the commands specifically
        if "open google" in query:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")
            continue
        
        elif "close google" in query:
            speak("Closing Google")
            # This will attempt to close the browser tab (works with specific browsers)
            speak("I am unable to directly close the browser tab.")
            continue

        elif "which day it is" in query:
            tellDay()
            continue

        elif "tell me the time" in query:
            tellTime()
            continue

        elif "close" in query:
            speak("Bye. Check Out GFG for more exciting things")
            exit()

        elif "from wikipedia" in query:
            speak("Checking Wikipedia")
            query = query.replace("wikipedia", "")

            try:
                result = wikipedia.summary(query, sentences=4)
                speak("According to Wikipedia")
                speak(result)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("There are multiple results for that query. Please specify more details.")
            except wikipedia.exceptions.HTTPTimeoutError:
                speak("The Wikipedia service is currently unavailable. Please try again later.")

        elif "tell me your name" in query:
            speak("I am Jarvis. Your desktop assistant")

if __name__ == '__main__':
    Take_query()
