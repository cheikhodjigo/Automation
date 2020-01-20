import sys
import os
import shutil
from filesClasses import MyFileToMove
from filesClasses import MyFileToDelete
from filesClasses import MyImageToMove
from filesClasses import MyMovieToMove

if(len(sys.argv) != 3):
    print("Please enter the directory to sort and the destination !")
    sys.exit(1)

if not (os.path.isdir(sys.argv[1])):
    print("This directory(%s) doesn't exists !" % sys.argv[1])
    sys.exit(2)

if not (os.path.isdir(sys.argv[2])):
    print("This directory(%s) doesn't exists !" % sys.argv[2])
    sys.exit(2)

directoryPath = sys.argv[1] 
filesToDelete = []
filesToMove = []
for filename in os.listdir(directoryPath):
    if filename.endswith(".zip") or filename.endswith(".tgz"):
        filesToDelete.append(MyFileToDelete(filename,directoryPath+filename))
    elif filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
        filesToMove.append(MyImageToMove(filename,directoryPath+filename,sys.argv[2]))
    elif filename.endswith(".mp4"):
        filesToMove.append(MyMovieToMove(filename,directoryPath+filename,sys.argv[2]))
    elif not filename.endswith(".ini"):
        filesToMove.append(MyFileToMove(filename,directoryPath+filename,sys.argv[2]))

## Delete Files
for fileToDelele in filesToDelete:
    fileToDelele.delete()

## Move files
for fileToMove in filesToMove:
    if fileToMove.verifyDestinationExist():
        fileToMove.move()
    else:
        print(fileToMove.filename + " : destination unknown")