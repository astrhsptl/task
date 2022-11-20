from PIL import Image

from compressor import archive
from preprocessor import getPreprocessedImage


def main():
    imageName = input('Just enter the image name here please =) (!full path): ')
    archiveName = input('Enter archive name, please =): ')
    print('''Just wait)))''')
    Image.fromarray(getPreprocessedImage(imageName, False)).save(imageName)
    archive(archiveName, imageName)
    print('Have a good day =)')

def coder(archiveName, imageName):
    Image.fromarray(getPreprocessedImage(imageName, False)).save(imageName)
    archive(archiveName, imageName)

if __name__ == "__main__":
    main()