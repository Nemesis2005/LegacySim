#This program creates classes of player stats for use with legacysimulation
#
############################################################################
#imports modules
############################################################################
from math import floor, ceil
from legacyequip import *

#############################################################################
#player stat class
#############################################################################

#atype has to be either standard,aimed, or takecover
class pstats:
    attack_types = ["standard", "aimed", "takecover", "quick"]

    "Player Stats - weapon is optional"
    def __init__(self,hp,acc,dod,speed,mskill,pskill,gskill,dskill,
                 mind=0, maxd=0, armor=0, weap1=nowep, weap2=nowep,
                 arm=noarm, misc1=nomisc, misc2=nomisc, atype="standard",
                 level=80):
        #creates object for basestats
        self.hp = hp
        self.acc = acc
        self.dod = dod
        self.speed = speed
        self.mskill = mskill
        self.pskill = pskill
        self.gskill = gskill
        self.dskill = dskill
        self.mind = mind
        self.maxd = maxd
        self.armor = armor
        self.weap1 = weap1
        self.weap2 = weap2
        self.arm = arm
        self.misc1 = misc1
        self.misc2 = misc2
        self.atype = atype
        self.level = level

        #creates total stats variables and calculate them
        self.tstats()

    #calculates the total stats of the player including item stats
    def tstats(self):
        eq = self.equip()
        self.tacc = self.acc
        self.tdod = self.dod
        self.tspeed = self.speed
        self.tarmor = self.armor
        self.tmskill = self.mskill
        self.tgskill = self.gskill
        self.tpskill = self.pskill
        self.tdskill = self.dskill
        for item in eq:
            self.tacc += item.tacc
            self.tdod += item.tdod
            self.tspeed += item.tspeed
            self.tarmor += item.tarmor
            self.tdskill += item.tdskill
            
        self.tmind1 = self.mind + self.weap1.tmind
        self.tmind2 = self.mind + self.weap2.tmind
        self.tmaxd1 = self.maxd + self.weap1.tmaxd
        self.tmaxd2 = self.maxd + self.weap2.tmaxd
        #calculates weapon skills
        #if they both have the same class then just add the item skills
        if (self.weap1.iclass == self.weap2.iclass):
            for item in eq:
                self.tmskill += item.tmskill
                self.tgskill += item.tgskill
                self.tpskill += item.tpskill
        #else doubles the contribution of the weapons
        else:
            self.tmskill += 2*self.weap1.tmskill + 2*self.weap2.tmskill
            self.tgskill += 2*self.weap1.tgskill + 2*self.weap2.tgskill
            self.tpskill += 2*self.weap1.tpskill + 2*self.weap2.tpskill
            for item in eq[2:]:
                self.tmskill += item.tmskill
                self.tgskill += item.tgskill
                self.tpskill += item.tpskill
        
        
        
    def __repr__(self):
        return '''pstats(hp = %s,acc = %s,dod = %s,speed = %s,mskill = %s,
pskill = %s,gskill = %s, dskill = %s)''' %\
               (self.hp,self.acc,self.dod,self.speed,self.mskill,self.pskill,\
                self.gskill,self.dskill)
    #chooses the weaponskill of the player based on weapon1 item type
    def w1skill(self):
        #if melee returns totalmskill
        if self.weap1.iclass == 'melee':
            return self.tmskill
        #if projectile returns tpskill
        if self.weap1.iclass == 'projectile':
            return self.tpskill
        #if gun, then returns tgskill
        if self.weap1.iclass == 'gun':
            return self.tgskill
    #chooses the weaponskill of the player based on weapon2 item type
    def w2skill(self):
        #if melee returns totalmskill
        if self.weap2.iclass == 'melee':
            return self.tmskill
        #if projectile returns tpskill
        if self.weap2.iclass == 'projectile':
            return self.tpskill
        #if gun, then returns tgskill
        if self.weap2.iclass == 'gun':
            return self.tgskill
    #changes the weapon 1 of the player
    def cweap1(self,weap):
        self.weap1 = weap
        #recalculates the total stats of the player with the new weapon
        self.tstats()
    #changes weapon 2 of the player
    def cweap2(self,weap):
        self.weap2 = weap
        #recalculates the total stats of the player with the new weapon
        self.tstats()
    #changes the armor of the player
    def carm(self,arm):
        self.arm = arm
        self.tstats()
    #changes the misc1 of the player
    def cmisc1(self,misc):
        self.misc1 = misc
        self.tstats()
    #changes the misc2 of the player
    def cmisc2(self,misc):
        self.misc2 = misc
        self.tstats()

    #returns the equipment of the player in a list in class equip form
    def equip(self):
        return [self.weap1,self.weap2,self.arm,self.misc1,self.misc2]
    #returns a list of equipment of the player in a list in string form
    def equipment(self):
        return [self.arm.name,self.weap1.name,self.weap2.name,\
                self.misc1.name,self.misc2.name]

    #Modifies the attack type
    #resets stats to standard attack first and then adds new modifier
    #resets to standard attack type
    def standard(self):
        self.tstats()
    #quick attack - +20% speed, - 10% acc, -10% dod
    def quick(self):
        self.tstats()
        self.tspeed = int(floor(1.2*self.tspeed))
        self.tacc = int(floor(0.9*self.tacc))
        self.tdod = int(floor(0.9*self.tdod))
    #aimed attack - -10% speed, +20% acc, -10% dodge
    def aimed(self):
        self.tstats()
        self.tspeed = int(floor(0.9*self.tspeed))
        self.tacc = int(floor(1.2*self.tacc))
        self.tdod = int(floor(0.9*self.tdod))
    #take cover - -10% speed, -10% acc, +20% dod
    def takecover(self):
        self.tstats()
        self.tspeed = int(floor(0.9*self.tspeed))
        self.tacc = int(floor(0.9*self.tacc))
        self.tdod = int(floor(1.2*self.tdod))

    #function that modifies stats
    #changes acc
    def cacc(self,acc):
        self.acc = acc
        self.tstats()
    #changes dod
    def cdod(self,dod):
        self.dod = dod
        self.tstats()
    #changes speed
    def cspeed(self,speed):
        self.speed = speed
        self.tstats()
#############################################################################

##############################################################################
#test
##scythe.socket([pair,pfire,pfire])
##p1 = pstats(230,68,68,20,400,400,400,400,mind = 5,maxd = 5,armor = 5,\
##            weap1 = scythe,weap2 = scythe,arm = titan,misc1 = cring,\
##            misc2 = cring)
