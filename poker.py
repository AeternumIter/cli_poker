import os
from dataclasses import dataclass


starting_amt = 1000
ante = 5
sb = 20
bb = 40
players = {}

@dataclass
class Player:
    name: str
    money: int = starting_amt
    def __str__(self):
        return self.name
    def __repr__(self):
        return f"{self.name} [{self.money}]"
    def __hash__(self):
        return self.name.__hash__()

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
            elif ans <= player.money:
                return ans
            else:
                print(f"You only have ${players[player]} to bet.")
        except:
            print("You must enter a number or valid move (c/f)")


num_players = int(input("How many players? "))
print("Enter players in order")
players = [Player(input()) for _ in range(num_players)]

dealer = 0
round_num = 0

# main game loop
while len(players) > 1:
    # clears screen
    small_blind = (dealer + 1) % num_players
    big_blind = (dealer + 2) % num_players

    round_num += 1
    clear()
    print("--------------------------")
    print(f"Round {round_num}")
    print(f"Small blind: {players[small_blind]}")
    print(f"Big blind: {players[big_blind]}")
    print("--------------------------")

    pots = [(0, set(players.copy()))] # all players start in the main pot
    still_betting = set(players)

    for betting_round in ["the pre-flop", "the flop", "the turn", "the river"]:
        print(f"### Now placing bets for {betting_round}")

        for p in players:
            bet = get_bet(p)
            if not still_betting: pass
    dealer = small_blind
print(f"The winner is {next(iter(players))}.")
