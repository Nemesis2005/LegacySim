#LegacySimulation1
#This program simulates a standard legacy attack system N times
############################################################################
#imports modules
import time
import sys
import math

import pp

from legacystats import *
from legacyitemdatabase import *
import legacysim
import legacychance

#############################################################################
#player stats
#############################################################################
#Default fully trained avatar stats
#hp - 10
#acc - 14
#dod - 14
#speed - 60
#Unspent stats - 171
#Remember that 1 stat point = 5hp and = 5speed

##############################################################################
#player 1 stats
#############################################################################
#Please include abilities too
hp = 420
acc= 15
dod = 90
speed = 120
mskill = 450
pskill = 450
gskill = 450
dskill = 450

#create variable for player 1 stats
#choose attack type - aimed(), takecover(), quick(), standard()
p1 = pstats(hp,acc,dod,speed,mskill,pskill,gskill,dskill,mind = 5,\
            maxd = 5,armor = 5, weap1 = rift4a, weap2 = vbowls4amcrys,arm = hf4v,\
            misc1 = orphic4o,misc2 = orphic4o,atype = "aimed")

#############################################################################
#player 2 stats
#############################################################################
#Please include abilities too
hp = 300
acc = 14
dod = 126
speed = 65
mskill = 450
pskill = 450
gskill = 450
dskill = 450

#create variable for player 2 stats
p2 = pstats(hp,acc,dod,speed,mskill,pskill,gskill,dskill,\
            mind = 5,maxd = 5,armor = 5, weap1 = rift4f, weap2 = rift4f,\
            arm = dl4v,misc1 = biospine4p, misc2 = biospine4p,\
            atype = "normal")
#DEBUG
import legacyplist
p2 = legacyplist.Merlin

###########################################################################
#Number of times to do simulation
N = 1000
###########################################################################
#main program
###########################################################################
#simulates a legacy fight N times

#creates win count
win1 = 0.0
win2 = 0.0

#sets up parallel python servers
ppservers = ()

if len(sys.argv) > 1:
    ncpus = int(sys.argv[1])
    # Creates jobserver with ncpus workers
    job_server = pp.Server(ncpus, ppservers=ppservers)
else:
    # Creates jobserver with automatically detected number of workers
    job_server = pp.Server(ppservers=ppservers)


#simulates N times

jobs = [job_server.submit(legacysim.simulation,(p1,p2),\
            (legacysim.hitmiss,legacysim.damage),\
            modules=("legacysim","legacychance","random","math","legacystats"))\
            for k in range(N)]
starttime = time.time()
for k in range(N):
    w = jobs[k]()
    #checks who wins and adds it to their win count
    if w ==1:
        win1 += 1.0
    elif w==2:
        win2 += 1.0

total = win1 + win2

#changes attack type for calculation of tohit percentage
if p1.atype == "standard":
    p1.standard()
elif p1.atype == "aimed":
    p1.aimed()
elif p1.atype == "takecover":
    p1.takecover()
elif p1.atype == "quick":
    p1.quick()
p2.standard()
#calculates chance to hit of player 1 and player 2
p1hit,p1dam1,p1dam2 = legacychance.tohit(p1,p2)
p2hit,p2dam1,p2dam2 = legacychance.tohit(p2,p1)

#prints the Stats
print "Speed of Player1, Player2: ", p1.tspeed,",", p2.tspeed
print "Player 1 hit chance, w1 dam chance/w2 dam chance", round(p1hit,1),\
      "%, ", round(p1dam1,1), "%/", round(p1dam2,1), "%"
print "Player 2 hit chance, w1 dam chance/w2 dam chance", round(p2hit,1),\
      "%, ", round(p2dam1,1), "%/", round(p2dam2,1), "%"
##print "Speed of Player1, Player2: ", p1.tspeed,",", p2.tspeed
##print "Player 1 hit chance, w1 dam chance/w2 dam chance", math.ceil(p1hit),\
##      "%, ", math.ceil(p1dam1), "%/", math.ceil(p1dam2), "%"
##print "Player 2 hit chance, w1 dam chance/w2 dam chance", math.ceil(p2hit),\
##      "%, ", math.ceil(p2dam1), "%/", math.ceil(p2dam2), "%"

print "Player 1 wins: ", win1
print "Player 2 wins: ", win2
print "Player 1 win percentage: ", (win1/total)*100, "%"
print "Player 2 win percentage: ", (win2/total)*100, "%"

print "Total time is ", time.time() - starttime
