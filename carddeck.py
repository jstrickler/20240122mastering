import random
from card import Card

class CardDeck:
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self):
        print("HELLO FROM CARDDECK CONSTRUCTOR")
        self._make_deck()

    def _make_deck(self) -> None:
        self._cards = list()
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)

    @property
    def cards(self):
        return tuple(self._cards)

    def __str__(self):
        my_class = type(self)
        return f"{my_class.__name__}:{len(self)}"
        
    def __len__(self):
        return len(self.cards)
    
    def __repr__(self):
        my_class = type(self)
        return f"{my_class.__name__}()"
    
    def shuffle(self) -> None:
        random.shuffle(self._cards)

    def draw(self) -> None:
        return self._cards.pop()

if __name__ == "__main__":
    d1 = CardDeck()
    d2 = CardDeck()
    print(f"{d1 = }")
    print(d1)
    d1.shuffle()
    print(f"{d1.cards = }")
    print(f"{len(d1) = }")
    for _ in range(5):
        print(f"{d1.draw() = }")
    
        