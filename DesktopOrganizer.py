#Desktop Organizer
"""
Todo:
1. Create an ignore function that will ignore all files in a textfile under "ignore.txt"
2. Integrate GUI
3. ....
"""

import os
import shutil

# Declare all required valiables and group directories for ease of calling the lot
home = os.path.expanduser('~')
desktop = os.path.join(home,'Desktop')
desktoplist = os.listdir(desktop)
docdir = os.path.join(desktop,'Documents')
mediadir = os.path.join(desktop,'Media')
picdir = os.path.join(desktop,'Images')
folderdir = os.path.join(desktop,'Folders')
otherdir = os.path.join(desktop,'Others')
dirs = [docdir, mediadir, picdir, folderdir, otherdir]
docextensions = ('.pdf', '.doc', '.txt', '.docx', '.rtf', '.odt')
mediaextensions = ('.mp4', '.mpeg4', '.avi', '.mov', '.flv', '.wmv', '.mp3', '.obb', '.wav', '.aac', '.aiff', '.wma', '.m4a')
picextensions = ('.jpg', '.jpeg', '.png', '.raw', '.gif', '.tiff', '.bmp')
appdir = os.path.dirname(os.path.abspath(__file__))

def appDirList():
    appdirlist = os.listdir(appdir)
    return appdirlist

def getIgnore():
    #Check if there are any files or folders to ignore from 'ignore.txt'
    if "ignore.txt" not in appDirList(): #Check if ignore.txt exists
        with open(os.path.join(appdir, "ignore.txt"), "w"):
            pass
        appDirList()
        ignorelist = []
        return ignorelist
    else:
        with open(os.path.join(appdir, "ignore.txt"), "r") as ignorelist:
            ignorelist = ignorelist.read().split(",")
            return ignorelist

def organize():

    #Check if the folders are present, and create them if they arent
    for folder in dirs:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print('Creating ' + folder)

    print('\n' * 3)

    #Check every file for its extension and move it to the correct folder
    for file in desktoplist:
        ignorelist = getIgnore()
        i = 1
        filepath = os.path.join(desktop, file)
        for ignorefile in ignorelist:
            if file == ignorefile or file == "desktop.ini":
                print("     Ignoring file:", file)
                break
            elif i != len(ignorelist):
                i += 1
                continue
            
            print("     Organizing:", file)
            #Organize the Documents
            if (file.lower().endswith(docextensions)):
                shutil.move(filepath, os.path.join(docdir, file))
                #print('Organized to Documents: ' + file)

            #Organize the Media
            elif (file.lower().endswith(mediaextensions)):
                shutil.move(filepath, os.path.join(mediadir, file))
                #print('Organized to Media: ' + file)

            #Organize the Pictures
            elif (file.lower().endswith(picextensions)):
                shutil.move(filepath, os.path.join(picdir, file))
                #print('Organized to Images: ' + file)

            #Organize the Folders
            elif os.path.isdir(filepath):
                if not (filepath in dirs):
                    shutil.move(filepath, os.path.join(folderdir, file))
                    #print('Organized to Folders: ' + file)

            #Organize the rest
            elif not os.path.isdir(filepath):
                shutil.move(filepath, os.path.join(otherdir, file))
                #print('Organized to others: ' + file)
    return True

if __name__ == "__main__":
    input('Press Enter to start organizer: \n')
    if organize() is True:
        input('         --DONE') #Wait for input
    else:
        print('Creating \'ignore.txt\' ')
        input('Add files to ignore.txt to prevent them from being organized!')
