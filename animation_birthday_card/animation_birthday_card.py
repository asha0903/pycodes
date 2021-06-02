4import pygame
import time

pygame.init()
display_surface=pygame.display.set_mode((600,600))
done=False
image=pygame.image.load("backgroundone.jpg")

font=pygame.font.SysFont("Times New Roman",72)
text=font.render("Happy",True,(0,0,0))
text2=font.render("Birthday",True,(0,0,0))
display_surface.fill((255,255,255))
display_surface.blit(image,(0,0))
display_surface.blit(text,(210,180))
display_surface.blit(text2,(180,264))
pygame.display.update()
time.sleep(2)

image2=pygame.image.load("backgroundtwo.jpg")
font2=pygame.font.SysFont("Arial",36)
text3=font2.render("Wish you a bright future ahead",True,(0,0,0))
display_surface.fill((255,255,255))
display_surface.blit(image2,(0,0))
display_surface.blit(text3,(30,30))
pygame.display.update()
time.sleep(2)

image3=pygame.image.load("backgroundthree.jpg")
display_surface.fill((255,255,255))
display_surface.blit(image3,(0,0))
pygame.display.update()
time.sleep(4)
