from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter.filedialog import *


window=Tk()
window.title('Address Book')
#-----------------------------------------------------------------------
#functions
AddressBook_dict={}

#clears all the text boxes on main screen
def clear_all():
    name.delete(0,END)
    address.delete(0,END)
    mobile.delete(0,END)
    email.delete(0,END)
    birthday.delete(0,END)

#update the listbox
def update():
    key=name.get()
    if key=="":
        messagebox.showinfo("Error", "Name cannot be empty")
    else:
        #adds to list box only if it is a new entry
        if key not in AddressBook_dict.keys():
            book_list.insert(END,key)
        #update dictionary
        AddressBook_dict[key]=(address.get(),mobile.get(),email.get(),birthday.get())
        #clear the textboxes
        clear_all()

#edit the selected item
def edit():
    #clear the textboxes if any
    clear_all()
    # get selected line index
    index = book_list.curselection()
    if index:
        #add name to text
        name.insert(0,book_list.get(index))
        #get details corresponding to name from dictionary
        details=AddressBook_dict[name.get()]        
        #add details to text boxes
        address.insert(0,details[0])
        mobile.insert(0,details[1])
        email.insert(0,details[2])
        birthday.insert(0,details[3])
    else:
        messagebox.showinfo("Error", "Select a name.")

#delete selected item
def delete():
    # get selected line index
    index = book_list.curselection()
    if index:
        #delete from dictionary
        del AddressBook_dict[book_list.get(index)]
        #delete from listbox
        book_list.delete(index)
        #clear the textboxes if any
        clear_all()
    else:
        messagebox.showinfo("Error", "Select a name.")

#-----------------------------------------------------------------------
def display(event):
    # Toplevel creates a new window
    newWindow = Toplevel(window)  
    # get selected line index
    index = book_list.curselection()
    #variable to store details
    contact=""
    if index:
        key=book_list.get(index)
        contact= "NAME     : "+key+"\n\n"        
        details=AddressBook_dict[key]        
        #add details to text boxes
        contact+="ADDRESS  : "+details[0]+"\n"
        contact+="MOBILE   : "+details[1]+"\n"
        contact+="E-MAIL   : "+details[2]+"\n"
        contact+="BIRTHDAY : "+details[3]+"\n"
  
    # A Label widget to show in toplevel 
    lbl=Label(newWindow)
    lbl.grid(row=0,column=0)
    lbl.configure(text=contact)
    
def reset():
    clear_all()
    #deletes the listbox
    book_list.delete(0,END)
    #Removes all existing entries
    AddressBook_dict.clear()
    bookName.configure(text='My Address Book')
    
#function to save dictionary to file                
def save():
    #get file using dialog
    #default extension is optional, here will add .txt if missing
    fout=asksaveasfile(defaultextension=".txt") #if filename selected
    if fout:
        print(AddressBook_dict,file=fout)
        reset()            
    else:
        messagebox.showinfo("Warning", "Address Book not saved")
        
#function to open a dictionary file
def openFile():
    global AddressBook_dict
    reset()
    #opens file using dialog
    fin=askopenfile(title='Open File')
    #if filename selected
    if fin:
        #read file 
        AddressBook_dict=eval(fin.read())
        #populate listbox
        for key in AddressBook_dict.keys():
            book_list.insert(END,key)
        #dispaly filename on screen
        bookName.configure(text=os.path.basename(fin.name))
    else:
        messagebox.showinfo("Warning", "No address book opened.")
        

#---------------------------------------------------------------------------

#design mainwindow

#Label address book name
bookName = Label(window, text='My Address Book',width=35)
bookName.grid(row = 0, column = 1,pady = 10,columnspan=3)

#Open address book 
open_button = Button(window, text='Open',command=openFile)
open_button.grid(row = 0, column = 3,pady = 10)

# Contact list
book_list =Listbox(window,height=15,width=30)
book_list.grid(row = 2, column = 0,columnspan=3, rowspan = 5 )
book_list.bind('<<ListboxSelect>>',display)


### Text fields to display contact information ###
# name
name_label =Label(window, text = 'Name:')
name_label.grid(row= 2, column = 3)
name =Entry(window)
name.grid(row = 2, column = 4,padx=5)

# Address 
address_label =Label(window, text = 'Address :')
address_label.grid(row = 3, column = 3)
address =Entry(window)
address.grid(row = 3, column = 4,padx=5)

# Mobile phone
mobile_label =Label(window, text = 'Mobile:')
mobile_label.grid(row = 4, column = 3)
mobile =Entry(window)
mobile.grid(row = 4, column = 4,padx=5)

# Email
email_label = Label(window, text = 'Email:')
email_label.grid(row = 5, column = 3)
email =Entry(window)
email.grid(row = 5, column = 4,padx=5)

# Birthday
birthday_label = Label(window, text = 'Birthday:')
birthday_label.grid(row = 6, column = 3)
birthday = Entry(window)
birthday.grid(row =6, column = 4,padx=5)

#buttons

# Edit contact button
Edit_button = Button(window, text = 'Edit',width=10,command=edit)
Edit_button.grid(row = 7, column = 0, padx = 12,pady=12) 

# Delete contact button
delete_button =Button(window, text = 'Delete',width=10,command=delete)
delete_button.grid(row = 7, column = 1,pady=12 )

# Update/Add  contact button
add_button =Button(window, text = 'Update/Add',command=update)
add_button.grid(row = 7, column = 4,pady=12)

#save address book button
save_button = Button(window, text='Save',width=35,command=save)
save_button.grid(row = 8, column = 1,pady = 10,columnspan=3)

window.mainloop()
