import tkinter
import customtkinter
from pytubefix import YouTube as yt

# download function
def streamDownload(stream):
    try:
        stream.download()
        status_label.configure(text="downloaded")
    except Exception as e:
        print("download failed, {e}")

def displayMenu(ytObject):
    # Clear previous buttons if any
    for widget in menu_frame.winfo_children():
        widget.destroy()

    # Video streams (sorted by resolution)
    video_streams = ytObject.streams.filter(progressive=True, file_extension="mp4").order_by("resolution")
    for stream in video_streams:
        resolution_button = customtkinter.CTkButton(
            menu_frame, text=f"Video {stream.resolution}", command=lambda s=stream: streamDownload(s)
        )
        resolution_button.pack(pady=5)

    # Audio-only streams
    audio_streams = ytObject.streams.filter(only_audio=True).order_by("abr")
    for stream in audio_streams:
        audio_button = customtkinter.CTkButton(
            menu_frame, text=f"audio {stream.abr}", command=lambda s=stream: streamDownload(s)
        )
        audio_button.pack(pady=5)

def startDownload():
    ytLink = link.get().strip()
    if not ytLink:
        status_label.configure(text="invalid url")
        return
    try:
        ytObject = yt(ytLink)
        status_label.configure(text="fetching available streams...")
        displayMenu(ytObject)
    except Exception as e:
        status_label.configure(text=f"error: {e}")


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

# status label
status_label = customtkinter.CTkLabel(app, text="")
status_label.pack(pady=10)

# link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# search button
download = customtkinter.CTkButton(app, text="search", command=startDownload)
download.pack(pady=10)

# menu frame for resolution/audio buttons
menu_frame = customtkinter.CTkFrame(app)
menu_frame.pack(pady=10, fill="both", expand=True)

# run
app.mainloop()
