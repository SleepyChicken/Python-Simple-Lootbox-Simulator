import random

s = 0
a = 0
b = 0
c = 0 
selectMode = None
countS = 0
countA = 0
countB = 0
countC = 0

rate = []

def modeSelect(selectMode) :
    print('select mode')
    print('1.Roll n time')
    print('2.Roll until you get s rank')

    selectMode = int(input('Please select : '))

    if selectMode == 1 :
        mode1(s, a, b, c, countS, countA, countB, countC)
    elif selectMode == 2 :
        mode2(s, a, b, c, countS, countA, countB, countC)

def userInput(s,a,b,c) :
    s = float(input('Rank S rate (percentage) : '))
    a = float(input('Rank A rate (percentage) : '))
    b = float(input('Rank B rate (percentage) : '))
    c = 100 - s - a - b
    
    sumRate = s + a + b + c
   
    if sumRate != 100 : # if rate is more than 100 return to mode select
        print('Invalid Number')
        modeSelect()
   
    print('Rank C rate (percentage) : '+str(c))

    return s,a,b,c

def mode1(s, a, b, c, countS, countA, countB, countC) :
    rand = 0
    n = int(input('How many time ? : '))
        
    for i in range(n) :
        rand = random.randrange(1, int((100/s)+1))
        if 0 < rand <= ((100/s)*(s/100)) :
            countS = countS + 1
        elif ((100/s)*(s/100)) < rand <= ((100/s)*(a/100)) :
            countA = countA + 1
        elif ((100/s)*(a/100)) < rand <= ((100/s)*(b/100))+((100/s)*(a/100)) :
            countB = countB + 1
        elif ((100/s)*(b/100))+((100/s)*(a/100)) < rand <= ((100/s)*(c/100))+((100/s)*(b/100))+((100/s)*(a/100))+1 :
            countC = countC + 1

    print('You rolled rank S '+str(countS)+' time')   
    print('You rolled rank A '+str(countA)+' time')
    print('You rolled rank B '+str(countB)+' time')   
    print('You rolled rank C '+str(countC)+' time')

def mode2(s, a, b, c, countS, countA, countB, countC) : # roll until get s rank
    rand = 0
    
    while countS == 0 :
        rand = random.randrange(1, int((100/s)+1))
        if 0 < rand <= ((100/s)*(s/100)) : # break if s rank is rolled
            countS = countS + 1
            break
        elif ((100/s)*(s/100)) < rand <= ((100/s)*(a/100)) :
            countA = countA + 1
        elif ((100/s)*(a/100)) < rand <= ((100/s)*(b/100))+((100/s)*(a/100)) :
            countB = countB + 1
        elif ((100/s)*(b/100))+((100/s)*(a/100)) < rand <= ((100/s)*(c/100))+((100/s)*(b/100))+((100/s)*(a/100))+1 :
            countC = countC + 1

    print('Get rank S in '+str(countA + countB + countC)+' try')
    print('You rolled rank S '+str(countS)+' time')   
    print('You rolled rank A '+str(countA)+' time')
    print('You rolled rank B '+str(countB)+' time')   
    print('You rolled rank C '+str(countC)+' time')

rate = userInput(s,a,b,c)
s = rate[0]
a = rate[1]
b = rate[2]
c = rate[3]
modeSelect(selectMode)