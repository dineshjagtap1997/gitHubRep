# from tkinter import ttk
# import tkinter as tk
# import pytube
#
# win=tk.Tk()
# entry=ttk.Entry(win)
# entry.grid(row=0,column=2)
#
#
# def download():
#     url=entry.get()
#
#     video=pytube.YouTube(url)
#     youtube=video.streams.first()
#     youtube.download(r'E:\mca\1Apython\project')
#
# button=ttk.Button(win,text="Download",command=download)
# button.grid(row=1,column=2)
# #
#
# win.mainloop()



import pytube
url="https://www.youtube.com/watch?v=FfZk1SrCyFs"
video=pytube.YouTube(url)
youtube=video.streams.first()
youtube.download(r'E:\mca\1Apython\project')
