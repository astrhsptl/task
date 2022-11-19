'''
1) get image
2) preprocessing image
3) save image
'''

from PIL import Image

from compressor import archive
from preprocessor import getPreprocessedImage


if __name__ == '__main__':
    print('''Hello! 
I can coding and save ur image)''')
    imageName = input('Just enter the image name here please =): ')
    print('''Okay, thanks)
Next step: ''')
    archiveName = input('Enter archive name, please =): ')
    print('''Need u to get intermediate result? 
(y - yes, other - no)''')
    intermadiate = True if input('Enter, please: ').capitalize().strip() == 'Y'  else False
    print('''Just wait)))''')
    Image.fromarray(getPreprocessedImage(imageName, intermadiate)).save(imageName)
    archive(archiveName, imageName)