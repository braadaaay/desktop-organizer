import DesktopOrganizer as do
import wx
import os
import subprocess
import sys

class Window(wx.Frame):

    def __init__(self, title, size, ):
        self.desktop = do.desktop
        self.appdir = do.appdir
        self.appdirlist = do.appDirList
        self.ignoreFile = os.path.join(do.appdir, "ignore.txt")
        self.ignorelist = do.getIgnore()
        self.frame = wx.Frame.__init__(self, None, -1, style=wx.CLOSE_BOX | wx.CAPTION,  title=title, pos=(0,0), size=size)
        panel = wx.Panel(self, -1)
        addtoignorebtn = wx.Button(panel, -1, "Add to ignore.txt", (15,5)) #Create buttons
        clearbtn = wx.Button(panel, -1, "Clear ignore.txt", (129, 5))
        organizebtn = wx.Button(panel, -1, "Organize desktop", (15, 35), (215.5,65))
        self.txtctrl = wx.TextCtrl(panel, -1, pos=(16, 110), size=(215,130), style=wx.TE_READONLY|wx.TE_MULTILINE|wx.HSCROLL)
        addtoignorebtn.Bind(wx.EVT_BUTTON, self.openDialog) #Set the button to an open dialogue
        clearbtn.Bind(wx.EVT_BUTTON, self.clearIgnore) #Set the button to clear ignore.txt
        organizebtn.Bind(wx.EVT_BUTTON, self.organize) #Set the button to organize
        icon = wx.Icon()
        icon.CopyFromBitmap(wx.Bitmap(os.path.join(self.appdir, "folder.ico"), wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon)
        self.setText()
        self.Show()
        self.Centre()


    def setText(self):
        self.txtctrl.SetValue("Ignore files:" + "\n")
        for i in open(self.ignoreFile, "r").read().split(","):
            self.txtctrl.AppendText(i + "\n")

    def openDialog(self, event):
        dialog = wx.FileDialog(self.frame, "Add", self.desktop, "", "*", style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST | wx.FD_MULTIPLE) #Create the file dialog and show it
        dialog.ShowModal()
        files = dialog.GetFilenames()
        for file in files:
            ignore = open(self.ignoreFile, "r")
            if file not in ignore.read():
                ignore = open(self.ignoreFile, "a")
                ignore.writelines(file + ",")
            ignore.close()
        self.appdirlist = os.listdir(self.appdir)
        self.setText()

    def clearIgnore(self, event):
        with open(self.ignoreFile, "w") as ignore:
            ignore.write("")
            self.setText()

    def organize(self, event):
        do.organize()
        ok = wx.MessageDialog(self.frame, "The desktop has been organized.", "Organized", style=wx.OK | wx.ICON_EXCLAMATION)
        ok.ShowModal()
        sys.exit()
        

def main():
    app = wx.App() #Create process
    frame = Window("Desktop Organizer", (260,300)) #Create Window
    app.MainLoop() #Run

main()