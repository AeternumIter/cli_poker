import os
from dataclasses import dataclass


# Constants -- will likely configure based on cli inputs
starting_amt = 500
ante = 1
sb = 5
bb = 10


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
class Game:
    players: list[Player]
    curr_round: int = 0
    dealer_index: int = 0

    # variables associated w/ betting
    requirement: int = 0
    investments: dict[Player, int] = {}
    players_in : set[Player] = None
    side_pots: set[(Player, amt)] = {}

    def start_round(self):
        self.requirement = 0
        self.investments = {}
        self.players_in = set(players)
        self.side_pots = {}
        # TODO filter players that need to be removed

    def place_bet(self, player : Player, amt : int):
        if amt < 0:
            # fold by betting -1
            self.players_in.remove(player)
            return
        player.money -= amt
        self.investments[player] = self.investments.get(player, 0) + amt
        if self.investments[player] < requirement:
            side_pots.add((player, self.investments[player]))

    def payout():
        # TODO deal w/ payout logic -- promting for rankings happens here

        """
        basic idea -- ask for winners. If the winners are in a side pot, distribute said pot and all lower valued pots to the winners, and remove these players -- then ask for the runner up etc [etc does a lot of work lol]

        """

        pass


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
