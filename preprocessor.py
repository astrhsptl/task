import cv2
import numpy as np

def getImageMask(imagePath,):
    image = cv2.imread(imagePath)
    mask = np.ones(image.shape, dtype=np.uint8) * 255
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2,2))
    dilate = cv2.dilate(thresh, kernel, iterations=5)

    cnts = cv2.findContours(dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]


    for c in cnts:
        area = cv2.contourArea(c)
        if area < 80000:
            x,y,w,h = cv2.boundingRect(c)
            mask[y:y+h, x:x+w] = image[y:y+h, x:x+w]
    
    return mask