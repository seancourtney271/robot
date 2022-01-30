from picamera import PiCamera
from time import sleep
import os
from datetime import datetime


class camera:
    def __init__(self):
        self.camera = PiCamera()
        self.dir_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '/images/'

        self.camera.start_preview()
        pass

    def take_picture(self):
        time = datetime.now()
        file_name = (str(time.day) + "-" + str(time.month) + "-" + str(time.year) + "-" + str(time.hour) + "-" + str(time.minute) + "-" + str(time.second))
        image_name = file_name + ".jpg"
        image_file = self.dir_path + image_name

        self.camera.capture(image_file)
        pass
    
    def tear_down(self):
        self.camera.stop_preview()
        pass

if __name__ == '__main__':
    robot_camera = camera()
    robot_camera.take_picture()
    robot_camera.tear_down()
    pass