import os
import cv2
import numpy as np
from PIL import Image

from filters import (
    negativeImageFilter, lightingImage, 
    grayFilter, maskFilter)

def getPreprocessedImage(
    imagePath: str, 
    sideEffectImages: str or bool = False) -> np.array:

    img = np.array(Image.open(imagePath))
    saved = lambda x: Image.fromarray(img).save(os.path.join(sideEffectImages, x)) if sideEffectImages else 0

    if np.mean(img) < 145.0:
        img = lightingImage(img, 0.2) 
        saved('lightner.png')

    elif np.mean(img) < 155.0:
        img = maskFilter(img)
        saved('masked.png')
        
    img = negativeImageFilter(img)
    saved('negative.png')
    
    final = grayFilter(img)
    
    return final