import cv2
a = cv2.CascadeClassifier(r"C:\Users\punke\OneDrive\Desktop\code\Pythonprojects\haarcascade_frontalface_alt.xml")
b = cv2.VideoCapture(0)
while True:

    c_rec,d_img = b.read()
    e  = cv2.cvtColor(d_img,cv2.COLOR_BGR2GRAY)
    f = a.detectMultiScale(e,1.3,6)

    for(x1,y1,w1,h1) in f:
        cv2.rectangle(d_img,(x1,y1), (x1+w1,y1+h1), (0,0,255),5)

    cv2.imshow('img', d_img)
    h = cv2.waitKey(40) & 0xff
    if h== 40:
        break
    
b.release()
cv2.destroyAllWindows()

import time
def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"Starting in {i}")
        time.sleep(1)
    print("start")

countdown(3)
mustache = cv2.imread('mustache.png', cv2.IMREAD_UNCHANGED)
mustache_resized = cv2.resize(mustache, (w1, h1))
d_img[y1:y1 + h1, x1:x1 + w1] = cv2.addWeighted(d_img[y1:y1 + h1, x1:x1 + w1], 1, mustache_resized, 0.7, 0)

if h ==ord('c'):
    cv2.imwrite(f"captured_face_{d_img}.jpg", d_img)

import pygame
pygame.init()
beep_sound = pygame.mixer.Sound('beep.wav')
if d_img > 0:
    beep_sound.play()

