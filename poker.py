starting_amt = 100
ante = 5

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
            return ans
        except:
            print("You must enter a number or valid move (c/f)")

def __main__():
    num_players = int(input("How many players? "))
    print("Enter players in order")
    players = {input():starting_amt for _ in range(num_players)}

    dealer = 0

    while len(players) > 1:
        bets = {player:0 for player in players}
        pot = 0
        small_blind = (dealer + 1) % num_players
        big_blind = (dealer + 2) % num_players

        for p in players:
            bet = get_bet(p)


        dealer = small_blind
    print(next(iter(players)))

__main__()
