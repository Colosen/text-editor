from tkinter import *
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfile

#initializing global variables
current_working_file_name = ""


def saveAs():
    #creating "Save as" window
    save_as_filetypes = [
        ("All files", "*.*"),
        ("Text documents", "*.txt"),
        ("Python files", "*.py")
        ]
    file = asksaveasfile(initialfile="Untitled.txt", defaultextension=".txt", filetypes=save_as_filetypes)
    print("File name is", file.name)
    file_name = file.name
    text_to_save = text_box.get("1.0", "end-1c")
    print(text_to_save)

    with open(str(file_name), 'w') as f:
        f.write(text_to_save)


def save(file_name=current_working_file_name): # @TODO Fix default parameter file_name to take the address of current_working_file_name
    print("File name as passed to save() function: ", file_name)
    print(f"Value of current_working_file_name: {current_working_file_name}")

    # save changes made to document in question
    text_to_update = text_box.get("1.0", "end-1c")
    print("Changes made to current working file before save: ", text_to_update)

    print(f"opening {current_working_file_name} to write changes to file.")
    with open(current_working_file_name, 'w') as f:
        f.write(text_to_update)
    print("Changes saved to file.")


def open_file():
    open_filetypes = [
        ("All files", "*.*"),
        ("Text documents", "*.txt"),
        ("Python files", "*.py")
        ]
    file = askopenfile(initialdir="D:", filetypes=open_filetypes)

    print("File IO wrapper: ", file)

    file_name = file.name
    print("File name as opened by user: ", file_name)

    global current_working_file_name
    current_working_file_name = file_name

    print(f"Opening {file_name} to read file.")
    with open(file_name, 'r') as f:
        text = f.read()
    print("Successfully read file.")

    text_box.insert(INSERT, text)
    print("Successfully inserted text into text box.")
    print(f"Text inserted into file at {file_name}:", text)

    win.title(file_name) # changing window title bar text to file_name


def close():
    win.destroy()


# creating main window
win = Tk()
win.geometry("900x900")
win.minsize(900, 900)
win.title("Untitled.txt")

# creating title text
text_box = Text(win, height=800, width=900)
text_box.place(x=0, y=25)

# creating header buttons
save_as_button = Button(win, text="Save as", height=1, width=5, command=saveAs)
save_button = Button(win, text="Save", height=1, width=5, command=save)
open_button = Button(win, text="Open", height=1, width=5, command=open_file)

# placing header buttons
save_as_button.place(x=0, y=0)
save_button.place(x=45, y=0)
open_button.place(x=90, y=0)

# console output
print("Program starting!")

# close all windows if there is an input to the console
dialogue = input("Enter any input to exit:\n")
if dialogue:
    print("Closing program...")
    close()

win.mainloop()

