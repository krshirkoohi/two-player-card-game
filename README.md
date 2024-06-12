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
