import tkinter
import customtkinter
from pytubefix import YouTube as yt

# download function
def startDownload():
    try:
        ytLink = link.get()
        ytObject = yt(ytLink)
        video = ytObject.streams.get_highest_resolution()
        video.download()
    except:
        print("download failed")
    print("downloaded.")


# settings
customtkinter.set_appearance_mode("Dark") # dark mode only because its superior
customtkinter.set_default_color_theme("green")

# frame
app = customtkinter.CTk()
app.geometry("480x480")
app.title("yt downloader")

# UI
title = customtkinter.CTkLabel(app, text="insert link")
title.pack(padx=12, pady=12)

# link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# download button
download = customtkinter.CTkButton(app, text="download", command=startDownload)
download.pack(pady=10)

# run

app.mainloop()
