#Main Optimization Program
#Optimizes the stats of currently equipped weapon
#FUNCTIONS ONLY, FOR USE, USE legacyoptimization2.py
###########################################################################
#imports modules
############################################################################
import copy
import numpy
import legacychance


###########################################################################
#user defined functions
###########################################################################
#Optimization functions
#takes a bunch of stats and optimizes avtratio

#This function optimizes p1 hp by finding a maximum rating(local or global)
#using golden ratio search and distributing the rest of the stats evenly
#among acc and dod
#atype ='standard', 'quick','aimed', 'takecover'
def opthp(p1,p2list,weight,minhp,maxhp,atype = 'standard'):
    ###total distributable stats
    tstats = 171
    #initial values
    hp1 = minhp
    hp4 = maxhp
    hp3 = (hp4-hp1)*(2.0/(1+numpy.sqrt(5))) + hp1
    hp2 = hp4 - hp3 + hp1
    #creates an array of hp
    hplist = numpy.array([hp1,hp2,hp3,hp4])

    #evalutes the maximum using golden ratio
    while abs(hp1 - hp4)>2:
        #calculates statpoints in each hp in an array
        hps = (hplist-10-(hplist%5))/5

        #total distributable stat points left
        tstatsleft = tstats - hps

        #distributes the rest of the stat points into acc and dodge evenly
        #with more to acc if uneven
        accs = numpy.empty(len(hps),dtype=int)
        dods = numpy.empty(len(hps),dtype=int)
        for i in range(4):
            accs[i] = tstatsleft[i]/2
            dods[i] = tstatsleft[i]/2
            if tstatsleft[i]%2 == 1:
                accs[i] += 1
        
        #creates a list of player object for each stats
        p1list = numpy.array([copy.copy(p1) for i in range(4)])
        for i in range(len(p1list)):
            p1list[i].speed = 60
            p1list[i].hp = hplist[i]
            p1list[i].acc = accs[i]+14
            p1list[i].dod = dods[i]+14
            

        #maximum is between hp2 and hp4
        rate1 = legacychance.rating(p1list[1],p2list,weight)[0]
        rate2 = legacychance.rating(p1list[2],p2list,weight)[0]
        if  rate1 < rate2:
            hp1 = hp2
            hp2 = hp3
            hp3 = hp4 + hp1 - hp2
        #maximum is between hp1 and hp3
        else:
            hp4 = hp3
            hp3 = hp2
            hp2 = hp4 - hp3 + hp1
        hplist = numpy.array([hp1,hp2,hp3,hp4])

    #creates player object for all possible max hp including boundary
    #calculates statpoints in each hp in an array
    hplist[0] = minhp
    hplist[3] = maxhp
    hplist[1] = (hplist[1] + hplist[2])/2.0
    hplist[2] = copy.copy(hplist[1])
    hps = (hplist-10-(hplist%5))/5
    hps[2] += 1
    hplist = hps*5+10

    #total distributable stat points left
    tstatsleft = tstats - hps


    #distributes the rest of the stat points into acc and dodge evenly
    #with more to acc if uneven
    accs = numpy.empty(len(hps),dtype=int)
    dods = numpy.empty(len(hps),dtype=int)
    for i in range(4):
        accs[i] = tstatsleft[i]/2
        dods[i] = tstatsleft[i]/2
        if tstatsleft[i]%2 == 1:
            accs[i] += 1
    
    #creates a list of player object for each stats and calculates
    #the rating for each and returns the maximum
    p1list = numpy.array([copy.copy(p1) for i in range(4)])
    ratings = numpy.empty(4,dtype=float)
    maxim = [0,copy.copy(p1)]
    for i in range(len(p1list)):
        p1list[i].speed = 60
        p1list[i].hp = int(hplist[i])
        p1list[i].acc = accs[i]+14
        p1list[i].dod = dods[i]+14
        
        #attack type
        if atype == 'standard':
            p1list[i].standard()
        elif atype == 'quick':
            p1list[i].quick()
        elif atype == 'aimed':
            p1list[i].aimed()
        elif atype == 'takecover':
            p1list[i].takecover()
        
        #calculates ratings of each stats
        ratings[i] = legacychance.rating(p1list[i],p2list,weight)[0]
        #calculates the maximum
        if maxim[0]<ratings[i]:
            maxim[0] = ratings[i]
            maxim[1] = p1list[i]
            
    #returns stats with maximum legacychance.rating
    return maxim[1]

#This function optimizes p1 speed by finding a maximum rating(local or global)
#using golden ratio search and distributing the rest of the stats evenly
#among acc and dod
def optspeed(p1,p2list,weight,minspeed,maxspeed,atype='standard'):
    ###total distributable stats
    tstats = 171
    #initial values
    speed1 = minspeed
    speed4 = maxspeed
    speed3 = (speed4-speed1)*(2.0/(1+numpy.sqrt(5))) + speed1
    speed2 = speed4 - speed3 + speed1
    #creates an array of hp
    speedlist = numpy.array([speed1,speed2,speed3,speed4])

    #evalutes the maximum using golden ratio
    while abs(speed1 - speed4)>2:
        #calculates statpoints used for each speed in an array
        speeds = (speedlist-60-(p1.speed%5))/5

        #total distributable stat points left
        tstatsleft = tstats - speeds - (p1.hp-10)/5

        #distributes the rest of the stat points into acc and dodge evenly
        #with more to acc if uneven
        accs = numpy.empty(len(speeds),dtype=int)
        dods = numpy.empty(len(speeds),dtype=int)
        for i in range(4):
            accs[i] = tstatsleft[i]/2
            dods[i] = tstatsleft[i]/2
            if tstatsleft[i]%2 == 1:
                accs[i] += 1
        
        #creates a list of player object for each stats
        p1list = numpy.array([copy.copy(p1) for i in range(4)])
        for i in range(len(p1list)):
            p1list[i].speed = speedlist[i]
            p1list[i].acc = accs[i]+14
            p1list[i].dod = dods[i]+14


        #maximum is between hp2 and hp4
        rate1 = legacychance.rating(p1list[1],p2list,weight)[0]
        rate2 = legacychance.rating(p1list[2],p2list,weight)[0]
        if (rate1<rate2):
            speed1 = speed2
            speed2 = speed3
            speed3 = speed4 + speed1 - speed2
        #maximum is between hp1 and hp3
        else:
            speed4 = speed3
            speed3 = speed2
            speed2 = speed4 - speed3 + speed1
        speedlist = numpy.array([speed1,speed2,speed3,speed4])

    #creates player object for all possible max hp including boundary
    #calculates statpoints in each hp in an array
    speedlist[0] = minspeed
    speedlist[3] = maxspeed
    speedlist[1] = (speedlist[1] + speedlist[2])/2.0
    speedlist[2] = copy.copy(speedlist[1])
    speeds = (speedlist-60-(speedlist%5))/5
    speeds[2] += 1
    speedlist = speeds*5+60

    #total distributable stat points left
    tstatsleft = tstats - speeds - (p1.hp-10)/5


    #distributes the rest of the stat points into acc and dodge evenly
    #with more to acc if uneven
    accs = numpy.empty(len(speeds),dtype=int)
    dods = numpy.empty(len(speeds),dtype=int)
    for i in range(4):
        accs[i] = tstatsleft[i]/2
        dods[i] = tstatsleft[i]/2
        if tstatsleft[i]%2 == 1:
            accs[i] += 1
    
    #creates a list of player object for each stats and calculates
    #the rating for each and returns the maximum
    p1list = numpy.array([copy.copy(p1) for i in range(4)])
    ratings = numpy.empty(4,dtype=float)
    maxim = [0,copy.copy(p1)]
    for i in range(len(p1list)):
        p1list[i].speed = int(speedlist[i])
        p1list[i].acc = accs[i]+14
        p1list[i].dod = dods[i]+14
        
        #calculates rating of each stats
        ratings[i] = legacychance.rating(p1list[i],p2list,weight)[0]
        #calculates the maximum
        if maxim[0]<ratings[i]:
            maxim[0] = ratings[i]
            maxim[1] = p1list[i]
            
    #returns stats with maximum rating
    return maxim[1]

#This function optimizes the acc and dod stats using golden ratio search
#and finds the combination with highest rating and returns it
def optaccdod(p1,p2list,weight,atype='standard'):
    ###total distributable stats
    tstats = 171
    #total stats left
    tstatsleft = tstats-(p1.hp-10)/5-(p1.speed-60)/5
    #minimum acc to optimize from
    minacc = 14
    #maximum acc to optimize from
    maxacc = 14+tstatsleft
    #initial values
    acc1 = minacc
    acc4 = maxacc
    acc3 = (acc4-acc1)*(2.0/(1+numpy.sqrt(5))) + acc1
    acc2 = acc4 - acc3 + acc1
    #creates an array of acc and dod
    acclist = numpy.array([acc1,acc2,acc3,acc4])
    dodlist = tstatsleft+14 - (acclist-14)


    #evalutes the maximum using golden ratio
    while abs(acc1 - acc4)>1:
        #creates a list of player object for each stats
        p1list = numpy.array([copy.copy(p1) for i in range(4)])
        for i in range(len(p1list)):
            p1list[i].acc = acclist[i]
            p1list[i].dod = dodlist[i]
            

        #maximum is between hp2 and hp4
        rate1 = legacychance.rating(p1list[1],p2list,weight)[0]
        rate2 = legacychance.rating(p1list[2],p2list,weight)[0]
        if (rate1 < rate2):
            acc1 = acc2
            acc2 = acc3
            acc3 = acc4 + acc1 - acc2
        #maximum is between hp1 and hp3
        else:
            acc4 = acc3
            acc3 = acc2
            acc2 = acc4 - acc3 + acc1
        acclist = numpy.array([acc1,acc2,acc3,acc4])
        dodlist = tstatsleft+14 - (acclist-14)

    #creates player object for all possible maximum for acc and dod including
    #boundary
    acclist[0] = minacc
    acclist[3] = maxacc
    acclist[1] = int((acclist[1] + acclist[2])/2.0)
    acclist[2] = copy.copy(acclist[1])
    acclist[2] += 1
    #converts acclist to int and calculates dodlist
    temp = numpy.empty(4,dtype=int)
    for i in range(4):
        temp[i] = acclist[i]
    acclist = temp
    dodlist = tstatsleft+14 - (acclist-14)
    
    #creates a list of player object for each stats and calculates
    #the rating for each and returns the maximum
    p1list = numpy.array([copy.copy(p1) for i in range(4)])
    ratings = numpy.empty(4,dtype=float)
    maxim = [0,copy.copy(p1)]
    for i in range(len(p1list)):
        p1list[i].acc = acclist[i]
        p1list[i].dod = dodlist[i]
        
        #calculates rating of each stats
        ratings[i] = legacychance.rating(p1list[i],p2list,weight)[0]
        #calculates the maximum
        if maxim[0]<ratings[i]:
            maxim[0] = ratings[i]
            maxim[1] = p1list[i]
            
    #returns stats with maximum rating
    return maxim[1]

#This function optimizes stats quickly for different attack types
def quickopt(p1,p2list,weight,minhp=260,maxhp=360,minspeed=60,maxspeed=180):
    #creates a list of attack types to optimize from and empty plist
    #and pratings to store data in
    attacktype = ['standard','aimed','takecover']
    plist = []
    pratings = []
    #creates maximum rating array
    maximum = [0,copy.copy(p1),'standard']
    #optimizes for each attack type and calculates which attack type
    #has the maximum rating
    for k in attacktype:
        p1.atype = k
        player = opthp(p1,p2list,weight,minhp,maxhp,atype = k)
        player = optspeed(player,p2list,weight,minspeed,maxspeed,atype = k)
        player = optaccdod(player,p2list,weight,atype = k)
        plist.append(player)
        rate = legacychance.rating(player,p2list,weight)[0]
        pratings.append(rate)
        if maximum[0] < rate:
            maximum[0] = rate
            maximum[1] = player
            maximum[2] = k
    #returns player stats with maximum rating and attack type
    return maximum[1],maximum[2]

#Runs the quickopt Function only and returns results
def runquickopt(p1,p2list,weight,minhp=260,maxhp=360,minspeed=60,maxspeed=180):
    p1opt, attack = quickopt(p1,p2list,weight,minhp=minhp,maxhp=maxhp,\
                             minspeed=minspeed,maxspeed=maxspeed)
    print "Ratings vs Player List"
    print legacychance.rating(p1opt,p2list,weight)
    print p1opt, attack
    
############################################################################
