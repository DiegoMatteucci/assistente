import speech_recognition as sr 

#cria um reconhecimento
r = sr.Recognizer()

# abre microfone para captura
with sr.Microphone() as source:
    audio = r.listen(source)
    print(r.recognize_google(audio))