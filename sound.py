import speech_recognition as sr

rec = sr.Recognizer()
arquivoAudio = sr.AudioFile('cansada.wav')

with arquivoAudio as fonte:
    rec.adjust_for_ambient_noise(fonte)
    audio = rec.record(fonte)
    resultado = rec.recognize_google(audio, language='pt')

print(resultado)