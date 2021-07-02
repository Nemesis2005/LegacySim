#This program calculates the % of hitting and damaging an enemy attack in
#legacy
##########################################################################
#Imports Modules
##########################################################################
import math
import legacycommon
###########################################################################
#User Defined Functions
###########################################################################

#calculates the hit percentage that is displayed.
#attack can be either accuracy or weapon skill
#defense can be either dodge or defense skill

#function that gives the general hit percentage formula
def hitpercent(attack,defense):
    if defense>attack:
        x = (attack + 1) - (defense/4)
        if x<0:
            x = 0
        percentage = ((x*(x/2.0))/float(((defense+1)-(defense/4))*\
                                   ((attack+1)-(attack/4))))*100
    else:
        x = (defense + 1)-(attack/4)
        if x<0:
            x = 0
        percentage = ((((defense+1-(defense/4))*(attack+1-(attack/4))) -\
                       (x*(x/2.0)))/float(((defense+1)-(defense/4))*\
                                     ((attack+1)-(attack/4))))*100
    return percentage

#function that calculates zorg's code
def hitpercent2(attack,defense):
    if defense>attack:
        x = (attack + 1) - (defense/4)
        if x<0:
            x = 0
        percentage = 100*(x*(x/2))/(((defense+1)-(defense/4))*\
                                   ((attack+1)-(attack/4)))
    else:
        x = (defense + 1)-(attack/4)
        if x<0:
            x = 0
        percentage = 100*(((defense+1-(defense/4))*(attack+1-(attack/4))) -\
                       (x*(x/2)))/(((defense+1)-(defense/4))*\
                                   ((attack+1)-(attack/4)))
    return percentage

#calculates the total hit percentage/damage percentage of player 1 to
#player 2
#P1 is attacker while P2 is defender
def tohit(p1,p2):
    #calculates hit chance
    hit = hitpercent(p1.tacc,p2.tdod)
    #calculates damage chance for weapon 1
    #if melee use mskill
    if p1.weap1.iclass == 'melee':
        dam1 = hitpercent(p1.tmskill,p2.tdskill)
    #else if projectile use pskill
    elif p1.weap1.iclass == 'projectile':
        dam1 = hitpercent(p1.tpskill,p2.tdskill)
    #else if gun use gskill
    elif p1.weap1.iclass == 'gun':
        dam1 = hitpercent(p1.tgskill,p2.tdskill)
    #calculates damage chance for weapon 2
    #if melee use mskill
    if p1.weap2.iclass == 'melee':
        dam2 = hitpercent(p1.tmskill,p2.tdskill)
    #else if projectile use pskill
    elif p1.weap2.iclass == 'projectile':
        dam2 = hitpercent(p1.tpskill,p2.tdskill)
    #else if gun use gskill
    elif p1.weap2.iclass == 'gun':
        dam2 = hitpercent(p1.tgskill,p2.tdskill)
    #returns hit percentage and damage percentage
    return hit,dam1,dam2

#trying to simulate zorg's display percentage code
#to player 2
def tohit2(p1,p2):
    #calculates hit chance
    hit = hitpercent2(p1.tacc,p2.tdod)
    #calculates damage chance for weapon 1
    #if melee use mskill
    if p1.weap1.iclass == 'melee':
        dam1 = hitpercent2(p1.tmskill,p2.tdskill)
    #else if projectile use pskill
    elif p1.weap1.iclass == 'projectile':
        dam1 = hitpercent2(p1.tpskill,p2.tdskill)
    #else if gun use gskill
    elif p1.weap1.iclass == 'gun':
        dam1 = hitpercent2(p1.tgskill,p2.tdskill)
    #calculates damage chance for weapon 2
    #if melee use mskill
    if p1.weap2.iclass == 'melee':
        dam2 = hitpercent2(p1.tmskill,p2.tdskill)
    #else if projectile use pskill
    elif p1.weap2.iclass == 'projectile':
        dam2 = hitpercent2(p1.tpskill,p2.tdskill)
    #else if gun use gskill
    elif p1.weap2.iclass == 'gun':
        dam2 = hitpercent2(p1.tgskill,p2.tdskill)
    #returns hit percentage and damage percentage
    return hit,dam1,dam2

#this function calculates the average damage/turn that p1 inflicts on p2
def avdam(p1,p2):
    #calculates chance to hit and chance to damage
    hit,dam1,dam2 = tohit(p1,p2)
    #calculates average damage of player 1 with weapon 1
    level = min(p1.level, 80)
    modifier = level * legacycommon.armor_mult
    mult = (modifier/(modifier + p2.tarmor))
    weap1ave = (math.ceil(p1.tmind1 * mult) + math.ceil(p1.tmaxd1 * mult))/2.0
    #calculates average damage of player 2 with weapon 2
    weap2ave = (math.ceil(p1.tmind2 * mult) + math.ceil(p1.tmaxd2 * mult))/2.0

    #calculates damage per turn and returns it
    damperturn = weap1ave*(hit/100)*(dam1/100) + weap2ave*(hit/100)*(dam2/100)
    return damperturn

#This function returns the avg # of turns it takes for p1 to kill p2
def avturns(p1,p2):
    p1avdam = avdam(p1,p2)
    return max(1.0, p2.hp/p1avdam)

#This function returns the ratio of avg # of turns it takes for p1 to kill p2
#and for p2 to kill p1
def avtratio(p1,p2):
    p1avt = avturns(p1,p2)
    p2avt = avturns(p2,p1)
    #if player 1 has greater or equal speed then add + 0.5 avturn to player 2
    if p1.tspeed> p2.tspeed:
        p2avt += 0.5
    #Otherwise, add + 0.5 avturn to player 1
    elif p1.tspeed<p2.tspeed:
        p1avt += 0.5
    rate1 = p2avt/(p1avt+p2avt)
    rate2 = p1avt/(p1avt+p2avt)
    return rate1,rate2

#This function calculates the weighted mean of the avtratio for a list of players
#This is the value that is going to be maximized
def rating(p1,p2list,weight):
    n = len(p2list)             #length of list of players
    avtrats = []
    mean = 0.0
    #calculates the avtratio for each player
    for i in range(n):
        #changes the attack of player 1 into default
        if p1.atype == "standard":
            p1.standard()
        elif p1.atype == "aimed":
            p1.aimed()
        elif p1.atype == "takecover":
            p1.takecover()
        elif p1.atype == "quick":
            p1.quick()
        #changes the attack of player 2 to normal attack
        p2list[i].standard()
        temp1, temp2 = avtratio(p1,p2list[i])

        #calculates the avtratio when defending
        #changes attack of player 2 to default
        if p2list[i].atype == "standard":
            p2list[i].standard()
        elif p2list[i].atype == "aimed":
            p2list[i].aimed()
        elif p2list[i].atype == "takecover":
            p2list[i].takecover()
        elif p2list[i].atype == "quick":
            p2list[i].quick()
        #changes the attack of player 1 to default
        p1.standard()
        temp3, temp4 = avtratio(p1,p2list[i])

        #takes the average of the two ratings
        avtrats.append((temp1+temp3)/2.0)

        #calculates the weighted mean
        mean += avtrats[i]*weight[i]

    #calculates the mean and returns it
    mean /= n
    return mean, avtrats
############################################################################
