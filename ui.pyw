import tkinter
from tkinter import *
import webbrowser
import subprocess


window = Tk()

window.title("BlockMyKeyboard")

window.iconbitmap('icon.ico')

window.geometry('300x120')

def open_tips():
    webbrowser.open('https://www.paypal.com/donate/?hosted_button_id=W4EXEC4V7H3NS')

def open_about():
    subprocess.run(["pythonw", "about.pyw"])

def start_block():
    subprocess.run(["python", "blockmykeyboard.py"])

cadre_vertical = tkinter.Frame(window)
cadre_vertical.pack(fill=tkinter.BOTH, expand=True)

menubar = Menu(window)

window.config(menu=menubar)

menufile = Menu(menubar,tearoff=0)
menubar.add_cascade(label="File", menu=menufile)
menufile.add_command(label="About", command=open_about)
menufile.add_separator()
menufile.add_command(label="Quit", command=window.destroy)

menutips = Menu(menubar, tearoff=0)
menubar.add_command(label="Tips", command=open_tips)

start_button = tkinter.Button(window, text="Start", command=start_block, width=30, height=4)
start_button.pack(pady=40)

window.mainloop()