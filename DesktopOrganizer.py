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
    #First check if the folders are present, and create them if they arent
    for folder in dirs:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print('Creating ' + folder)
        else:
            print(folder + ' exists')

    print('\n' * 3)

    #Check every file for its extension and move it to the correct folder
    for file in desktoplist:
        filepath = os.path.join(desktop, file)

        if not (file.lower().endswith('.ini')):
            #Organize the Documents
            if (file.lower().endswith(docextensions)):
                shutil.move(filepath, os.path.join(docdir, file))
                print('Organized to Documents: ' + file)

            #Organize the Media
            elif (file.lower().endswith(mediaextensions)):
                shutil.move(filepath, os.path.join(mediadir, file))
                print('Organized to Media: ' + file)

            #Organize the Pictures
            elif (file.lower().endswith(picextensions)):
                shutil.move(filepath, os.path.join(picdir, file))
                print('Organized to Images: ' + file)

            #Organize the Folders
            elif os.path.isdir(filepath):
                if not (filepath in dirs):
                    shutil.move(filepath, os.path.join(folderdir, file))
                    print('Organized to Folders: ' + file)

            #Organize the rest
            elif not os.path.isdir(filepath):
                shutil.move(filepath, os.path.join(otherdir, file))
                print('Organized to others: ' + file)


if __name__ == "__main__":
    input('Press Enter to start organizer: \n')
    organize()
    input('         --DONE')#Wait for input
