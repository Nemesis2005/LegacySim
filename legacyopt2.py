#Optimization
#Runs the Optimization program
#Adds Crystal Optimization
##############################################################################
#imports modules
import time
import sys
import copy

import legacyopt
import legacystats
import legacychance
import legacysim
from legacyplist import *

#import pp for parallelization
import pp
#############################################################################
#Constants
#############################################################################
#Crystal Optimization Constants
#Choose which crystals you'd like to have optimized for each equipment
#weapon crystals
wep1c = [pfire, amcrys]
wep2c = [pfire, amcrys]
#armor crystals
armc = [abyss, cabr, pvoid]
#misc crystal
#miscc = [ppink,pgreen,porange,pyellow,pair,amcrys]
miscc = [ppink, amcrys]

#Stats Optimization Constants
#minimum hp to optimize from
minhp = 350
#maximum hp to optimize from
maxhp = 500
#minimum speed to optimize from
minspeed = 60
#maximum speed to optimize from
maxspeed = 120

#Equipment Item Constants
#Items to be iterated on
wep = [vbowls,vbowpt,cstaff,void,rift,q15]
#wep = [cstaff,void,rift,q15]
arm = [dl, hf, sg1]
misc = [scout, pbot]

#Number of simulation per player
N = 100
#N = 20

tstats = 171

#Prints optimization progress for different item combination
printprogress = True

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
#player 1 stats - stats themselves are not important, this is simply
#for defining initial stats
##############################################################################
#Please include abilities too
hp = 360
acc= 107
dod = 14
speed = 100
mskill = 450
pskill = 450
gskill = 450
dskill = 450

#create variable for player 1 stats
#choose attack type as well - standard,aimed,takecover
p1 = legacystats.pstats(hp,acc,dod,speed,mskill,pskill,gskill,dskill,mind = 5,maxd = 5,\
            armor = 5, weap1 = void4f, weap2 = void4f,arm = dl4v,\
            misc1 = orphic4o,misc2 = orphic4o,atype = "aimed")


##############################################################################
#User-Defined Function
#############################################################################
#This function optimizes which crystals are the best combination among the
#ones selected and optimizes the stats that go with it
def crystalopt(p1,p2list,weight, w1crystal,w2crystal,acrystal,mcrystal,\
                minhp = 260,maxhp = 360,minspeed = 60, maxspeed = 180):
    #creates a list of equipment for player1
    p1equip = p1.equip()
    #creates a copy of p1
    p1copy = copy.deepcopy(p1)
    
    #sets the current crystals equipped to none
    noc = []
    n = len(p1equip)
    for i in range(n):
        p1equip[i].socket(noc)
    p1copy.cweap1(p1equip[0])
    p1copy.cweap2(p1equip[1])
    p1copy.carm(p1equip[2])
    p1copy.cmisc1(p1equip[3])
    p1copy.cmisc2(p1equip[4])

    
    #Optimizes the crystal of each equipment
    p1copy,atype = weap1crystopt(p1copy,p2list,weight,w1crystal,\
                                  minhp,maxhp,minspeed,maxspeed)[1:]
    p1copy,atype = weap2crystopt(p1copy,p2list,weight,w1crystal,
                                  minhp,maxhp,minspeed,maxspeed)[1:]
    p1copy,atype = armcrystopt(p1copy,p2list,weight,acrystal,
                                minhp,maxhp,minspeed,maxspeed)[1:]
    p1copy,atype = misccrystopt(p1copy,p2list,weight,mcrystal,
                                 minhp,maxhp,minspeed,maxspeed)[1:]
    #returns optimized equipment and attack type
    return p1copy,atype

#This function optimizes which crystals are the best combination among the
#ones selected for weap1 and optimizes the stats at the same time
def weap1crystopt(p1,p2list,weight,w1crystal,minhp,maxhp,minspeed,maxspeed):
    #creates a list of equipment for player1
    p1equip = p1.equip()
    #creates a list of 4 things to put crystals in
    weap1c = [0,0,0,0]
    #length of crystal list
    n = len(w1crystal)
    #creates a copy of p1
    p1copy = copy.deepcopy(p1)
    #creates maximum list
    maximum = [0.0, copy.deepcopy(p1),'standard']

    #sets up parallel programming
    jobs = []
    #stores result here
    result = []
    modules = ("math","copy","numpy","legacyopt","random","legacychance",\
               "legacystats")
    depfunc = (legacyopt.opthp,legacyopt.optspeed,legacyopt.optaccdod)
    
    #optimizes crystal for weap1
    #iterate over each crystal for each slot
    for k1 in range(n):
        weap1c[0] = w1crystal[k1]
        for k2 in range(k1,n):
            weap1c[1] = w1crystal[k2]
            for k3 in range(k2,n):
                weap1c[2] = w1crystal[k3]
                for k4 in range(k3,n):
                    weap1c[3] = w1crystal[k4]
                    p1equip[0].socket(weap1c)
                    p1copy.cweap1(p1equip[0])
                    
                    #optimizes the stats for crystal combination
                    jobs.append(job_server.submit(legacyopt.quickopt,\
                    (p1copy,p2list,weight,minhp,maxhp,minspeed,maxspeed),\
                    depfuncs = depfunc,modules = modules))
    K = len(jobs)
    #runs the quickopt parallelly
    for job in jobs:
        result.append(job())

    for k in range(K):
    #calculates rating for each combination
        p1copy = result[k][0]
        atype = result[k][1]
        rate = legacychance.rating(p1copy,p2list,weight)[0]
        #stores maximum value
        if maximum[0] < rate:
            maximum[0] = rate
            maximum[1] = copy.deepcopy(p1copy)
            maximum[2] = atype
    return maximum

#This function optimizes which crystals are the best combination among the
#ones selected for weap2 and optimizes the stats at the same time
def weap2crystopt(p1,p2list,weight,w2crystal,minhp,maxhp,minspeed,maxspeed):
    #creates a list of equipment for player1
    p1equip = p1.equip()
    #creates a list of 4 things to put crystals in
    weap2c = [0,0,0,0]
    #length of crystal list
    n = len(w2crystal)
    #creates a copy of p1
    p1copy = copy.deepcopy(p1)
    #creates maximum list
    maximum = [0.0, copy.deepcopy(p1copy),'standard']

    #sets up parallel programming
    jobs = []
    #stores result here
    result = []
    modules = ("math","copy","numpy","legacyopt","random","legacychance",\
               "legacystats")
    depfunc = (legacyopt.opthp,legacyopt.optspeed,legacyopt.optaccdod)
    
    #optimizes crystal for weap2
    for k1 in range(n):
        weap2c[0] = w2crystal[k1]
        for k2 in range(k1,n):
            weap2c[1] = w2crystal[k2]
            for k3 in range(k2,n):
                weap2c[2] = w2crystal[k3]
                for k4 in range(k3,n):
                    weap2c[3] = w2crystal[k4]
                    p1equip[1].socket(weap2c)
                    p1copy.cweap2(p1equip[1])

                    #optimizes the stats for crystal combination
                    jobs.append(job_server.submit(legacyopt.quickopt,\
                    (p1copy,p2list,weight,minhp,maxhp,minspeed,maxspeed),\
                    depfuncs = depfunc,modules = modules))
    K = len(jobs)
    #runs the quickopt parallelly
    for job in jobs:
        result.append(job())

    for k in range(K):
    #calculates rating for each combination
        p1copy = result[k][0]
        atype = result[k][1]
        rate = legacychance.rating(p1copy,p2list,weight)[0]
        #stores maximum value
        if maximum[0] < rate:
            maximum[0] = rate
            maximum[1] = copy.deepcopy(p1copy)
            maximum[2] = atype
    return maximum

#This function optimizes which crystals are the best combination among the
#ones selected for armor and optimizes the stats at the same time
def armcrystopt(p1,p2list,weight,acrystal,minhp,maxhp,minspeed,maxspeed):
    #creates a list of equipment for player1
    p1equip = p1.equip()
    #creates an empty list of crystals to put in
    armorc = [0,0,0,0]
    #length of crystal list
    n = len(acrystal)
    #creates a copy of p1
    p1copy = copy.deepcopy(p1)
    #creates maximum list
    maximum = [0.0, copy.deepcopy(p1copy),'standard']

    #sets up parallel programming
    jobs = []
    #stores result here
    result = []
    modules = ("math","copy","numpy","legacyopt","random","legacychance",\
               "legacystats")
    depfunc = (legacyopt.opthp,legacyopt.optspeed,legacyopt.optaccdod)
    
    #optimizes crystal for armor
    for k1 in range(n):
        armorc[0] = acrystal[k1]
        for k2 in range(k1,n):
            armorc[1] = acrystal[k2]
            for k3 in range(k2,n):
                armorc[2] = acrystal[k3]
                for k4 in range(k3,n):
                    armorc[3] = acrystal[k4]
                    p1equip[2].socket(armorc)
                    p1copy.carm(p1equip[2])

                    #optimizes the stats for crystal combination
                    jobs.append(job_server.submit(legacyopt.quickopt,\
                    (p1copy,p2list,weight,minhp,maxhp,minspeed,maxspeed),\
                    depfuncs = depfunc,modules = modules))
    K = len(jobs)
    #runs the quickopt parallelly
    for job in jobs:
        result.append(job())

    for k in range(K):
    #calculates rating for each combination
        p1copy = result[k][0]
        atype = result[k][1]
        rate = legacychance.rating(p1copy,p2list,weight)[0]
        #stores maximum value
        if maximum[0] < rate:
            maximum[0] = rate
            maximum[1] = copy.deepcopy(p1copy)
            maximum[2] = atype
    return maximum

#This function optimizes which crystals are the best combination among the
#ones selected for armor and optimizes the stats at the same time
def misccrystopt(p1,p2list,weight,mcrystal,minhp,maxhp,minspeed,maxspeed):
    #creates a list of equipment for player1
    p1equip = p1.equip()
    #creates a list of 4 things to put crystals in
    misc1c = [0,0,0,0]
    misc2c = [0,0,0,0]
    #length of crystal list
    n = len(mcrystal)
    #creates a copy of p1
    p1copy = copy.deepcopy(p1)
    #creates maximum list
    maximum = [0.0, copy.deepcopy(p1copy),'standard']

    #sets up parallel programming
    jobs = []
    #stores result here
    result = []
    modules = ("math","copy","numpy","legacyopt","random","legacychance",\
               "legacystats")
    depfunc = (legacyopt.opthp,legacyopt.optspeed,legacyopt.optaccdod)
    
    #optimizes crystal for misc1
    for k1 in range(n):
        misc1c[0] = mcrystal[k1]
        for k2 in range(k1,n):
            misc1c[1] = mcrystal[k2]
            for k3 in range(k2,n):
                misc1c[2] = mcrystal[k3]
                for k4 in range(k3,n):
                    misc1c[3] = mcrystal[k4]
                    #sockets crystal
                    p1equip[3].socket(misc1c)
                    p1copy.cmisc1(p1equip[3])

                    #optimizes the stats for crystal combination
                    jobs.append(job_server.submit(legacyopt.quickopt,\
                    (p1copy,p2list,weight,minhp,maxhp,minspeed,maxspeed),\
                    depfuncs = depfunc,modules = modules))
    K = len(jobs)
    #runs the quickopt parallelly
    for job in jobs:
        result.append(job())

    for k in range(K):
    #calculates rating for each combination
        p1copy = result[k][0]
        atype = result[k][1]
        rate = legacychance.rating(p1copy,p2list,weight)[0]
        #stores maximum value
        if maximum[0] < rate:
            maximum[0] = rate
            maximum[1] = copy.deepcopy(p1copy)
            maximum[2] = atype
    #resets results
    result = []
    #sets stats to maximum crystal
    p1copy = copy.deepcopy(maximum[1])
    #optimizes crystal for misc1
    for k1 in range(n):
        misc2c[0] = mcrystal[k1]
        for k2 in range(k1,n):
            misc2c[1] = mcrystal[k2]
            for k3 in range(k2,n):
                misc2c[2] = mcrystal[k3]
                for k4 in range(k3,n):
                    misc2c[3] = mcrystal[k4]
                    #sockets crystal
                    p1equip[4].socket(misc2c)
                    p1copy.cmisc2(p1equip[4])

                    #optimizes the stats for crystal combination
                    jobs.append(job_server.submit(legacyopt.quickopt,\
                    (p1copy,p2list,weight,minhp,maxhp,minspeed,maxspeed),\
                    depfuncs = depfunc,modules = modules))
    K = len(jobs)
    #runs the quickopt parallelly
    for job in jobs:
        result.append(job())

    for k in range(K):
    #calculates rating for each combination
        p1copy = result[k][0]
        atype = result[k][1]
        rate = legacychance.rating(p1copy,p2list,weight)[0]
        #stores maximum value
        if maximum[0] < rate:
            maximum[0] = rate
            maximum[1] = copy.deepcopy(p1copy)
            maximum[2] = atype
    #returns crystal comb with maximum rating
    return maximum

#This function runs the crystalopt program and returns the results
def runcrystalopt(p1,p2list,weight,wep1c,wep2c,armc,miscc,\
                  minhp=260,maxhp=360,minspeed=60,maxspeed=180):
    #optimizes crystals for player 1
    p1opt, attack = crystalopt(p1,p2list,weight,wep1c,wep2c,\
                                armc,miscc,minhp,maxhp,minspeed,maxspeed)
    print legacychance.rating(p1opt, p2list,weight)
    print p1opt, attack
    print ""
    print "Crystals: "
    #prints the equipment and their crystals
    for i in range(5):
        print p1opt.equip()[i].name
        print p1opt.equip()[i].crystaln()


#This function optimizes equipment by optimizing simrating and going through
#each possible iteration of equipments
#wep,arm,misc are all lists and N is the number of simulations per player
def equipopt(p1,p2list,weight,N,wep,arm,misc,w1crys,w2crys,acrys,mcrys,
             minhp=260,maxhp=360,minspeed=60,maxspeed=180,
             printprogress = False):
    #creates a copy of p1 to do operation in
    p1copy = copy.deepcopy(p1)
    #calculates the length of each list
    n1 = len(wep)
    n2 = len(arm)
    n3 = len(misc)
    #creates a variable to store strongest optimization and rating
    p1opt = copy.deepcopy(p1)
    rating = 0.0
    ratinglist = []
    atypereturn = "normal"

    #Iterates through each items and equips it
    for i1 in range(n1):
        p1copy.cweap1(wep[i1])
        for i2 in range(i1,n1):
            p1copy.cweap2(wep[i2])
            for j in range(n2):
                p1copy.carm(arm[j])
                for k1 in range(n3):
                    p1copy.cmisc1(misc[k1])
                    for k2 in range(k1,n3):
                        p1copy.cmisc2(misc[k2])
                        
                        #optimizes crystal for current iteration
                        p1copy,atype = crystalopt(p1copy,p2list,weight,w1crys,\
                                                   w2crys,acrys,mcrys,minhp,\
                                                   maxhp,minspeed,maxspeed)
                        #simulates N times and chooses the strongest combination
                        tempperc,tempwinperc = legacysim.simrating(p1copy,p2list,\
                                                N,weight)
                        if tempperc>rating:
                            p1opt = copy.deepcopy(p1copy)
                            rating = tempperc
                            ratinglist = tempwinperc
                            atypereturn = atype
                        #Prints results of current iteration if printprogress
                        #is true
                        if printprogress:
                            print "Win Rate", tempperc,tempwinperc
                            print p1copy,atype
                            print "Equipment and Crystals"
                            for i in range(5):
                                print p1copy.equip()[i].name
                                mods = p1copy.equip()[i].get_mod_name()
                                if mods:
                                    print mods
                                print p1copy.equip()[i].crystaln()
                            print ""
    return [rating,ratinglist,p1opt,atypereturn]

#Runs equipment optimization
def runequipopt(p1,p2list,weight,N,wep,arm,misc,w1crys,w2crys,acrys,mcrys,\
                minhp=260,maxhp=360,minspeed=60,maxspeed=180, printprogress = False):
    #optimizes equipment for player 1 against p2list
    result = equipopt(p1, p2list, weight, N, wep, arm, misc, w1crys, w2crys,
                     acrys, mcrys, minhp, maxhp, minspeed, maxspeed,
                      printprogress = printprogress)
    print "------------------"
    print "FINAL RESULTS"
    print "Win Rate", result[0], result[1]
    p1opt = result[2]
    print p1opt, result[3]
    print "Equipment and Crystals "
    #prints the equipment and their crystals
    for i in range(5):
        print p1opt.equip()[i].name
        mods = p1opt.equip()[i].get_mod_name()
        if mods:
            print mods
        print p1opt.equip()[i].crystaln()

                        
##############################################################################
#Main Program
##############################################################################
def main(equipopt_is_on = True, crystalopt_is_on = True, printprogress = False):
    #Runs Equipment Optimization Program
    startt = time.time()
    print "legacyopt2: Starting main optimization..."
    if equipopt_is_on:
        runequipopt(p1,plist,w,N,wep,arm,misc,wep1c,wep2c,armc,miscc,\
                    minhp,maxhp,minspeed,maxspeed, printprogress)
    elif crystalopt_is_on:
        #Runs crystalopt only
        runcrystalopt(p1,plist,w,wep1c,wep2c,armc,miscc,minhp,maxhp,minspeed,maxspeed)
    else:
        #quickopt only
        legacyopt.runquickopt(p1,plist,w,minhp,maxhp,minspeed,maxspeed)
    print "Total time is", time.time()-startt


if __name__ == "__main__":
    #sets up parallel programming by creating servers
    ppservers = ()
    if len(sys.argv) > 1:
        ncpus = int(sys.argv[1])
        # Creates jobserver with ncpus workers
        job_server = pp.Server(ncpus, ppservers=ppservers)
    else:
        # Creates jobserver with automatically detected number of workers
        job_server = pp.Server(ppservers=ppservers)

    
    main(equipopt_is_on = True, crystalopt_is_on = True,
         printprogress = printprogress)
