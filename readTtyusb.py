import glob
from threading import Thread
import select
import time
import sys
import serial

quit = False
cp2102Port = None

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
   global cp2102Port   
   numDevices = 0
   while not quit:
      time.sleep (1.0)
      ports = findConnectedDevices("ttyUSB") 
      if (len(ports) != numDevices): 
         if (len(ports) == 1):
            cp2102Port = serial.Serial(port =ports[0], baudrate = 9600, timeout = 0.01)            
            print ("CP2102 Connected " + str(len(ports)) );
            cp2102Port.write ( 'Connected yo\n' );
         else:
            print ("CP2102 Disconnected " + str(len(ports)));
            cp2102Port = None
         numDevices = len(ports)
   
def readCp2102():
   global cp2102Port
   while not quit:
      if cp2102Port == None: 
         time.sleep (0.1)
      else: 
         line = cp2102Port.read()
         if line != "": 
            print (line )                  
            
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

t1 = Thread(target=checkTTYUSB)
t1.start()
t2 = Thread(target=readCp2102)
t2.start()

runUntilEnter()
cp2102Port.close()