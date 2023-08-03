                     # Tkinter project        
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
root=Tk()
root.geometry("500x488")
root.title("NOTEPAD")
img =  PhotoImage(file="logo.png")
root.iconphoto(0,img)

# Add TextArea
TextArea = Text(root, font="Aerial 18 italic bold")
file = None
TextArea.pack(expand=True , fill=BOTH)
#Lets create a menu bar


def newfile():
    global file
    root.title("Untitled - Notepad")
    file =None
    TextArea.delete(1.0,END)

def openfile():
    global file
    file = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file =="":
        file=None
    else:
        root.title(os.path.basename(file)+" - Notepad")
        TextArea.delete(1.0,END)
        f= open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close()

def savefile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

        if file=="":
            file =None
        else:
            #save the file
            f = open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+" - Notepad")
            #print("file saved")
def quitApp():
    pass

def cut():
    TextArea.event_generate("<<Cut>>")
def copy():
    TextArea.event_generate("<<Copy>>")
def paste():
    TextArea.event_generate("<<Paste>>")

def about():
    showinfo("Notepad",f"Notepad by Lalit...{chr(128512)}")


MenuBar = Menu(root)

#file menu starts
FileMenu = Menu(MenuBar,tearoff=0)
# To open a new file
FileMenu.add_command(label="New",command=newfile)
# To open already existing file
FileMenu.add_command(label="Open",command=openfile)
# To save the current file
FileMenu.add_command(label="Save",command=savefile)
FileMenu.add_separator()
#Exit from the Notepad
FileMenu.add_command(label="Exit", command=quitApp())
MenuBar.add_cascade(label="File",menu=FileMenu)

#File menu ends.

#Edit Menu Starts

editmenu = Menu(MenuBar,tearoff=0)
#To give feature of cut, copy and paste
editmenu.add_command(label="Cut",command=cut)
editmenu.add_command(label="Copy",command=copy)
editmenu.add_command(label="Paste",command=paste)

MenuBar.add_cascade(label="Edit",menu=editmenu)

#Edit Menu Ends

#helps Menu Starts

helpmenu = Menu(MenuBar,tearoff=0)
helpmenu.add_command(label="About Notepad",command=about)
MenuBar.add_cascade(label='Help',menu=helpmenu)

#help Menu Ends



root.config(menu=MenuBar)

#Adding Scroolbar

Scroll = Scrollbar(TextArea,background="red",borderwidth=5)
Scroll.pack(side=RIGHT, fill=Y)
Scroll.config(command=TextArea.yview)
TextArea.config(yscrollcommand=Scroll.set,background="white")

root.mainloop()
