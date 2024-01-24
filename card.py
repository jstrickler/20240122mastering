class Card:   # inherits from 'object'
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit
    
    @property
    def rank(self):  # getter property
        return self._rank

    @rank.setter
    def rank(self, value):  # setter property
        self._rank = value
    
    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self, value):
        self._suit = value
    
    def __str__(self):  # human-friendly
        return f"Card: {self.rank}-{self.suit}"

    def __repr__(self):  # code-friendly -- code to create object
        return f"Card('{self.rank}', '{self.suit}')"

if __name__ == "__main__":
    c1 = Card("3", "Hearts")   #  __init__()
    print(f"{type(c1) = }")
    print(f"{c1 = }")   #  repr()  -->  __repr__()
    print(f"c1 = {c1}")   #  str()  -->  __str__()
    # print(f"{c1._rank = }") NAUGHTY PROGRAMMER!
    print(f"{c1.rank = }")
    print(f"{c1.suit = }")
    c1.rank = "Q"
    print(f"{c1.rank = }")
    
    
    