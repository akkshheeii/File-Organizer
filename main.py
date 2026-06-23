import os
import shutil
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
folder = filedialog.askdirectory()
print("Selected Folder: ", folder)
categories = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".webp": "Images",
    ".pdf": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".mp4": "Videos",
    ".mov": "Videos",
    ".mp3": "Audio"
}
count=0
img=[]
doc=[]
vid=[]
aud=[]
print("Total Files Found :  ")
for file in os.listdir(folder):
    count+=1
    print(f"{count}: {file}")
    file_path = os.path.join(folder, file)

    if os.path.isfile(file_path):

        extension = os.path.splitext(file)[1].lower()

        if extension in categories:
            if categories[extension] == "Images":
                img.append(file)
            elif categories[extension] == "Documents":
                doc.append(file)
            elif categories[extension] == "Videos":
                vid.append(file)
            elif categories[extension] == "Audio":
                aud.append(file)


            target_folder = os.path.join(
                folder,
                categories[extension]
            )

            os.makedirs(target_folder,
                        exist_ok=True)

            shutil.move(
                file_path,
                os.path.join(target_folder,
                             file)
            )

print("\n\nOrganized Files : ")
if img:
    print("Images: ", img)
if doc:
    print("Documents: ", doc)
if vid:
    print("Videos: ", vid)
if aud:
    print("Audio: ", aud)
if not img and not doc and not vid and not aud:
    print("No Files To Organize !")
