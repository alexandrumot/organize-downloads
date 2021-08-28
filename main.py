import shutil
import os
import os.path
import time

from zipfile import ZipFile
import patoolib

# Init folders and paths

DOWNLOADS_FOLDER = 'C:/Users/<USER>/Downloads'

IMAGES_FOLDER = 'C:/Users/<USER>/Downloads/Images'
ZIPS_FOLDER = 'C:/Users/<USER>/Downloads/Zips'
OTHER_FOLDER = 'C:/Users/<USER>/Downloads/Others'
APPS_FOLDER = 'C:/Users/<USER>/Downloads/Apps'


IMAGE_EXTENSIONS = ['tif', 'tiff', 'bmp', 'jpg', 'png', 'jpeg', 'gif', 'eps', 'raw']

EXCEPTION_LIST = ['Apps', 'Others', 'Zips', 'Images']

def moveItem(file, folder, folder_name):
    try:
        shutil.move(os.path.join(DOWNLOADS_FOLDER, file), folder)
    except shutil.Error:
        os.remove(os.path.join(DOWNLOADS_FOLDER, file))
        print(f'{file} IS DELETED FROM {folder_name}')

def organizeDownloads():

    files = []

    for item in os.listdir(DOWNLOADS_FOLDER):
        if os.path.isdir(os.path.join(DOWNLOADS_FOLDER, item)) == False:
            files.append(item)

    for file in files:
        file_parts = file.rsplit('.', 1)

        if file in EXCEPTION_LIST:
            continue
        elif file_parts[-1] == 'tmp' or file_parts[-1] == 'crdownload':
            continue

        # Checking the extension of file 
        # And moving it to specific folder

        if file_parts[-1] in IMAGE_EXTENSIONS:
            moveItem(file, IMAGES_FOLDER, 'Images')
            print(f'{file} IS MOVED TO {IMAGES_FOLDER[-6:]}')

        # Extract .zip folders and .rar files
        elif str(file).endswith('.zip') or str(file).endswith('.rar'):
            # Unzipping Process
            try:
                # Creating Destination
                os.mkdir(os.path.join(DOWNLOADS_FOLDER, file)[:-4])
                EXCEPTION_LIST.append(file[:-4])

                # Unzipping to Destination
                if str(file).endswith('.zip'):
                    with ZipFile(os.path.join(DOWNLOADS_FOLDER, file), 'r') as zip:
                        zip.extractall(os.path.join(DOWNLOADS_FOLDER, file)[:-4])
                    print(f'{file} IS UNZIPPED AT {file[:-4]}')
                else:
                    # Extracting to Destination
                    patoolib.extract_archive(file, outdir=os.path.join(DOWNLOADS_FOLDER, file)[:-4])
                    
            except FileExistsError:
                pass

            moveItem(file, ZIPS_FOLDER, 'Zips')
            print(f'{file} IS MOVED TO {ZIPS_FOLDER[-4:]}')

        elif str(file).endswith('.exe'):    
            moveItem(file, APPS_FOLDER, 'Apps')
            print(f'{file} IS MOVED TO {APPS_FOLDER[-4:]}')

        elif os.path.isdir(os.path.join(DOWNLOADS_FOLDER, file)) == False and str(file).endswith('.tmp') == False:
            moveItem(file, OTHER_FOLDER, 'Others')
            print(f'{file} IS MOVED TO {OTHER_FOLDER[-6:]}')

if __name__ == '__main__':
    while 1:
        # Checks Downloads every 5 sec
        # Change it to your liking :)
        organizeDownloads()
        time.sleep(5) 


