import cv2
import numpy as np
from stack_images import stackImages
from contours import getContours

#Imagenes
img = cv2.imread('images/obstaculo_verde.jpg')
imgContour = img.copy()
blurred_gaussian = cv2.GaussianBlur(img, (5, 5), 0)
imgHSV = cv2.cvtColor(blurred_gaussian, cv2.COLOR_BGR2HSV)
imgAux = np.zeros_like(img)

#Rangos HSV
lower = np.array([42, 45, 119])
upper = np.array([70, 255, 255])

#Mascara
mask = cv2.inRange(imgHSV, lower, upper)
result = cv2.bitwise_and(img, img, mask=mask)
getContours(imgContour, mask)

#Muestra matriz de imagenes
imgStack = stackImages(0.3,([img, imgHSV, result], [mask, imgContour, imgAux]))
cv2.imshow('obstaculo verde', imgStack)

cv2.waitKey()
cv2.destroyAllWindows()