import glob
from threading import Thread
import select
import time
import sys

quit = False
cp2102Connected = False

# ttyUSB is used by the cp2102
# ttyACM is used by the other devices
def findConnectedDevices(port):
   ports = []
   globs = glob.glob ( '/dev/' + port + '[0-9]')       
   if len(globs) > 0:         
      for g in globs: 
         ports.append (g);    
   return ports   
   
def checkTTYUSB (): 
   global quit
   numDevices = 0
   while not quit:
      time.sleep (0.5)
      ports = findConnectedDevices("ttyUSB") 
      if (len(ports) != numDevices): 
         if (len(ports) == 1):
            cp2102Connected = True
            print ("CP2102 Connected " + str(len(ports)) );
         else:
            cp2102Connected = False
            print ("CP2102 Disconnected " + str(len(ports)));
         numDevices = len(ports)
                     
def runUntilEnter():
   global quit
   # Run until Enter is pressed
   while not quit:
      i,o,e = select.select ([sys.stdin],[],[],0.0001)
      for s in i:
         if s == sys.stdin:
            input = sys.stdin.readline()
            if input != "":
               print ( "Got input: [" + input + "]" )
               quit = True

t = Thread(target=checkTTYUSB)
t.start()

runUntilEnter()