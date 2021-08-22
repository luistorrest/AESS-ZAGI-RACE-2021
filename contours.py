import cv2

def getContours(imgContour, img):
    #almacena el listado de posiciciones para los contornos de los obstaculos
    listPositions = []
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area>1000:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
            print('x: ', x, '\ny: ', y, '\nw: ', w, '\nh: ', h )

            # Rectangulo direccion Zagi y posicionamiento del centro
            listPositions.append(cv2.boundingRect(approx)) #listado de tuplas (posiciones de contornos)
            try:
                cv2.rectangle(imgContour, (listPositions[0][0], listPositions[0][1]), (listPositions[1][0],
                                          (listPositions[1][3] + listPositions[1][1])), (0, 255, 0), 3)
                cv2.circle(imgContour, (listPositions[0][0] + (listPositions[1][0] // 2),
                                        (listPositions[0][1] + (listPositions[0][3]) // 2)), 20, (0, 0, 255),
                           cv2.FILLED)
            except IndexError:
                print('indice fuera de rango')
