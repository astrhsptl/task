import cv2
import numpy as np

from PIL import Image


def lightingImage(img: np.array, coef) -> np.array:
    '''
    Just makes image lightner 
    Get: np.array, lightning coefficient
    Return: np.array
    '''
    img = np.array(img) / 255
    img = img + img * coef
    img[img > 1] = 1
    img = img * 255
    return img.astype(np.uint8)

def maskFilter(image: np.array) -> np.array:
    '''
    Highlights most needly 
    information from image

    Get: np.array
    Return: np.array
    '''
    mask = np.ones(image.shape, dtype=np.uint8) * 255
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2,2))
    dilate = cv2.dilate(thresh, kernel, iterations=10)

    cnts = cv2.findContours(dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    for c in cnts:
        area = cv2.contourArea(c)
        if area < 100000:
            x,y,w,h = cv2.boundingRect(c)
            mask[y:y+h, x:x+w] = image[y:y+h, x:x+w]
    
    return mask


def grayFilter(image: np.array) -> np.array:
    '''
    Rigid Black-White filter
    
    Get: np.array
    Return: np.array
    '''
    image = Image.fromarray(image).convert('L')
    image = np.array(image)

    for i in range(image.shape[1]):
        for j in range(image.shape[0]):
            if image[j][i] < 45:
                image[j][i] = 255
            else:
                image[j][i] = 0    
    return image 


def negativeImageFilter(mask: np.array) -> np.array:
    '''
    Convert image to negative 
    Get: np.array
    Return: np.array
    '''
    image = Image.fromarray(mask)
    pixels = image.load()
    x, y = image.size
    for i in range(x):
        for j in range(y):
            r, g, b = pixels[i, j]
            pixels[i, j] =  200-r,  200-g , 200-b

    return np.array(image)
