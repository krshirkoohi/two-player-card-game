# two-player-card-game

This is a Python implementation of an automated simulation of a simple two-player card game. Players take turns drawing cards from their decks and comparing their values. The player with the higher card value wins the round and takes both cards. The game continues until one player has no cards left or the maximum number of rounds is reached.

## Game Rules

- The game involves two players and a standard deck of 52 cards.
- At the start, the deck is shuffled, and the cards are dealt equally to both players.
- Each turn consists of the following steps:
  - Both players reveal their top-most card.
  - The player with the higher valued card wins the round, taking both cards and adding them to their deck.
  - If the card values are equal, it is considered a tie, and no cards are taken.
- The game continues until one player has no cards left or the maximum number of rounds is reached.
- The player with the most cards at the end of the game is declared the winner.

## Code Structure

### Player Class

The `Player` class defines the properties and methods for each player:
```python
class Player:
    def __init__(self, name = "", deck=[]):
        self.name = name
        self.deck = deck
        self.score = 0
        self.card = []
```

### TwoPlayerGame Class

The `TwoPlayerGame` class sets up the game:
```python
class TwoPlayerGame:
    def __init__(self, suits=[], ranks=[], deck=[[]], maxRounds=25):
        self.suits = ['Clubs','Diamonds','Hearts','Spades']
        self.ranks = ['2','3','4','5','6','7','8','9','10','JACK','QUEEN','KING','ACE']
        self.deck = [(rank, suit) for suit in self.suits for rank in self.ranks]
        self.maxRounds = maxRounds
```

### End Game Function

The `endTheGame` function determines the winner:
```python
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
```

### Play Game Function

The `playTwoPlayerGame` function simulates the game:
```python
def playTwoPlayerGame(game,p1,p2,maxRounds):
    round = 0

    while len(p1.deck) > 0 and len(p2.deck) > 0:
        round += 1; print(f"\nRound #{round}")

        p1.card, p2.card = p1.deck.pop(0), p2.deck.pop(0)
        p1.score, p2.score = game.ranks.index(p1.card[0]), game.ranks.index(p2.card[0])
        print(f"{p1.name}'s card: {p1.card[0]} of {p1.card[1]}"
              f"\n{p2.name}'s card: {p2.card[0]} of {p2.card[1]}")

        if p1.score > p2.score:
            p1.deck.append(p1.card); p1.deck.append(p2.card)
            print(f"{p1.name} wins the round!")

        elif p1.score < p2.score:
            p2.deck.append(p1.card); p2.deck.append(p2.card)
            print(f"{p2.name} wins the round!")

        else:
            print("It's a tie!")

        print(f"{p1.name}'s deck has: {len(p1.deck)} cards remaining!\n"
              f"{p2.name}'s deck has: {len(p2.deck)} cards remaining!")

        input("Press Enter to play the next round...")

        if (game.maxRounds == -1 and ((len(p1.deck) == 0 or len(p2.deck) == 0)))\
                or (game.maxRounds != -1 and round >= maxRounds):
            return endTheGame(p1, p2)
```

## Running the Game

1. Create an instance of the game and shuffle the deck:
```python
game = TwoPlayerGame(maxRounds=25)
random.shuffle(game.deck)
```

2. Deal the cards to the players:
```python
p1 = Player("Clarence", game.deck[26:])
p2 = Player("Bob", game.deck[:26])
```

3. Start the game:
```python
print(f"Rule 1: In this game, all suits are equal!")
maxRounds = game.maxRounds
if maxRounds == -1:
    print("Rule 2: It's a tournament! This game continues until a player has no cards left!")
else:
    print(f"Rule 2: This game goes on for {maxRounds} rounds! At the end of the game, the scores are evaluated to decide which player won!")
playTwoPlayerGame(game,p1,p2,maxRounds)
```


