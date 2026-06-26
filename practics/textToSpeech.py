# import pyttsx3

# engine = pyttsx3.init()
# engine.say("Hello, this is a test.")
# engine.runAndWait()

import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Try different indexes like 1 for female voice
engine.say("Testing different voices.")
engine.runAndWait()
