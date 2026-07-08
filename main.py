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
Image=[]
Video=[]
Audio=[]
Document=[]
Archive=[]
Code=[]
Application=[]
Font=[]
Database=[]
Other=[]

print("Total Files Found :  ")
for file in os.listdir(folder):
    count+=1
    print(f"{count}: {file}")
    file_path = os.path.join(folder, file)

    if os.path.isfile(file_path):

        extension = os.path.splitext(file)[1].lower()
        if extension in [
                "jpg", "jpeg", "png", "gif", "bmp", "webp",
                "svg", "ico", "tiff", "heic"
            ]:
                Image.append(file)

        elif extension in [
                "mp4", "avi", "mov", "mkv", "wmv",
                "flv", "webm", "mpeg", "3gp"
            ]:
                Video.append(file)

        elif extension in [
                "mp3", "wav", "aac", "flac",
                "ogg", "m4a", "wma"
            ]:
                Audio.append(file)

        elif extension in [
                "pdf", "doc", "docx", "txt", "rtf",
                "ppt", "pptx", "xls", "xlsx",
                "csv", "odt", "ods", "odp"
            ]:
                Document.append(file)

        elif extension in [
                "zip", "rar", "7z", "tar",
                "gz", "bz2", "xz", "iso"
            ]:
                Archive.append(file)

        elif extension in [
                "py", "java", "cpp", "c",
                "cs", "js", "ts", "html",
                "css", "php", "rb", "go",
                "swift", "kt", "sql", "json",
                "xml", "yml", "yaml", "sh"
            ]:
                Code.append(file)

        elif extension in [
                "exe", "msi", "apk", "ipa",
                "deb", "rpm", "dmg", "app"
            ]:
                Application.append(file)

        elif extension in [
                "ttf", "otf", "woff", "woff2"
            ]:
                Font.append(file)

        elif extension in [
                "db", "sqlite", "sqlite3"
            ]:
                Database.append(file)

        else:
                Other.append(file)
        
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
if Image:
    print("Images : ", Image,'/n/n')
if Video:
    print("Video : ", Video,'/n/n')
if Audio:
    print("Audio : ", Audio)
if Document:
    print("Documents : ", Document)
if Archive:
    print("Archive : ", Archive,'/n/n')
if Code:
    print("Code : ", Code,'/n/n')
if Application:
    print("Application : ", Application)
if Font:
    print("Font : ", Font)
if Database:
    print("Database : ", Database)
if Other:
    print("Other : ", Other)


if (len(Image) + len(Video) + len(Audio) + len(Document)+len(Archive)+len(Code)+len(Application)+len(Font)+len(Database)+len(Other))==0:
    print("No Files To Organize !")
