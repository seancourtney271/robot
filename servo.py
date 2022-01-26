from adafruit_servokit import ServoKit    #https://circuitpython.readthedocs.io/projects/servokit/en/latest/

class servo:
    def __init__(self) -> None:
        #Constants
        nbPCAServo = 15

        # Initialize servos
        self.pca = ServoKit(channels = 16)

        # Servo Parameters
        min_imp = 500
        max_imp = 2500

        for i in range(nbPCAServo):
            self.pca.servo[i].set_pulse_width_range(min_imp , max_imp)

        # Servo Angles
        self.min_angle = 0
        self.max_angle = 180

        # Servo List
        self.servo_number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        pass

    def set_servo_angle(self, servo_id_number, angle):
        if not(type(angle) == int and servo_id_number in self.servo_number_list):
            if(angle > self.max_angle and angle < self.min_angle):
                print('Angle out of range (0 - 180')
                return 'Fail'
            print('Angle not of type int or servo_id not in range (0 - 15)')
            return 'Fail'
        self.pca.servo[servo_id_number].angle = angle
        return 'Success'

if __name__ == '__main__':
    servo_device = servo()

    try:
        servo_number = int(input("Input servo number: "))
        run = True
    except:
        print('Input bad servo number')
        run = False

    while(run):
        angle = input("Input the servo angle: ")
        if(angle == 'q'):
            run = False
            break
        try:
            angle = int(angle)
            servo_device.set_servo_angle(servo_number, angle)
        except:
            print('Bad angle input')