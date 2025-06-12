#demo.py

import cv2
import numpy as np
from matplotlib import pyplot as plt

#load the image
img = cv2.imread('eminem.jpg')
# cv2.line(img, (0,0), (150,150), (0,255,0), 15)
# cv2.rectangle(img, (150,50), (25,150), (0,255,0), 5)
# cv2.circle(img, (100,30), 35, (0,0 ,225), 5)
cv2.putText(img, 'The Real Slim Shady',
            (20, 140),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (250,250,250),
            2)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img[206:236, 224:313] = [255,255,255]
plt.imshow(img)
plt.show()
print(img)
cv2.imshow('Eminem', img)
#cv2.imshow('Eminem', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("image", gray)

# cap = cv2.VideoCapture(0)
# x=1
# while(True):
#     ret, frame = cap.read()
#     x+=1
#     cv2.putText(frame, 'Saumya Gupta' + str(x),
#             (20, 140),
#             cv2.FONT_HERSHEY_SIMPLEX,
#             0.7,
#             (250,250,250),
#             2)
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     cv2.rectangle(gray, (150,150), (300,300), (0,255,0), 5)
#     cv2.imshow('frame', gray)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# cap.destroyAllWindows()


