from Adafruit_PWM_Servo_Driver import PWM
import time 


pwm = PWM(0x40)

servoMin  = 150
servomax = 600

def setServoPulse(channel, pulse):
    pulseLength = 1000000
    pulseLength /= 60
    print "%d us per period" % pulseLength 
    pulseLength /= 4096
    print "%d us per bit" % pulseLength
    pulse *= 1000
    pulse /= pulseLength
    pwm.setPWM(channel, 0, pulse)


pwm.setPWMFreq(60)
while(True):
    pwm.setPWM(0,0,servoMin)
    time.sleep(1)
    pwm.setPWM(0,0, servoMax)
    time.sleep(1)