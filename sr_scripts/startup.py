'''
Start Up Script to test servos for movement of the mechanical arm. 
All 6 servos will be rotates and return to their original position.
The Gripper will open and close
This scrip will execute all tests in ___ seconds


'''
import sys
import random
import math
import clr
import time
import System
from System import Byte

clr.AddReference("MissionPlanner")
import MissionPlanner
clr.AddReference("MissionPlanner.Utilities")
from MissionPlanner.Utilities import Locationwp
clr.AddReference("MAVLink") 
import MAVLink
############################################################



servos = [1, 2, 3, 4, 5]

gripper = 6 #Not sure how this works

pwm1 = [1000, 1000, 1000, 1000]

pwm2 = [1000, 1000, 1000, 1000]

position = 0 
 
for i in range(5): 
    MAV.doCommand(MAVLink.MAV_CMD.DO_SET_SERVO, servos[i], pwm1[i], 0, 0, 0, 0, 0)
    Script.Sleep(5000)
    MAV.doCommand(MAVLink.MAV_CMD.DO_SET_SERVO, servos[i], pwm2[i], 0, 0, 0, 0, 0)
    print 'The Arm has been successfully tested'
    Script.Sleep(300)
    

MAV.doCommand(MAVLink.MAV_CMD.DO_SET_SERVO, gripper, open, 0, 0, 0, 0, 0)

print 'Gripper Tested'
Script.Sleep(1000)
print 'The Arm is mission ready'














