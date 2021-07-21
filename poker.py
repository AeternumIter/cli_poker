import os

# Constants -- will likely configure based on cli inputs
starting_amt = 500
ante = 1
sb = 5
bb = 10


class Game:
    players: list[str]
    player_money: dict[str, int] = {}
    curr_round: int = 0
    dealer_index: int = 0

    # variables associated w/ betting
    requirement: int = 0
    investments: dict[str, int] = {}
    players_in: set[str] = None

    dealer: int = 0
    small_blind: int = 1
    big_blind: int

    def __init__(self, players):
        self.players = [player.lower() for player in players]
        self.player_money = {player: starting_amt for player in players}
        self.dealer = 0
        self.small_blind = 1
        self.big_blind = 2 % len(self.players)

    def start_round(self):
        self.requirement = 0
        self.investments = {p: 0 for p in self.players}
        self.players_in = set(self.players)
        self.curr_round += 1

        clear()
        print("--------------------------")
        print(f"Round {self.curr_round}")
        print(f"Small blind: {self.players[self.small_blind % len(self.players)]}")
        print(f"Big blind: {self.players[self.big_blind % len(self.players)]}")
        print("--------------------------")

    def pass_button(self):
        self.dealer = (self.dealer + 1) % len(self.players)
        self.small_blind = (self.dealer + 1) % len(self.players)
        self.big_blind = (self.dealer + 2) % len(self.players)

    def players_that_can_bet(self):
        return filter(lambda x: self.player_money[x] > 0, self.players_in)

    def place_bet(self, player: str, amt: int):
        if amt < 0:
            # fold by betting -1
            self.players_in.remove(player)
            return
        player.money -= amt
        self.investments[player] = self.investments.get(player, 0) + amt

    def payout(self):
        # TODO: deal with ties [shouldnt be hard]
        prompt = "Who won overall?"
        while sum(self.investments.values()) > 0:
            # gets the curr best player still in
            print(prompt)
            ans = input().lower()
            while ans not in self.players_in:
                print(f"Please enter one of the following: [{', '.join(self.players_in)}]")
                ans = input().lower()

            # if winner not in a side pot, we are done in one step
            if self.investments[ans] >= self.requirement:
                self.player_money[ans] += sum(self.investments.values())
                break

            for player, amt in self.investments.items():
                if player == ans:
                    continue
                winnings = min(amt, self.investments[ans])
                self.player_money[ans] += winnings
                self.investments[player] -= winnings

            # always get ur $ back when win"
            self.player_money[ans] += self.investments[player]
            self.investments[ans] = 0
            self.players_in.remove(ans)
            prompt = f"After {ans}, who won?"

        # print resulting scores
        print("RESULTS: ")
        to_remove = set()
        for player, amt in self.player_money.items():
            print(f"{player} has ${amt}{'' if amt else ' [eliminated]'}")
            if amt == 0:
                to_remove.add(player)
        for player in to_remove:
            del self.player_money[player]
            self.players.remove(player)

    def must_bet(self, player):
        return player in self.players_in and self.investments[player] < self.requirement and self.player_money[player]

    def more_rounds_needed(self):
        return len(list(filter(lambda p: self.must_bet(p), self.players))) > 0


def clear():
    try:
        os.system('clear')
    except:
        print('\n\n\n')


def convert_bet_or_prompt(number_string, prompt="You must enter a number or valid move (c/f)", maximum=float('inf')):
    try:
        number = int(number_string)
        if number < 0:
            print("You cannot raise by a negative amount")
        elif number <= maximum:
            return number
        else:
            print(f"You only have ${maximum} to raise by.")
    except:
        print(prompt)


def get_bet(game, player):
    print(f"Now betting: {player}")
    if game.player_money[player] + game.investments[player] <= game.requirement:
        print(f"All in at ${game.player_money[player] + game.investments[player]}? (y)es/(n)o: ")
        while True:
            ans = input().lower().strip()
            if ans == 'y' or ans == 'yes':
                return game.player_money[player]
            elif ans == 'n' or ans == 'no':
                return -1
            else:
                print("Enter (y)es or (n)o: ")
    if game.investments[player] == game.requirement:
        print(f"The pot contains ${sum(game.investments.values())}. You can (c)heck or raise up to "
              f"${game.player_money[player]} above the current bet size of ${game.requirement}")
        print(f"Please enter your bet (enter '(c)heck' or raise amount)")
        while True:
            ans = input().lower().strip()
            if ans == 'c' or ans == 'call':
                return 0
            ans = convert_bet_or_prompt(ans, prompt="You must enter a valid number or '(c)all'")
            if ans is not None:
                return ans

    print(f"The pot contains ${sum(game.investments.values())}. You can call with an additional "
          f"${game.requirement - game.investments[player]}, or raise beyond that by up "
          f"to ${game.player_money[player] - game.requirement}")
    print(f"{player}, please enter your bet (enter '(c)all', '(f)old', or raise amount):")
    while True:
        ans = input().lower().strip()
        if ans == "fold" or ans == "f":
            return -1
        if ans == "call" or ans == "c":
            return game.requirement - game.investments[player]
        ans = convert_bet_or_prompt(ans, maximum=game.player_money[player] - game.requirement)
        if ans is not None:
            return ans + game.requirement

def play_hand(game):
    # handle ante & blinds (TODO)
    # go through 4 stages of betting
    for betting_round in ["the pre-flop", "the flop", "the turn", "the river"]:
        print(f"### Now placing bets for {betting_round}")

        # go through each player to get bets
        # TODO: ensure propper ordering relative to dealer
        another_round = True
        while another_round:
            for i, p in enumerate(game.players):
                if p not in game.players_in:
                    continue
                bet = get_bet(game, p)
                if bet == -1:
                    game.players_in.remove(p)
                else:
                    game.player_money[p] -= bet
                    game.investments[p] = game.investments.get(p, 0) + bet
                    game.requirement = max(game.requirement, game.investments[p])
            another_round = game.more_rounds_needed()


def __main__():
    num_players = int(input("How many players? "))
    print("Enter players in order")
    game = Game([input() for _ in range(num_players)])

    # main game loop
    while len(game.players) > 1:
        game.start_round()
        play_hand(game)
        game.payout()
    print(f"The winner is {next(iter(game.players))}.")


__main__()
