import pyttsx3
import speech_recognition as sr
import requests
import time
import openai
import webbrowser

# OpenWeatherMap API key
apiKey = 'your key';

# OpenAI API key
OPENAI_API_KEY = "your key";
openai.api_key = OPENAI_API_KEY

# Initialize text-to-speech engine
engine = pyttsx3.init()

def say(text):
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

def getWeather(city):
    base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&units=metric"
    try:
        response = requests.get(base_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
    return {"cod": "404"}

def executeCommand(command):
    if 'weather' in command.lower():
        say("Which city do you want to know the weather for?")
        city = takeCommand()
        if city:
            weather_data = getWeather(city)
            if weather_data["cod"] == 200:
                main = weather_data['main']
                weather_desc = weather_data['weather'][0]['description']
                temp = main['temp']
                humidity = main['humidity']
                wind_speed = weather_data['wind']['speed']
                weather_report = f"The weather in {city} is currently {weather_desc} with a temperature of {temp} degrees Celsius, humidity of {humidity} percent, and wind speed of {wind_speed} meters per second."
                print(weather_report)
                say(weather_report)
            else:
                say(f"Sorry, I couldn't find the weather for {city}. Please try again.")
        else:
            say("I didn't catch the city name. Please try again.")
    elif 'youtube' in command.lower():
        say("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif 'song' in command.lower():
        say("Playing your favorite song")
        webbrowser.open("https://youtu.be/CB3OhCtnDcs")



if __name__ == "__main__":
    say("soumyajyoti das")

    # Set the timeout period (in seconds)
    timeout = 60
    start_time = time.time()

    while True:
        # Check if the timeout period has been reached
        if time.time() - start_time > timeout:
            say("Timeout reached, ending script.")
            break

        text = takeCommand()
        if text:
            executeCommand(text)
