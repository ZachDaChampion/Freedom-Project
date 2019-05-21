import face_recognition
import threading
import camera
import keylogger
import time

zach_image = face_recognition.load_image_file("zach.png")
dad_image = face_recognition.load_image_file("dad.png")
zach_encoding = face_recognition.face_encodings(zach_image)[0]
dad_encoding = face_recognition.face_encodings(dad_image)[0]

encodings = [
    ('Zach', zach_encoding),
    ('Dad', dad_encoding),
]

current_faces = {}

def cam_process():
    global encodings, current_faces, zach_encoding, zach_image

    while True:

        frame = camera.get_frame()
        if frame is None:
            break

        # find faces
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        # identify faces
        for enc in encodings:
            if not enc[0] in current_faces.keys():
                current_faces[enc[0]] = 0
            current_faces[enc[0]] = 1 if True in face_recognition.compare_faces(face_encodings, enc[1]) else current_faces[enc[0]] * .75

        # tell the keylogger what faces are visible
        faces = []
        for key in current_faces.keys():
            if current_faces[key] >= .25:
                faces.append(key)
        keylogger.set_faces(faces)
        print(current_faces)
        time.sleep(.3)

cam = threading.Thread(target=cam_process, args=())
cam.start()
keylogger.init()
