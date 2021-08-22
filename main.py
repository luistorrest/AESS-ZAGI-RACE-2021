# Antes de la competencia, ajustar los rangos de colores HSV con ayuda de los controles deslizables (sliders)
# para obtener una máscara nítida en función de los colores del entorno que capture la camara del Zagi.

import cv2
import numpy as np
from stack_images import stackImages
from contours import getContours

listPositions = []

# Imagenes
img = cv2.imread('images/obstaculo_verde.jpg')
imgContour = img.copy()
blurred_gaussian = cv2.GaussianBlur(img, (9,9), 2)
imgHSV = cv2.cvtColor(blurred_gaussian, cv2.COLOR_BGR2HSV)
imgAux = np.zeros_like(img)

# Rangos HSV
lowerGreen = np.array([43, 171, 72])
upperGreen = np.array([70, 255, 255])
lowerPink = np.array([145, 52, 106])
upperPink = np.array([170, 255, 255])

# Mascaras
greenMask = cv2.inRange(imgHSV, lowerGreen, upperGreen)
pinkMask = cv2.inRange(imgHSV, lowerPink, upperPink)
mask = cv2.bitwise_or(greenMask, pinkMask)

# Obtiene los contornos de las mascara clasificados por color
# getContours(imgContour, mask)

getContours(imgContour, greenMask, "GREEN", listPositions)
getContours(imgContour, pinkMask, "PINK", listPositions)
print(listPositions)

# Interseccion de mascara e imagen orginal(BGR)
result = cv2.bitwise_and(img, img, mask=mask)

# Muestra matriz de imagenes
imgStack = stackImages(0.1,([img, imgHSV, result], [mask, imgContour, imgAux]))
cv2.imshow('obstaculo verde', imgStack)

cv2.waitKey()
cv2.destroyAllWindows()