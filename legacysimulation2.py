#LegacySimulation2
#This program simulates a standard legacy attack system N times and if they have
#the same speed, half the time p1 hits first, the other half p2 hits first.
############################################################################
#imports modules
from random import randint
from copy import copy
from legacystats import *
from legacyitemdatabase import *
from legacysim import *
from legacychance import *

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
#Please include abilities too
hp = 300
acc= 118
dod = 14
speed = 105
mskill = 450
pskill = 450
gskill = 450
dskill = 450

#create variable for player 1 stats
#choose attack type - aimed, takecover, quick, standard
p1 = pstats(hp,acc,dod,speed,mskill,pskill,gskill,dskill,mind = 5,maxd = 5,\
            armor = 5, weap1 = void, weap2 = void,arm = ntitan,\
            misc1 = ninferno,misc2 = nprime,atype = "aimed")

#############################################################################
#player 2 stats
#Please include abilities too
hp = 450
acc= 71
dod = 35
speed = 85
mskill = 450
pskill = 450
gskill = 450
dskill = 450

#create variable for player 2 stats
p2 = pstats(hp,acc,dod,speed,mskill,pskill,gskill,dskill,mind = 5,maxd = 5,\
            armor = 5, weap1 = scythe2, weap2 = scythe1,arm = titan3,\
            misc1 = prime2, misc2 = prime3,atype = "aimed")


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

#simulates N/2 times with p1 hitting first if speed is equal
for k in range(N/2):
    w = simulation(p1,p2)
    #checks who wins and adds it to their win count
    if w ==1:
        win1 += 1.0
    else:
        win2 += 1.0

#simulates N-N/2 times with p2 hitting first if speed is equal
for k in range(N-N/2):
    w = simulation(p2,p1)
    #checks who wins and adds it to their win count
    if w ==1:
        win2 += 1.0
    else:
        win1 += 1.0
        
total = win1 + win2

#calculates chance to hit of player 1 and player 2
p1hit,p1dam1,p1dam2 = tohit(p1,p2)
p2hit,p2dam1,p2dam2 = tohit(p2,p1)

#prints the Stats
print "Speed of Player1, Player2: ", p1.tspeed,",", p2.tspeed
print "Player 1 hit chance, w1 dam chance/w2 dam chance", round(p1hit,1),\
      "%, ",round(p1dam1,1), "%/",round(p1dam2,1), "%"
print "Player 2 hit chance, w1 dam chance/w2 dam chance", round(p2hit,1),\
      "%, ",round(p2dam1,1), "%/",round(p2dam2,1), "%"
##print "Player 1 hit chance, w1 dam chance/w2 dam chance", p1hit,\
##      "%, ",p1dam1, "%/",p1dam2, "%"
##print "Player 2 hit chance, w1 dam chance/w2 dam chance", p2hit,\
##      "%, ",p2dam1, "%/",p2dam2, "%"
print "Player 1 wins: ", win1
print "Player 2 wins: ", win2
print "Player 1 win percentage: ", (win1/total)*100, "%"
print "Player 2 win percentage: ", (win2/total)*100, "%"
