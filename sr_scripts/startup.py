'''
Start Up Script to test servos for movement of the mechanical arm. 
All 6 servos will be rotates and return to their original position.
This scrip will execute all tests in ___ seconds


'''


import time, os
import sys, traceback
from math import*

import clr
clr.AddReference(“MissionPlanner”)
import MissionPlanner
clr.AddReference(“MAVLink”)
import MAVLink

############################################################

n = 0

MAV.doCommand(MAVLink.MAV_CMD.DO_SET_SERVO, servo, pwm, 0, 0, 0, 0, 0)

print 'Gripper Tested'

Script.Sleep(1000)


MAV.doCommand(MAVLink.MAV_CMD.DO_SET_SERVO, servo, pwm, 0, 0, 0, 0, 0)

Script.Sleep(1000)












