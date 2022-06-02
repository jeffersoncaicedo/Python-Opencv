import cv2
import numpy as np
import requests

from pyzbar.pyzbar import decode

global aux
global c
global est

aut = cv2.imread('Aut.jpg')
naut = cv2.imread('NAut.jpg')
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)


while True:
    cred, img = cap.read()
    l1 = np.array([[490, 240], [490, 210]], np.int32)
    l2 = np.array([[490, 210], [520, 210]], np.int32)

    l3 = np.array([[760, 210], [790, 210]], np.int32)
    l4 = np.array([[790, 210], [790, 240]], np.int32)

    l5 = np.array([[790, 480], [790, 510]], np.int32)
    l6 = np.array([[790, 510], [760, 510]], np.int32)

    l7 = np.array([[520, 510], [490, 510]], np.int32)
    l8 = np.array([[490, 510], [490, 480]], np.int32)

    cv2.polylines(img, [l1, l2, l3, l4, l5, l6, l7, l8], False, (0, 0, 0), 5)
    for barcode in decode(img):
        listaqr = barcode.data.decode('utf-8')
        url = "URL al que se le hace la petición" + str(listaqr)
        r = requests.get(url)
        resp = r.text
        if resp == "True":
            c = (0, 255, 0)
            est = aut
            aux = 1
        elif resp == "False":
            c = (0, 0, 255)
            est = naut
            aux = 0

        cv2.imshow('AVISO', est)
        cv2.waitKey(5000)
        cv2.destroyWindow('AVISO')
        """if aux == 1:
            print("Abierto")
        else:
            print("Cerrado")"""

    cv2.imshow('ESCANER', img)
    cv2.waitKey(1)
