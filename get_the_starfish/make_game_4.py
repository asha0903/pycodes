# Import the pygame module
import pygame,sys
import time
# Import random for random numbers
import random
# Import pygame.locals for easier access to key coordinates
from pygame.locals import *


# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# Initialize pygame
pygame.init()
# Create the screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


#initialize
#colours
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
#initialize sound
pygame.mixer.init()
# Setup the clock for a decent framerate
clock = pygame.time.Clock()
#initilize font
myFont=pygame.font.SysFont("Times New Roman",50)
smallFont=pygame.font.SysFont("Times New Roman",20)
#----------------------------------------------------------------------------

# Change the background 
def changeBackground(img):
    # Add background image    
    background = pygame.image.load(img)
    #set its size
    bg = pygame.transform.scale(background, (SCREEN_WIDTH,SCREEN_HEIGHT))
    screen.blit(bg,(0,0))
    pygame.display.set_caption("Make your own game")
    pygame.display.update()


#-----------------------------------------------------------------------------


#first screen
def welcomeScreen():
    #sound
    pygame.mixer.music.load("startsound.mp3")
    pygame.mixer.music.play(-1)
    #background
    changeBackground("startscreen.jpg")
    #Aim
    text=myFont.render("   Help Turtle find Starfish    ",True,RED)         
    screen.blit(text,(100,70))
    #rules
    text=smallFont.render("   Press space to start.    ",True,WHITE)         
    screen.blit(text,(20,300))
    text=smallFont.render("   Use arrow keys to navigate.    ",True,WHITE)         
    screen.blit(text,(20,325))
    text=smallFont.render("   Touching enemies will reduce your life.    ",True,WHITE)         
    screen.blit(text,(20,350))
    text=smallFont.render("   Touching obstacles will relocate you .    ",True,WHITE)         
    screen.blit(text,(20,375))
    text=smallFont.render("   Click on Cross(X) to quit    ",True,RED)
    screen.blit(text,(20,400))
    pygame.display.update()
    #capture events
    while True:
        for event in pygame.event.get():
            # if user clicks on cross button, close the game
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # If the user presses space, start the game for them
            elif event.type==KEYDOWN and (event.key==K_SPACE):                
                startgame()
                return


#---------------------------------------------------------------------------

# Define the Player sprite
#Player starts at (0,0) by deafult
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (70,70))
        self.rect = self.image.get_rect()
    # Move the sprite based on keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

#-----------------------------------------------------------------------------

#Target sprite of player 
class Target(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('target.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (70,70))
        self.rect = self.image.get_rect()
        self.rect.x = 1
        self.rect.y = 500
        #this determines target has to moveLeft or right
        self.moveLeft=False
    def update(self):
        #make target move left and right
        if self.moveLeft:
            self.rect.move_ip(-2, 0)
            if self.rect.x<=5:
                self.moveLeft=False
        else:
            self.rect.move_ip(2, 0)
            if self.rect.x>=SCREEN_WIDTH-50:
                self.moveLeft=True

#----------------------------------------------------------------------------

#Enemy sprites
class Enemy(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()        
        self.image = pygame.transform.scale(self.image, (60,60))
        # The starting position is randomly generated
        self.rect=self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH)
        self.rect.y = random.randrange(SCREEN_HEIGHT)
        #speed is randomly generated
        self.speed = random.randint(1,7)
    # Move the enemy based on speed
    # Remove it when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
#-----------------------------------------------------------------------------
   
#obstacle sprites
class Obstacle(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()                
        self.image = pygame.transform.scale(self.image, (70,70))
        self.rect=self.image.get_rect()
        # The starting position is randomly generated
        self.rect.x = random.randrange(SCREEN_WIDTH)
        self.rect.y = random.randrange(SCREEN_HEIGHT)
    # make the obstacles float by moving it randomly
    # Remove it when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(random.randint(-3,3),random.randint(-1,1))
        if self.rect.right < 0:
            self.kill()

#-----------------------------------------------------------------------------

enemies=["enemy1.png","enemy2.png","enemy3.png","enemy4.png"]
obstacles=["obstacle1.png","obstacle2.png","obstacle3.png","obstacle4.png"]

# Create groups to hold sprites
enemy_group = pygame.sprite.Group()
obstacle_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()


def createEnemy():
    # Create enemy, and add to groups
    new_enemy = Enemy(random.choice(enemies))
    enemy_group.add(new_enemy)
    all_sprites.add(new_enemy)
    return new_enemy

def createObstacle():
    # Create obstacle, and add to groups
    new_obstacle = Obstacle(random.choice(obstacles))
    obstacle_group.add(new_obstacle)
    all_sprites.add(new_obstacle)
    return new_obstacle


def createPlayerTarget():
    # Create player ,add to group
    player = Player()
    all_sprites.add(player)
    #create target,add to group
    target=Target()
    all_sprites.add(target)
    return player,target
    
#-----------------------------------------------------------------------------
#bounce 
def bounce(obj):
    pygame.mixer.music.load("bounce.mp3")
    pygame.mixer.music.play()
    obj.rect.move_ip(random.randint(-30,30),random.randint(-30,30))

#-----------------------------------------------------------------------------
#last screen
def endScreen(sound,img,text):
    #sound
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play()
    #background
    changeBackground(img)
    #output message
    screen.blit(text,(150,50))  
    #what next
    text=smallFont.render("   Press space to restart    ",True,WHITE)         
    screen.blit(text,(20,200))
    text=smallFont.render("   Click on Close(X) to quit    ",True,RED)
    screen.blit(text,(20,240))
    pygame.display.update()
    #capture events
    while True:
        for event in pygame.event.get():
            # if user clicks on cross button, close the game
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # If the user presses space, start the game for them
            elif event.type==KEYDOWN and (event.key==K_SPACE):
                welcomeScreen()
                return


#-----------------------------------------------------------------------------
def startgame():

    # empty the groups(for restart)
    enemy_group.empty()
    obstacle_group.empty()
    all_sprites.empty()
    
    #Create custom events for adding a new enemy and obstacle
    #raise event for ADD_ENEMY after 600ms
    ADD_ENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADD_ENEMY, 600)
    #raise event for ADD_OBSTACLE after 1000ms
    ADD_OBSTACLE = pygame.USEREVENT + 2
    pygame.time.set_timer(ADD_OBSTACLE, 1000)

    
    player,target=createPlayerTarget()    
    #need to be removed in next session
    #createEnemy()
    #createObstacle()

    #variable to maintain life
    life=20
    

    #game loop
    while True:
        # Look at every event in the queue
        for event in pygame.event.get():
            # Did the user click the window close button? If so, stop the loop
            if event.type == QUIT:
                return
            # Should we add a new enemy?
            elif event.type == ADD_ENEMY:
                # Create the new enemy, and add it to our sprite groups
                createEnemy()

            # Should we add a new obstacle?
            elif event.type == ADD_OBSTACLE:
                # Create the new obstacle, and add it to our sprite groups
                createObstacle()

        # Get the set of keys pressed and check for user input
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)

        
        # Check if any obstacle have collided with the player
        if pygame.sprite.spritecollideany(player, obstacle_group):
            bounce(player)

        # Check if any enemy has collided with the player
        if pygame.sprite.spritecollideany(player, enemy_group):
            # If so, bounce player and reduce life
            bounce(player) 
            life-=1                 
            if life==0:
                #sound
                sound="losesound.mp3" 
                #image
                image="endscreen.jpg"
                #text
                text=myFont.render("   You lose..try again next time    ",True,RED)
                #call endscreen
                endScreen(sound,image,text)
                return

        # Check if any target and player have collided 
        if pygame.sprite.collide_rect(player, target):
            #sound
            sound="winsound.mp3"
            #image
            image="endscreen.jpg"
            #text
            text=myFont.render("   You won..play and enjoy ",True,WHITE)
            #call end screen
            endScreen(sound,image,text)
            return

        # Update the position of our enemies,obstacles and target
        enemy_group.update()
        obstacle_group.update()
        target.update()

        # Add background image
        screen.blit(pygame.image.load("background.jpg"),(0,0))
        #draw the life strip on screen
        pygame.draw.rect(screen,RED,(500,10,life*10,10))

        #draw sprites
        all_sprites.draw(screen)


        # Ensure we maintain a 30 frames per second rate
        clock.tick(30)
        
        
        pygame.display.update()

#-----------------------------------------------------------------------------

#startgame()
welcomeScreen()
pygame.quit()


          
        
