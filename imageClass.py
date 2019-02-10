import pygame
import time

class ImageClass: 
   def __init__(self):
      self.display = pygame.display.set_mode((800,600)) 
      self.angle = 0
      # self.RED = (255, 0, 0)
      
   def clear (self):
      self.display.fill((0,0,0)) #Black
      
   def show (self):
      self.display.blit (self.image, (self.x,self.y))      
      
   def rotate (self,newAngle):
      angleDiff = self.angle - newAngle
      self.angle = newAngle  
      if angleDiff != 0.0:       
         try: 
            #orig_rect = self.originalImage.get_rect()
            
            rot_image = pygame.transform.rotate(self.originalImage, newAngle)
            rot_rect  = self.originalImage.get_rect()
            
            rot_rect.center = rot_image.get_rect().center 
            rot_image  = rot_image.subsurface(rot_rect).copy()
            self.image = rot_image
         except Exception as exception:
            try: 
               rot_image = pygame.transform.rotate(self.originalImage, newAngle) 
               self.image = rot_image
            except Exception as exception:
               print ("Image is probably not square, try squaring up the image")

         self.show()     
      
   def draw (self,filename,x,y):
      self.originalImage = pygame.image.load(filename).convert()
      self.image = pygame.image.load(filename).convert()
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
