import random

compwin=0
compint = 0
noofcard = random.randint(1,12)
while noofcard > 0:
    
    if (noofcard-1)%3 == 0:
     compint = 1
     noofcard-=compint
    else:
     compint = 2
     noofcard-=compint
    noofcard = noofcard - compint 
    print("num of cards left: ",noofcard)
    if noofcard <= 0:
        compwin = compwin + 1
    else:
        userinput = int(input("please put a number: "))
        if userinput > 2 or userinput < 1:
            while userinput > 2 or userinput < 1:
                userinput = int(input("please renter: "))
                if userinput == 1 or userinput == 2:
                    noofcard = noofcard - userinput
        else:
         noofcard = noofcard - userinput
    

if compwin > 0:
    print("computer wins")
else:
    print("player wins")