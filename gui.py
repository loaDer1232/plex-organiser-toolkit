from customtkinter import *
import subprocess
from platform import system

class GUI:
    def __init__(self) -> None:
        self.file_path: str

    def fileDialog(self)-> str:
        self.file_path = filedialog.askdirectory()
    
    def getPath(self) -> str:
        return self.file_path
    

window = CTk()
window.geometry("400x300")
set_appearance_mode("System") 
set_default_color_theme("blue")
c = GUI()
movie: bool = 0
nameEntry = Entry(window, width=7, textvariable="")


def pyCalc(os: str)-> str:
   match os:
        case "Windows":
           return "python"
        case "Linux":
           return "python3"
        case "Darwin":
            return "python3"
        case _:
           exit(code=1)

def submit()-> None:
    path = c.getPath()
    name = nameEntry.get()
    pyver = pyCalc(system())

    if movie:
        dump = subprocess.run([pyver, "File_Renamer.py", "-m", path, name])
        return None
    else:
        dump = subprocess.run([pyver, "File_Renamer.py", path, name])
        return None

movieBox = CTkCheckBox(window, text='movie')
nameEntry = CTkEntry(window, width=120, textvariable="")
header = CTkLabel(window, text="pyhton function renamer", font=("bold", 13))
newName = CTkLabel(window, text="enter new name:", font=("bold", 13))
miscOpptions = CTkLabel(window, text="addtional opptions:", font=("bold", 13))
fileLocation = CTkButton(window, text="Select File location", command=c.fileDialog ,width=50)
submmitButton = CTkButton(window, text="submit", command=submit ,width=50)

movieBox = CTkCheckBox(window, text='movie')
nameEntry = CTkEntry(window, width=120, textvariable="")
header = CTkLabel(window, text="pyhton function renamer", font=("bold", 13))
newName = CTkLabel(window, text="enter new name:", font=("bold", 13))
miscOpptions = CTkLabel(window, text="addtional opptions:", font=("bold", 13))
fileLocation = CTkButton(window, text="Select File location", command=c.fileDialog ,width=50)
submmitButton = CTkButton(window, text="submit", command=submit ,width=50)

def main()-> None:
    header.place(relx=0.5, anchor=N)
    newName.place(relx=0.3, rely=0.2, anchor=CENTER)
    nameEntry.place(relx=0.7, rely=0.2, anchor=CENTER)
    fileLocation.place(relx=0.5, rely=0.4, anchor=CENTER)
    miscOpptions.place(relx=0.5, rely=0.6, anchor=CENTER)
    movieBox.place(relx=0.7, rely=0.7, anchor=CENTER)
    submmitButton.place(relx=0.5, rely=0.9, anchor=CENTER)

if __name__ == "__main__":
    main()
    window.mainloop()