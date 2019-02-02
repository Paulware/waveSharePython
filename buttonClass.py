import RPi.GPIO as GPIO
import time

class ButtonsClass: 
   def __init__(self):
      GPIO.setmode(GPIO.BCM)
      self.pinList = {"TL":23, "TR":18, "Left":13, "Up":5, "Right":19, "Down":6, 
                      "Press":3, "Start":21, "Select":4, "Y":20, "B":12, "A":26, 
                      "X":16 }
      # Sets the pin as input and sets Pull-up mode for the pin.
      for pin,number in self.pinList.items():
         GPIO.setup (number,GPIO.IN, GPIO.PUD_UP)

   def checkKey (self,pin):
      pressed = False
      pinNumber = self.pinList [pin]
      if GPIO.input(pinNumber) == 0:
         pressed = True
      return pressed 
      
   def checkAll(self):         
      for pin,number in self.pinList.items():
         if self.checkKey (pin):
            print pin + " pressed"
            time.sleep (0.01) # avoid lockup   
            
if __name__ == "__main__":
   buttons = ButtonsClass()
   while True:
       time.sleep(0.05)
       buttons.checkAll()
       if buttons.checkKey  ("TL"): 
          print ("TL was pressed yo" )

