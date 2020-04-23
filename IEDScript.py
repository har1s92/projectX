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

idmavcmd = MAVLink.MAV_CMD.WAYPOINT
id = int(idmavcmd)

# issues existed if altitude was zero
alt = 50

print 'Starting Follow'
Script.ChangeMode("Guided")                     # changes mode to "Guided"
print 'Guided Mode'

def isActive():
	cnt=0
	for i in range(10):
		cnt+=cs.ied_voltage
        print(cs.ied_voltage)
        print(cs.roll)
        Script.Sleep(1000)
	return (cnt/5.0) > 1.0

#iedHome = Locationwp().Set(38.7512568,-77.4966480, alt, id)

iedCenterWaypoints = [[38.7512887,-77.4967492],
				[38.7512665,-77.4967476],
				[38.7512417,-77.4967452]]
				
iedExitWaypoints = [[38.7512887,-77.4967492],
				[38.7512665,-77.4967476],
				[38.7512417,-77.4967452]]
				
fob = Locationwp().Set(38.7512662,-77.4968163, alt, id)

zoneStatus = []

for iedWp in iedCenterWaypoints:
    Script.Sleep(10000)
    wp = Locationwp().Set(iedWp[0], iedWp[1], alt, id)
    MAV.setGuidedModeWP(wp)
    print "upload ied wp" + str(len(zoneStatus))
    Script.Sleep(10000)
    iedStatus = isActive()
    print(iedStatus)
    zoneStatus.append(iedStatus)
    if (iedStatus):
        print("An active IED was found in Zone " + str(len(zoneStatus)) + "!")
	
inactiveZone = zoneStatus.index(min(zoneStatus))
print("Going to Inactive IED Zone " + str(inactiveZone+1))
inactiveIedWaypoint = Locationwp().Set(iedExitWaypoints[inactiveZone][0], iedExitWaypoints[inactiveZone][1], alt, id)

Script.Sleep(10000)
MAV.setGuidedModeWP(inactiveIedWaypoint)
Script.Sleep(10000)
MAV.setGuidedModeWP(fob)

    
print "final ack"
MAV.setWPACK();

print "done"
