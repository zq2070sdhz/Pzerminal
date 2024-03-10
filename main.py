# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox
import download
import requests
window=Tk()
window.title("Pzerminal")
window.geometry("1000x500")
window.resizable(False, False)
title = Label(window, text="Welcome to Pzerminal!", font=("Cascadia Code", 20))
title.grid(row=0, column=0)
url_text = Entry(window, font=("Cascadia Code", 16),width=50)
url_text.grid(row=1, column=1)
download_text = Label(window, text="Download Url:", font=("Cascadia Code", 16))
download_text.grid(row=1, column=0)
button = Button(window, text="Download Now!", font=("Cascadia Code", 20), command=lambda: Test_button(url_text))
button.grid(row=3, column=1)
update_button = Button(window, text="Update", font=("Cascadia Code", 20), command=lambda: update())
update_button.grid(row=4, column=0)
import urllib.request
from tqdm.tk import tqdm
encodings = ["utf-8", "ISO-8859-1", "windows-1252"]
def update():
    current_version = "1.0.0"
    version_url = "https://github.com/zq2070sdhz/Pzerminal/releases/download/LATEST/latest_version.txt"
    url_response = urllib.request.urlopen(version_url)
    latest_version = url_response.read().decode('utf-8').strip()

    if latest_version > current_version:
        url_file = "https://github.com/zq2070sdhz/Pzerminal/releases/download/LATEST/latest_url.txt"
        url_response = urllib.request.urlopen(url_file)
        download_url = url_response.read().decode('utf-8').strip()

        with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc="Downloading") as t:
            import os
            file_name = os.path.basename(download_url)
            file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)

            urllib.request.urlretrieve(download_url, file_path, reporthook=lambda blocknum, blocksize, totalsize: t.update(blocknum * blocksize))


        messagebox.showinfo("Success", "Update completed!")
    else:
        messagebox.showinfo("Info", "No updates available.")

def Test_button(url_text):
    url = url_text.get()
    if url == "":
        messagebox.showerror("Error", "Please enter a URL!")
    else:
        download.download(url)
        messagebox.showinfo("Success", "Download completed!")

window.mainloop()