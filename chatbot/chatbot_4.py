from tkinter import *
import random
from chatterbot  import ChatBot
from chatterbot.trainers import ListTrainer


root = Tk()
root.title("Comicbot")
bubbles = []


canvas = Canvas(root, width=350, height=500,bg="SlateBlue1")
canvas.grid(row=0,column=0,columnspan=3)


#-------------------------------------------------------------------
#create bot with logic adaptor
bot = ChatBot('Bot',  
    logic_adapters=[
        'chatterbot.logic.BestMatch'],)

# First, lets train our bot with some data
trainer = ListTrainer(bot)

#default response
default_response=open('default_response.txt','r').readlines()

#train using some selected conversation statements

files=['chat.txt','mickey.txt']

for file in files:
    conversation = open(file,'r').readlines()
    trainer.train(conversation)
#-------------------------------------------------------------------


class ChatBubble:
    def __init__(self,master,user,message=""):
        #user 1 is bot
        if user==1:
            colour="lightgrey"
            xpos=50
            ypos=450
            col=1
        else: #human
            colour="pink"
            xpos=150
            ypos=450
            col=2
            
        self.master = master
        #bubble formed by label + triangle at its bottom left corner
        #frame has label and window
        self.frame = Frame(master)        
        lbl=Label(self.frame, text=message,bg=colour,wraplength=200, anchor=W)
        lbl.pack()
        self.window = self.master.create_window(xpos,ypos,anchor=SW,window=self.frame)
        #window has triangle
        self.master.create_polygon(self.draw_triangle(self.window), fill=colour)        

    def draw_triangle(self,widget):
        x1, y1, x2, y2 = self.master.bbox(widget)
        return x1, y2 - 10, x1 - 15, y2 + 10, x1, y2
#----------------------------------------------------------------------------

def send_message(user,message):
    if bubbles:
        #move the existing bubbles upwards
        canvas.move(ALL, 0, -35)    
    a = ChatBubble(canvas,user,message)
    bubbles.append(a)

#------------------------------------------------------------------------------

name="" 
def send():
    global name
    message=entry.get()
    send_message(2,entry.get())
    entry.delete(0,END)
    #assuming first response from user will be name once Bot asks for it
    if name=="":
        name=message
        send_message(1,"Hello "+name+" .How are you doing?")
    else:
        if message.strip().lower()!= 'bye':
            reply = bot.get_response(message)
            if reply.confidence<0.70:
                send_message(1,random.choice(default_response).strip())
            else:
                send_message(1,str(reply).strip())
        else:
            send_message(1,'Nice talking to you')
            send_message(1,'Bye')

#Bot starts the conversation    
send_message(1,"Welcome to the magical world of Comics!!")
send_message(1,"What is your name?")

#----------------------------------------------------------------------
    
entry = Entry(root,width=50)
entry.grid(row=1,column=0,columnspan=2)
Button(root,text="Send",width=5,command=send).grid(row=1,column=2)
root.mainloop()
