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

print 'Starting Follow'
Script.ChangeMode("Guided")                     # changes mode to "Guided"
print 'Guided Mode'

waypoints = [
    [38.7511215,-77.4966506],
    [38.7512588,-77.496437],
    ]

for i in range(len(waypoints)):
    #need a posiitive alt value otherwise guided mode doesn't work
    #not sure why this is
    wp = Locationwp().Set(waypoints[i][0], waypoints[i][1], 50, id)
    MAV.setGuidedModeWP(wp)
    print "upload wp" + str(i)
    Script.Sleep(10000)

iedHome = Locationwp().Set(38.7512568,-77.4966480, 50, id)
fob = Locationwp().Set(38.7512662,-77.4968163, 50, id)
iedWaypoints = [
    [38.7512887,-77.4967492],
    [38.7512665,-77.4967476],
    [38.7512417,-77.4967452]
    ]

MAV.setGuidedModeWP(iedHome)
for i in range(len(iedWaypoints)):
    Script.Sleep(10000)
    wp = Locationwp().Set(iedWaypoints[i][0], iedWaypoints[i][1], 50, id)
    MAV.setGuidedModeWP(wp)
    print "upload ied wp" + str(i)
    Script.Sleep(10000)
    MAV.setGuidedModeWP(iedHome)

randomNum = random.randint(0,2)
print "Going to Inactive IED Zone " + str(randomNum)
inactiveIedWaypoint = iedWaypoints[randomNum]
inactiveIedZone = Locationwp().Set(inactiveIedWaypoint[0], inactiveIedWaypoint[1], 50, id)

Script.Sleep(10000)
MAV.setGuidedModeWP(inactiveIedZone)
Script.Sleep(10000)
MAV.setGuidedModeWP(fob)

    
print "final ack"
MAV.setWPACK();

print "done"
