import time
start=time.time()
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os
import numpy as np
import picamera
camera=picamera.PiCamera()
camera.capture('/home/pi/Desktop/dataset/Product/Tester/test/testing.jpg')
print("Captured the Image")
PATH = os.path.join("/home/pi/Desktop/dataset", 'Product')
batch_size = 32
IMG_HEIGHT = 64
IMG_WIDTH = 64

test_dir=os.path.join(PATH,'Tester')

test_image_generator = ImageDataGenerator(rescale=1./255)

test_data_gen=test_image_generator.flow_from_directory(batch_size=batch_size,
                                                              directory=test_dir,
                                                              target_size=(IMG_HEIGHT,IMG_WIDTH),
                                                              class_mode="categorical")
new_model = tf.keras.models.load_model('Product.h5')
Products={0:"Product1",1:"Product2",2:"Product3",3:"Product4"}
                
highestConfidence=max(new_model.predict(test_data_gen)[0])
print("The confidence is "+str(highestConfidence))
if highestConfidence>=0.9:
    print(Products[np.argmax(new_model.predict(test_data_gen))])
else:
    print("No Product")
print(new_model.predict(test_data_gen))
print(str(time.time()-start)+"seconds are taken to execute the above code")


