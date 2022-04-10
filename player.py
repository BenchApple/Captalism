# Benjamin Chappell

# Stores all the attributes of a player
class Player:
    def __init__(self, pos, hand) -> None:
        self.pos = pos
        self.hand = hand
    
    def get_pos(self):
        return self.pos
    
    def set_pos(self, pos):
        self.pos = pos
    
    def get_hand(self):
        return self.hand
    
    def set_hand(self, hand):
        self.hand = hand

    pos = property(get_pos, set_pos)
    hand = property(get_hand, set_hand)
