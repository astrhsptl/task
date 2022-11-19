import os
import zipfile

from PIL import Image

def archive(archiveFilename: str, arhivedFile: str, mode:str ='w') -> str or None:
    modes = ['a', 'w']
    if mode in modes:
        try:
            archiveFile = zipfile.ZipFile(archiveFilename, mode)
            archiveFile.write(arhivedFile)
        except:
            return None
        
        archiveFile.close()
        return archiveFilename
    else:
        return None

def dearchive(archiveFilename: str, exctractDirectory: str = '') -> str or None:
    try:
        archiveFile = zipfile.ZipFile(archiveFilename, 'r')
        archiveFile.extractall(exctractDirectory)
        archiveFile.close()
    except:
        return None
    return exctractDirectory