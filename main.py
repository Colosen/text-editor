from tkinter import *
from tkinter.filedialog import asksaveasfile


def saveAs():
    #creating "Save as" window
    global save_as_window

    file = asksaveasfile(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("All files", "*.*"), ("Text documents", "*.txt")])
    print("\n" , " My file  Name is" , file.name)
    file_name = file.name
    text_to_save = text_box.get("1.0", "end-1c")
    print(text_to_save)

    with open(str(file_name), 'w') as f:
        f.write(text_to_save)


def save():
    # save changes made to document in question
    pass


def open_file():
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
text_box = Text(win, height=800, width=900)
text_box.place(x=0, y=25)

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

# close all windows if there is an input to the console
dialogue = int(input("Enter any input to exit:\n")) 
if dialogue:
    close()

win.mainloop()

 