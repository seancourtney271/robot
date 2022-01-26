import RPi.GPIO as GPIO          
from time import sleep

class motor:
    def __init__(self) -> None:
        self.ena = 14
        self.in1 = 15
        self.in2 = 18

        self.enb = 22
        self.in3 = 27
        self.in4 = 17

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.in1,GPIO.OUT)
        GPIO.setup(self.in2,GPIO.OUT)
        GPIO.setup(self.ena,GPIO.OUT)

        GPIO.setup(self.in3,GPIO.OUT)
        GPIO.setup(self.in4,GPIO.OUT)
        GPIO.setup(self.enb,GPIO.OUT)

        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.LOW)

        GPIO.output(self.in3,GPIO.LOW)
        GPIO.output(self.in4,GPIO.LOW)

        self.p=GPIO.PWM(self.ena,1000)
        self.b=GPIO.PWM(self.enb,1000)

        self.p.start(25)
        self.b.start(25)
        pass
    
    def forward(self, speed):
        GPIO.output(self.ena,GPIO.HIGH)
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.HIGH)

        GPIO.output(self.enb,GPIO.HIGH)
        GPIO.output(self.in3,GPIO.LOW)
        GPIO.output(self.in4,GPIO.HIGH)

        self.p.ChangeDutyCycle(speed)
        self.b.ChangeDutyCycle(speed)
        pass

    def backward(self, speed):
        GPIO.output(self.ena,GPIO.HIGH)
        GPIO.output(self.in1,GPIO.HIGH)
        GPIO.output(self.in2,GPIO.LOW)

        GPIO.output(self.enb,GPIO.HIGH)
        GPIO.output(self.in3,GPIO.HIGH)
        GPIO.output(self.in4,GPIO.LOW)

        self.p.ChangeDutyCycle(speed)
        self.b.ChangeDutyCycle(speed)
        pass

    def turn_left(self, speed):
        GPIO.output(self.ena,GPIO.HIGH)
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.HIGH)

        GPIO.output(self.enb,GPIO.HIGH)
        GPIO.output(self.in3,GPIO.LOW)
        GPIO.output(self.in4,GPIO.HIGH)

        self.p.ChangeDutyCycle(speed / 3)
        self.b.ChangeDutyCycle(speed)
        pass
    
    def turn_right(self, speed):
        GPIO.output(self.ena,GPIO.HIGH)
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.HIGH)

        GPIO.output(self.enb,GPIO.HIGH)
        GPIO.output(self.in3,GPIO.LOW)
        GPIO.output(self.in4,GPIO.HIGH)

        self.p.ChangeDutyCycle(speed)
        self.b.ChangeDutyCycle(speed / 3)
        pass

    def tear_down(self):
        GPIO.cleanup()

if __name__ == '__main__':
    drive_train = motor()
    # All functions have been verified
    # drive_train.forward(75)
    # drive_train.backward(75)
    # drive_train.turn_left(75)
    # drive_train.turn_right(75)
    sleep(1)
    drive_train.tear_down()
