import tkinter
from tkinter import filedialog 
import customtkinter
from pytube import YouTube
from PIL import Image 

def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progess)
        video = ytObject.streams.get_highest_resolution()

        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")

        # Open file selection dialog
        download_path = filedialog.askdirectory(title="Select Download Folder")

        if download_path:
            video.download(output_path=download_path)
            finishLabel.configure(text="Download succeful check your folder!", text_color="white")
        else:
            finishLabel.configure(text="Download cancelled", text_color="orange")

    except:
        finishLabel.configure(text="Download Error or invalid link", text_color="red")


def on_progess(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()

    # Update percentage
    progressBar.set(float(percentage_of_completion) / 100)

#system settings
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

#Our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("DOWNLOAD YOUTUBE VIDEO")

my_image = customtkinter.CTkImage(light_image=Image.open('yt.jpeg'), dark_image=Image.open('yt.jpeg'), size=(100, 100))
my_label = customtkinter.CTkLabel(app, text="", image=my_image)
my_label.pack(pady=10)

#Adding UI Elements
title = customtkinter.CTkLabel(app, text="Insert youtube link")
title.pack(padx=10, pady=10)

#Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

#Finish downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

#Progress percentage
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

#Download Button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

#Run app
app.mainloop()
