'''
1) get archive name
2) extract image
'''

from PIL import Image

from compressor import dearchive


if __name__ == '__main__':
    print('''Hello! 
I can decoding and save ur image)''')
    archiveName = input('Just enter the archive name here please =): ')
    print('''And last step)''')
    excDirectory = input('Enter the exctractall directory, please: ')
    dearchive(archiveName, excDirectory)
    print('Have a fun day)')