# Virtual-Assistant
Here I created Virtual Assistant through following steps;

1.WolframAlpha : http://developer.wolframalpha.com/portal/myapps/
Visit here create account and get the key to use api. 
>>>pip install wolframalpha
now you can use it in your assistant.
Code refference : https://pypi.org/project/wolframalpha/

2.Wikipedia
>>>pip install wikipedia
Code refference : https://pypi.org/project/wikipedia/
We can use some conditions for wikipedia. First to limit the number of sentences to be displayed and other is the language.
wikipedia.summary(user_input,sentences=3)
wikipedia.set_lang("es")

Here I have added gui to python using tkinter module and used .place() for layout managing.
<<<<<<< HEAD

Adding text to speech using Pytsxx.Some of code related to it is as follows :
import pyttsx3
engine = pyttsx3.init() # object creation

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female
=======
