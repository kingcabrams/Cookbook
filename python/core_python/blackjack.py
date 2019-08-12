"""Blackjack card game"""

import random
import sys


def hit(player):
    player[1] += random.randint(1, 13)
    print(player[0] + " your cards now add up to " + str(player[1]))
    if player[1] > 21:
        player.append('out')


def end_game(player):
    print("\n" + player[0] + " wins") if player[1] == 21 else player.append('lose')
     

def player_setup(player):
    name = input("What is your name: ")
    player.insert(0, name)


def player_turn(player):
    ans = input("\n" + player[0] + " would you like to hit or stay: ")
    if ans == 'stay':
        end_game(player)
    else:
        hit(player)


def main():
    play = True
    while play:
        player = [0]
        print("Welcome to blackjack")
        game = True
        player_setup(player)
        while game:
            if len(player) == 3:
                print("Sorry you lose")
                play = False
                break
            game = True
            num = 0
            player_turn(player)
        ans = input("Would you like to play again? [Y/n]: ")
        play = (ans.lower() != 'n')
    print("Thanks for playing blackjack")


main()
