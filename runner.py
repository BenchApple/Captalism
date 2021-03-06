# Benjamin Chappell

# This file runs the game and directs each player what to do

import requests
from player import Player, hand_to_string
from position import Position
from deck import Deck
from cards import Cards

def main():
    num_players = 6
    players = [Player(Position(i), None) for i in range(0, num_players)]

    for p in players:
        print(p)

    d = Deck()
    d.shuffle_deck()
    
    hands = build_hands(d, num_players)

    # show the hands with their first cards overturned and then have the players pick them in order
    hands_left = [i for i in range(0, len(hands))]
    print()
    for i in range(0, len(hands)):
        print("Hand %i: %s, Length: %i" % (i, str(Cards(hands[i][0]).name), len(hands[i])))
    print()

    # assign hands to players in order the first round
    for i in range(0, len(players)):
        c = players[i].choose_hand(hands_left)
        hands_left.remove(c)

        players[i].set_hand(hands[c])
    
    for p in players:
        print(p)

    # Perform the card swaps
    # For the president player, have them choose the two cards to get rid of
    print()
    for i in range(0, len(players)):
        print("Player in position " + str(players[i].pos) + ":")
        print(str(players[i]))
        offloads = players[i].choose_offloads()
        requests = players[i].choose_requests(players[num_players - 1 - i])

        for off in offloads:
            players[num_players - 1 - i].add_card_to_hand(players[i].hand[off])
            players[i].remove_card_from_hand(players[i].hand[off])
        
        for req in requests:
            players[i].add_card_to_hand(players[num_players - 1 - i].hand[req])
            players[num_players - 1 - i].remove_card_from_hand(players[num_players - 1 - i].hand[req])
        
        print(players[i])
        print(players[num_players - 1 - i])

        input()
        
    
    for p in players:
        print(p)


def build_hands(deck, num_players):
    hands = [[] for i in range(0, num_players)]
    print(hands)

    n = 0
    while not deck.is_empty():
        hands[n % num_players].append(deck.get_next_card())
        n += 1 
    
    return hands


if __name__ == "__main__":
    main()