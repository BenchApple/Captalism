# Benjamin Chappell

# Stores all the attributes of a player
from position import Position
from cards import Cards

def hand_to_string(hand):
    s = ""
    if hand != None:
        for card in hand:
            if card != None:
                s = s + "\n" + str(Cards(card).name)

    return s

class Player:
    def __init__(self, pos, hand) -> None:
        self.pos = pos
        self.hand = hand
    
    def get_pos(self):
        return self._pos
    
    def set_pos(self, pos):
        self._pos = pos
    
    def get_hand(self):
        return self._hand
    
    def set_hand(self, hand):
        self._hand = hand

    pos = property(get_pos, set_pos)
    hand = property(get_hand, set_hand)

    def __str__(self) -> str:
        s = "Position: %s; Hand: %s" % (self._pos, hand_to_string(self._hand))
        return s
