import time
import os
import shutil

def removeFolder (path) :

    shutil.rmtree(path)

def removeFile (path) :

    os.remove(path)

def getAge (path) :

    ctime = os.stat(path).st_ctime
    return ctime

def main() :
    
    deleteFolderCount = 0
    deleteFilesCound = 0

    path = "/PATH_TO_DELETE"
    days = 30 

    seconds = time.time() - (days * 24 * 60 * 60)

    if os.path.exists(path):

        for root_folder, folders, files in os.walk(path):

            if seconds >= getAge(root_folder):

                removeFolder(root_folder)
				deleteFolderCount += 1
                break

            else :

                for folder in folders:

                    folder_path = os.path.join(root_folder, folder)
                    if seconds >= getAge(folder_path):

                        removeFolder(folder_path)
						deleteFolderCount += 1
                    
                for file in files:

                    file_path = os.path.join(root_folder, file)
                    if seconds >= getAge(file_path):

                        removeFile(file_path)
						deleteFilesCound += 1

                else :

                    if seconds >= getAge(path):

                        removeFile(path)
				        deleteFilesCound += 1



if __name__ == '__main__' :
    main()