import RPi.GPIO as gpio 
import time
gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
gpio.setup(3,gpio.OUT)
pwm_obj=gpio.PWM(3,100)
pwm_obj.start()
a=0
while True:
    time.sleep(0.1)
    pwm_obj.start(a)
    time.sleep(0.1)
    a=a+1
    print("This is a ", a)

    if a==100:
        for x in range(99):
            time.sleep(0.1)
            b=a-x
            pwm_obj.start(b)
            time.sleep(0.1)
            print("This is b ",b)
            if b==2:
                a=0