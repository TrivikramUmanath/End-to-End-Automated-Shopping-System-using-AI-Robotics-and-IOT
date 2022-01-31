import RPi.GPIO as IO
import time

IO.setwarnings(False)
IO.setmode(IO.BCM)
IO.setup(21,IO.IN)#GPIO 21 For stopping and picking objects
IO.setup(2,IO.IN) #GPIO 2 -> Left IR out
IO.setup(3,IO.IN) #GPIO 3 -> Right IR out

IO.setup(4,IO.OUT) #GPIO 4 -> Motor Right terminal A
IO.setup(14,IO.OUT) #GPIO 14 -> Motor Right terminal B

IO.setup(17,IO.OUT) #GPIO 17 -> Motor Left terminal A
IO.setup(18,IO.OUT) #GPIO 18 -> Motor Left terminal B

IO.output(4,True) #1A+
IO.output(14,False) #1B-
IO.output(17,True) #2A+
IO.output(18,False) #2B-

time.sleep(5)

IO.output(4,False) #1A+
IO.output(14,True) #1B-
IO.output(17,False) #2A+
IO.output(18,True) #2B-

time.sleep(5)
