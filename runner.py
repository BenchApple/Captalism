# Benjamin Chappell

# This file runs the game and directs each player what to do

from player import Player
from position import Position
from deck import Deck

def main():
    num_players = 6
    players = [Player(Position(i), None) for i in range(0, num_players)]

    for p in players:
        print(p)

    d = Deck()
    d.shuffle_deck()
    
    hands = build_hands(d, num_players)

    # assign hands to players in order the first round
    for i in range(0, len(players)):
        players[i].set_hand(hands[i].copy())
    
    print()
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