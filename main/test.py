import tkinter
from tkinter import filedialog

root = tkinter.Tk()
root.filename = tkinter.filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
print (root.filename)