#This communicates with the Arduino using com
import serial
import time
from gtts import *
from playsound import playsound
import os
#Allows us to access files on your PC
import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate',130)
arduinoData = serial.Serial('com4',9600)
#Sends data to arduino

#Pyttsx3
def speak(text):
    engine.say(text)
    engine.runAndWait()
    print(text)
#GTTS
def speakg(text):
    myobj = gTTS(text=text, lang="en-US", slow=False)
    myobj.save("gtts.mp3")
    playsound('gtts.mp3')
    os.remove('gtts.mp3')

#Turn on the LED
def led_on():
    arduinoData.write('ON'.encode())
    speak("LED is ON")
    #speakg("LED is ON")

#Turn off the LED
def led_off():
    arduinoData.write('OFF'.encode())
    speak("LED is OFF")
    #speakg("LED is OFF")

while 1:
    print("ON for turning on the LED, OFF for turning off the LED, EXIT to exit the program")
    speak("Say ON or OFF or EXIT")
    #speakg("SAY on or off or exit")
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        f = r.listen(source)
        mytext = r.recognize_google(f)
        mytext = mytext.upper()
        # "go" ==> "GO"
        if mytext == "ON":
            led_on()
            print('Done LED is ON')
            time.sleep(3)
        elif mytext == "OFF" or mytext == "OF":
            led_off()
            print("Done LED is OFF")
            time.sleep(3)
        elif mytext == "EXIT":
            exit()
        elif mytext == mytext:
            speak("Didn't quite get you. Try again!")
        elif mytext == None:
            speak("Didn't quite get you. Try again!")





