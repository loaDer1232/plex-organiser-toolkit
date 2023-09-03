from tkinter import Tk, filedialog, Label, Button, Entry, Checkbutton
import subprocess

class GUI:
    def __init__(self) -> None:
        self.file_path: str

    def fileDialog(self)-> str:
        self.file_path = filedialog.askdirectory()
    
    def getPath(self) -> str:
        return self.file_path
    

window = Tk()
c = GUI()
movie: bool = 0
nameEntry = Entry(window, width=7, textvariable="")


def submit():
    path = c.getPath()
    name = nameEntry.get()
    if movie == True:
        dump = subprocess.run(["python", "File_Renamer.py", "-m", path, name])
    else:
        dump = subprocess.run(["python", "File_Renamer.py", path, name])

def main()-> None:
    Label(window, text="pyhton function renamer", font=("bold", 13)).grid(row=1, column=1)
    Label(window, text="enter new name:", font=("bold", 13)).grid(row=2, column=1)
    nameEntry.grid(row=2, column=3)
    Checkbutton(window, text='movie', variable=movie, onvalue=1, offvalue=0, ).grid(row=3, column=1)
    Button(window, text="File location", command=c.fileDialog ,width=10, height=1).grid(row=3, column=3)
    Button(window, text="submit", command=submit ,width=10, height=1).grid(row=4, column=1)

main()
window.mainloop()