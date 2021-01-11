import os 
import vt # vt-py
import tkinter
import infi.systray # infini.systray

from tkinter import filedialog

# Important defenitions (partly to avoid not-defined error)
cwd = os.getcwd()

checkFileBtn = tkinter.Button()
filenameTxt = tkinter.Label()
resultTxt = tkinter.Label()

# GUI
win = tkinter.Tk()
win.title("copper - Dashboard")
win.config(bg="#141414")
win.geometry("500x400")
# win.iconphoto(False, tkinter.PhotoImage(file=cwd + "\\src\\icon_small.png"))
print(cwd + "\\src\\icon_small.png")

# Tray
try:
    def say_hello(systray):
        print("Hello, World!")

    systray = infi.systray.SysTrayIcon(cwd + "\\src\\favicon.ico", "copper", (("Say Hello", None, say_hello),))
    systray.start()
except:
    print("Systr")

# API
with open (cwd + "\\config\\token.txt") as f:
    token = f.read()
print(token)

try:
    client = vt.Client(token)
except:
    print("ERROR - Failed to connect to API. Invalid token?")

# Function
def check_file(file):
    try:
        file_analysis = client.get_object(file)
        return file_analysis.last_analysis_stats
    except:
        print("WARNING - Failed file analysis.")

        with open("/path/to/file", "rb") as f:
            resultTxt["text"] = "Checking file..."
            file_analysis = client.scan_file(f, wait_for_completion=True)
            return file_analysis


def check_file_button(): # on button press
    checkFileBtn["text"] = "Select a file..."
    selected_file = tkinter.filedialog.askopenfilename(title="Select file", filetypes = (("all files","*.*")))
    filename = selected_file.split("/")[-1]
    check_result = check_file(selected_file)
    
    filenameTxt["text"] = filename
    resultTxt["text"] = check_result

# GUI:
checkFileTxt = tkinter.Label(win, text="Check a file for viruses", font=("Yu Gothic Light", 25), fg="white", bg="#141414")
checkFileTxt.pack()

checkFileBtn = tkinter.Button(win, text="Check file", command=check_file_button, font=("Yu Gothic Light", 20), fg="white", bg="#0080FF", relief="flat")
checkFileBtn.pack()

filenameTxt = tkinter.Label(win, text="Please select a file", font=("Yu Gothic Light", 25), fg="white", bg="#141414")
filenameTxt.pack()

resultTxt = tkinter.Label(win, text="", font=("Yu Gothic Light", 20), fg="white", bg="#141414")
resultTxt.pack()

# Mainloop
win.mainloop()
