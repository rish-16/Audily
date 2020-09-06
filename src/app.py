import requests, json, cv2, glob, os
from playsound import playsound

addr = 'http://localhost:5000'
test_url = addr + '/audify'

content_type = 'image/jpeg'
headers = {'content-type': content_type}

img = cv2.imread('../assets/book1.jpg')
_, img_encoded = cv2.imencode('.jpg', img)

response = requests.post(test_url, data=img_encoded.tostring(), headers=headers)

list_of_files = glob.glob('./all_recordings/*')
latest_file = max(list_of_files, key=os.path.getctime)
print (latest_file)
playsound(latest_file)