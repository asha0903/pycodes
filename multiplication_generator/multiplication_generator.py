from tkinter import *
#combobox is defined inside ttk
from tkinter.ttk import *
  
# Creating tkinter window 
window = Tk() 
window.title('Mathematical table generator')
  
# label text for title 
title=Label(window, text = "Mathematical table")
# label 
caption=Label(window, text = "Number and Range:")

#place labels
title.grid(row = 0, column = 0,columnspan=3,pady=25)
caption.grid(column = 0,row = 1,padx=10)
  
# Combobox creation 
theNum = IntVar() 
numbers=Combobox(window,textvariable = theNum,width=5)   
# Adding combobox drop down list 
numbers['values'] = tuple(range(101))


#radio buttons
endVal = IntVar()
r10=Radiobutton(window,text="10",variable=endVal,value=10)
r20=Radiobutton(window,text="20",variable=endVal,value=20)
r30=Radiobutton(window,text="30",variable=endVal,value=30)
#set the default value
endVal.set(10)


#place radiobuttons and combobox
numbers.grid(column = 1, row = 1)
r10.grid(column = 2, row = 1,padx=30)
r20.grid(column = 2, row = 2,padx=30)
r30.grid(column = 2, row = 3,padx=30)


def generateMulTable():
    tables=""
    for i in range(endVal.get()+1):
        #tables+="{:^10d} X {:^10d} = {:^10d}\n".format(theNum.get(),i,theNum.get()*i)
        tables+=str(theNum.get())+"   X   "+str(i)+"   =   "+str(theNum.get()*i)+"\n" 
    table.configure(text=tables)

#create button and result table
generateButton=Button(window,text="Generate",command=generateMulTable)
table=Label(window,anchor="center")

#place button and result table
generateButton.grid(row=4,column=1)
table.grid(row=5,column=1,pady=20)


window.mainloop() 
