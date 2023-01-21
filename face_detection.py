import cv2
import requests
import json
import os
import face_recognition



IMG_URL = "temp/data/"

def surface(face_location):
    top, right, bottom, left = face_location
    return abs(bottom - top) + abs(left - right)


def one_face_detection(img):
    # cropped_faces = []
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(img, 1.1, 4)
    if len (faces) > 0:
        closest_face_location = max(faces, key=surface)
        x, y, w, h = closest_face_location
        return img[y:y+h, x:x+w]
    return None

def local_face_recognition(img):
    IMG_DIR = "./data/images/"
    for filename in os.listdir(IMG_DIR):
        user_image = face_recognition.load_image_file(IMG_DIR + filename)
        try:
           user_image_code = face_recognition.face_encodings(user_image)[0]

           img_code = face_recognition.face_encodings(img)[0]

           if face_recognition.compare_faces([img_code], user_image_code)[0]:
               return True
        except:
           pass
    return False



def record():
    i = 0
    capture = cv2.VideoCapture(0)
    open_door = False

    while not open_door:
        i = i + 1
        _, img = capture.read()
        cropped_face = one_face_detection(img)
        url = 'http://192.168.238.179:5000/api/V1.0.0/devices/facial-detection'
        if cropped_face is not None:
            print("face_detected")
            try:
                _, img_encoded = cv2.imencode('.jpg', img)
                file = {'userImage': ('image.jpg', img_encoded)}
                #im_b64 = base64.b64encode(img)
                # json_object = {
                #     "image": im_b64.decode()
                # }
                token_file = open("./data/token.json")
                token = json.load(token_file)
                response = requests.post(url, headers={"Authorization": "Bearer " + token}, files = file).json()
                print(response)
                result = response["open"]
            except requests.exceptions.RequestException as e:
                print("server is unreachable", e)
                result = local_face_recognition(img)
            if result:
                print("open door")
                exec(open('arduino_accept.py').read())
                break
            else:
               print("wrong face")
               exec(open('arduino_refuse.py').read())
               break
        if i == 100:
            break
    capture.release()


record()
