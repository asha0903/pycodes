#CREATING A BIRHDAY CARD

#importing the required libraries

from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter.filedialog import *
import pygame
import time


window=Tk()
#window.geometry("300x200")
window.title('Fill in the details')

store_dict={}

#store it in dictionary
def generate():
    
    key=name_entry.get()
    if key=="":
        messagebox.showinfo("Error", "Name cannot be empty")
    else:
        
        #update dictionary
        
        #store_dict[key]=(age_entry.get(),date_entry.get(),time_entry.get(),address_entry.get(),rsvp_entry.get())
        #details=store_dict[key]
        
        pygame.init()
        display_surface=pygame.display.set_mode((600,650))
        
        image=pygame.image.load("rose_gold_background.jpg")
        image=pygame.transform.scale(image,(600,650))
        
        font=pygame.font.SysFont("Comic Sans MS",60)
        font3=pygame.font.SysFont("Times New Roman",20)
        font2=pygame.font.SysFont("Forte",50)
        font4=pygame.font.SysFont("Forte",20)
        font5=pygame.font.SysFont("Times New Roman",15)
        
        text=font.render("Birthday Party!!!",True,(255,255,255))        
        text2=font3.render("HONORING", True,(0,0,0))        
        text3=font2.render(name_entry.get(),True,(128,0,128))
        text4=font3.render("AS SHE TURNS "+age_entry.get()+"!",True,(0,0,0))        
        text5=font4.render("Join us",True,(128,0,128))
        text6=font5.render("Date : "+ date_entry.get(),True, (0,0,0))
        text7=font5.render("Time : "+ time_entry.get(),True, (0,0,0))
        text8=font5.render("Address : "+ address_entry.get(),True, (0,0,0))
        text9=font5.render("RSVP : "+ rsvp_entry.get(),True, (0,0,0))

        
        
        display_surface.blit(image,(0,0))
        display_surface.blit(text,(80,100))
        display_surface.blit(text2,(240,200))
        display_surface.blit(text3,(180,250))
        display_surface.blit(text4,(220,330))
        display_surface.blit(text5,(250,380))
        display_surface.blit(text6,(200,440))
        display_surface.blit(text7,(200,480))
        display_surface.blit(text8,(200,520))
        display_surface.blit(text9,(200,560))
        pygame.display.update()
        

heading=Label(window,text="FILL IN THE DETAILS")
heading.grid(row=0, column=1, columnspan=3)

name_lbl=Label(window,text="Name:")
name_lbl.grid(row=2, column=1,padx=10,pady=10)

name_entry=Entry(window,width=25)
name_entry.grid(row=2,column=3,padx=10)

age_lbl=Label(window,text="Age:")
age_lbl.grid(row=3, column=1,padx=10,pady=10)

age_entry=Entry(window,width=25)
age_entry.grid(row=3,column=3,padx=10)


date_lbl=Label(window,text="Date:")
date_lbl.grid(row=4, column=1,padx=10,pady=10)

date_entry=Entry(window,width=25)
date_entry.grid(row=4,column=3,padx=10)


time_lbl=Label(window,text="Time:")
time_lbl.grid(row=5, column=1,padx=10,pady=10)

time_entry=Entry(window,width=25)
time_entry.grid(row=5,column=3,padx=10)


address_lbl=Label(window,text="Address:")
address_lbl.grid(row=6, column=1,padx=10,pady=10)

address_entry=Entry(window,width=25)
address_entry.grid(row=6,column=3,padx=10)


rsvp_lbl=Label(window,text="RSVP:")
rsvp_lbl.grid(row=7, column=1,padx=10,pady=10)

rsvp_entry=Entry(window,width=25)
rsvp_entry.grid(row=7,column=3,padx=10)


generate_button=Button(window,text="GENERATE", command=generate)
generate_button.grid(row=9, column=1, columnspan=3,pady=10)

window.mainloop()







