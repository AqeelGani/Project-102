import os
import cv2
import dropbox
import time

days = 2
path = input('Enter The Path : ')
path = path.replace('\\', '/')
path = path + '/'
seconds = time.time() - days * 60 * 60 * 24

def removeFiles(lpath):
    if not os.remove(lpath):
        print(f'{lpath} Removed Succesfully')

def main():
    if os.path.exists(path):
        for root, folders, files in os.walk(path):
            for file in files:
                filePath = os.path.join(root, file)
                if os.stat(filePath).st_mtime <= seconds:
                    removeFiles(filePath)
    else:
        print('Path Not Found!')

main()