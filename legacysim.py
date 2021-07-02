#Legacy Simulation Functions
#This program creates a function that simulates a single battle of Legacy-Game
#battle system
#This uses the custom classes that I've created for easier use
##############################################################################
#imports modules
import math
import numpy
import random
import legacycommon
#############################################################################
#user defined functions
#############################################################################
#calculates whether a hit lands or not, 1 if it hits, 0 if it misses
def hitmiss(attack, defense):
    x = random.randint(attack/4,attack) -\
        random.randint(defense/4,defense)
    if x>0:
        return 1
    elif x == 0:
        y = random.randint(0,1)
        return y
    else:
        return 0

#calculates the damage output
def damage(mindam, maxdam, armor, level):
    absorb = 0
    dam = random.randint(mindam,maxdam)
    level = min(level, 80)
    modifier = level * legacycommon.armor_mult
    dam *= (modifier/ (modifier + armor))
    return math.ceil(dam)


#simulation function
#simulates the results of standard legacy battles once and returns 1 if p1 wins
#or returns 2 if p2 wins
def simulation(p1,p2):
    #variables
    win1 = 0.0      #times player 1 wins
    win2 = 0.0      #times player 2 wins
    dam = 0         #placeholder variable for damage
    #creates a variable for currenthp
    currenthp1 = p1.hp
    currenthp2 = p2.hp

    #chooses attack type - player 1's default attack type, player 2 - standard
    if p1.atype == "standard":
        p1.standard()
    elif p1.atype == "aimed":
        p1.aimed()
    elif p1.atype == "takecover":
        p1.takecover()
    elif p1.atype == "quick":
        p1.quick()
    p2.standard()

    #simulates the battle
    while currenthp2>0 and currenthp1>0:
        #if player 2 has more speed than player 1
        if p2.tspeed>p1.tspeed:   #player 2 hits first
            #first weapon roll
            #checks whether it hits
            if hitmiss(p2.tacc,p1.tdod)==1:
                #checks whether it damages
                if hitmiss(p2.w1skill(),p1.dskill):
                    #calculates the damage
                    dam = damage(p2.tmind1, p2.tmaxd1, p1.tarmor, p2.level)
                    currenthp1 -= dam
            #second weapon roll
            #checks whether it hits
            if hitmiss(p2.tacc,p1.tdod)==1:
                #checks whether it damages
                if hitmiss(p2.w2skill(),p1.dskill):
                    #calculates the damage
                    dam = damage(p2.tmind2, p2.tmaxd2, p1.tarmor, p2.level)
                    currenthp1 -= dam
                    
            #ends the battle if player1 is dead, else player 1
            #counterattacks
            if currenthp1>0:
                #first weapon roll
                if hitmiss(p1.tacc,p2.tdod) == 1:
                    if hitmiss(p1.w1skill(), p2.dskill) == 1:
                        dam = damage(p1.tmind1, p1.tmaxd1, p2.tarmor, p1.level)
                        currenthp2 -= dam
                #second weapon roll
                if hitmiss(p1.tacc,p2.tdod) == 1:
                    if hitmiss(p1.w2skill(), p2.dskill) == 1:
                        dam = damage(p1.tmind2, p1.tmaxd2, p2.tarmor, p1.level)
                        currenthp2 -= dam
            else:
                return 2
                
            #print "HP1 = ", currenthp1
            #print "HP2 = ", currenthp2
        #else player 1 hits first
        else:
            #first weapon roll
            if hitmiss(p1.tacc,p2.tdod) == 1:
                if hitmiss(p1.w1skill(), p2.dskill) == 1:
                    dam = damage(p1.tmind1, p1.tmaxd1, p2.tarmor, p1.level)
                    currenthp2 -= dam
            #second weapon roll
            if hitmiss(p1.tacc, p2.tdod) == 1:
                if hitmiss(p1.w2skill(), p2.dskill) == 1:
                    dam = damage(p1.tmind2, p1.tmaxd2, p2.tarmor, p1.level)
                    currenthp2 -= dam

            #checks if player 2 is still alive, if so he counterattacks
            if currenthp2>0:
                #first weapon roll
                #checks whether it hits
                if hitmiss(p2.tacc, p1.tdod) == 1:
                    #checks whether it damages
                    if hitmiss(p2.w1skill(), p1.dskill):
                        #calculates the damage
                        dam = damage(p2.tmind1, p2.tmaxd1, p1.tarmor, p2.level)
                        currenthp1 -= dam
                #second weapon roll
                #checks whether it hits
                if hitmiss(p2.tacc, p1.tdod)==1:
                    #checks whether it damages
                    if hitmiss(p2.w2skill(), p1.dskill):
                        #calculates the damage
                        dam = damage(p2.tmind2, p2.tmaxd2, p1.tarmor, p2.level)
                        currenthp1 -= dam
            #ends battle and returns 1 if player 2 is dead
            else:
                return 1
            #print  "HP1 = ", currenthp1
            #print  "HP2 = ", currenthp2
    #returns 1 if player 1 is still alive, otherwise returns 2
    if currenthp1 > 0:
        return 1
    else:
        return 2

#Simulates a battle N times against a list of opponents, N/2 times as 1st player
#N/2 times as 2nd player
def simrating(p1 ,plist, N, weight):
    #length of player list
    L = len(plist)

    #creates win count
    winpercent = numpy.zeros(L)

    #simulates N times for each player
    for i in range(L):
        win1 = 0.0
        win2 = 0.0
        #N/2 times as attacking player
        for k in range(N/2):
            w = simulation(p1, plist[i])
            #checks who wins and adds it to their win count
            if w == 1:
                win1 += 1.0
            else:
                win2 += 1.0
        #N/2 times as defending player
        for k in range(N/2, N):
            w = simulation(plist[i], p1)
            #checks who wins and adds it to their win count
            if w == 2:
                win1 += 1.0
            else:
                win2 += 1.0
        #calculates winpercentage and appends it to list
        percent = win1/N
        winpercent[i] = percent
    

    #calculates average winpercent
    avwinp = numpy.dot(winpercent,weight)/L

    return avwinp, winpercent

#############################################################################
