from compressor import dearchive


def main():
    archiveName = input('Just enter the archive name here please =): ')
    excDirectory = input('Enter the exctractall directory, please (full path): ')
    dearchive(archiveName, excDirectory)

def decoder(archiveName, excDirectory):
    dearchive(archiveName, excDirectory)

if __name__ == '__main__':
    main()