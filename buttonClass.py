import RPi.GPIO as GPIO
import time
import pygame
from pygame.locals import * # For Key codes 

class ButtonsClass: 
   def __init__(self, timeout = 0.1):
      self.timeout = timeout
      GPIO.setmode(GPIO.BCM)
      self.pinList = {"TL":23, "TR":18, "Left":13, "Up":5, "Right":19, "Down":6, 
                      "Press":3, "Start":21, "Select":4, "Y":20, "B":12, "A":26, 
                      "X":16 }
      # Sets the pin as input and sets Pull-up mode for the pin.
      for pin,number in self.pinList.items():
         try:
            GPIO.setup (number,GPIO.IN, GPIO.PUD_UP)
         except:
            pass             
      self.lastPress = time.time()
   
   def checkKey (self,pin):
      pressed = False
      if (time.time() - self.lastPress) > self.timeout: 
         pinNumber = self.pinList [pin]
         if GPIO.input(pinNumber) == 0:
            pressed = True
            self.lastPress = time.time()
         
      return pressed 
   
   def eventGet (self):
      events = pygame.event.get()
      if events == []:      
         event = self.addButtons()
         if event != None:
            time.sleep (.01)
            events = [event]         
      else: 
         print ("Got an event from pygame" )
      return events 
  
   '''
   def keyGet_Pressed(self):
      keystate = pygame.key.get_pressed()
      events = self.eventGet()
      for event in events:
         list = []
         #for key in keystate:
         #  list.append(keystate[key])  
         list[event.key] = 1
         keys = tuple(list)
         # print ("keys: " + str (keys)) 
         return keys
         #keystate[pygame.K_h] = 1
         #print ("event: " + str(event)) 
         #keystate[event.key] = event.value
      return keystate
   '''  
   def addButtons (self):
      # "TL":23, "TR":18, "Left":13, "Up":5, "Right":19, "Down":6, 
      # "Press":3, "Start":21, "Select":4, "Y":20, "B":12, "A":26, 
      # "X":16
      if self.checkKey ("A"):
         event = pygame.event.Event (pygame.KEYDOWN)    
         event.key = K_a       
      elif self.checkKey ("Start"):
         event = pygame.event.Event (pygame.KEYDOWN)     
         event.key = K_ESCAPE
      elif self.checkKey ("Select"):
         event = pygame.event.Event (pygame.KEYDOWN)     
         event.key = K_BACKSPACE
      elif self.checkKey ("Left"):
         event = pygame.event.Event (pygame.KEYDOWN)      
         event.key = K_LEFT         
      elif self.checkKey ("Right"):
         event = pygame.event.Event (pygame.KEYDOWN)     
         event.key = K_RIGHT         
      elif self.checkKey ("Up"):
         event = pygame.event.Event (pygame.KEYDOWN)     
         event.key = K_UP                
      elif self.checkKey ("Down"):
         event = pygame.event.Event (pygame.KEYDOWN)    
         event.key = K_DOWN        
      elif self.checkKey ("B"):
         event = pygame.event.Event (pygame.KEYDOWN)    
         event.key = K_b         
      elif self.checkKey ("X"):
         event = pygame.event.Event (pygame.KEYDOWN)    
         event.key = K_x         
      elif self.checkKey ("Y"):
         event = pygame.event.Event (pygame.KEYDOWN)    
         event.key = K_y 
      elif self.checkKey ("TR"): # next
         event = pygame.event.Event (pygame.KEYDOWN)    
         event.key = K_n 
      elif self.checkKey ("TL"): # back
         event = pygame.event.Event (pygame.KEYDOWN)    
         event.key = K_b         
      elif self.checkKey ("Press"): # back
         event = pygame.event.Event (pygame.KEYDOWN)    
         event.key = K_p         
      else:
         event = None
      if event != None:
         print ("Got event: " + str(event)) 
      return event      
      
   def checkAll(self):         
      for pin,number in self.pinList.items():
         if self.checkKey (pin):
            print pin + " pressed"
            time.sleep (0.01) # avoid lockup   
            
if __name__ == "__main__":
   buttons = ButtonsClass()
   pygame.init()
   quit = False
   while not quit: # Main loop for the start screen.
       for event in buttons.eventGet(): # pygame.event.get():
           if event.type == QUIT:
               print ("Got a quit") 
           elif event.type == KEYDOWN:
               print ("Got a keydown")
               if event.key == K_ESCAPE:
                   print ("Got an escape")
                   quit = True
   '''             
   while True:
       buttons.checkAll()
       if buttons.checkKey  ("TL"): 
          print ("TL was pressed yo" )
   '''
