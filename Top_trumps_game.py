## Top_Trumps_Game
## Python code for top trumps game on command line.

## 01/03/2019 ;)

# Created as an assignment by Chenyang Li and Jasamrit Rahala. 
# This is code for a Top Trumps Game with two players.
# The aim of the game is to win each round and win all the cards.
# Each card has five attributes and these attributes are randomly generated. 
# There are twenty cards, each with their own name. 
# An attribute is chosen; if it is higher than the other person's attribute, the other player forfits a card to the first player. 
# Winner is left with 20 cards

import random as rnd
import os
import time as tm

def intro():
    print("Welcome to the Top Trumps game, made by Jam and Chen.")
    print("\nIn this game, you compare different \"skills\" for each card to determine the best.")
    print("\nYou have 7 seconds now to decide who wants to be player 1. BE WARNED. Player 1 always loses in a draw.")
    tm.sleep(7)
    print("\nLet the games begin!" )
    tm.sleep(0.5)


def make_cards(Players, Names, Parameters):

    file = open("NameFile.txt", "w")
    for Name in Names:
        file.write(Name + "\n")
    file.close()
    Names = []
    
    file = open("NameFile.txt", "r")

    for line in file:
        Names.append(line.strip("\n"))
    file.close()

    for Name in Names:
        Name_List = []
        for Parameter in Parameters:
            Name_List.append((rnd.randint(1, 10) + rnd.randint(1, 10))//2) ## takes average of two for a more balance result
        Players[Name] = Name_List
    Player_1_Cards = []

    while len(Player_1_Cards) < len(Names):
        index = rnd.randint(0, len(Names)-1)
        Player_1_Cards.append(Names[index])
        Names.pop(index)

    Player_2_Cards = Names

    return(Player_1_Cards, Player_2_Cards, Players)


def move(player, Player_1_Cards, Player_2_Cards, Format_Parameters, Players, Parameters):
   
    finished = False ## flag

    if player == 1:
        opposition = 2
        player1_deck = Player_1_Cards
        player2_deck = Player_2_Cards

    else:
        player = 2
        opposition = 1
        player1_deck = Player_2_Cards
        player2_deck = Player_1_Cards


    print("\n\nPlayer", player, "turn...")
    print("Your card is: ", player1_deck[0], "\n")

    for index in range(len(Players[player1_deck[0]])):
        print([index], Parameters[index], Players[player1_deck[0]][index])

    while True:
        try:
            choice = int(input("\n [choice] >> "))
            while choice > 5 or choice < 0:
                    print("Oops! That was not valid. Try again...")
                    choice = input("\n [choice] >> ")
            break
        
        except (ValueError, TypeError):
            print("Oops! That was not valid. Try again...")
    
    print("\n\nOpposition card,", player2_deck[0], "has", Format_Parameters[choice], "level ", Players[player2_deck[0]][choice])
    print("Player card,", player1_deck[0], "has", Format_Parameters[choice], "level ", Players[player1_deck[0]][choice])

    if Players[player2_deck[0]][choice]<Players[player1_deck[0]][choice]:
        print("\nPlayer", player, "has won the round")

        player1_deck.append(player1_deck[0])
        player1_deck.append(player2_deck[0])
        
        player1_deck.pop(0)
        player2_deck.pop(0)

        if len(player2_deck) < 1:
            finished = "win1" 
    
    elif Players[player2_deck[0]][choice] == Players[player1_deck[0]][choice]:
        print("\nAlthough this is a draw, player", opposition, "has won the round.")
            
    else:
        print("\nPlayer", opposition, "has won the round")

        player2_deck.append(player2_deck[0])
        player2_deck.append(player1_deck[0])
        
        player2_deck.pop(0)
        player1_deck.pop(0)

        if len(player1_deck) < 1:
            finished = "win2" ## player 2 has won the round
        elif len(player2_deck) < 1:
            finished = "win1" ## player 1 has won the round 

    print("\n\n-------------------------------")
    print("Cards remaining: ")
    print("Player 1", len(Player_1_Cards))
    print("Player 2", len(Player_2_Cards))
    print("-------------------------------")

    stop = input("Do you still wish to continue? Y/N")
    if stop == "N":
        stop = ("Are you sure? Y/N")
        if stop == "Y":
            finished = True

    return finished


def main():
    Players             = {}
    Names               = ["Jon", "John", "Joe", "Craig", "Stew", "Ian", "Rob", "Paul", "Brian", "Peter", "Hector", "Albert", "Seb", "Oleg", "Chen", "Hugo", "Hugh", "Alex", "Bob"]
    Format_Parameters   = ["speed", "accuracy", "defence", "shooting", "passing", "strategy"]
    Parameters          = ["speed.............",
                        "accuracy..........",
                        "defence...........",
                        "shooting..........",
                        "passing...........",
                        "strategy.........."]

    intro() ## calls the introduction. See top

    finished = False ## flag that denotes when the game should continue.

    Player_1_Cards, Player_2_Cards, Players = make_cards(Players, Names, Parameters)

    turn = 1 ## this is "player's turn". 1 means "Player 1" and 2 means "Player 2"

    while finished == False:
        finished = move(turn, Player_1_Cards, Player_2_Cards, Format_Parameters, Players, Parameters)
        
        if turn == 1:
           turn = 2
        else:
           turn = 1

    if turn == 1:
        opposition_end = 2
    else:
        opposition_end = 1
        
    print("\n")

    if finished == "win1":
        print("Player 1 has won the game")
        print("\nPlayer 2 has lost the game\n\n")

    elif finished == "win2":
        print("Player 2 has won the game")
        print("\nPlayer 1 has lost the game\n\n")

    else: 
        print("As you have decided to quit, there is no winner. Unlucky. :(\n\n")
    
    print("""\n  __                                    
                /   _  _  _  _ _ |_   | _ |_. _  _  _  |
                \__(_)| )(_)| (_||_|_||(_||_|(_)| )_)  .
                         _/  
                        """)

    input("\n\nPress enter to now quit >> ")

main()

