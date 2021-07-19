import os
from dataclasses import dataclass


# Constants -- will likely configure based on cli inputs
starting_amt = 1000
ante = 5
sb = 20
bb = 40


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

@dataclass
class Pot:
    players_invested: set[Player]
    size: int = 0


@dataclass
class Game:
    players: list[Player]
    curr_round: int = 0
    dealer_index: int = 0




def clear():
    try:
        os.system('clear')
    except:
        print('\n\n\n')

def get_bet(game, player):
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
                print(f"You only have ${player.money} to bet.")
        except:
            print("You must enter a number or valid move (c/f)")



def __main__():
    num_players = int(input("How many players? "))
    print("Enter players in order")
    game = Game([Player(input()) for _ in range(num_players)])



    # main game loop
    while len(game.players) > 1:
        # sets up round
        small_blind = (game.dealer_index + 1) % num_players
        big_blind = (game.dealer_index + 2) % num_players

        clear()
        print("--------------------------")
        print(f"Round {game.curr_round}")
        print(f"Small blind: {game.players[small_blind]}")
        print(f"Big blind: {game.players[big_blind]}")
        print("--------------------------")


        still_betting = set(game.players)
        pots = [Pot(still_betting, 0)]

        #TODO: put logic for side pots somewhere

        # handle ante & blinds (TODO)

        # go through 4 stages of betting
        for betting_round in ["the pre-flop", "the flop", "the turn", "the river"]:
            print(f"### Now placing bets for {betting_round}")

            # go through each player to get bets
            # TODO: ensure propper ordering relative to dealer
            for p in game.players:
                bet = get_bet(game, p)
                if not still_betting: pass
        game.dealer_index = small_blind
        game.curr_round += 1
    print(f"The winner is {next(iter(players))}.")

__main__()
