import cv2
import numpy
image = cv2.imread("D:\\Pictures\\ryan full crip yes.jpg", 1)
def basicImageWorking(image):

    print(image)
    image = cv2.resize(image,(image.shape[1]*3, image.shape[0]*3))
    cv2.imshow('image',image)
    cv2.resizeWindow("image",400,300)
    cv2.waitKey()
    print(image.shape)
#k = cv2.waitKey()
#print(k)
def faceDetection(image):
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    grayscale_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grayscale_image,scaleFactor=1.05,minNeighbors=5)
    print(type(faces))
    print(faces)
    for x,y,w,h in faces:
        image = cv2.rectangle(image,(x+y),(x+w,y+h), (0,255,0),3)
    cv2.imshow("gray",image)
    cv2.waitKey(0)
def Main():
    faceDetection(image)
Main()
