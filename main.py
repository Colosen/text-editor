from tkinter import *

win = Tk()
win.geometry("900x900")
win.minsize(900, 900)
win.title("Text editor")

title_text = Text(win, height=800, width=900)
title_text.place(x=0, y=25)

save_button = Button(win, text="Save", height=1, width=5)
open_button = Button(win, text="Open", height=1, width=5)

save_button.place(x=0, y=0)
open_button.place(x=45, y=0)

print("Hello world!!")
win.mainloop()