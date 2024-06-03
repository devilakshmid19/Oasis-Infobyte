import speech_recognition as sp
import pyttsx3
import datetime
import webbrowser

n = sp.Recognizer()
res = pyttsx3.init()

def speak(text):
    res.say(text)
    res.runAndWait()


def audio():
    with sp.Microphone() as address:
        print("Speak...")
        path = n.record(address,duration=4)
        try:
            cmd = n.recognize_google(path)
            return cmd
        except sp.UnknownValueError:
            print("Didn't hear that. Try again later.")
            return ""

def wish_user():
    present_hour= datetime.datetime.now().hour
    if 0 <= present_hour <= 12:
        print("Good Morning...")
        speak("Good Morning...")
    elif 12 <= present_hour <= 18:
        print("Good Afternoon..")
        speak("Good Afternoon..")
    else:
        print("Good Evening...")
        speak("Good Evening...")

def take_command(command):
    if "hello" in command:
        print("Hello! How Can I Help You?")
        speak("Hello! How Can I Help You?")
    elif "What is the time now?" in command:
        present_time = datetime.datetime.now().strftime("&H:%M:%S")
        print(f"Time is {present_time}")
        speak(f"Time is {present_time}")
    elif "open chrome" in command:
        print("Opening Chrome...")
        speak("Opening Chrome...")
        url = "https://chrome.google.com"
        webbrowser.open(url)
    elif "Open YouTube" in command:
        print("Opening YouTube...")
        speak("Opening YouTube...")
        url = "https://www.youtube.com/"
        webbrowser.open(url)
    elif "thank you" in command:
        print("You're Welcome!")
        speak("You're Welcome!")
    else:
        print("Didn't hear that. Try again later.")
        speak("Didn't hear that. Try again later.")


def main():
    wish_user()
    while True:
        command = audio()
        if "exit" in command:
            print("Goodbye!Have a good day! ")
            speak("Goodbye!Have a good day! ")
            break
        take_command(command)

if __name__ == "__main__":
    main()