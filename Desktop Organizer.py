import os
import shutil

home = os.path.expanduser('~')
desktop = os.path.join(home,"Desktop")
desktoplist = os.listdir(desktop)
docdir = os.path.join(desktop,"Documents")
mediadir = os.path.join(desktop,"Media")
picdir = os.path.join(desktop,"Images")
foldersdir = os.path.join(desktop,"Folders")
othersdir = os.path.join(desktop,"Others")

def organize():
    input("Press Enter to start organizer")
    docs()
    media()
    pics()
    folders()
    others()
    input("-------------Done")

def docs():
    if not os.path.exists(docdir):
        os.makedirs(docdir)
        
        
    for file in desktoplist:
        if (file.endswith(".pdf") or file.endswith(".doc") or
            file.endswith(".txt") or file.endswith(".docx") or
            file.endswith(".rtf") or file.endswith(".odt")):
                shutil.move(desktop + "\\" + file, docdir + "\\" + file)

    print("--Organized Documents")

def media():
    if not os.path.exists(mediadir):
        os.makedirs(mediadir)
        
    for file in desktoplist:
        if (file.endswith(".mp4") or file.endswith(".mpeg4") or
            file.endswith(".avi") or file.endswith(".mov") or
            file.endswith(".flv") or file.endswith(".wmv") or
            file.endswith(".mp3") or file.endswith(".obb") or
            file.endswith(".wav") or file.endswith(".aac") or
            file.endswith(".aiff") or file.endswith(".wma") or
            file.endswith(".m4a")):
                shutil.move(desktop + "\\" + file, mediadir + "\\" + file)

    print("--Organized Media")

def pics():
    if not os.path.exists(picdir):
        os.makedirs(picdir)
        
    for file in desktoplist:
        if (file.endswith(".jpg") or file.endswith(".jpeg") or
            file.endswith(".png") or file.endswith(".raw") or
            file.endswith(".gif") or file.endswith(".tiff") or
            file.endswith(".bmp")):
                shutil.move(desktop + "\\" + file, picdir + "\\" + file)

    print("--Organized Images")

def folders():
    if not os.path.exists(foldersdir):
        os.makedirs(foldersdir)

    for file in desktoplist:
        filepath = os.path.join(desktop,file)
        if os.path.isdir(filepath):
            if (filepath != docdir and
            filepath != mediadir and filepath != picdir and
            filepath != foldersdir and filepath != othersdir):
                shutil.move(filepath, os.path.join(foldersdir,file))

    print("--Organized Folders")
            
def others():
    if not os.path.exists(othersdir):
        os.makedirs(othersdir)

    for file in desktoplist:
        filepath = os.path.join(desktop,file)
        if os.path.isfile(filepath):
            shutil.move(filepath, os.path.join(othersdir,file))
            

    print("--Organized The Rest")

organize()
