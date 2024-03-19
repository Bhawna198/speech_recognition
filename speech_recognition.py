#!/usr/bin/env python
# coding: utf-8

# In[7]:


get_ipython().system('pip install SpeechRecognition')


# In[9]:


get_ipython().system('pip3 install pyttsx3')


# In[12]:


import speech_recognition as sr


# In[11]:


import pyttsx3


# In[13]:


import webbrowser as web


# In[14]:


get_ipython().system('pip install pyaudio')


# In[15]:


import pyaudio


# In[2]:


import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Please say something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

if __name__ == "__main__":
    recognize_speech() 


# In[ ]:





# In[ ]:





# In[ ]:




