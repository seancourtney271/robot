import RPi.GPIO as GPIO          
from time import sleep

class motor:

    def __init__(self):
        ena = 14
        in1 = 15
        in2 = 18

        enb = 22
        in3 = 27
        in4 = 17

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(in1,GPIO.OUT)
        GPIO.setup(in2,GPIO.OUT)
        GPIO.setup(ena,GPIO.OUT)

        GPIO.setup(in3,GPIO.OUT)
        GPIO.setup(in4,GPIO.OUT)
        GPIO.setup(enb,GPIO.OUT)

        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)

        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)

        p=GPIO.PWM(ena,1000)
        b=GPIO.PWM(enb,1000)

        p.start(25)
        b.start(25)
        pass
    
    def forward(self, speed):
        GPIO.output(ena,GPIO.HIGH)
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)

        GPIO.output(enb,GPIO.HIGH)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)

        p.ChangeDutyCycle(speed)
        b.ChangeDutyCycle(speed)
        pass

    def backward(self, speed):
        GPIO.output(ena,GPIO.HIGH)
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)

        GPIO.output(enb,GPIO.HIGH)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)

        p.ChangeDutyCycle(speed)
        b.ChangeDutyCycle(speed)
        pass

    def turn_left(self, speed):
        GPIO.output(ena,GPIO.HIGH)
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)

        GPIO.output(enb,GPIO.HIGH)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)

        p.ChangeDutyCycle(speed / 2)
        b.ChangeDutyCycle(speed)
        pass
    
    def turn_right(self, speed):
        GPIO.output(ena,GPIO.HIGH)
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)

        GPIO.output(enb,GPIO.HIGH)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)

        p.ChangeDutyCycle(speed)
        b.ChangeDutyCycle(speed / 2)
        pass