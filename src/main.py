from flask import Flask, Response
from flask import send_file

import gtts, random, pytesseract
from playsound import playsound
from PIL import Image

app = Flask(__name__)

@app.route('/')
def hello():
    return "Welcome to the Audily API!"
    
@app.route('audify')    
def audify():
    img = flask.request.files.get('imagefile', '')
    full_text = pytesseract.image_to_string(img)
    print (full_text)
    
    random_id = "".join([str(random.randint(0, 9)) for i in range(8)])
    tts = gtts.gTTS(full_text)
    
    path_to_file = "./all_recordings/recording_{}.mp3".format(random_id)
    tts.save(path_to_file)
    
    return send_file(
            path_to_file, 
            mimetype="audio/mp3", 
            as_attachment=True, 
            attachment_filename="recording_{}.mp3".format(random_id)
        )