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


def organize():
    input('Press Enter to start organizer')

    #First check if the folders are present, and create them if they arent
    for folder in dirs:
        if not os.path.exists(folder):
            os.makedirs(folder)


    #Check every file for its extension and move it to the correct folder
    for file in desktoplist:
        filepath = os.path.join(desktop, file)
        print('Organized: ' + file)

        #Organize the Documents
        if (file.lower().endswith(docextensions)):
            shutil.move(filepath, os.path.join(docdir, file))
            continue

        #Organize the Media
        if (file.lower().endswith(mediaextensions)):
            shutil.move(filepath, os.path.join(mediadir, file))
            continue

        #Organize the Pictures
        if (file.lower().endswith(picextensions)):
            shutil.move(filepath, os.path.join(picdir, file))
            continue

        #Organize the Folders
        if os.path.isdir(filepath):
            if not (filepath in dirs):
                shutil.move(filepath, os.path.join(folderdir, file))
                continue

        #Organize the rest
        if not os.path.isdir(filepath):
            if not (file.lower().endswith('.ini')):
                shutil.move(filepath, os.path.join(otherdir, file))
                continue



organize()

#Wait for input
input('         --DONE')
