# Author:  Duderman
# Version: 1.0
# Date:    4/28/18
import random
import time
from datetime import date

# ----------------Display build version and local time---------------------
today = date.today()
build_version = 1.0
current_time = time.asctime(time.localtime(time.time()))
print("\n\nBuild Version:", str(build_version), "\nTime:", str(current_time), "\n\n")
# -------------------------------------------------------------------------

#Global Scope
bankRoll = 0
currentPoint = 0
currentBets = []
rollState = 0
rollCount = 0
die1 = 0
die2 = 0
dice = 0
gamesToPlay = 10
totalComeOutWins = 0
totalComeOutLoss = 0
totalField = 0
totalFieldDouble = 0
totalPoint5 = 0
totalPoint6 = 0
totalPoint8 = 0

def printState():
    print("\nprintState(): bankRoll:", str(bankRoll), " rollState:", str(rollState), "rollCount:", str(rollCount))
    betlen = len(currentBets) / 2
    print("currentBets:", currentBets)
    print("Current Dice:", dice, "Die1:", die1, "Die2:", die2)
    print("ComeOutWins:", totalComeOutWins, "ComeOutLosses:", totalComeOutLoss, "TotalPoint5:", totalPoint5, "TotalPoint6:", totalPoint6, "TotalPoint8:", totalPoint8)
    print("TotalField:", totalField, "totalFieldDouble:", totalFieldDouble)
    print("currentBetsLen:", str(betlen), "currentPoint:", str(currentPoint), "\n")

def placeBets():
    #place bet strategy
    #current plan, field bet, place 5,6,8
    print("hold for placeBets()")
    
def addBet(betType, amount):
    global bankRoll, rollCount
    #add a bet to the bet array
    currentBets.append(betType)
    currentBets.append(amount)
    bankRoll = bankRoll - amount
    print("Added bet:", str(betType), ":", str(amount), "bankRoll:", bankRoll)

def takeDown(betName):
    #remove a bet and credit bankroll
    global currentBets,bankRoll
    
    i = 0
    while i < len(currentBets):
        if currentBets[i] == betName:
            #credit bet
            bankRoll = bankRoll + currentBets[i+1]
            print("Takedown: ", currentBets[i], "for", currentBets[i+1], "bankRoll:", bankRoll)
            
            #remove bet on next add bet
            currentBets[i] = "delete"
            currentBets[i+1] = 0
        i = i + 2
        
def payBets():
    #TODO loop thru currentBets, eval for win and calc payout
    #currentBets format is currentBets[0] currentBets[1] =  betType (place5, place4, field) and amount (10,20,100, etc) in pairs
    
    global bankRoll, currentBets, currentPoint, dice, rollState, totalComeOutLoss, totalComeOutWins, totalPoint5, totalPoint6, totalPoint8, totalField, totalFieldDouble, bankRoll
        
    #New single loop
    #Loop thru bets, pay and remove bets
    i = 0
    while i < len(currentBets):
        
        #print("Checking current bets:", currentBets[i], " at ", currentBets[i+1] )
           
        #pass bets
        if currentBets[i] == "pass":
            if rollState == 0:
                #Check for come out roll win
                if dice == 7 or dice == 11:
                    bankRoll = bankRoll + currentBets[i+1] * 2
                    print("pass line bet pays ", currentBets[i+1], "bankRoll:", bankRoll)
                    currentBets[i] = "delete"
                    currentBets[i+1] = 0
                    totalComeOutWins = totalComeOutWins + 1
                #Check for come out roll lose    
                if dice == 2 or dice == 3 or dice == 12:
                    print("pass line lose, lose bet", "bankRoll:", bankRoll)
                    currentBets[i] = "delete"
                    currentBets[i+1] = 0
                    totalComeOutLoss = totalComeOutLoss + 1
            #Check for point win
            if rollState == 1:
                if dice == currentPoint:
                  bankRoll = bankRoll + currentBets[i+1] * 2
                  print("pass line bet pays ", currentBets[i+1], "bankRoll:", bankRoll)
                  currentBets[i] = "delete"
                  currentBets[i+1] = 0
            #Check for point loss
                if dice == 7:
                    #kill all bets, prob should do delete 
                      currentBets[i] = "delete"
                      currentBets[i+1] = 0

            
        #Check for field win 3,4,9,10,11 1:2 pay, 2/12 2x pay
        if currentBets[i] == "field":
            if dice == 3 or dice == 4 or dice == 9 or dice == 10 or dice == 11:           
                bankRoll = bankRoll + (currentBets[i+1] * 2)
                print("field bet pays 1:1 ", currentBets[i+1] * 2, "bankRoll:", bankRoll)
                totalField = totalField + 1
            if dice == 2 or dice == 12:           
                bankRoll = bankRoll + currentBets[i+1] * 3
                print("2/12 field bet pays 2:1 ", currentBets[i+1] * 3, "bankRoll:", bankRoll)
                totalFieldDouble = totalFieldDouble + 1
            
            #Either way field bet comes down
            currentBets[i] = "delete"
            currentBets[i+1] = 0
        
        #Check for Place Wins, will come down automatically with 7-out
        if currentBets[i] == "place4" and dice == 4:
                bankRoll = bankRoll + currentBets[i+1] * .8
                print("Place 4 bet pays 9/5 ", currentBets[i+1] * .8, "bankRoll:", bankRoll)
        if currentBets[i] == "place10" and dice == 10:
                bankRoll = bankRoll + currentBets[i+1] * .8
                print("Place 10 bet pays 9/5 ", currentBets[i+1] * .8, "bankRoll:", bankRoll)
        if currentBets[i] == "place5" and dice == 5:
                bankRoll = bankRoll + currentBets[i+1] * .4
                print("Place 5 bet pays 7/5 ", currentBets[i+1] * .4, "bankRoll:", bankRoll)
                totalPoint5 = totalPoint5 + 1
        if currentBets[i] == "place9" and dice == 9:
                bankRoll = bankRoll + currentBets[i+1] * .4                
                print("Place 9 bet pays 7/5 ", currentBets[i+1] * .4, "bankRoll:", bankRoll)
        if currentBets[i] == "place6" and dice == 6:
                bankRoll = bankRoll + round(currentBets[i+1] * .1667,0)
                print("Place 6 bet pays 7/6 ", currentBets[i+1] * .1667, "bankRoll:", bankRoll)
                totalPoint6 = totalPoint6 + 1
        if currentBets[i] == "place8" and dice == 8:
                bankRoll = bankRoll + round(currentBets[i+1] * .1667, 0)
                print("Place 8 bet pays 7/6 ", currentBets[i+1] * .1667, "bankRoll:", bankRoll)
                totalPoint8 = totalPoint8 + 1

        if dice == 7: 
            #Every bet gets killed on 7
            currentBets[i] = "delete"
            currentBets[i+1] = 0
            
            
        #keep on looping, mofo
        i += 2   

    #Cycle thru and remove all delete bets        
    for item in currentBets[:]:
        if item == "delete":
            currentBets.remove(item)
        if item == 0:
            currentBets.remove(item)



    
def comeOutRoll():
    #TODO roll dice, eval for win/loss/point - not going to program pass line at this time (iron cross)
    global currentPoint, rollState
    rollState=0
    
    print("ComeOutRoll")
    rollDice()
    payBets()
    
    if dice == 7 or dice == 11 or dice == 2 or dice == 3 or dice == 12 :
        doNothing=0
    else:
        print("point: ", dice)
        currentPoint = dice
        rollState = 1
        pointRoll()

    #printState()  
    
def pointRoll():
    #TODO roll the dice until point comes in.  Have ability to pull bets down (place)
    global rollState, currentPoint, rollCount
    stillRolling = 1
    rollCount = 1
    while stillRolling == 1:
        #print("rolling for point: ", currentPoint)
        rollDice()
        payBets()
        
        #conditions
        if dice == 7:
            print("out, remove bets")
            stillRolling = 0
            rollState = 0
        elif dice == currentPoint:
            print("point hit, pay bets")
            stillRolling = 0
            rollState = 0
            #takedown field bets, if there
            takeDown("place4")
            takeDown("place5")
            takeDown("place6")
            takeDown("place8")
            takeDown("place9")
            takeDown("place10")
            
        print("RollCount: ", rollCount)
        rollCount = rollCount + 1

def rollDice():
        global die1,die2,dice,rollCount
        addBets()
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        dice = die1 + die2
        print("You roll a", die1, "and", die2, "for a total of", dice)

def addBets():
        #Start up for adding bets at any point during the game, multiple games
        global rollCount, rollState
        #print("In addBets, rollState and rollCount", rollState, rollCount)
        
        #always play the field
        #addBet("field", 10)
        
        if rollState == 0:
            #Start of a game, place passline bet
            #addBet("pass", 100)
            doNothing = 0
        
        if rollState == 1:
            doNothing = 0
            
            #bet only on the 1st roll after point
            if rollCount == 1:
                addBet("field", 200)
                addBet("place5",200)
                addBet("place6",220)
                addBet("place8",220)

                
                doNothing = 0

            if rollCount == 2 or rollCount == 3:
                takeDown("place5")
                takeDown("place6")
                takeDown("place8")
                addBet("field", 50)
                addBet("place5",50)
                addBet("place6",50)
                addBet("place8",50)
                    
            
    
        
if __name__ == '__main__':

    try:
        print("Start")
        printState()
     
        g = 1
        while g <= gamesToPlay:
            print("Game:", g)
            comeOutRoll()
            printState() 
            g = g + 1
        
        #printState()        
    except KeyboardInterrupt:
       print('\nGamed ended by user!')
    # TODO: Maybe a little game summary here
