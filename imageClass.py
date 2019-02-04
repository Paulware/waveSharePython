import pygame
import time

class ImageClass: 
   def __init__(self):
      self.display = pygame.display.set_mode((800,600)) 
      # self.RED = (255, 0, 0)
      
   def clear (self):
      self.display.fill((0,0,0)) #Black
      
   def show (self):
      self.display.blit (self.image, (self.x,self.y))      
      
   def draw (self,filename,x,y):
      self.image= pygame.image.load(filename).convert()
      self.x = x
      self.y = y
      self.show()
      
   def moveX (self,offset):
      self.x = self.x + offset
      self.show()
      
   def moveY (self,offset):
      self.y = self.y + offset
      self.show()   
            
if __name__ == "__main__":
   pygame.init()
   image = ImageClass()
   image.draw ('/home/tryImage/townscape.jpg',200,100)
   time.sleep (5)
   pygame.quit()
