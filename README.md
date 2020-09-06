# Audily
📑🤖 Convert PDFs to Audiobooks with a click!

## Setup
You can test Audily on your local system by installing the necessary packages. You must have `pip` and `brew` (Homebrew) installed:

```bash
pip install -r requirements.txt
brew install tesseract
```

Or simply, run `setup.sh` in your terminal:

```bash
sh setup.sh
```

## Usage

To use Audily, you must send a JPEG image to the API backend. On a separate terminal window, start the Flask API server from within the `src` directory:

```bash
env FLASK_APP=main.py flask run
```

Once the server is live, create a script that sends a request to the API from another terminal window:

```python
import requests, json, cv2, glob, os
from playsound import playsound

addr = 'http://localhost:5000'
test_url = addr + '/audify'

content_type = 'image/jpeg'
headers = {'content-type': content_type}

# replace with your own JPEG image file
img = cv2.imread('../assets/book1.jpg')
_, img_encoded = cv2.imencode('.jpg', img)

# send a POST request to the server
response = requests.post(test_url, data=img_encoded.tostring(), headers=headers)

# gets and plays most recently-added file in directory
list_of_files = glob.glob('./all_recordings/*')
latest_file = max(list_of_files, key=os.path.getctime)
print (latest_file)
playsound(latest_file)
```

Run this script in your terminal:

```bash
python app.py
```

This should save the recording in the `all_recordings` directory created for all audio output.

## License

[MIT](https://github.com/rish-16/Audily/blob/master/LICENSE)