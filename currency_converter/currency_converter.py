from tkinter import *
#combobox is defined inside ttk
from tkinter.ttk import *


#create the window
window=Tk()
#set size of window
window.geometry("400x120")
#title of window
window.title("Currency Converter")

#add widgets to window
#heading label
heading=Label(window, text='CURRENCY CONVERTER')
#source currency label
sLabel=Label(window, text='Source Currency amount (Rs.)')
#target currency label
tLabel=Label(window, text='Target Currency')

x = StringVar() 
currency=Combobox(window,textvariable = x,width=10)
currency['values']=["Dollar","Euro","Pound"]
currency.grid(row=3,column=2, pady=10)

#source currency entry
sEntry = Entry(window)
#result-target currency
result=Label(window)

#arrange widgets on a grid
heading.grid(row=0,column=1) 
sLabel.grid(row=1,column=0)
tLabel.grid(row=3,column=0)
sEntry.grid(row=1,column=2) 
result.grid(row=4,column=2)

#function to convert from Rs to Dollar
def convert():
    sCurrency=float(sEntry.get())
    if str(x.get())=="Dollar":        
        result.configure(text=sCurrency*0.014)
    elif str(x.get())=="Euro":        
        result.configure(text=sCurrency*0.011)
    elif str(x.get())=="Pound":        
        result.configure(text=sCurrency*0.0097)
      

#add a button
button = Button(window, text = "Convert",command=convert)
button.grid(row=4,column=0)

#call main loop
window.mainloop()



