import cv2
import dlib
import os
import base64
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return '<h1>Face Detection</h1>'

@app.route('/encodeimage', methods=['GET'])
def encodingimage():
	image = open('test1.jpg', 'rb')
	image_read = image.read()
	print('image encoding')
	image_64_encode = base64.urlsafe_b64encode(image_read)
	return image_64_encode

@app.route('/detect', methods=['POST'])
def decodingimage():
	
	data = request.form
	image_64_encode = data['es']


	image_64_decode = base64.urlsafe_b64decode(image_64_encode)
	image_result = open('testimage.jpg', 'wb')
	image_result.write(image_64_decode)
	
	image = cv2.imread('testimage.jpg', 0)

	face_detector = dlib.get_frontal_face_detector()

	img = face_detector(image)
	length = len(img)

	if img:
		if length == 1:
			status = "detected"
		else:
			status = "multiple face"	
	else:
		status = "undetected"

	os.remove('testimage.jpg')


	return status



if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) 
    except:
        port = 5000 

    app.run(port=port, debug=True)

