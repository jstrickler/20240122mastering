from card import Card
from carddeck import CardDeck

class JokerDeck(CardDeck):
    def __init__(self):
        super().__init__()  # call carddeck constructor
        print("HELLO from JOKERDECK constructor")

    def _make_deck(self):
        super()._make_deck()  # call CardDeck._make_deck()
        j1 = Card('JOKER', 'JOKER')
        self._cards.append(j1)
        j2 = Card('JOKER', 'JOKER')
        self._cards.append(j2)


# if running as a script:
if __name__ == "__main__":
    j1 = JokerDeck()
    j1.shuffle()
    print(j1.cards)
    print(j1)
    print(f"{j1 = }")
    