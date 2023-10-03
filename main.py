import tkinter
import customtkinter
from pytube import YouTube

# funtions
def start_download():
  try:
    yt_link = link.get()
    yt_object = YouTube(yt_link, on_progress_callback=on_progress)
    video = yt_object.streams.get_highest_resolution()
    video.download()
    title.configure(text=yt_object.title, text_color="white")
    finishe_label.configure(text="Download completo!", text_color="white")

  except:
    finishe_label.configure(text="falha no download!", text_color="red")

def on_progress(stream, chunk, bytes_remaining):
  total_size = stream.filesize
  bytes_downloaded = total_size - bytes_remaining
  porcentage_of_completion = bytes_downloaded / total_size * 100
  percent = str(int(porcentage_of_completion))
  porcentagem.configure(text=percent + "%")
  porcentagem.update()

  # Update Progressbar
  progress_bar.set(float(porcentage_of_completion) / 100)

    

# sistem settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# adding UI Elements
title = customtkinter.CTkLabel(app, text="Insira o link do vídeo do Youtube:")
title.pack(padx=10, pady=10)

# link do Youtube
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Finished download
finishe_label = customtkinter.CTkLabel(app, text="Clic aqui!")
finishe_label.pack(padx=10, pady=10)

# Download Button
btn_downlad = customtkinter.CTkButton(app, text="Download", command=start_download)
btn_downlad.pack(padx=10, pady=10)

# Progressbar
progress_bar = customtkinter.CTkProgressBar(app, width=400)
progress_bar.set(0)
progress_bar.pack(padx=10, pady=10)

porcentagem = customtkinter.CTkLabel(app, text="0%")
porcentagem.pack(padx=10, pady=10)





# Run app
if __name__=='__main__':
  app.mainloop()
