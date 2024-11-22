import speech_recognition as sr

recogniser = sr.Recognizer()

with sr.Microphone() as source:
    print("Adjusting for ambient noise...")
    recogniser.adjust_for_ambient_noise(source)
    print("Listening...")
    audio = recogniser.listen(source)


try:
    print("Transcribing...")
    text = recogniser.recognize_google(audio)
    print("You said: "+ text)
except sr.UnknownValueError:
    print("Sorry, I could not understand the audio.")
except sr.RequestError:
    print("Sorry, i could not request from google services")