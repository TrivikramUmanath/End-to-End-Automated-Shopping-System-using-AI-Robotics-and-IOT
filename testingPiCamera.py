import picamera

camera=picamera.PiCamera()
camera.resolution = (640, 480)
camera.framerate = 80
camera.capture('/home/pi/Desktop/test.jpg')

