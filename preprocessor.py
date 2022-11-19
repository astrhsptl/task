import os
import cv2
import numpy as np
from PIL import Image

from filters import (
    negativeImageFilter, lightingImage, 
    grayFilter, maskFilter)

def getPreprocessedImage(imagePath: str, sideEffectImages: str or bool) -> np.array:
    img = np.array(Image.open(imagePath))

    if np.mean(img) < 145.0:
        img = lightingImage(img, 0.2) 
        saved = Image.fromarray(img).save(os.path.join(sideEffectImages, 'lightner.jpg')) if sideEffectImages else 0

    elif np.mean(img) < 155.0:
        img = maskFilter(img)
        saved = Image.fromarray(img).save(os.path.join(sideEffectImages, 'masked.jpg')) if sideEffectImages else 0
        
    img = negativeImageFilter(img)
    saved = Image.fromarray(img).save(os.path.join(sideEffectImages, 'neg.jpg')) if sideEffectImages else 0
    
    final = grayFilter(img)
    
    return final