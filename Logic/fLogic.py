from Logic.mSettings import Settings

from shutil import copy2
from tkinter import filedialog

class FileLogic:
    def addFile(self):
        pass

    def addPhoto(self):
        files = filedialog.askopenfilenames(
            initialdir="/", title="Add photo", filetypes=(
                ("jpeg files", "*.jpg"),("all files", "*.*")
            )
        )
        photos = []

        for file in files:
            photo = copy2(file, Settings.resPath).replace('\\','/')
            photos.append(photo)
        return photos