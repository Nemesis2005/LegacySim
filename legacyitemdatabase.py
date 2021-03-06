#LegacyItemDatabase
#Database For Items
#############################################################################
#Import Modules
#############################################################################
from legacyequip import *
import copy

############################################################################
#Item Database
############################################################################

##########
##Armors##
##########

#Titan Armor
titan4v = copy.copy(titan)
titan4v.socket([pvoid,pvoid,pvoid,pvoid])
titan4w = copy.copy(titan)
titan4w.socket([pwater,pwater,pwater,pwater])

#Hellforge Armor
hf4v = copy.copy(hf)
hf4v.socket([pvoid,pvoid,pvoid,pvoid])
hf4w = copy.copy(hf)
hf4w.socket([pwater,pwater,pwater,pwater])
hf4abyss = copy.copy(hf)
hf4abyss.socket([abyss,abyss,abyss,abyss])
hf3ab1v = copy.copy(hf)
hf3ab1v.socket([abyss,abyss,abyss,pvoid])

#Dark Legion Armor
dl4v = copy.copy(dl)
dl4v.socket([pvoid,pvoid,pvoid,pvoid])
dl4w = copy.copy(dl)
dl4w.socket([pwater,pwater,pwater,pwater])
dl4aeon = copy.copy(dl)
dl4aeon.socket([aeoncrys,aeoncrys,aeoncrys,aeoncrys])
dl4abyss = copy.copy(dl)
dl4abyss.socket([abyss,abyss,abyss,abyss])

#SG1 Armor
sg14v = copy.copy(sg1)
sg14v.socket([pvoid,pvoid,pvoid,pvoid])
sg14w = copy.copy(sg1)
sg14w.socket([pwater,pwater,pwater,pwater])
sg14p = copy.copy(sg1)
sg14p.socket([ppink,ppink,ppink,ppink])
sg14abyss = copy.copy(sg1)
sg14abyss.socket([abyss,abyss,abyss,abyss])
sg12v1p1ab = copy.copy(sg1)
sg12v1p1ab.socket([pvoid,ppink,pvoid,abyss])

###########
##Weapons##
###########

#Split Crystal Bombs
scbomb4ammy = copy.copy(scbomb)
scbomb4ammy.socket([amcrys,amcrys,amcrys,amcrys])

#T2 Scythes
t2scythe4f = copy.copy(t2scythe)
t2scythe4f.socket([pfire,pfire,pfire,pfire])

#Void Swords
void4f = copy.copy(void)
void4f.socket([pfire,pfire,pfire,pfire])

#Rifts
rift4a = copy.copy(rift)
rift4a.socket([pair,pair,pair,pair])
rift4f = copy.copy(rift)
rift4f.socket([pfire,pfire,pfire,pfire])
rift4amcrys = copy.copy(rift)
rift4amcrys.socket([amcrys,amcrys,amcrys,amcrys])
rift2f2amcrys = copy.copy(rift)
rift2f2amcrys.socket([pfire,pfire,amcrys,amcrys])

#Core Staff
cstaff4o = copy.copy(cstaff)
cstaff4o.socket([porange,porange,porange,porange])
cstaff4amcrys = copy.copy(cstaff)
cstaff4amcrys.socket([amcrys,amcrys,amcrys,amcrys])
cstaff2o2pr = copy.copy(cstaff)
cstaff2o2pr.socket([porange,porange,primecrys,primecrys])

#Void Axe
vaxe4f = copy.copy(vaxe)
vaxe4f.socket([pfire,pfire,pfire,pfire])

#Void Bow
vbow4amcrys = copy.copy(vbow)
vbow4amcrys.socket([amcrys,amcrys,amcrys,amcrys])

#Void Bow + Laser Sight
vbowls4amcrys = copy.copy(vbowls)
vbowls4amcrys.socket([amcrys,amcrys,amcrys,amcrys])

#Void Bow + Poisoned Tip
vbowpt4amcrys = copy.copy(vbowpt)
vbowpt4amcrys.socket([amcrys,amcrys,amcrys,amcrys])
vbowpt3amcrys1f = copy.copy(vbowpt)
vbowpt4amcrys.socket([amcrys,amcrys,amcrys,pfire])

#Q15
q154f = copy.copy(q15)
q154f.socket([pfire,pfire,pfire,pfire])
q154amcrys = copy.copy(q15)
q154amcrys.socket([amcrys,amcrys,amcrys,amcrys])

# Double Barrel Sniper
dbarrel4f = copy.copy(dbarrel)
dbarrel4f.socket([pfire,pfire,pfire,pfire])
dbarrel3pr1f = copy.copy(dbarrel)
dbarrel3pr1f.socket([primecrys,primecrys,primecrys,pfire])


###########
###Miscs###
###########

#Orphic
orphic4o = copy.copy(orphic)
orphic4o.socket([porange,porange,porange,porange])
orphic4g = copy.copy(orphic)
orphic4g.socket([pgreen,pgreen,pgreen,pgreen])

#Inferno
inferno4o = copy.copy(inferno)
inferno4o.socket([porange,porange,porange,porange])
inferno4g = copy.copy(inferno)
inferno4g.socket([pgreen,pgreen,pgreen,pgreen])
inferno4p = copy.copy(inferno)
inferno4p.socket([ppink,ppink,ppink,ppink])

#Bio Spinal Enhancer
biospine4o = copy.copy(biospine)
biospine4o.socket([porange,porange,porange,porange])
biospine4g = copy.copy(biospine)
biospine4g.socket([pgreen,pgreen,pgreen,pgreen])
biospine4y = copy.copy(biospine)
biospine4y.socket([pyellow,pyellow,pyellow,pyellow])
biospine4p = copy.copy(biospine)
biospine4p.socket([ppink,ppink,ppink,ppink])
biospineryu = copy.copy(biospine)
biospineryu.socket([ppink,pgreen,amcrys,ppink])

#Scout Drone
scout4o = copy.copy(scout)
scout4o.socket([porange,porange,porange,porange])
scout4y = copy.copy(scout)
scout4y.socket([pyellow,pyellow,pyellow,pyellow])
scout4p = copy.copy(scout)
scout4p.socket([ppink,ppink,ppink,ppink])
scout4a = copy.copy(scout)
scout4a.socket([pair,pair,pair,pair])
scout4amcrys = copy.copy(scout)
scout4amcrys.socket([amcrys,amcrys,amcrys,amcrys])
scout3amcrys1a = copy.copy(scout)
scout3amcrys1a.socket([amcrys,amcrys,amcrys,pair])

#Projector Bots
pbot4o = copy.copy(pbot)
pbot4o.socket([porange,porange,porange,porange])
pbot4y = copy.copy(pbot)
pbot4y.socket([pyellow,pyellow,pyellow,pyellow])
pbot4p = copy.copy(pbot)
pbot4p.socket([ppink,ppink,ppink,ppink])
pbot4w = copy.copy(pbot)
pbot4w.socket([pwater,pwater,pwater,pwater])
pbot4aeon = copy.copy(pbot)
pbot4aeon.socket([aeoncrys,aeoncrys,aeoncrys,aeoncrys])
                    

#define your custom equipment here
#Nemesis equipment
nscythe = copy.copy(t2scythe)
nscythe.socket([pfire, pfire, pfire, amcrys])
nvoid1 = copy.copy(void)
nvoid1.socket([pfire,pfire,pfire])
nvoid2 = copy.copy(void)
nvoid2.socket([pfire,pfire])
ntitan = copy.copy(titan)
ntitan.socket([pvoid])
ncring = copy.copy(cring)
ncring.socket([ppink,ppink,ppink,pwater])
ninferno = copy.copy(inferno)
ninferno.socket([porange,porange,porange])
norphic = copy.copy(orphic)
