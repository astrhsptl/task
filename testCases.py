import os
import cv2

from preprocessor import getImageMask


testImages = os.listdir('testcase/images')

for i in testImages:
    cv2.imwrite(f'testcase/preprocessed/{i}', getImageMask(os.path.join('testcase/images', i)))

print('End test cases')