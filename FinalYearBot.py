import RPi.GPIO as IO
import time
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os
import numpy as np
import picamera

IO.setwarnings(False)
IO.setmode(IO.BCM)
IO.setup(21,IO.IN)#GPIO 21 Middle IR
IO.setup(2,IO.IN) #GPIO 2 -> Left IR out
IO.setup(3,IO.IN) #GPIO 3 -> Right IR out
IO.setup(26,IO.OUT) #GPIO 4 -> Motor Left terminal A
IO.setup(20,IO.OUT) #GPIO 14 -> Motor Left terminal B
IO.setup(17,IO.OUT) #GPIO 17 -> Motor Right terminal A
IO.setup(18,IO.OUT) #GPIO 18 -> Motor Right terminal B
IO.setup(11, GPIO.OUT)#claw
claw= IO.PWM(11, 50)
claw.start(7.5)

camera=picamera.PiCamera()
PATH = os.path.join("/home/pi/Desktop/dataset", 'Products')
test_dir=os.path.join(PATH,'Tester')
new_model = tf.keras.models.load_model('Product.h5')
batch_size = 32
IMG_HEIGHT = 64
IMG_WIDTH = 64
Products=["Product1","Product2","Product3","Product4"]
test_image_generator = ImageDataGenerator(rescale=1./255)

while True:

    if(IO.input(2)==False and IO.input(3)==False): #both white move forward
        
        IO.output(26,True) #1A+
        IO.output(20,False) #1B-
        IO.output(17,True) #2A+
        IO.output(18,False) #2B-

    elif(IO.input(2)==True and IO.input(3)==False): #turn right  
        IO.output(26,True)
        IO.output(20,False)
        IO.output(17,False)
        IO.output(18,False)

    elif(IO.input(2)==False and IO.input(3)==True): #turn left
        IO.output(26,False)
        IO.output(20,False)
        IO.output(17,True)
        IO.output(18,False)

        
    elif(IO.input(2)==True and IO.input(3)==True):
        IO.output(26,False) #1A+
        IO.output(20,False) #1B-
        IO.output(17,False) #2A+
        IO.output(18,False) #2B-
        time.sleep(2)
        camera.capture('/home/pi/Desktop/dataset/Products/Tester/test/testing.jpg')
        test_data_gen=test_image_generator.flow_from_directory(batch_size=batch_size,
                                                              directory=test_dir,
                                                              target_size=(IMG_HEIGHT,IMG_WIDTH),
                                                              class_mode="categorical")
        designatedProduct=np.argmax(new_model.predict(test_data_gen))
        prediction=Products[designatedProduct]     
        print(prediction)
        time.sleep(2)
        if(prediction!='No Product'):
            IO.output(26,True) #1A+
            IO.output(20,False) #1B-
            IO.output(17,True) #2A+
            IO.output(18,False) #2B-
        else:
            claw.changeDutyCycle(7.5)
            time.sleep(3)
            IO.output(26,True) #1A+
            IO.output(20,False) #1B-
            IO.output(17,True) #2A+
            IO.output(18,False) #2B-
            exit
while !(IO.input(2)==False and IO.input(3)==True): #Until a left turn keep moving forward
    IO.output(26,True) #1A+
    IO.output(20,False) #1B-
    IO.output(17,True) #2A+
    IO.output(18,False) #2B-
while !(IO.input(2)==False and Io.input(3)==False):#Keep turning left until path is straight
    IO.output(26,False)
    IO.output(20,False)
    IO.output(17,True)
    IO.output(18,False)
while IO.input(2)==False and IO.input(3)==False and IO.input(21)==True:
    IO.output(26,True) #1A+
    IO.output(20,False) #1B-
    IO.output(17,True) #2A+
    IO.output(18,False) #2B-
claw.changeDutyCycle(2.5)
    
    
    
