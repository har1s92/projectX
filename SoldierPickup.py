import sys
import random
import math
import clr
import time
import System
from System import Byte

clr.AddReference("MissionPlanner")
import MissionPlanner
clr.AddReference("MissionPlanner.Utilities") # includes the Utilities class
from MissionPlanner.Utilities import Locationwp
clr.AddReference("MAVLink") # includes the Utilities class
import MAVLink

############################################################

#define wrist servo ids
servos = [1, 2, 3, 4]

#define gripper servo
gripper = 5

#define the gripper open pwm values
open = 1500

#get the number of soldiers currently picked up
soldiers = cs.soldiers
print("Picking up soldier: " + str(soldiers+1))

#pwm will hold the array of servo pwm values to specify each position
pwm=[]

if (soldiers==0):
    pwm = [1000, 1100, 1200, 1300]
elif (soldiers==1):
    pwm = [1000, 1100, 1200, 1300]
elif (soldiers==2):
    pwm = [1000, 1100, 1200, 1300]
elif (soldiers==3):
    pwm = [1000, 1100, 1200, 1300]
elif (soldiers==4):
    pwm = [1000, 1100, 1200, 1300]
elif (soldiers==5):
    pwm = [1000, 1100, 1200, 1300]
elif (soldiers==6):
    pwm = [1000, 1100, 1200, 1300]
else:
    print("An invalid number of soldiers are currently held")

for i in range(4):
    print("Setting servo position for servo" + str(i+1))
    MAV.doCommand(MAVLink.MAV_CMD.DO_SET_SERVO, servos[i], pwm[i], 0, 0, 0, 0, 0)
    Script.Sleep(1000)
    
print("Opening Gripper Servo")
MAV.doCommand(MAVLink.MAV_CMD.DO_SET_SERVO, gripper, open, 0, 0, 0, 0, 0)
print("Succesfully stored soldier: " + str(soldiers+1))
cs.soldiers+=0












