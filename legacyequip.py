#This program creates a class for crystals and legacy equipment for use with
#other programs
#This also contains a database of crystals and items
############################################################################
#Imports Modules
############################################################################
import math
import copy

#############################################################################
#Crystal Class
############################################################################
#Creates a class for crystals to be socketed with stats in percentage

class crystalmod:
    def __init__(self,name,speed,dskill,mskill,gskill,pskill,armor,damage,acc,\
                 dod):
        self.name = name
        self.speed = speed
        self.dskill = dskill
        self.mskill = mskill
        self.gskill = gskill
        self.pskill = pskill
        self.armor = armor
        self.damage = damage
        self.acc = acc
        self.dod = dod
    def __repr__(self):
        return '''Crystal(speed = %s,dskill = %s,mskill = %s,gskill = %s,
pskill = %s, armor = %s, dam = %s, acc = %s,dod = %s)''' %\
                (self.speed,self.dskill,self.mskill,self.gskill,\
                self.pskill,self.armor,self.damage,self.acc,self.dod)
    def __str__(self):
        return self.name



##############################################################################
#Equipment Class
############################################################################
#Creates a class for item equipment
class equip:
    "Equipment stats"
    def __init__(self,mind,maxd,armor,acc,dod,speed,\
                 mskill,pskill,gskill,dskill,iclass,name):
        #creates variables for item stats
        self.mind = mind
        self.maxd = maxd
        self.armor = armor
        self.acc = acc
        self.dod = dod
        self.mskill = mskill
        self.pskill = pskill
        self.gskill = gskill
        self.dskill = dskill
        self.speed = speed
        self.iclass = iclass
        self.name = name
        
        #total stats that will actually be used in calculations - to include
        #crystal stats
        self.tmind = mind
        self.tmaxd = maxd
        self.tarmor = armor
        self.tacc = acc
        self.tdod = dod
        self.tmskill = mskill
        self.tpskill = pskill
        self.tgskill = gskill
        self.tdskill = dskill
        self.tspeed = speed
        
        self.cryst = []
        #initialize crystal percentage stats
        self.cspeed = 0
        self.cdskill = 0
        self.cmskill = 0
        self.cgskill = 0
        self.cpskill = 0
        self.carmor = 0
        self.cdamage = 0
        self.cacc = 0
        self.cdod = 0
        
        self.mods = []
        #initialize mod percentage stats
        self.mspeed = 0
        self.mdskill = 0
        self.mmskill = 0
        self.mgskill = 0
        self.mpskill = 0
        self.marmor = 0
        self.mdamage = 0
        self.macc = 0
        self.mdod = 0
    
    #what it prints out
    def __repr__(self):
        return '''Equip(mind = %s,maxd = %s,armor = %s,acc = %s,dod = %s,
speed = %s,mskill = %s,pskill = %s,gskill = %s,dskill = %s,%s)''' %\
               (self.mind,self.maxd,self.armor,self.acc,self.dod,\
                self.speed,self.mskill,self.pskill,self.gskill,\
                self.dskill,self.iclass)
    def __str__(self):
        return self.name
    
    #sockets an array of crystals
    def socket(self, cryst):
        self.cryst = cryst
        self.add_crystal_stats(cryst)
        self.calculate_total_stats()

    #returns what kind of crystals are currently socketed
    def crystal(self):
        return self.cryst

    #returns the names of the crystal currently socketed
    def crystaln(self):
        cryst2 = []
        for k in self.cryst:
            cryst2.append(k.name)
        return cryst2
    
    def modslot(self, mods):
        self.mods = mods
        self.add_mod_stats(mods)
        self.calculate_total_stats()
        
    def get_mod(self):
        return self.mods
    
    def get_mod_name(self):
        mod2 = []
        for k in self.mods:
            mod2.append(k.name)
        return mod2
    
    # Add all crystal related stats
    def add_crystal_stats(self, crystals):
        #resets the total percentage of stats to be added to crystals
        self.cspeed = 0
        self.cdskill = 0
        self.cmskill = 0
        self.cgskill = 0
        self.cpskill = 0
        self.carmor = 0
        self.cdamage = 0
        self.cacc = 0
        self.cdod = 0
        #calculates the total percentage of stats to be added to crystalsals
        for k in range(0,len(crystals)):
            self.cspeed += crystals[k].speed
            self.cdskill += crystals[k].dskill
            self.cmskill += crystals[k].mskill
            self.cgskill += crystals[k].gskill
            self.cpskill += crystals[k].pskill
            self.carmor += crystals[k].armor
            self.cdamage += crystals[k].damage
            self.cacc += crystals[k].acc
            self.cdod += crystals[k].dod
    
    # Adds all mod related stats
    def add_mod_stats(self, mods):
        #resets mod percentage stats
        self.mspeed = 0
        self.mdskill = 0
        self.mmskill = 0
        self.mgskill = 0
        self.mpskill = 0
        self.marmor = 0
        self.mdamage = 0
        self.macc = 0
        self.mdod = 0
        for k in range(0,len(mods)):
            self.mspeed += mods[k].speed
            self.mdskill += mods[k].dskill
            self.mmskill += mods[k].mskill
            self.mgskill += mods[k].gskill
            self.mpskill += mods[k].pskill
            self.marmor += mods[k].armor
            self.mdamage += mods[k].damage
            self.macc += mods[k].acc
            self.mdod += mods[k].dod
            
    def calculate_total_stats(self):
        #calculates the total stats of the equipment including crystals and mods
        self.tmind = (self.mind + int(math.ceil(self.mind*(self.cdamage/100.0))) +
                      int(math.ceil(self.mind*(self.mdamage/100.0))))
        self.tmaxd = (self.maxd + int(math.ceil(self.maxd*(self.cdamage/100.0))) +
                      int(math.ceil(self.maxd*(self.mdamage/100.0))))
        self.tarmor = (self.armor + int(math.ceil(self.armor*(self.carmor/100.0))) +
                       int(math.ceil(self.armor*(self.marmor/100.0))))
        self.tacc = (self.acc + int(math.ceil(self.acc*(self.cacc/100.0))) +
                     int(math.ceil(self.acc*(self.macc/100.0))))
        self.tdod = (self.dod + int(math.ceil(self.dod*(self.cdod/100.0))) + 
                     int(math.ceil(self.dod*(self.mdod/100.0))))
        self.tmskill = (self.mskill + int(math.ceil(self.mskill*(self.cmskill/100.0))) +
                        int(math.ceil(self.mskill*(self.mmskill/100.0))))
        self.tpskill = (self.pskill + int(math.ceil(self.pskill*(self.cpskill/100.0))) +
                        int(math.ceil(self.pskill*(self.mpskill/100.0))))
        self.tgskill = (self.gskill + int(math.ceil(self.gskill*(self.cgskill/100.0))) + 
                        int(math.ceil(self.gskill*(self.mgskill/100.0))))
        self.tdskill = (self.dskill + int(math.ceil(self.dskill*(self.cdskill/100.0))) + 
                        int(math.ceil(self.dskill*(self.mdskill/100.0))))
        self.tspeed = (self.speed + int(math.ceil(self.speed*(self.cspeed/100.0))) + 
                       int(math.ceil(self.speed*(self.mspeed/100.0))))
        

#############################################################################
#User defined function
#############################################################################
#This function prints takes a list of crystals and prints out the names
#of the crystals
def crystaln(lists):
    temp = []
    n = len(lists)
    for k in range(n):
        temp.append(lists[k].name)
    return temp
#############################################################################
#Database of Crystals and mods
############################################################################

# 'name',speed,dskill,mskill,gskill,pskill,armor,dmg,acc,dod

# Crystal Sockets
pnull = crystalmod('pnull',20,0,0,0,0,0,0,0,0)
ppink = crystalmod('ppink',0,20,0,0,0,0,0,0,0)
porange = crystalmod('porange',0,0,20,0,0,0,0,0,0)
pgreen = crystalmod('pgreen',0,0,0,20,0,0,0,0,0)
pyellow = crystalmod('pyellow',0,0,0,0,20,0,0,0,0)
pvoid = crystalmod('pvoid',0,0,0,0,0,10,0,0,0)
pfire = crystalmod('pfire',0,0,0,0,0,0,10,0,0)
pair = crystalmod('pair',0,0,0,0,0,0,0,5,0)
pwater = crystalmod('pwater',0,0,0,0,0,0,0,0,5)
primecrys = crystalmod('prime crystal',0,0,0,0,0,0,5,5,0)
aeoncrys = crystalmod('aeon crystal',0,3,0,0,0,0,0,0,6)
abyss = crystalmod('abyss',10,5,0,0,0,5,0,0,4)
amcrys = crystalmod('amcrys',0,10,10,10,10,0,6,6,0)
cabr = crystalmod('cabrusion',9,7,0,0,0,9,7,0,0)

# Mods
lsight = crystalmod('lsight',0,0,0,0,0,0,0,14,0)
ptip = crystalmod('ptip',0,0,0,0,0,0,10,0,0)


#############################################################################
#Database of Equipment Stats
############################################################################

#mindmg, maxdmg, armor, acc, dod, spd, mskill, pskill, gskill, dskill, 'type', 'name'

#none - no items equipped
nowep = equip(1,4,0,0,0,0,0,0,0,0,'melee','nowep')
noarm = equip(0,0,0,0,0,0,0,0,0,0,'armor','noarm')
nomisc = equip(0,0,0,0,0,0,0,0,0,0,'misc','nomisc')

###########
##Weapons##
###########

#Crystal Sword
csword = equip(68,84,0,34,0,70,26,0,0,14,'melee','Crystal Sword')

#T2 Crystal Sword
t2csword = equip(74,95,0,37,0,77,35,0,0,17,'melee','T2 Crystal Sword')

#Rail Gun
rgun = equip(56,88,0,36,0,70,0,0,26,14,'gun','Rail Gun')

#T2 Rail Gun
t2rgun = equip(70,90,0,39,0,74,0,0,34,16,'gun','T2 Rail Gun')

#Crystal Bomb
cbomb = equip(62,86,0,35,0,70,0,26,0,14,'projectile','Crystal Bomb')

#T2 Crystal Bomb
t2cbomb = equip(66,97,0,38,0,77,0,38,0,14,'projectile','T2 Crystal Bomb')

#Concentrated Crystal Bomb
concbomb = equip(87,112,0,35,0,65,0,9,0,5,'projectile','Concentrated Crystal Bomb')

#Split Crystal Bomb
scbomb = equip(55,87,0,23,0,79,0,84,0,83,'projectile','Split Crystal Bomb')

#Chain Blade
chain = equip(72,88,0,33,0,60,30,0,0,10,'melee','Chain Blade')

#T2 Chain Blade
t2chain = equip(78,94,0,37,0,72,37,0,0,10,'melee','T2 Chain Blade')

#Scythe
scythe = equip(76,92,0,31,0,60,40,0,0,10,'melee','Scythe')

#T2 Scythe
t2scythe = equip(80,101,0,38,0,75,41,0,0,10,'melee','T2 Scythe')

#Void Sword
void = equip(90,128,0,28,0,60,20,0,0,5,'melee','Void Sword')

#Rift Gun
rift = equip(60,65,0,85,0,50,0,0,85,5,'gun','Rift Gun')

#Core Ctaff
cstaff = equip(45,55,0,55,0,75,130,0,0,50,'melee','Core Staff')

#Void Axe
vaxe = equip(60,90,0,39,0,70,32,0,0,15,'melee','Void Axe')

#Void Bow
vbow = equip(5,125,0,48,0,70,0,65,0,20,'projectile','Void Bow')

#Void Bow with Laser Sight
vbowls = copy.copy(vbow)
vbowls.modslot([lsight])

#Void Bow with Poisoned Tip
vbowpt = copy.copy(vbow)
vbowpt.modslot([ptip])

#Havoc Launcher
hlauncher = equip(50,60,0,50,0,50,0,0,50,50,'gun','Havoc Launcher')

#Q15
q15 = equip(82,95,0,42,0,120,0,0,33,21,'gun','Q15')

# Duble Barrel Sniper Rifle
dbarrel = equip(89,91,0,83,0,0,0,0,0,0,'gun','Double Barrel')

##########
##Armors##
##########

#Titan Armor
titan = equip(0,0,40,0,68,55,0,0,0,40,'armor','Titan Armor')

#Hellforge Armor
hf = equip(0,0,105,0,55,65,0,0,0,50,'armor','Hellforge Armor')

#Dark Legion Armor
dl = equip(0,0,51,0,90,65,0,0,0,50,'armor','Dark Legion Armor')

#SG1 Armor
sg1 = equip(0,0,70,0,75,65,0,0,0,90,'armor','SG1 Armor')

###########
###Miscs###
###########

#Crystal Ring
cring = equip(0,0,0,5,5,0,8,8,8,18,'misc','Crystal Ring')

#Amulet
Amulet = equip(0,0,0,5,5,0,12,12,12,14,'misc','Amulet')

#Aeon Amulet
aeon = equip(0,0,0,6,6,0,25,25,25,25,'misc','Aeon Amulet')

#Prime Amulet
prime = equip(0,0,0,4,4,0,30,30,30,30,'misc','Prime Amulet')

#Orphic Amulet
orphic = equip(0,0,0,10,10,0,50,50,50,-25,'misc','Orphic Amulet')

#Inferno Amulet
inferno = equip(0,0,0,8,8,0,40,40,40,40,'misc','Inferno Amulet')

#Droid Drone
droid = equip(0,0,0,9,-2,0,40,40,40,-40,'misc','Droid Drone')

#Recon Drone
recon = equip(0,0,0,-2,9,0,-30,-30,-30,60,'misc','Recon Drones')

#Nerve Gauntlet
nerve = equip(0,0,0,6,6,0,40,50,40,25,'misc','Nerve Gauntlet')

#Core Shield
shield = equip(0,0,10,0,7,0,25,25,25,55,'misc','Core Shield')

#Bio Spinal Enhancer
biospine = equip(0,0,0,1,1,0,65,65,65,65,'misc','Bio Spinal Enhancer')

#Scout Drone
scout = equip(0,0,0,32,5,0,30,50,30,30,'misc','Scout Drone')

#Projector Bots
pbot = equip(0,0,0,25,10,0,5,40,15,40,'misc','Projector Bots')
