from pygame.locals import *
import math
class EventClass: 
   def __init__ (self): 
      self.mouseX = 0
      self.mouseY = 0
      self.mouseClicked = False
      self.mouseReleased = False
      self.mousePressed = False
      self.angle = 0.0

   def spriteMouseCollision (self, pygame): 
      # self.rect.collidepoint(pygame.mouse.get_pos()
      return False

   def update (self,  pygame):
      self.mouseClicked = False
      for event in pygame.event.get(): # event handling loop
         if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
         elif event.type == MOUSEMOTION:
            self.mouseX, self.mouseY = event.pos
            yDiff = self.mouseY - 300 # Y positive going down
            xDiff = 400.0 - self.mouseX
            if xDiff != 0.0: 
               self.angle = math.degrees(math.atan2(yDiff,xDiff))
               print ("[" + str(self.mouseX) + "," + str(self.mouseY) + "]" )
               print ("Angle: [rise,run,tan1,angle] : [" + str(yDiff) + "," + 
                      str(xDiff) + "," + str (self.angle) + "]" )           
          
            
         elif event.type == MOUSEBUTTONDOWN:
            self.mousePressed = True
            leftButton, pressed2, pressed3 = pygame.mouse.get_pressed() 
            self.mouseClicked = False            
            if leftButton and self.mouseReleased : 
               self.mouseClicked = True
            self.mouseReleased = False
            if self.mouseClicked:
               print ("Left Mouse Clicked" )
               
         elif event.type == MOUSEBUTTONUP:
            self.mouseReleased = True
            self.mousePressed = False
            leftButton, pressed2, pressed3 = pygame.mouse.get_pressed()            
            if not leftButton: 
               self.mouseClicked = False
               print ("Left Mouse Released")
   