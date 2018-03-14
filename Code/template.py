from Adafruit_PWM_Servo_Driver import PWM
import time
from math import sqrt


"""
Initialize
"""
# Set Address
pwm = PWM(0x40)
pwm.setPWMFreq(60)
# ****** Setup IK variables ******
PI = 3.14159265

servoMin = 150
servomax = 600

"""
Define Lengths of Segments
"""
ShoulderLength = 9.5
ElbowLength = 9.0
WristLength = 9.0
FingerLength = 5.8

"""
Define Names
"""
Hypot = 0
Slope = 0
CirclePointX = 0
CirclePointY = 0
x1 = 28
y1 = 9.0
"""
Origin Point Start
"""

x2 = 0.0
y2 = 0.0
A, B, C = 0.0, 0.0, 0.0
PosXAnswer  # positive X portion of Quadratic Equation.
PosYAnswer  # positive Y portion of Qudratic Equation.
NegXAnswer  # negative X portion of Quadratic Equation.
NegYAnswer  # negative Y portion of Quadratic Equation.
Angle_A  # Angle located at origin (0,0).
# Second 1/2 of Angle located at origin (0,0).Shoulder servo setting.
Angle_A_Temp
Angle_B  # Elbow servo setting.
Angle_C



  
   """
   Pin Names 

   Pin 0  Finger
   Pin 2  Wrist
   Pin 4  Elbow
   Pin 6  Shoulder
   Pin 8  Base
   Pin 12 BaseRotator
   Pin 15 Gripper
   """

def setup():

    pinFinger = 0
    pinWrist = 2
    pinElbow = 4
    pinShoulder = 6
    pinBase = 8
    pinBaseRotate = 12
    pinGripper = 15

    """
    Object to Control the servo
    Servo BasePan, GripTilt, ShoulderTilt, ElbowTilt, WristTitle
    """"
loop():
    x1 =3 
    y1 = 1
    endX = 14
    endY = 15
    for x in range (x1, endX):
        for y in range(y1, endY):
            print ("********")
            print ("Point: (")
            print(x1, " , " , y1)
            print(")")

            if x1<ShoulderLength and y1< ShoulderLength:
                Special_Calc_Point()
            else:
                Calc_Point()

def Special_Calc_Point():
"""
  //******************************************************************
  //*********** Starting Special Circle Calcs ********************************
  //******************************************************************
"""


  Hypot = sqrt(sq(x1) + sq(y1)) + WristLength
  A = ElbowLength
  B = Hypot
  C = ShoulderLength


Angle_A = acos((sq(B) + sq(C) - sq(A)) / (2 * B * C)) * (180 / PI)

Angle_B =  acos((sq(C) + sq(A) - sq(B)) / (2 * A * C)) * (180 / PI)

Angle_C = acos((sq(A) + sq(B) - sq(C)) / (2 * A * B)) * (180 / PI)

Angle_A = Angle_A * (1 + (Angle_A / (Angle_B + Angle_C)))


if Angle_A < 35:
    Angle_A = 35

if not isnan(Angle_A)
    print(Angle_A)
    # ShoulderTilt.write(Angle_A)
    delay(1000)

if not isnan(Angle_B) 

    CurrentAngle = ElbowTilt.read();

    if (Angle_B > CurrentAngle):
      
        print(CurrentAngle);
        print("< \n", Angle_B)
        Serial.print(" < ");
        Serial.println(Angle_B);
        for i in range( CurrentAngle, Angle_B)
        for (i = CurrentAngle; i < Angle_B; i = i + 1): //if Angle_B > CurrentAngle.
        {

    ElbowTilt.write(i);
    delay(5);
    }//end for CurrentAngle.

}//end if Angle_B > CurrentAngle.

def reset_servos():
    # ShoulderTilt.write(65);//was 50.60.35.55
    delay(2000);


    # ElbowTilt.write(90 );//was 60.70.50.90.40.90
    delay(500);


    # WristTilt.write(90);//was 60.50.40
    delay(500);


    # GripTilt.write(90); //was 40,35,90,20,60.10.45
    delay(500);
# pwm.setPWMFreq(60)
# while(True):
#     pwm.setPWM(0,0,servoMin)
#     time.sleep(1)
#     pwm.setPWM(0,0, servoMax)
#     time.sleep(1)


def setServoPulse(channel, pulse):
    pulseLength = 1000000
    pulseLength /= 60
    print "%d us per period" % pulseLength 
    pulseLength /= 4096
    print "%d us per bit" % pulseLength
    pulse *= 1000
    pulse /= pulseLength
    pwm.setPWM(channel, 0, pulse)



