import os
from tkinter import Button, Label, Entry, StringVar,Tk
from tkinter.filedialog import askdirectory
from tkinter import messagebox

root=Tk()
contain=StringVar()
replace=StringVar()
filepath=StringVar()
def brow():
    address=askdirectory(title="select directory")
    print (address)
    filepath.set(address)


def junk() :
    temp=[]
    if contain.get() != "" :
        for file in os.listdir(filepath.get()) :
            temp.append(file)
        
        for names in temp:
            if  str(names).lower().find(contain.get().lower()) != -1 :
                indstr=(str(names).lower().index(contain.get().lower()))
                print(str(names).replace(str(names)[indstr:indstr+len(contain.get())], replace.get()))
                os.renames(os.path.join(filepath.get(),names), os.path.join(filepath.get(),str(names).replace(str(names)[indstr:indstr+len(contain.get())], replace.get())))
    else :
        messagebox.showinfo("Warning!", "Contain Field Can't Be Empty!")
        

Button(text="Browse",command = brow).grid(row=3,column=0)
Label(text="contain").grid(row=1,column=0)
Label(text="replace with:").grid(row=2,column=0)
Entry(textvariable=contain).grid(row=1,column=1)
Entry(textvariable=replace).grid(row=2,column=1)
Button(text="remove Junk!",command=junk,fg="red").grid(row=3,column=1)

root.mainloop()