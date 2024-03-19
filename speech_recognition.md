```python
!pip install SpeechRecognition
```

    Requirement already satisfied: SpeechRecognition in c:\users\lenovo\.conda\new folder\lib\site-packages (3.10.1)
    Requirement already satisfied: requests>=2.26.0 in c:\users\lenovo\.conda\new folder\lib\site-packages (from SpeechRecognition) (2.31.0)
    Requirement already satisfied: typing-extensions in c:\users\lenovo\.conda\new folder\lib\site-packages (from SpeechRecognition) (4.9.0)
    Requirement already satisfied: charset-normalizer<4,>=2 in c:\users\lenovo\.conda\new folder\lib\site-packages (from requests>=2.26.0->SpeechRecognition) (2.0.4)
    Requirement already satisfied: idna<4,>=2.5 in c:\users\lenovo\.conda\new folder\lib\site-packages (from requests>=2.26.0->SpeechRecognition) (3.4)
    Requirement already satisfied: urllib3<3,>=1.21.1 in c:\users\lenovo\.conda\new folder\lib\site-packages (from requests>=2.26.0->SpeechRecognition) (2.0.7)
    Requirement already satisfied: certifi>=2017.4.17 in c:\users\lenovo\.conda\new folder\lib\site-packages (from requests>=2.26.0->SpeechRecognition) (2024.2.2)
    


```python
!pip3 install pyttsx3
```

    Requirement already satisfied: pyttsx3 in c:\users\lenovo\.conda\new folder\lib\site-packages (2.90)
    Requirement already satisfied: comtypes in c:\users\lenovo\.conda\new folder\lib\site-packages (from pyttsx3) (1.3.1)
    Requirement already satisfied: pypiwin32 in c:\users\lenovo\.conda\new folder\lib\site-packages (from pyttsx3) (223)
    Requirement already satisfied: pywin32 in c:\users\lenovo\.conda\new folder\lib\site-packages (from pyttsx3) (305.1)
    


```python
import speech_recognition as sr
```


```python
import pyttsx3

```


```python
import webbrowser as web
```


```python
!pip install pyaudio

```

    Collecting pyaudio
      Downloading PyAudio-0.2.14-cp311-cp311-win_amd64.whl.metadata (2.7 kB)
    Downloading PyAudio-0.2.14-cp311-cp311-win_amd64.whl (164 kB)
       ---------------------------------------- 0.0/164.1 kB ? eta -:--:--
       -- ------------------------------------- 10.2/164.1 kB ? eta -:--:--
       ------- ------------------------------- 30.7/164.1 kB 435.7 kB/s eta 0:00:01
       ----------------- --------------------- 71.7/164.1 kB 491.5 kB/s eta 0:00:01
       --------------------------------- ---- 143.4/164.1 kB 853.3 kB/s eta 0:00:01
       -------------------------------------- 164.1/164.1 kB 822.6 kB/s eta 0:00:00
    Installing collected packages: pyaudio
    Successfully installed pyaudio-0.2.14
    


```python
import pyaudio

```


```python
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
```

    Please say something...
    Recognizing...
    You said: hello
    


```python

```


```python

```


```python

```
