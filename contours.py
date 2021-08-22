# Este fichero contiene una función que clasifica y ordena los contornos por color, tambien hace el cálculo
# por donde tiene que pasar el Zagi

import cv2

def getContours(imgContour, img, label, listPositions):
    #almacena el listado de posiciciones para los contornos de los obstaculos

    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area>1000:
            cv2.drawContours(imgContour, cnt, -1, (0, 0, 0), 5)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),15)
            print('contorno: ', label)
            print('x: ', x, '\ny: ', y, '\nw: ', w, '\nh: ', h )

            #Coloca el nombre del color del contorno
            cv2.putText(imgContour,label,
                        (x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,4,
                        (0,255,255),14)

            #listado de tuplas (posiciones de contornos)
            listPositions.append(cv2.boundingRect(approx))

    if label == 'PINK': #Se es el ultimo contorno entonces ...
        #Orde todos los contornos en funcion de las coordenadas (x, y)
        listPositions.sort(key=lambda x: x[0] + x[1])

        # Rectangulo direccion Zagi y posicionamiento del centro
        cv2.rectangle(imgContour, (listPositions[0][0], listPositions[0][1]),
                      (listPositions[-1][0], listPositions[-1][1] + listPositions[-1][3]), (0, 255, 0), 15)

        # Circulo posicionado en el centro del rectangulo
        cv2.circle(imgContour,  ((listPositions[0][0]+listPositions[-1][0])//2,(listPositions[0][1]+(listPositions[-1][1]+listPositions[-1][3]))//2),
               20, (0, 0, 255), cv2.FILLED)