#LegacySimulation3
#This program simulates a standard legacy attack system N times against a list
#of players
############################################################################
#imports modules
from random import randint
from copy import copy
from legacysim import *
from legacychance import *
from legacyplist import *

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

###########################################################################
#Number of times to do simulation
N = 500

###########################################################################
#main program
###########################################################################
#simulates a legacy fight N times against a list of players
#length of player list
L = len(plist)

#creates win count
win1 = 0.0
win2 = 0.0
winpercent = []

#simulates N times for each player
for i in range(L):
    for k in range(N):
        w = simulation(p1,plist[i])
        #checks who wins and adds it to their win count
        if w ==1:
            win1 += 1.0
        else:
            win2 += 1.0
    total = win1 + win2
    #calculates winpercentage and appends it to list
    percent = win1/total
    winpercent.append(percent)

#calculates average winpercent
avwinp = sum(winpercent)/L

#Returns win percentagecount
print "Average Win Percent: ", avwinp
print "Individual Win Percent: ", winpercent
