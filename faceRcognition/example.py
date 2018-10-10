import face_recognition
import os
import cv2
names = ["catherine", "william"]
dir = os.path.join(os.getcwd(), 'data')
images = []
for name in names:
    filename = name + ".jpg"
    imagedir = os.path.join(dir, 'knowPic', filename)
    img = face_recognition.load_image_file(imagedir)
    images.append(img)

detectdir = os.path.join(dir, 'unknowPic', "unknown.jpeg")
unknown_image = face_recognition.load_image_file(detectdir)

face_encodings = []

for img in images:
    encoding = face_recognition.face_encodings(img)[0]
    face_encodings.append(encoding)
unknown_face_encodings = face_recognition.face_encodings(unknown_image)

face_locations = face_recognition.face_locations(unknown_image)
for i in range(len(unknown_face_encodings)):
    unknown_encoding = unknown_face_encodings[i]
    face_location = face_locations[i]
    top, right, bottom, left = face_location
    cv2.rectangle(unknown_image, (left, top), (right, bottom), (0, 255, 0), 2)
    results = face_recognition.compare_faces(face_encodings, unknown_encoding)
    for j in range(len(results)):
        if results[j]:
            name = names[j]
            cv2.putText(unknown_image, name, (left-10, top-10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0), 2)


unknown_image_rgb = cv2.cvtColor(unknown_image, cv2.COLOR_BGR2RGB)
cv2.imshow('output', unknown_image_rgb)

cv2.waitKey(0)
