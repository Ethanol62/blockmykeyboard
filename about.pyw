from tkinter import *

window = Tk()

window.iconbitmap('icon.ico')

window.title("About")

title = Label(window, text = "  Welcome to BlockMyKeyboard (v1.0 -stable)  ", font = (16))
text = Label(window, text = "BlockMyKeyboard has the utility of blocking your keyboard\nin order to be able to clean it for example.\nLimited by Windows, unfortunately the Windows key cannot be blocked.\nFor laptops, volume keys, brightness etc... cannot be blocked.\n", font = (16))
text2 = Label(window, text = "Developed by Éthanol (https://github.com/Ethanol62)\n", font = (16))
footer = Label(window, text = "  © 2023, BlockMyKeyboard - All rights reserved  ", font = (16))
space = Label(window, text=" ", font=(16))

title.pack()
space.pack()
text.pack()
text2.pack()
footer.pack()

window.mainloop()