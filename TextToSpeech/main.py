import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty('rate', 150)  # Speed of speech (default is 200)
engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)

# Get text input and convert it to speech
text = input("Enter text to convert to speech: ")
engine.say(text)

# Wait until the speech is finished
engine.runAndWait()
