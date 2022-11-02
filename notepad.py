
def newFile():
    global file 
    file = None
    TextArea.delete(1.0,END)
    

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - amanpad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


def saveAs():
    global file 
    if file == None:
        file  = asksaveasfilename(initialfile = "Untitled.txt",
        defaultextension =".txt",filetype = [("All files","*.*"),
        ("Text Documents","*.txt")])
        if file == "":
            file == None
        else:
            #save as newFile
            f = open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()
            
            root.title(os.path.basename(file)+"- amanpad")
            
            print("file saved")
    else:
        #save the file 
        
        f = open(file ,"w")
        f.write(TextArea.get(1.0,END))
        f.close()
        
    

def Exit():
    if askyesno("amanpad","Confirm if you want to quit") :
        root.destroy()
        return


def cut():
    TextArea.event_generate(("<<Cut>>"))
def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))
    
def undo():
    TextArea.event_generate(("<<Undo>>"))


def redo():
    TextArea.event_generate(("<<redo>>"))

def find():
    top = Toplevel()
    top.geometry("655x333")
    
    top.title("find text for amanpad")
    #top.configure(bg = "black")
    def findstring():
        pass
    def findNext():
        ans = findentry.get()
        result = TextArea.find(val)
        print("substring {} found at the index {}".format(ans,result))
        
        if(TextArea.find(ans) != -1):
            print("substring {} found at the index {}".format(ans,result))
        else:
            print("substring",ans,"doesnot found in the textarea")
        
    def cancel():
        top.destroy()
            




    fin = Label(top, text="find what")
    fin.grid()
    string = "my name is aman jha"
    findvalue = StringVar()

    findentry = Entry(top, textvariable = findvalue,bd = 4,relief = SUNKEN)
    findentry.grid(row=0, column=1)

    Button(text="Submit", command=findstring).pack(anchor = S)

    var = IntVar()


    Label(top, text = "direction",font="lucida 20 bold",justify=RIGHT, ).grid(row = 4,column = 11)

                
    radio = Radiobutton(top,text ="up",padx =  5,variable = var,value = "1").grid(pady = 3,row  = 5,column = 11)
    radio = Radiobutton(top,text ="down",padx =  5,variable = var,value = "2").grid(pady =3,row = 5,column = 12)


    CheckVar1 = IntVar()
    CheckVar2 = IntVar()
    C1 = Checkbutton(text = "match case", variable = CheckVar1)
    C2 = Checkbutton(text = "wrap around", variable = CheckVar2)
    C1.pack()
    C2.pack()

    b1 = Button(top,fg = "red",text = "find_next")
    b2 = Button(top,fg = "red",text = "Cancel",command = cancel)

    b1.grid(row = 9, column = 30, sticky = E, pady = 2) 
    b2.grid(row = 10, column = 30, sticky = E, pady = 2) 




    top.mainloop()


def replace():
    pass


def about():
    showinfo("amanpad","on the basis of notepad here made amanpad by aman jha")

def rate():
    print("Rate us")
    value =askquestion("Was your experience Good?", 
                    "You used this gui.. Was your experience Good?")
    if value =="yes":
        message = ("Thanks for your feedback.plz spread it among your friend as it is totally swadeshi app")
    else:
        message = ("Sorry for inconvenience. plz tell your problem so that  we can fix it  out")
    showinfo("experiance",message)                   



from tkinter import *
from tkinter.messagebox import showinfo,askyesno,askquestion
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
import time as tm

if __name__ == "__main__":
    
    #Basic tkinter setup
    root =Tk()
    root.title("Untitled - Amanpad")
    root.geometry("500x500")
    # root.wm_iconbitmap("info.ico")
    
    #setting scrollbar for y axis
    Scroll = Scrollbar(root)
    Scroll.pack(side=RIGHT,  fill=Y)    
    
    #setting scrollbar for x-axis
    Scroll2 = Scrollbar(root,orient ="horizontal")
    Scroll2.pack(side="bottom",fill=X)
    
    
    #Addd TextArea
    
               
    TextArea = Text(root,font = "georgia 20",yscrollcommand = Scroll.set, 
               xscrollcommand = Scroll2.set,  
               wrap = "none")               
    file = None
    TextArea.pack(expand = False ,fill = BOTH)
    
    
    #creating a menubar
    MenuBar = Menu(root)
    
    #file menu starts
    FileMenu = Menu(MenuBar,tearoff = 0)
    
    #to open a new file 
    FileMenu.add_command(label = "New",command = newFile)
    
    #to open existing file 
    FileMenu.add_command(label = "Open",command = openFile)
    
    # to save current file 
    FileMenu.add_command(label = "Save",command = saveAs)
    
    #to add separator after the save file 
    FileMenu.add_separator()
    
    #to exit the amanpad
    FileMenu.add_command(label = "Exit",command = Exit)
    
    # to add these all submenu to the main menu 
    MenuBar.add_cascade(label ="File",menu = FileMenu)
    
    
    
    #file menu ends
    
    #edit menu starts
    EditMenu = Menu(MenuBar,tearoff = 0)
    
    #to cut the selected content
    EditMenu.add_command(label = "Cut",command = cut)
    
    #to to copy the selected content 
    EditMenu.add_command(label = "Copy",command = copy)
    
    # to paste the copied content
    EditMenu.add_command(label = "Paste",command = paste)
    
    #to add separator after the paste function
    EditMenu.add_separator()
    
    #to undo the gui
    EditMenu.add_command(label = "Undo",command = undo)
    
    #to redo the gui
    EditMenu.add_command(label = "Redo",command = redo)
    
    
    #to add separator after the redo function    
    EditMenu.add_separator()
    
    #to find the substring
    EditMenu.add_command(label = "Find",command = find)
    
    #to replace the substring
    EditMenu.add_command(label = "Replace",command =replace)
    
    
    
    # to add these all submenu to the main menu 
    MenuBar.add_cascade(label ="Edit",menu = EditMenu)
    
    # Help Menu Starts
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label = "About amanpad", command=about)
    HelpMenu.add_command(label = "rate us", command=rate)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)

    # Help Menu Ends
    
    current_time = tm.strftime("%H:%M:%S")
    clock_label = Label(root,font = "arial 30",bg = "black",fg = "red",text = current_time)
    clock_label.pack()
    
    root.config(menu=MenuBar)

    #adding scrollbar for the y axis of amanpad

    Scroll.config(command=TextArea.yview)
    #TextArea.config(yscrollcommand=Scroll.set)

    
    #adding scroll to the x axis of amanpad
    Scroll2.config(command=TextArea.xview)
    #TextArea.config(yscrollcommand=Scroll.set)    
    
    
    
    root.mainloop()
    