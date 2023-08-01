import cv2
import numpy as np
import face_recognition

imgElon = face_recognition.load_image_file('img/ElonMusk.jpg')
imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)

imgTest = face_recognition.load_image_file('img/ElonMuskTest.jpg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

faceloc = face_recognition.face_locations(imgElon)[0]
encodeElon = face_recognition.face_encodings(imgElon)[0]

cv2.rectangle(imgElon, (faceloc[3], faceloc[0]), (faceloc[1], faceloc[2]), (255,0,255), 2)


facelocTest = face_recognition.face_locations(imgTest)[0]
encodeElonTest = face_recognition.face_encodings(imgTest)[0]

cv2.rectangle(imgTest, (facelocTest[3], facelocTest[0]), (facelocTest[1], facelocTest[2]), (255,0,255), 2)


results = face_recognition.compare_faces([encodeElon], encodeElonTest)
faceDis = face_recognition.face_distance([encodeElon], encodeElonTest)
print(results, faceDis)

cv2.imshow('Elon Musk', cv2.resize(imgElon,(500,500)))
cv2.imshow('Elon MuskTest', cv2.resize(imgTest,(500,500)))
cv2.waitKey(0)
