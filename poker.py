import os

starting_amt = 1000
ante = 5
sb = 20
bb = 40
players = {}

def clear():
    try:
        os.system('clear')
    except:
        print('\n\n\n')

def get_bet(player):
    print(f"{player}, please enter your bet (enter '(c)all'/'(c)heck', '(f)old', or raise amount):")
    while True:
        ans = input().lower()
        if ans == "fold" or ans == "f":
            return -1
        if ans == "check" or ans == "call" or ans == "c":
            return 0
        try:
            ans = int(ans)
            if (ans < 0):
                print("You cannot raise by a negative amount")
            elif ans <= players[player]:
                return ans
            else:
                print(f"You only have ${players[player]} to bet.")
        except:
            print("You must enter a number or valid move (c/f)")


num_players = int(input("How many players? "))
print("Enter players in order")
players = {input():starting_amt for _ in range(num_players)}

dealer = 0
round = 0

# main game loop
while len(players) > 1:
    # clears screen
    small_blind = (dealer + 1) % num_players
    big_blind = (dealer + 2) % num_players

    round += 1
    clear()
    print("--------------------------")
    print(f"Round {round}")
    print(f"Small blind: {list(players.keys())[small_blind]}")
    print(f"Big blind: {list(players.keys())[big_blind]}")
    print("--------------------------")



    pots = [(0, list(players.keys()))] # all players start in the main pot

    for p in players:
        bet = get_bet(p)



    dealer = small_blind
print(f"The winner is {next(iter(players))}.")
