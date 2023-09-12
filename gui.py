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

def osDetector(os: str)-> str:
   match os:
        case "Windows":
           return "python"
        case "Linux":
           return "python3"
        case "Darwin":
            return "python3"
        case _:
           exit(code=1)

def optionsAdder()-> list[str, str]:
    optionslist = [osDetector(system()), "File_Renamer.py"]
    if movieBox.get():
        optionslist.append("-m")
    if strictFileMode.get():
        optionslist.append("-cu")
    if log.get():
        optionslist.append("-l")
    
    optionslist.append(c.getPath())
    optionslist.append(nameEntry.get())
    return optionslist

def submit()-> None:
    command: list[str, str] = optionsAdder()
    dump = subprocess.run(command)
    return None

header = CTkLabel(window, text="Pyhton Function Renamer")
newName = CTkLabel(window, text="Enter New Name:")
miscOpptions = CTkLabel(window, text="addtional opptions:")

movieBox = CTkCheckBox(window, text='Movie')
strictFileMode = CTkCheckBox(window, text='Strict File Mode')
log = CTkCheckBox(window, text='Log')

nameEntry = CTkEntry(window, width=120, textvariable="")

fileLocation = CTkButton(window, text="Select File location", command=c.fileDialog ,width=50)
submmitButton = CTkButton(window, text="Submit", command=submit ,width=50)

def main()-> None:
    header.place(relx=0.5, anchor=N)
    newName.place(relx=0.3, rely=0.2, anchor=CENTER)
    nameEntry.place(relx=0.7, rely=0.2, anchor=CENTER)
    fileLocation.place(relx=0.5, rely=0.4, anchor=CENTER)
    miscOpptions.place(relx=0.5, rely=0.6, anchor=CENTER)
    movieBox.place(relx=0.9, rely=0.7, anchor=CENTER)
    strictFileMode.place(relx=0.5, rely=0.7, anchor=CENTER)
    log.place(relx=0.2, rely=0.7, anchor=CENTER)
    submmitButton.place(relx=0.5, rely=0.9, anchor=CENTER)

if __name__ == "__main__":
    main()
    window.mainloop()