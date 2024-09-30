#Here we will be using pyttsx3 its a text to speech module 
#installation: pip install pyttsx3

import pyttsx3
engine = pyttsx3.init()
rate = engine.getProperty('rate')
volume = engine.getProperty('volume')

engine.setProperty('rate',170)
engine.setProperty('volume',2.0)
engine.say("Hello, My name is Anirudh CM!!")
engine.save_to_file('Hello world','demo.mp3')
engine.runAndWait()