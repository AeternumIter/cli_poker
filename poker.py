starting_amt = 100 #All players start at 100
ante = 5 #Ante is set to 5

num_players = int(input("How many players?")) #Asks how many players are in the game
print("Enter players, starting with dealer going clockwise")
players = {input():starting_amt for _ in range(num_players)} #Records all of the player names
currentplayers = []
for i in players: 
    currentplayers.append(i) #Adds the players to the "currentplayers" list
dealer = 0 #Defines the dealer variable
callamount = 0 #Defines the call amount variable
checkpossible = true #Defines the checkpossible variable



def roundr():
      smallblind = (dealer + 1) % num_players #Finds the first player (left of the dealer)
      big_blind = (dealer + 2) % num_players #I'm not sure what this one does.
      currentplayer = smallblind #Sets the "currentplayer" variable to the first player
      currentplayers = [] #clears the currentplayers list
      for i in players:
        currentplayers.append(i) #Remakes the currentplayers list
      pot = 0 #Defines and empties the pot
      for i in players: #Adds the Ante for each player
        pot += 5
        players[currentplayers[currentplayer]] -= 5

      callamount = 0 #Resets the call amount
      checkpossible = true #Resets the checkpossible variable
      
      while len(currentplayers) > 1: #When there is more than one player playing
        print(currentplayers[currentplayer] + " Has " + str(players[currentplayers[currentplayer]])) #Displays how much money the player has (I think)
        cpa = input("what will "+ currentplayers[currentplayer] + " do? ") #asks the action of the player
        if cpa == "call": #if the player calls the bet
            players[currentplayers[currentplayer]] -= callamount #Subtracting money from account
            pot += callamount #Adding money to the pot
            
            if callamount == 0: #If there is no bet to call
                print("hmmm, it seems a bet hasn't been made yet. Try using the 'bet' command instead")
            else: 
                if currentplayer == len(currentplayers) - 1: #Goes to the next player
                    currentplayer = 0
                else: 
                    currentplayer += 1
        elif cpa == "raise": #If the player raises the bet
            if callamount != 0:
                raiseamount = int(input("How much do you want to raise the bet? (The current bet is " + callamount + ")"))
                players[currentplayers[currentplayer]] -= (raiseamount + callamount) #Subtracting money from account
                pot += (raiseamount + callamount) #Adding money to pot
                if currentplayer == len(currentplayers) - 1: #Goes to the next player
                    currentplayer = 0
                else: 
                    currentplayer += 1
            else:
                print("hmmm, there isn't a bet to be raised. Try using the 'bet' command instead")
        elif cpa == "fold": #If the player folds
            currentplayers.remove(currentplayers[currentplayer]) #Remove the player from the round
            if currentplayer == len(currentplayers) - 1: #Goes to the next player
                currentplayer = 0
            else: 
                currentplayer += 1
        elif cpa == "bet": #If the player bets
            callamount = int(input("What shall the bet be? "))
            players[currentplayers[currentplayer]] -= callamount #Subtracting money from account
            pot += callamount #Adding Money to pot
            checkpossible = false
            if currentplayer == len(currentplayers) - 1: #Goes to the next player
                currentplayer = 0
            else: 
                currentplayer += 1
        elif cpa == "check": #If the player checks
            if currentplayer == smallblind or checkpossible = true: #Checks if they can check     
                pass
                if currentplayer == len(currentplayers) - 1: #Goes to the next player
                    currentplayer = 0
                else: 
                    currentplayer += 1
            else:
                print("Sorry, you can't check right now")
      for i in currentplayers: #Gives the pot to the winner
          players[i] += pot
      checkforoutofmoney() #Checks if anyone is out of money
      
     
def checkforoutofmoney():
      for i in players:
            if players[i] <= 0:
                players.pop(i)
                
while(True):
    roundr() #Runs the function
