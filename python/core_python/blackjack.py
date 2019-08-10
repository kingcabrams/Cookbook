"""Blackjack card game"""

import random
import sys


def hit(player):
    player[1] += random.randint(1, 13)
    if player[0] is not 'Chuck':
        print("\n" + player[0] + " your cards now add up to " + str(player[1]) + "\n")
    if player[1] > 21:
        if player[0] is 'Chuck':
            print(player[0] + " you bust.\nGame Over!")
            print("Chuck: What? How did I bust I was counting the cards!")
            sys.exit()
        else:
            print(player[0] + " you bust.\nGame Over!")
            sys.exit()


def end_game(player, dealer):
    if len(player) == 3 and len(dealer) == 3:
        if player[1] > dealer[1]:
            print("\n" + player[0] + " wins")
            print("Chuck: You're lucky I was going easy on you")
            sys.exit()
        elif player[1] < dealer[1]:
            print(dealer[0] + " wins")
            print("Chuck's cards added up to " + str(dealer[1]))
            print("Chuck: You're too young to try and go up against me.")
            sys.exit()
        else:
            print("It's a tie")
            print("Chuck: I chose to stay early just so you could tie, your pathetic")
            sys.exit()


def player_setup(player):
    name = input("What is your name: ")
    player.insert(0, name)


def player_turn(player, hit_or_stay=False):
    try_end = False
    if hit_or_stay is False and len(player) == 2:
        ans = input(player[0] + " would you like to hit or stay: ")
        if ans == 'stay':
            player.append('out')
        else:
            hit_or_stay = True
    if hit_or_stay:
        hit(player)


def main():
    player = [0]
    dealer = ['Chuck', 0]
    print("Welcome to blackjack")
    play = True
    while play:
        player_setup(player)
        game = True
        num = 0
        while game:
            end_game(player, dealer)
            if num == 0:
                player_turn(player)
            else:
                if len(dealer) < 3:
                    if dealer[1] < 17:
                        if len(player) < 3:
                            print("Chuck: I guess I'll hit too\n")
                        else:
                            print("Chuck: What a punk. I can't believe you are too scared to hit.", end=' ')
                            print("Unlike you I'm gonna keep hitting\n")
                        player_turn(dealer, hit_or_stay=True)
                    else:
                        print("Chuck: I guess I'll stay now\n")
                        dealer.append('out')
            num += 1
            num = num % 2


main()
