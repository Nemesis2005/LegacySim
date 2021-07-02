#Player List
#A list of player stats for use with optimization
############################################################################
#import modules
############################################################################
from legacyitemdatabase import *
import legacystats
import numpy

##############################################################################
#RiftKing
#############################################################################
#Please include abilities too
hp = 450
acc = 14
dod = 97
speed = 60
mskill = 450
pskill = 450
gskill = 450
dskill = 450

#create variable for player 2 stats
RiftKing = legacystats.pstats(hp,acc,dod,speed, mskill,pskill,gskill,dskill,\
            mind=5, maxd=5, armor=5, weap1=rift4amcrys, weap2=rift2f2amcrys,\
            arm=dl4abyss, misc1=scout4amcrys, misc2=scout4amcrys,\
            atype = 'takecover')

##############################################################################
#Q15King
#############################################################################
#Please include abilities too
hp = 600
acc = 14
dod = 63
speed = 80
mskill = 450
pskill = 450
gskill = 450
dskill = 450

#create variable for player 2 stats
Q15King = legacystats.pstats(hp,acc,dod,speed, mskill,pskill,gskill,dskill,\
            mind = 5, maxd = 5,armor = 5, weap1 = rift4amcrys, weap2 = q154f,\
            arm = dl4abyss, misc1 = scout4amcrys, misc2 = scout4amcrys,\
            atype = 'takecover')

##############################################################################
#MeleeKing
#############################################################################
#Please include abilities too
hp = 600
acc = 61
dod = 14
speed = 90
mskill = 450
pskill = 450
gskill = 450
dskill = 450

#create variable for player 2 stats
MeleeKing = legacystats.pstats(hp,acc,dod,speed, mskill,pskill,gskill,dskill,\
            mind = 5, maxd = 5,armor = 5, weap1 = void4f, weap2 = cstaff4amcrys,\
            arm = dl4abyss, misc1 = scout4amcrys, misc2 = scout4amcrys,\
            atype = 'aimed')

############################################################################
#BombRiftKing
############################################################################
#Please include abilities too
hp = 500
acc = 14
dod = 87
speed = 60
mskill = 450
pskill = 450
gskill = 450
dskill = 450

#create variable for player 2 stats
BombRiftKing = legacystats.pstats(hp,acc,dod,speed, mskill,pskill,gskill,dskill,\
            mind = 5, maxd = 5,armor = 5, weap1 = scbomb4ammy, weap2 = rift4amcrys,\
            arm = dl4abyss, misc1 = scout4amcrys, misc2 = scout4amcrys,\
            atype = "takecover")

############################################################################
#DoubleVBowKing
############################################################################
#Please include abilities too
hp = 865
acc = 14
dod = 14
speed = 60
mskill = 450
pskill = 450
gskill = 450
dskill = 450

#create variable for player 2 stats
DoubleVBowKing = legacystats.pstats(hp,acc,dod,speed, mskill,pskill,gskill,dskill,\
            mind = 5, maxd = 5,armor = 5, weap1 = vbowpt4amcrys, weap2 = vbowpt4amcrys,\
            arm = hf4v, misc1 = scout4amcrys, misc2 = scout4amcrys,\
            atype = "takecover")


############################################################################
#DoubleConcbombKing
############################################################################
#Please include abilities too
hp = 650
acc = 14
dod = 57
speed = 60
mskill = 450
pskill = 450
gskill = 450
dskill = 450

#create variable for player 2 stats
DoubleConcbKing = legacystats.pstats(hp,acc,dod,speed, mskill,pskill,gskill,dskill,\
            mind = 5, maxd = 5,armor = 5, weap1 = concbomb3ammy1f, weap2 = concbomb3ammy1f,\
            arm = dl4abyss, misc1 = scout4amcrys, misc2 = scout4amcrys,\
            atype = "takecover")

############################################################################
#DbarrelKing
############################################################################
#Please include abilities too
hp = 650
acc = 14
dod = 57
speed = 60
mskill = 450
pskill = 450
gskill = 450
dskill = 450

#create variable for player 2 stats
DbarrelKing = legacystats.pstats(hp,acc,dod,speed, mskill,pskill,gskill,dskill,\
            mind = 5, maxd = 5,armor = 5, weap1 = rift4amcrys, weap2 = dbarrel3am1f,\
            arm = dl4abyss, misc1 = scout4amcrys, misc2 = scout4amcrys,\
            atype = "takecover")

#############################################################################
#k3nny
############################################################################
#Please include abilities too
hp = 400
acc = 14
dod = 107
speed = 60
mskill = 450
pskill = 450
gskill = 450
dskill = 450

#create variable for player 2 stats
k3nny = legacystats.pstats(hp,acc,dod,speed, mskill,pskill,gskill,dskill,\
            mind = 5, maxd = 5,armor = 5, weap1 = rift4amcrys, weap2 = vbowpt4amcrys,\
            arm = sg14p, misc1 = pbot4p, misc2 = scout4y,\
            atype = "takecover")

############################################################################
#Ryu
############################################################################
#Please include abilities too
hp = 360
acc = 14
dod = 113
speed = 70
mskill = 450
pskill = 450
gskill = 450
dskill = 450

#create variable for player 2 stats
Ryu = legacystats.pstats(hp,acc,dod,speed, mskill,pskill,gskill,dskill,\
            mind = 5, maxd = 5,armor = 5, weap1 = rift4amcrys, weap2 = dbarrel3pr1f,\
            arm = dl4abyss, misc1 = biospine4p, misc2 = biospineryu,\
            atype = "standard")

############################################################################
#Aaron
############################################################################
#Please include abilities too
hp = 600
acc = 14
dod = 67
speed = 65
mskill = 450
pskill = 450
gskill = 450
dskill = 450

Aaron = legacystats.pstats(hp,acc,dod,speed, mskill,pskill,gskill,dskill,\
            mind = 5, maxd = 5,armor = 5, weap1 = rift4amcrys, weap2=q154amcrys,\
            arm = hf3ab1v, misc1 = biospine4p, misc2 = biospine4p,\
            atype = "takecover")

############################################################################
#SGame
############################################################################
#Please include abilities too
hp = 600
acc = 65
dod = 14
speed = 70
mskill = 450
pskill = 450
gskill = 450
dskill = 450

#create variable for player 2 stats
SGame = legacystats.pstats(hp,acc,dod,speed, mskill,pskill,gskill,dskill,\
            mind = 5, maxd = 5,armor = 5, weap1 = void4f, weap2 = cstaff2o2pr,\
            arm = sg12v1p1ab, misc1 = scout3amcrys1a, misc2 = scout3amcrys1a,\
            atype = "aimed")

############################################################################
#matt770
############################################################################
#Please include abilities too
hp = 450
acc = 14
dod = 93
speed = 70
mskill = 450
pskill = 450
gskill = 450
dskill = 450

#create variable for player 2 stats
matt770 = legacystats.pstats(hp,acc,dod,speed, mskill,pskill,gskill,dskill,\
            mind = 5, maxd = 5,armor = 5, weap1 = vbowls4amcrys, weap2 = rift4amcrys,\
            arm = dl4v, misc1 = pbot4y, misc2 = pbot4y,\
            atype = "standard")


############################################################################
#HappyDays
############################################################################
#Please include abilities too
hp = 750
acc = 14
dod = 57
speed = 60
mskill = 450
pskill = 450
gskill = 450
dskill = 450

HappyDays = legacystats.pstats(hp,acc,dod,speed, mskill,pskill,gskill,dskill,\
            mind = 5, maxd = 5,armor = 5, weap1 = q154f, weap2 = rift4amcrys,\
            arm = hf4abyss, misc1 = scout4amcrys, misc2 = biospine4g,\
            atype = "takecover")

############################################################################
#Merlin
############################################################################
#Please include abilities too
hp = 600
acc = 14
dod = 87
speed = 60
mskill = 450
pskill = 450
gskill = 450
dskill = 450

Merlin = legacystats.pstats(hp,acc,dod,speed, mskill,pskill,gskill,dskill,\
            mind = 5, maxd = 5,armor = 5, weap1 = scbomb4ammy, weap2 = rift4amcrys,\
            arm = dl4abyss, misc1 = scout4a, misc2 = pbot4aeon,\
            atype = "takecover")

##############################################################################
#Player list
##############################################################################
#List of players to optimize against
plist = [RiftKing, Q15King, MeleeKing, BombRiftKing, DoubleVBowKing, DoubleConcbKing, k3nny, Ryu,
        DbarrelKing, Aaron, SGame, matt770, HappyDays, Merlin]

#plist = [DbarrelKing]
w = numpy.ones(len(plist))
#w[5] = 2.0


