from flask import Flask, Response, request
from flask import send_file

import os,  gtts, pytesseract, cv2
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
    
    full_text = pytesseract.image_to_string(img) # OCR
        
    random_id = "".join([str(np.random.randint(0, 9)) for i in range(8)])
    tts = gtts.gTTS(full_text) # TTS
    
    os.mkdir("all_recordings")
    path_to_file = "./all_recordings/recording_{}.mp3".format(random_id)
    tts.save(path_to_file)
    
    return send_file(
            path_to_file, 
            mimetype="audio/mp3", 
            as_attachment=True, 
            attachment_filename="recording_{}.mp3".format(random_id)
        )
        
if __name__ == "__main__":
    app.run(debug=True)