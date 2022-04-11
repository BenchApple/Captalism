# Benjamin Chappell

# Stores all the attributes of a player
from requests import request
from position import Position
from cards import Cards

def hand_to_string(hand):
    s = ""
    i = 0
    if hand != None:
        for card in hand:
            if card != None:
                s = s + "\n" + str(i) + ") " + str(Cards(card).name)
                i += 1

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
    
    def choose_hand(self, hands_left):
        choice = -1
        while choice not in hands_left:
            choice = int(input("Player in Position " + str(self._pos) + " - Which deck would you like? " + str(hands_left) + " "))
        
        return choice
    
    def add_card_to_hand(self, card):
        self.hand.append(card)
    
    def remove_card_from_hand(self, card):
        self.hand.remove(card)
    
    # Allows the player to choose which cards to offload if they're in the right position
    # ONLY returns the indices, the actual game runner handles the exchange of cards
    def choose_offloads(self):
        offloads = []
        if self._pos == Position.PRES:
            c1 = -1
            while c1 not in [i for i in range(0, len(self._hand))]:
                c1 = int(input("Choose the index of the first card you'd like to offload "))
            offloads.append(c1)
            
            c2 = -1
            while c2 not in [i for i in range(0, len(self._hand))] or c2 == c1:
                c2 = int(input("Choose the index of the second card you'd like to offload "))
            offloads.append(c2)

            # Check to make sure that the second one is smaller than the first. If not, 
            # Shift the second one down by one
            if offloads[0] < offloads[1]:
                offloads[1] = offloads[1] - 1
        if self._pos == Position.VICE_PRES:
            c1 = -1
            while c1 not in [i for i in range(0, len(self._hand))]:
                c1 = int(input("Choose the index of the first card you'd like to offload "))
            offloads.append(c1)
        
        return offloads
    
    # Allows the player to choose their requests from the opposing player
    # Returns the indices IN the list of the opponent where those cards are.
    # The game runner handles the exchange of cards
    def choose_requests(self, opp):
        requests = []

        # Request by rank, 0 is 2 12 is ace
        if self.pos == Position.PRES or self.pos == Position.VICE_PRES:
            req = -1
            found = False
            while not found:
                req = int(input("Choose the first rank of card you would like to request (0-12): "))

                # Search through the opponents hand and find the card you're looking for
                # If you find that card, keep it
                if req in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
                    for i in range(0, len(opp.hand)):
                        if opp.hand[i] % 13 == req:
                            requests.append(i)
                            found = True
                            break

        # Request by rank, 0 is 2 12 is ace
        # Request again, but this time only president gets to do it
        if self.pos == Position.PRES:
            req = -1
            found = False
            while not found:
                req = int(input("Choose the second rank of card you would like to request (0-12): "))

                # Search through the opponents hand and find the card you're looking for
                # If you find that card, keep it
                if req in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
                    for i in range(0, len(opp.hand)):
                        if opp.hand[i] % 13 == req and i != requests[0]:
                            requests.append(i)
                            found = True
                            break
            
            # Same as for the offloads
            # If the first index is smaller than the second one, decrement the second one by 1
            if requests[0] < requests[1]:
                requests[1] = requests[1] - 1
        
        return requests
