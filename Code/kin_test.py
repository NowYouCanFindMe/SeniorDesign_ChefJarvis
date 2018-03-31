from Adafruit_PWM_Servo_Driver import PWM

from math import sqrt
from math import pow
from math import acos
from math import isnan
import numpy as np
import time

import serial

"""
Pin Names 

Pin 0  Finger       Servo F
Pin 2  Wrist        Servo E 
Pin 4  Elbow        Servo Dpwm = PWM(0x40)
Pin 6  Shoulder     Servo C
Pin 8  Base         Servo A
Pin 12 BaseRotator  ServoB

"""
"""     
                  Servo(E) ------Servo(F)
                 /
              _-/
            Servo(D)         
           /
          /
         /
       Servo(C)
       /
      /
     /
Servo(A,B)
"""


pos = 0
CurrentAngle = 0.00
i = 0

dutycycle=0
"""
Initialize
"""
# Set Address
pwm = PWM(0x40)
pwm.setPWMFreq(60)
       

# ****** Setup IK variables ******
PI = 3.14159265


ShoulderLength = 9.0 #6.0
ElbowLength = 9.0 #4.0
WristLength = 5.8 #4.0

Hypot = 0
Slope = 0
CirclePointX = 0
CirclePointY = 0


"""
Target End point
"""
x1 = 23.8
y1 = 10.0
"""
Origin Point Start
"""

x2 = 0.0
y2 = 0.0

A, B, C = 0.0, 0.0, 0.0
PosXAnswer = 0  # positive X portion of Quadratic Equation.
PosYAnswer = 0  # positive Y portion of Qudratic Equation.
NegXAnswer = 0 # negative X portion of Quadratic Equation.
NegYAnswer = 0 # negative Y portion of Quadratic Equation.
Angle_A = 0  # Angle located at origin (0,0).
# Second 1/2 of Angle located at origin (0,0).Shoulder servo setting.
Angle_A_Temp = 0
Angle_B = 0# Elbow servo setting.
Angle_C = 0



  



def setup():
    #address pin
    pinFinger = 0
    pinWrist = 2
    pinElbow = 4
    pinShoulder = 6
    pinBase = 8
    pinBaseRotate = 12
        
    Servo 
    BasePan
    GripTilt
    ShoulderTilt #15
    ElbowTilt #13
    WristTilt # 3

    pos = 0 
    CurrentAngle = 0.0
    i = 0

    PI = 3.14159265

    """
    Define Lengths of Segments
    """
    ShoulderLength = 6.0
    ElbowLength = 4.0
    WristLength = 4.0

  

    """
    Define Names
    """
    Hypot = 0
    Slope = 0
    CirclePointX = 0
    CirclePointY = 0
    

    x1 = 10.0
    y1 = 7.0
    x2 = 0.0
    y2 = 0.0

    A = 0
    B = 0
    C = 0

    PosXAnswer = 0.0
    PosYAnswer = 0.0
    NegXAnswer = 0.0
    NegYAnswer = 0.0

    print("Initializing Servos")

    reset_servos()



def Special_Calc_Point():
    """
    ******************************************************************
    *********** Starting Special Circle Calcs ********************************
    ******************************************************************
    """

    Hypot = sqrt(pow(x1,2) + pow(y1,2)) + WristLength
    A = ElbowLength
    B = Hypot
    C = ShoulderLength


    Angle_A = acos((pow(B,2) + pow(C,2) - pow(A,2)) / (2 * B * C)) * (180 / PI)

    Angle_B =  acos((pow(C,2) + pow(A,2) - pow(B,2)) / (2 * A * C)) * (180 / PI)

    Angle_C = acos((pow(A,2) + pow(B,2) - pow(C,2)) / (2 * A * B)) * (180 / PI)

    Angle_A = Angle_A * (1 + (Angle_A / (Angle_B + Angle_C)))


    if Angle_A < 35:
        Angle_A = 35

    if not isnan(Angle_A):
        print(Angle_A)
        cycle = duty_cycle(Angle_A)
        pwm.setPWM(15,0,cycle)
        #timer 1 second
    # ShoulderTilt.write(Angle_A)
    
    #pwm.setPWM(pinShoulder, 0, d2a[Angle_A])
  

    if not isnan(Angle_B):

    #CurrentAngle = ElbowTilt.read()

        if (Angle_B > CurrentAngle):
        
            print(CurrentAngle)
            print(" < ")
            print(Angle_B)
            
            for i in np.arange(CurrentAngle, Angle_B, +15):
                #if Angle_B > CurrentAngle.
                # ElbowTilt.write(i);
                cycle = duty_cycle(i)
                pwm.setPWM(13,0,cycle)
                time.sleep(0.23)
                
                #print(i)
                
        else:
            print(CurrentAngle)
            print(">")
            print(Angle_B)
            #decrement
            print("Elbow")
            for i in range(CurrentAngle, Angle_B, -15):
                
                #Elbow
                cycle = duty_cycle(i)
                pwm.setPWM(13,0,cycle)
                #print(i)
                time.sleep(0.23)
                
       
    

    if not isnan(Angle_C):
        # Read current angle 
        """
        Global reference 
        """

        if Angle_C > CurrentAngle:
            print(CurrentAngle)
            print('<')
            print(Angle_C)
            for i in np.arange(CurrentAngle, Angle_C, +15):
                #print(i)
                #wrist
                cycle = duty_cycle(i)
                pwm.setPWM(3,0,cycle)
                time.sleep(0.23)
               
        else: 
            print(CurrentAngle)
            print(">")
            print(Angle_C)
            #decrement 
            print("wrist")
            for i in np.arange(CurrentAngle, Angle_C, -15):
        
                
                #wrist
                cycle = duty_cycle(i)
                pwm.setPWM(3,0,cycle)
                #print(i)
                time.sleep(0.23)
         


def Calc_Point():

    Slope = (y2-y1) /(x2 -x1)
    print("SlopeL ")
    print(Slope, 4)
    temp = (y1/x1)
    A = 1 + pow(temp,2)
    B = (-2 * x1) + (-2 * y1 * Slope)
    C = pow(y1,2) + pow(x1,2) - pow(WristLength,2)

    print(A)
    print(B)
    print(C)
    temp = y1/x1
    A = 1 + pow(temp,2)
    B = (-2 * x1) + (-2 * y1 * Slope)
    C =pow(y1,2) + pow(x1,2) - pow(WristLength,2)

    NegXAnswer = ((-1 * B) - (sqrt(pow(B,2) - (4*A*C)))) / (2*A)
    NegYAnswer = Slope * NegXAnswer

    if not isnan(NegXAnswer):
        print("Negative Point")
        print(NegXAnswer)
        print(",")
        print(NegYAnswer)
        print()
        Calc_Circle(NegXAnswer, NegYAnswer)
    else:
        PosXAnswer = ((-1 * B) + (sqrt(pow(B,2) - (4 * A * C)))) / (2 * A)
        PosYAnswer = Slope * PosXAnswer

        if not isnan(PosXAnswer):
            print("Positive Point")
            print(PosXAnswer)
            print(",")
            print(PosYAnswer)
            print()

            Calc_Circle(PosXAnswer, PosYAnswer)

def Calc_Circle(BXValue, BYValue):
    Hypot = sqrt(pow(BXValue,2) + pow(BYValue,2))
    A = ElbowLength
    B = Hypot
    C = ShoulderLength

    Angle_B =  acos((pow(C,2) + pow(A,2) - pow(B,2)) / (2 * A * C)) * (180 / PI)


    # Calculate Angle C
    print (A,' ', B)
    Angle_C = acos((pow(A,2) + pow(B,2) - pow(C,2)) / (2 * A * B)) * (180 / PI)
    Angle_C = 180 - Angle_C


   
    Angle_A = acos((pow(B,2) + pow(C,2) - pow(A,2)) / (2 * B * C)) * (180 / PI)

    Angle_A = Angle_A * (1 + (Angle_A / (Angle_B + Angle_C)))

    if (Angle_A < 35):
        Angle_A = 35

    if not isnan(Angle_A):
        print(Angle_A)

        #Serial.println(Angle_A)
         #ShoulderTilt.write(Angle_A);
         #insert here
        cycle = duty_cycle(Angle_A)
        pwm.setPWM(15,0,cycle)
    
    
    if not isnan(Angle_B):

    #CurrentAngle = ElbowTilt.read()

        if Angle_B > CurrentAngle:
            print(CurrentAngle)
            print(" < ")
            print(Angle_B)
            print("elbow")
            for i in np.arange(CurrentAngle, Angle_B, +1):
                #elbow
                print(i)
                cycle = duty_cycle(i)
                pwm.setPWM(13,0,cycle)
                #timer 5
                
    else:
      print(CurrentAngle)
      print(" > ")
      println(Angle_B)
      for i in np.arange(CurrentAngle, Angle_B, -1):
        #ElbowTilt.write(i);
        cycle = duty_cyle(i)
        pwm.setPWM(13,0,cycle)
        #print(i)
        #delay 5 seconds
     

    if not isnan(Angle_C):

        #CurrentAngle 

        if Angle_C > CurrentAngle:
            print(CurrentAngle)
            print("<")
            print(Angle_C)
            print ("wrist")
            for i in np.arange(CurrentAngle, Angle_C, +1):
                #print(i)
                #wrist
                cycle = duty_cycle(i)
                pwm.setPWM(3,0,cycle)
                

        else:
            print(CurrentAngle)
            print(">")
            print(Angle_C)
            for i in np.arange(CurrentAngle, Angle_C, -1):
                #Wrist
                #print(i)
                cycle = duty_cycle(i)
                pwm.setPWM(3,0,cycle)
                #delay 5 seconds
           


def reset_servos():
    print("Setting Shoulder to 65 degrees")
    cycle = duty_cycle(10)
    pwm.setPWM(15,0,cycle)
    print("Setting Elbow to 90 degrees")
    cycle = duty_cycle(40)
    pwm.setPWM(13,0,cycle)
    print ("Setting Wrist to 90 degrees")
    cycle = duty_cycle(40)
    pwm.setPWM(3,0,cycle)

def duty_cycle(angle):
    angle = int(angle)
    dutycycle = (((angle/180.0) + 1.0) * 5.0)*60.0
    answer= int(dutycycle)
    print("duty cycle" , answer)
    return answer

while True:
    x1 =  1
    y1 = 3
    #Distance of object
    # read_arduino()
    endX = 24
    endY = 25
    for x in range (x1, endX,+1):
        for y in range(y1, endY,+1):
            print ("********")
            print ("Point: (")
            print(x, " , " , y)
            print(")")

            if x < ShoulderLength and y < ShoulderLength:
                Special_Calc_Point()
                
            else:
                Calc_Point()

