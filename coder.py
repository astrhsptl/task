from PIL import Image

from compressor import archive
from preprocessor import getPreprocessedImage


def main():
    imageName = input('Just enter the image name here please =) (!full path): ')
    archiveName = input('Enter archive name, please =): ')
    intermadiate = True if input('Enter, please: ').capitalize().strip() == 'Y'  else False
    print('''Just wait)))''')
    Image.fromarray(getPreprocessedImage(imageName, intermadiate)).save(imageName)
    archive(archiveName, imageName)
    print('Have a good day =)')