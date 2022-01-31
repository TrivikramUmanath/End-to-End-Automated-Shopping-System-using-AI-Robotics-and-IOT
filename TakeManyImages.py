import io
import time
import picamera
#from PIL import Image



with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.framerate = 80
    time.sleep(2)
    start = time.time()
    #camera.capture_sequence(outputs(), 'jpeg', use_video_port=True)
    for i in range(250):
        camera.capture('/home/pi/Desktop/dataset/Products/Product2/image'+str(i)+'.jpg')
    print('Captured 250 images of front side')
    while input()!='1':
        pass
    for i in range(250,500):
        camera.capture('/home/pi/Desktop/dataset/Products/Product2/image'+str(i)+'.jpg')
    print('Captured 250 images of side left')
    while input()!='1':
        pass
    for i in range(500,750):
         camera.capture('/home/pi/Desktop/dataset/Products/Product2/image'+str(i)+'.jpg')
    print('Captured 250 images of side right')
    while input()!='1':
        pass
    for i in range(750,1000):
           camera.capture('/home/pi/Desktop/dataset/Products/Product2/image'+str(i)+'.jpg')
    print('Captured 250 images of backside')
        
