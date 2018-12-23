# Based on directory naming convention, this will only work for Windows. Sorry :(
import getpass
import os
import re
import shutil

currentDirectory = os.path.dirname(os.path.realpath(__file__))
user = getpass.getuser()
documentsDirectory = "C:\\Users\\" + user + "\\Documents"
classFolders = list()
subjects = list()
fileSplit = list()

for fileName in os.listdir(documentsDirectory):
    if fileName.lower().__contains__("class"):
        classFolders.append(fileName)

for word in classFolders:
    subjects.append(re.sub(" Class", "", word))

for fileName in os.listdir(currentDirectory):
    trueFileName = os.path.splitext(fileName)[0]
    fileSplit = trueFileName.split()
    for subject in subjects:
        if subject.__contains__(fileSplit[0]):
                if (os.path.isfile(documentsDirectory + "\\" + subject + " Class" + "\\" + fileName)):
                        dupeFileName = trueFileName + "(1)" + os.path.splitext(fileName)[1]
                        os.rename(fileName, dupeFileName)
                        shutil.move(currentDirectory + "\\" + dupeFileName, documentsDirectory + "\\" + subject + " Class")
                else:
                        shutil.move(currentDirectory + "\\" + fileName, documentsDirectory + "\\" + subject + " Class")
