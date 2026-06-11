#use the external module and use it to perform an operation of your interest.
# import requests

# response = requests.get("https://api.github.com")

# if response.status_code == 200:
#     print("Successfully connected to GitHub API!")
# else:
#     print("Failed to connect.")


import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("I will speak this text")
engine.runAndWait()