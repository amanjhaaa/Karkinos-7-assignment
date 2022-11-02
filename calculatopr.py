from tkinter import *
from math import *

from tkinter import messagebox

 


def deg_rad():
    selection = var.get()
    if selection == 1:
        result = radians(eval(value.get()))
        var.set(result)
    else :
        result = degrees(eval(value.get()))   
        var.set(result)

def isPowerSignExist(text):
    if "^" in text:
        return True
    else:
        return False
        
def isgcdsignexist(text):
    if "gcd" in text:
        return True
    else:
        return False
        

def input1(event):
    text = event.widget.cget("text")
    # print(text)

    if text == "=":
        try:
            if isPowerSignExist(value.get()):
                result = pow(eval(value.get().split("^")[0]),eval(value.get().split("^")[1]))
            
            elif isgcdsignexist(value.get()):
                result = gcd(eval(value.get().split("gcd")[0]),eval(value.get().split("gcd")[1]))
            
            else:
                
                # try evaluating the resulting str
                result = eval(str(value.get()))
            value.set(result)
        except Exception as e:
            # if failed its as error
            value.set("Error")
            print("error", e)
           
    elif text == "X":
        try:
            fullstring = value.get()
            # we are replacing the last string item[-1] with blank or ""
            # String slicing method
            newstring = fullstring.replace(fullstring[-1], "")
            value.set(newstring)

            # print(newstring)
            entry1.update()
        except Exception as e:
            print(e)

    elif text == "C":
        """"This will clear the screen"""
        value.set("")
        entry1.update()
    elif text == "x!":
        #finding out the factorial of the given number 
        try:
            result = factorial(int(value.get()))
            value.set(result)
        except Exception as e:
            value.set("Error")
            print("Error",e)
            
    
       
    elif text == 'deg':
        result = degrees(int(value.get()))   
        value.set(result)
    
    elif text == "rad":
        result = radians(eval(value.get()))
        value.set(result)
    
    elif text == "sin":
        result = sin(radians(eval(value.get())))
        value.set(result)        
    
    elif text =="cos":
        result = cos(radians(eval(value.get())))
        value.set(result)
    
    
    elif text == "tan":
        
        result =tan(radians(eval(value.get())))
        value.set(result)
    

    elif text == "ln":
        result =log(float(value.get()))
        value.set(result)    
    
    elif text == "log10":
        result =log10(float(value.get()))
        value.set(result)    
    
    elif text == "sqrt":
        result = sqrt(eval(value.get()))
        value.set(result)
    
    
    
    
    else:
        """if 1st input is 5, 2nd is 4 or + , both will be converted into string ie 54 or 5+"""
        value.set(value.get() + text)
        
        entry1.update()
        print("print value",value.get())
        print("print text",text)

root = Tk()
root.geometry("550x550")
root.title("CALCULATOR FROM AMAN JHA")
root.configure(background = "grey")
value = StringVar()

#p1 = PhotoImage(file = 'info.png') 
  
# Setting icon of root window 
#root.iconphoto(False, 'info.png') 

# root.wm_iconbitmap("info.ico")

entryframe = Frame(root, borderwidth=5, relief=SUNKEN)
entry1 = Entry(entryframe, font="arialblack 20 bold", textvariable=value)
entry1.pack()
entryframe.pack(pady=20, padx=5)

var = IntVar()
#var.set("1")
radio = Radiobutton(root,text ="rad",padx =  5,variable = var,value = "1").pack(pady = 5)
radio = Radiobutton(root,text ="deg",padx =  5,variable = var,value = "2").pack(pady =5)
Button(text = "DONE",command =deg_rad).pack()



buttonframe = Frame(root,)

list1 = ["INV","deg","%","(",")","C","X","sin","cos","tan",
         "7","8","9","/","ln","log10","sqrt","4","5","6","*",
         "pi","e","^","1","2","3","-","x!","gcd","rad","0",
         ".","=","+"]
i = 0



for place in list1:
    button1 = Button(buttonframe, text = place, font="lucida 15 ", padx=15, width=1,pady=15)
    button1.grid(row=int(i / 7), column=i % 7,ipadx = 3,ipady = 3)
    i = i + 1

    button1.bind("<Button-1>", input1)
    
buttonframe.pack(padx = 5,pady = 5)

def Sci():
    root.resizable(width=True,height=True)
    root.geometry("835x568")


def Simple():
    root.resizable(width=True,height=True)
    root.geometry("480x568")

def Exit():
    if messagebox.askyesno("Calculator","Confirm if you want to quit"):
        root.destroy()
        return


menubar = Menu(root)

file_menu = Menu(menubar,tearoff=0)

file_menu.add_command(label="Simple",command=Simple)
file_menu.add_command(label="Scientific",command=Sci)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=Exit)
menubar.add_cascade(label="File",menu=file_menu)

root.config(menu=menubar)





root.mainloop()