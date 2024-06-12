"""
Game Simulation Description
- This is a two-player card game.
- The game starts with a deck of cards.
- The cards are dealt out to both players.
- On each turn:
    - Both players turn over their top-most card.
    - The player with the higher valued card takes the cards and puts them in their scoring pile (scoring 1 point per card).
    - This continues until the players have no cards left.
- The player with the highest score wins.
"""
import random

# define the player
class Player:
    def __init__(self, name = "", deck=[]):
        self.name = name
        self.deck = deck
        self.score = 0
        self.card = []

# define the game
class TwoPlayerGame:
    def __init__(self, suits=[], ranks=[], deck=[[]], maxRounds=25):
        self.suits = ['Clubs','Diamonds','Hearts','Spades']
        self.ranks = ['2','3','4','5','6','7','8','9','10','JACK','QUEEN','KING','ACE']
        self.deck = [(rank, suit) for suit in self.suits for rank in self.ranks]
        self.maxRounds = maxRounds

def endTheGame(player1, player2):
    if len(player1.deck) > len(player2.deck):
        print(f"{player1.name} wins the game!")
        return 1
    elif len(player1.deck) < len(player2.deck):
        print(f"{player2.name} wins the game!")
        return 2
    else:
        print("It's a tie!")
        return 0

# start game simulation
def playTwoPlayerGame(game,p1,p2,maxRounds):
    round = 0

    while len(p1.deck) > 0 and len(p2.deck) > 0:
        round += 1; print(f"\nRound #{round}")

        # play the cards for both players
        p1.card, p2.card = p1.deck.pop(0), p2.deck.pop(0)
        p1.score, p2.score = game.ranks.index(p1.card[0]), game.ranks.index(p2.card[0]) # could weight with suits too
        print(f"{p1.name}'s card: {p1.card[0]} of {p1.card[1]}"
              f"\n{p2.name}'s card: {p2.card[0]} of {p2.card[1]}")

        # round conditions

        # case: player 1 win
        if p1.score > p2.score:
            p1.deck.append(p1.card); p1.deck.append(p2.card)
            print(f"{p1.name} wins the round!")

        # case: player 2 win
        elif p1.score < p2.score:
            p2.deck.append(p1.card); p2.deck.append(p2.card)
            print(f"{p2.name} wins the round!")

        # case: tie
        else:
            print("It's a tie!")

        print(f"{p1.name}'s deck has: {len(p1.deck)} cards remaining!\n"
              f"{p2.name}'s deck has: {len(p2.deck)} cards remaining!")

        # wait for input to move on to next round
        input("Press Enter to play the next round...")

        # end of game evaluation
        if (game.maxRounds == -1 and ((len(p1.deck) == 0 or len(p2.deck) == 0)))\
                or (game.maxRounds != -1 and round >= maxRounds):
            return endTheGame(p1, p2)

# create the game and deal the cards
game = TwoPlayerGame(maxRounds=25)
random.shuffle(game.deck)
p1 = Player("Clarence", game.deck[26:])
p2 = Player("Bob", game.deck[:26])
print(f"Rule 1: In this game, all suits are equal!")
maxRounds = game.maxRounds
if maxRounds == -1:
    print("Rule 2: It's a tournament! This game continues until a player has no cards left!")
else:
    print(f"Rule 2: This game goes on for {maxRounds} rounds! At the end of the game, the scores are evaluated to decide which player won!")
playTwoPlayerGame(game,p1,p2,maxRounds)