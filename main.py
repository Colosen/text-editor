from tkinter import *

def saveAs():
    #creating "Save as" window
    global save_as_window
    save_as_window = Tk()
    width, height = 250, 100
    save_as_window.geometry("250x100")
    save_as_window.resizable(0, 0)

    name_text_box = Text(save_as_window, height=1, width=15) # the text in which to enter the filename
    name_text_box.place(x=width//2 - 60, y=height//2 - 5)

    final_save_button = Button(save_as_window, text="Save", height=1, width=5)
    final_cancel_button = Button(save_as_window, text="Cancel", height=1, width=5)

    pass

def save():
    # save changes made to document in question
    pass

def open():
    # open document @TODO file explorer implementation
    pass

def close():
    save_as_window.destroy()
    win.destroy()

# creating main window
win = Tk()
win.geometry("900x900")
win.minsize(900, 900)
win.title("Text editor")

# creating title text
title_text = Text(win, height=800, width=900)
title_text.place(x=0, y=25)

# creating header buttons
save_as_button = Button(win, text="Save as", height=1, width=5, command=saveAs)
save_button = Button(win, text="Save", height=1, width=5, command=save)
open_button = Button(win, text="Open", height=1, width=5, command=open)

# placing header buttons
save_as_button.place(x=0, y=0)
save_button.place(x=45, y=0)
open_button.place(x=90, y=0)

# console output
print("Hello world!!")

dialogue = int(input("Enter any input to exit:")) # close all windows if there is an input to the console
if dialogue:
    close()

win.mainloop()

