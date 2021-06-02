import pygame
import random
from pygame.locals import *
import time

#change background
def changeBackground(img):
    # Change the background 
    background = pygame.image.load(img)
    #set its size
    bg = pygame.transform.scale(background, (screen_width,screen_height))
    screen.blit(bg,(0,0))
  
 

# Initialize Pygame
pygame.init()
pygame.display.set_caption('Treasure Hunt')
# Set the height and width of the screen
screen_width=900
screen_height=700
screen = pygame.display.set_mode([screen_width,screen_height])

#Player sprite (Pirate)
class Pirate(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('pirate.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (70,100))
        self.rect = self.image.get_rect()

#Stone sprite
class Stone(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.image = pygame.transform.scale(self.image, (30,30))
        self.rect = self.image.get_rect()


#Soldier sprite
class Soldier(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('soldier.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (40,40))
        self.rect = self.image.get_rect()

#List of images for Stone class
images=["stone1.png","stone2.png","stone3.png"]
  

#create sprite groups
stone_list = pygame.sprite.Group()
allsprites= pygame.sprite.Group()
soldier_list=pygame.sprite.Group()

#create stone sprites
for i in range(100):
    stone = Stone(random.choice(images)) 
    # Set a random location for the stone
    stone.rect.x = random.randrange(screen_width)
    stone.rect.y = random.randrange(screen_height)
    # Add to stone list
    stone_list.add(stone)
    allsprites.add(stone)

#create soldier
for i in range(20):
    soldier=Soldier()
    # Set a random location for the soldier
    soldier.rect.x = random.randrange(screen_width)
    soldier.rect.y = random.randrange(screen_height)
    # Add to soldier list
    soldier_list.add(soldier)
    allsprites.add(soldier)
    
    
 
# Create pirate
pirate = Pirate()
allsprites.add(pirate)



#initialize essential variables
# Define colour
WHITE = (255, 255, 255)
RED=(255,0,0)

playing=True
score = 0
#clock 
clock = pygame.time.Clock()
#start time
start_time = time.time()
#font to print score on screen 
myFont=pygame.font.SysFont("Times New Roman",40)
timingFont=pygame.font.SysFont("Times New Roman",70)
text=myFont.render("Score ="+str(0),True,WHITE)


# -------- Main Program Loop -----------
while playing:
    #refresh 60 times in a second
    #can be used to control speed
    clock.tick(30)
        
    #quit the game
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            playing=False
    
    #check if time>60 secs
    timeElapsed=time.time()-start_time
    if timeElapsed >=60:        
        if score>50:
            text=myFont.render("    Pirate loot successful    ",True,RED)
            # Change the background 
            changeBackground("winscreen.jpg")
        else:
            text=myFont.render("Better luck next time",True,WHITE)
            # Change the background 
            changeBackground("losescreen.jpg")
        screen.blit(text,(250,40))        
    else:
               
        # Change the background 
        changeBackground("b1.jpg")
        countDown=timingFont.render(str(60-int(timeElapsed)),True,RED)
        screen.blit(countDown,(800,10))
        
        
        #move the glove as per key pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]: # UP
            if pirate.rect.y> 0:     
                 pirate.rect.y -= 5
        if keys[pygame.K_DOWN] : # DOWN
            if pirate.rect.y <630:
                pirate.rect.y += 5 
        
        if keys[pygame.K_LEFT] : # LEFT
            if pirate.rect.x> 0:    
                 pirate.rect.x -= 5 
        
        if keys[pygame.K_RIGHT] : # RIGHT
             if pirate.rect.x <850:
                 pirate.rect.x += 5  
         
        
     
        # See if stone and pirate has collided
        stone_hit_list = pygame.sprite.spritecollide(pirate, stone_list, True)
        soldier_hit_list=pygame.sprite.spritecollide(pirate, soldier_list, True)
     
        # Check the list of collisions.
        for stone in stone_hit_list:
            score += 1
            #print(score)
            text=myFont.render("Score ="+str(score),True,WHITE)
        for soldier in soldier_hit_list:
            score -= 5
            #print(score)
            text=myFont.render("Score ="+str(score),True,WHITE)

        # print the score on screen
        screen.blit(text,(730,80))

             
        # Draw all the spites
        allsprites.draw(screen)
     
        
    pygame.display.update()
     
        
pygame.quit()
