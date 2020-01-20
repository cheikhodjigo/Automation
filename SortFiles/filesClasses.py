import os
import shutil

class MyFile:
    def __init__(self, filename, filePath):
        self.filename = filename
        self.filePath = filePath

class MyFileToMove(MyFile):
    def __init__(self, filename, filePath, destination):
        super(MyFileToMove,self).__init__(filename,filePath)
        self.setDestination(destination)
    
    def move(self):
        shutil.move(self.filePath, self.destination)
        print(self.filename + " moved to : " + self.destination)

    def setDestination(self, destination):
        parentDirectories = self.filename.split('_', 2)
        parentDirectories_size = len(parentDirectories)
        if parentDirectories_size > 1:
            del parentDirectories[parentDirectories_size-1]
        else:
            parentDirectories = []
        for directory in parentDirectories:
            destination += directory + "\\"
        self.destination=destination

    def verifyDestinationExist(self):
       return os.path.isdir(self.destination)

class MyFileToDelete(MyFile):
    def __init__(self, filename, filePath):
        super(MyFileToDelete,self).__init__(filename,filePath)
        print("File to delete created.")

    def delete(self):
        os.remove(self.filePath)
        print("Deleted: " + self.filename)


class MyImageToMove(MyFileToMove):
    def setDestination(self, destination):
        self.destination=destination+"Image\\"

class MyMovieToMove(MyFileToMove):
    def setDestination(self, destination):
        self.destination=destination+"Movie\\"    