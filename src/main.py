import easyocr
import gtts
from playsound import playsound

reader = easyocr.Reader(['en'])
result = reader.readtext("../assets/book1.jpg", detail=0)

full_text = " ".join(result)
print (full_text)

tts = gtts.gTTS(full_text)
tts.save("recording.mp3")
playsound("recording.mp3")