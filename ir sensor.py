import RPi.GPIO as IO
import time
IO.setwarnings(False)
IO.setmode(IO.BCM)

IO.setup(16,IO.IN) #GPIO 2 -> Left IR out
IO.setup(4,IO.OUT) #GPIO 2 -> Left IR out
IO.setup(14,IO.OUT) #GPIO 2 -> Left IR out


while True:
    print(IO.input(16))
