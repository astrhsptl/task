import zipfile

def archive(archiveFilename, arhivedFile, mode='w'):
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

def dearchive(archiveFilename, exctractDirectory):
    try:
        archiveFile = zipfile.ZipFile(archiveFilename, 'r')
        archiveFile.extractall(exctractDirectory)
        archiveFile.close()
    except:
        return None
    return exctractDirectory