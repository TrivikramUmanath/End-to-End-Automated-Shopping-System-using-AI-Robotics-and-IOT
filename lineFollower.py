import RPi.GPIO as IO
import time
IO.setwarnings(False)
IO.setmode(IO.BCM)

IO.setup(21,IO.IN) #GPIO 2 -> Left IR out
IO.setup(16,IO.IN) #GPIO 3 -> Right IR out

IO.setup(26,IO.OUT) #GPIO 4 -> Motor Left terminal A
IO.setup(20,IO.OUT) #GPIO 14 -> Motor Left terminal B

IO.setup(17,IO.OUT) #GPIO 17 -> Motor Right terminal A
IO.setup(18,IO.OUT) #GPIO 18 -> Motor Right terminal B

while 1:
    if(IO.input(16)==True and IO.input(21)==False):#turn right

        print('Right')
        IO.output(26,True)
        IO.output(20,False)
        IO.output(17,False)
        IO.output(18,False)

    elif(IO.input(16)==False and IO.input(21)==False): #both white move forward     
        print('Forward')
        IO.output(26,True) #1A+
        IO.output(20,False) #1B-
        IO.output(17,True) #2A+
        IO.output(18,False) #2B-

    elif(IO.input(16)==False and IO.input(21)==True):#turn left
        print('Left')
        IO.output(26,False)
        IO.output(20,False)
        IO.output(17,True)
        IO.output(18,False)

    else:
        print('Still')
        IO.output(26,False)
        IO.output(20,False)
        IO.output(17,False)
        IO.output(18,False)        
        

   


    
