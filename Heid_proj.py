
import random
import math
import time
from time import sleep

# Function to build and return random card deck
def BuildDeck ():
    built_deck = [0 for _ in range(52)]  # initialize list
    used_card = [False for _ in range(52)] # boolian list to track used cards
    i = 0
    
    while i < 52:
        card = random.randint(0,51)  #RNG
        # Assigns RNG to deck if not already used
        if used_card[card] is False: 
            built_deck[i] = card
            used_card[card] = True  # Mark TRUE for used
            i += 1
        else:
            card = random.randint(0,51)  # Reassign RNG if already used
            
    return (built_deck) #returns random list 0-51 wihtout duplication.

# Function takes in single int 0-51, returns coresponding card    
def PrintCard(card):
    rank = card % 13
    suit = math.floor(card / 13)
   
    if rank == 0:
        rank = "K"
    elif rank == 1:
        rank = "A"
    elif rank == 11:
        rank = "J"
    elif rank == 12:
        rank = "Q"
        
    if suit == 0:
        return(str(rank)+ "\u2663") # Club
    elif suit == 1:
        return(str(rank)+ "\u2665")  # Heart
    elif suit == 2:
        return(str(rank)+ "\u2666" ) # Diamond
    elif suit == 3:
        return(str(rank)+ "\u2660")   # Spade  

# Function takes in deck list, playing grid, and chosen column
def PickUp(deck, play_matrix, col):
    card = 0
    first = 0 # for column order
    last = 0  # for column order
    
    # statement to rearrange columns
    if col == 0:
        first = 1
        last = 2
    elif col == 1:
        first = 0
        last = 2
    elif col == 2:
        first = 1
        last = 0
        
    for row in range(7):     # first column to be picked up
        deck[card] = play_matrix[row][first]
        card += 1

    for row in range(7):     # for middle column (chosen column)
        deck[card] = play_matrix[row][col]
        card += 1

    for row in range(7):     # last column to be picked up
        deck[card] = play_matrix[row][last]
        card += 1

# Function to display cards in 3x7 grid
def Deal(deck_list, play_matrix):
    card = 0

    for r in range(7):  #Rebuilds play matrix with deck list
        for c in range(3):
            play_matrix[r][c] = deck_list[card]
            card += 1
            
    print("\nColumn   0       1       2 ")
    print("        ====================")
    
    #  Prints out each row with proper card symbol
    card=0
    for _ in range(7):
        col1 = PrintCard(deck_list[card])
        card+=1
        col2 = PrintCard(deck_list[card])
        card+=1
        col3 = PrintCard(deck_list[card])
        card+=1
        
        print("\t", col1, "\t", col2, "\t", col3)

#  reveals 11th card in deck (index10)    
def SecretCard(deck_list):
    print("\nFinding secret card", end=' ')

    loading = ".........."
    for i in range(10):
        print(loading[i], sep=' ', end=' ', flush=True); sleep(0.4)
    
    secret_card = PrintCard(deck_list[10])
    print(" \n")
    print(secret_card, "is your secret card.")
    
# Function takes in string input, returns boolean
def ask_yesno(question):
    ans = ""
    while True:
        ans = input(question + " [y/n] ")
        if ans == "y":
            return True
        elif ans == "n":
            return False     
        
# Main game sequence    
def GAME():
    
    print("\nLet's play a card game!")
    name = input("What's your name? ")
    name = name.capitalize()
    print("Hello, " + name + ".", end = " ")
    if ask_yesno("Would you like to see the Deck?\n") is True:
        for rw in range(4):  #Displays cards if prompted
            shw = []
            bye = "',[]" #Strings to remove
            for cl in range(13):
                crd=PrintCard(rw*13+cl)
                shw.append(crd)   
            shw = str(shw) 
            for bye in bye:  
                shw = shw.replace(bye,"")
            print(shw)

    game_deck = BuildDeck()
    game_deck = game_deck[0:21] #RNG deck with only first 21 cards
    
    play = [[0,0,0] for _ in range(7)]  #Empty grid/matrix for game
    
    time.sleep(1)
    print("\n\nOkay! Please pick a card below and remember it.")

    for _ in range(3):
        Deal(game_deck,play)  #Function call to display game deck
        column = 3
        while column < 0 or column > 2:
                column = input("\nWhich column is your card in? (0, 1, or 2)\n")
                column = int(column)
        time.sleep(.5)    
        PickUp(game_deck, play, column) #Function call to retreive game deck
    
    SecretCard(game_deck)  #Function call to reveal secret card
    time.sleep(1)
    print("\n Thanks for playing,", name + "!\n")
    
GAME()  #Game Function call