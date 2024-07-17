import pyttsx3
import speech_recognition as sr
import time
import webbrowser

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
    except Exception as e:
        print("Sorry, I did not catch that. Please say that again.")
        return None
    return query

def executeCommand(command):
    if 'youtube' in command.lower():
        say("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif 'song' in command.lower():
        say("Playing your favorite song")
        # Example of opening a specific YouTube video for a song
        webbrowser.open("https://youtu.be/qxbHtcfHq2s")


if __name__ == "__main__":
    print('Pycharm')
    say("ami tomake bhalobashi")

    # Set the timeout period (in seconds)
    timeout = 30
    start_time = time.time()

    while True:
        # Check if the timeout period has been reached
        if time.time() - start_time > timeout:
            say("Timeout reached, ending script.")
            break

        text = takeCommand()
        if text:
            executeCommand(text)
