from tkinter import *
from tkinter.filedialog import *


#create the window
master = Tk()
#title of window
master.title("To Do List")

#callback function to open file
def openFile():
    #opens file using dialog
    fin=askopenfile(title='Open File')
    #if filename selected
    if fin is not None:
        #delete items in listbox
        listbox.delete(0, END)
        #read from file
        items = fin.readlines()
        #insert to listbox
        for item in items:
            listbox.insert(END, item.strip())

#callback function to save file                
def saveFile():
    #get file using dialog
    # default extension is optional, here will add .txt if missing
    fout=asksaveasfile(defaultextension=".txt")
    #if filename selected
    if fout is not None:
        #get items in listbox and add to file
        for item in listbox.get(0,END):
            print(item.strip(),file=fout)
        #delete items in listbox
        listbox.delete(0, END)

#Function to add item to listbox
def addItem():
    listbox.insert(END,item.get())
    #delete from textbox
    item.delete(0,END)

#Function to delete item from listbox
def deleteItem():
    # get selected line index
    index = listbox.curselection()
    if index:        
        listbox.delete(index)
        

#create all buttons and place them on screen
fOpen=Button(master,text="OPEN",command=openFile,width=15)
lDelete=Button(master,text="DELETE",command=deleteItem,width=15)
fSave=Button(master,text="SAVE",command=saveFile,width=15)
fOpen.grid(row=0,column=0,padx=5,pady=5)
lDelete.grid(row=0,column=1,padx=5,pady=5)
fSave.grid(row=0,column=2,padx=5,pady=5)

#create add button and input, place them on screen
lAdd=Button(master,text="ADD",command=addItem,width=15)
item=Entry(master,width=35)
item.grid(row=1,column=0,columnspan=2,padx=5,pady=5)
lAdd.grid(row=1,column=2,padx=5,pady=5)

#create listbox and place on screen
listbox = Listbox(master,width=55)
listbox.grid(row=2,column=0,columnspan=3,pady=20,padx=5)


mainloop()
