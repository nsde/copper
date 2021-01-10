import os
import tkinter
import infi.systray

# Important variables
cwd = os.getcwd()

# GUI
win = tkinter.Tk()
win.title("copper - Dashboard")
win.config(bg="#141414")
win.geometry("500x400")
win.iconphoto(False, tkinter.PhotoImage(file=cwd + "\\src\\icon_small.png"))

# Tray
def say_hello(systray):
    print("Hello, World!")

tray_options = (("Say Hello", None, say_hello),)
systray = infi.systray.SysTrayIcon(cwd + "\\src\\favicon.ico", "copper", tray_options)
systray.start()

# API
with open (cwd + "\\config\\token.txt") as f:
    token = f.read()
print(token)

# Mainloop
win.mainloop()
