import random
import os

def make_cards():
    Players             = {}
    Names               = ["Jon", "John", "Joe", "Craig", "Stew", "Ian", "Rob", "Paul", "Brian", "Peter", "Hector", "Albert", "Seb", "Oleg", "Chen", "Hugo", "Hugh", "Alex", "Bob"]
    Format_Parameters   = ["speed", "accuracy", "defence", "shooting", "passing", "strategy"]
    Parameters          = ["speed.............",
                        "accuracy..........",
                        "defence...........",
                        "shooting..........",
                        "passing...........",
                        "strategy.........."]


    for Name in Names:
        Name_List = []

        for Parameter in Parameters:
            Name_List.append((random.randint(1, 10) + random.randint(1, 10)/2)) ## takes average of two for a more balance result


        Players[Name] = Name_List

def assign():

    Player_1_Cards = []

    while len(Player_1_Cards) < len(Names):

        index = random.randint(0, len(Names)-1)
        Player_1_Cards.append(Names[index])
        Names.pop(index)


    Player_2_Cards = Names


def move(player, local_finished):
   
    if player == 1:

        player = 1
        opposition = 2

        playerDeck = Player_1_Cards
        opposDeck = Player_2_Cards


    else:
        
        player = 2
        opposition = 1

        playerDeck = Player_2_Cards
        opposDeck = Player_1_Cards


    print("\n\nPlayer ", player, " turn...")
    print("Your card is: ", playerDeck[0], "\n")

    for index in range(len(Players[playerDeck[0]])):
        print([index], Parameters[index], Players[playerDeck[0]][index])


    choice = input("\n [choice] >> ")

    try:
        choice = int(choice)
        
    except ValueError:
        print("Incorrect answer, random skill assigned")
        choice = random.randint(0,5)
    

    print("\n\nOpposition card,", opposDeck[0], "has", Format_Parameters[choice], "level ", Players[opposDeck[0]][choice])
    print("Player card,", playerDeck[0], "has", Format_Parameters[choice], "level ", Players[playerDeck[0]][choice])

    if Players[opposDeck[0]][choice]<Players[playerDeck[0]][choice]:
        print("\nPlayer", player, "has won the round")

        playerDeck.append(playerDeck[0])
        playerDeck.append(opposDeck[0])
        
        playerDeck.pop(0)
        opposDeck.pop(0)

        if len(opposDeck) < 1:
            local_finished
            finished = "win" ## make local finished and then set if descision in main to choose 
            return finished
        
    else:
        print("\nPlayer", opposition, "has won the round")

        opposDeck.append(opposDeck[0])
        opposDeck.append(playerDeck[0])
        
        opposDeck.pop(0)
        playerDeck.pop(0)

        if len(playerDeck) < 1:
            finished = "loss"
            return finished


    print("\n\n-------------------------------")
    print("Cards remaining: ")
    print("Player 1", len(Player_1_Cards))
    print("Player 2", len(Player_2_Cards))
    print("-------------------------------")


def main():

    finished = False ## Flag that denotes when the game should continue
    
    player = 1 ## this is "player's turn". 1 means "Player 1" and 2 means "Player 2"

    while finished == False:
        
        move(player, finished)

        if finished == False:  

            if player == 1:
                player = 2
            else:
                player = 1

    if player == 1:
        opposition_end = 2
    else:
        opposition_end = 1

        
    print("\n")

    if finished == "loss":
        print("Player", player, "has lost the game")
        print("Player", opposition_end, "has won the game")
        
    else:
        print("Player", player, "has won the game")
        print("Player", opposition_end, "has lost the game")

    input("\n\nPress enter to now quit >> ")

main()

