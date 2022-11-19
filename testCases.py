import os
from PIL import Image
from preprocessor import getPreprocessedImage


testImages = os.listdir('testcase/images')
for i in range(len(testImages)):
    dirName = os.path.join('testcase/preprocessed/', f'test{i}Case')
    try:
        os.mkdir(dirName)
    except Exception as e:
        print(e)
    image = Image.fromarray(getPreprocessedImage(os.path.join('testcase/images', testImages[i]), dirName)) # False))
    image.save(os.path.join(dirName, testImages[i]))

print('End test cases')