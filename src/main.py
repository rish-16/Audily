from flask import Flask, Response, request
from flask import send_file

import gtts, pytesseract, cv2
import numpy as np
from PIL import Image

app = Flask(__name__)

@app.route('/')
def hello():
    return "Welcome to the Audily API!"
    
@app.route('/audify', methods=['POST'])
def audify():
    np_arr = np.fromstring(request.data, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    
    full_text = pytesseract.image_to_string(img)
    print (full_text)
    
    random_id = "".join([str(np.random.randint(0, 9)) for i in range(8)])
    tts = gtts.gTTS(full_text)
    
    path_to_file = "./all_recordings/recording_{}.mp3".format(random_id)
    tts.save(path_to_file)
    
    return send_file(
            path_to_file, 
            mimetype="audio/mp3", 
            as_attachment=True, 
            attachment_filename="recording_{}.mp3".format(random_id)
        )