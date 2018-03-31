from Adafruit_PWM_Servo_Driver import PWM
import time
from math import sqrt

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
  
   """
   Pin Names 

   Pin 0  Finger       Servo F
   Pin 2  Wrist        Servo E 
   Pin 4  Elbow        Servo D
   Pin 6  Shoulder     Servo C
   Pin 8  Base         Servo A
   Pin 12 BaseRotator  ServoB

   """
# Set Address
pwm = PWM(0x40)
pwm.setPWMFreq(60)
#set frequency 

#Set Pin Association
pinFinger = 0
pinWrist = 2
pinElbow = 4
pinShoulder = 6
pinBase = 8
pinBaseRotate = 12

"""
Initialize
"""

BasePan
GripTilt 
ShoulderTilt
ElbowTilt
WristTilt



# ****** Setup IK variables ******
PI = 3.14159265




"""
Define Lengths of Segments
"""
ShoulderLength = 9.5
ElbowLength = 9.0
WristLength = 5.8


"""
Define Names
"""
Hypot = 0
Slope = 0
CirclePointX = 0
CirclePointY = 0
"""
End Angle
"""

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


print("Initializing Servos")
reset_servos()





  
    

    """
    Object to Control the servo
    Servo BasePan, GripTilt, ShoulderTilt, ElbowTilt, WristTitle
    """"
while True:
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

	if not isnan(Angle_A):
	    print(Angle_A)
	   
	    # ShoulderTilt.write(Angle_A)
	    
	    pwm.setPWM(pinShoulder, 0, d2a[Angle_A])
	    delay(1000)

	if not isnan(Angle_B):

	    #CurrentAngle = ElbowTilt.read()

	    if (Angle_B > CurrentAngle):
	      
		print(CurrentAngle)
		print("< \n", Angle_B)
		Serial.print(" < ")
		Serial.println(Angle_B)
		for i in range( CurrentAngle, Angle_B)
		    #if Angle_B > CurrentAngle.
		    # ElbowTilt.write(i);
		    i*=(200/45)
		     pwm.setPWM(pinElbow, 0, d2a[Angle_A])
		     #delay(5)
	    else:
		print(CurrentAngle)
		print(">")
		print(Angle_B)

		for i in range(CurrentAngle, Angle_B, -1)
		    i += (200/45)
		    pwm.setPWM(pinElbow, 0, i)
		    #delay(5)
	if not isnan(Angle_C):
		# CurrentAngle = WristTilt.read()
		
		if Angle_C > CurrentAngle: 
			print(CurrentAngle)
			print(" < ")
			print(Angle_C)
			
			for i in range(CurrentAngle, Angle_C)
				pwm.setPWM(pinWrist, 0, i)
				print("New angle: ", i)
			
			

	       
    


def reset_servos():
   
   """
   Pins
   """
    # delay(2000);
    # pinFinger = 0
    # pinWrist = 2
    # pinElbow = 4
    # pinShoulder = 6
    # pinBase = 8
    # pinBaseRotate = 12
   

    """
    Servo A
    """
    # WristTilt.write(90);//was 60.50.40
    pwm.setPWM(pinBaseRotate, 0, 450)

    """
    Servo B
    """
    # GripTilt.write(90); //was 40,35,90,20,60.10.45
    delay(500)
    pwm.setPWM(pinBase, 0, 450)

    """
    Servo C
    Shoulder
    """
    delay(2000)
    pwm.setPWM(pinShoulder, 0, 450)

    """
    Servo D
    Shoulder
    """

    delay(2000)
    pwm.setPWM(pinElbow, 0, 450)
    """
    Servo E
    """
    delay(2000)
    pwm.setPWM(pinWrist, 0, 450)
    """
    Servo F
    """
    delay(2000)
    pwm.setPWM(pinFinger, 0, 450)





# pwm.setPWMFreq(60)
# while(True):
#     pwm.setPWM(0,0,servoMin)
#     time.sleep(1)
#     pwm.setPWM(0,0, servoMax)
#     time.sleep(1)



"""""""""
def setServoPulse(channel, pulse):
    pulseLength = 1000000
    pulseLength /= 60
    print "%d us per period" % pulseLength 
    pulseLength /= 4096
    print "%d us per bit" % pulseLength
    pulse *= 1000
    pulse /= pulseLength
    pwm.setPWM(channel, 0, pulse)



