import time
import picamera

WAIT_TIME = 30

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    for filename in camera.capture_continuous('/home/pi/timelapse/img{timestamp:%H-%M-%S-%f}.jpg'):
        time.sleep(WAIT_TIME)
