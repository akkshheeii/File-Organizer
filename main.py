import os
import shutil
import tkinter as tk
from tkinter import filedialog

categories = {

    "Images":[
        "jpg","jpeg","png","gif","bmp",
        "webp","svg","ico","tiff","heic"
    ],

    "Videos":[
        "mp4","avi","mov","mkv",
        "wmv","flv","webm","mpeg","3gp"
    ],

    "Audio":[
        "mp3","wav","aac","flac",
        "ogg","m4a","wma"
    ],

    "Documents":[
        "pdf","doc","docx","txt",
        "rtf","ppt","pptx",
        "xls","xlsx","csv"
    ],

    "Archives":[
        "zip","rar","7z",
        "tar","gz","iso"
    ],

    "Code":[
        "py","java","cpp",
        "c","js","html",
        "css","php","json",
        "sql"
    ],

    "Applications":[
        "exe","msi","apk",
        "deb","rpm"
    ],

    "Fonts":[
        "ttf","otf",
        "woff","woff2"
    ],

    "Database":[
        "db","sqlite",
        "sqlite3"
    ]

}
root=tk.Tk()
root.withdraw()
folder=filedialog.askdirectory()
if not folder:
    print("No folder selected")
    exit()
organized={}

for file in os.listdir(folder):
    path=os.path.join(folder,file)
    if os.path.isfile(path):
        ext=os.path.splitext(file)[1].lower().replace(".","")
        category="Other"
        for name,extensions in categories.items():
            if ext in extensions:
                category=name
                break
        target=os.path.join(folder,category)
        os.makedirs(target,exist_ok=True)
        shutil.move(
            path,
            os.path.join(target,file)
        )
        organized.setdefault(category,[]).append(file)
for category,files in organized.items():
    print("\n"+category)
    for f in files:
        print(" •",f)

if not organized:
    print("No files found!")
