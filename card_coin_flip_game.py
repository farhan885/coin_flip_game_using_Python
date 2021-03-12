"""
Project description

Intro To Game
1/ The player/user grabs a card from the deck

2/ The card will have heads or tails. Whichever card the user receives will determine his next move

3/ The player will flip the coin after picking a card.

4/ Once the player has flip his/her if it lands on the side that the cards says than the player moves 3 spaces.

5/ if the coin lands on the opposite side and not the same as the card they drew then the player will go back two spaces.

6/ when either player hits 30 points they will win
"""

# importing libraries
import random

# 1/ The player/user grabs a card from the deck
cardsValues = list(range(1,50))
moves = [3,2]

player1_score = 0
player2_score = 0

flips = 50

while flips > 0:
    
    flips = flips-1

    while True:
        print("Player-1's turn")
        
        try:
            card =  int(input("Pick a Card 1-50: "))
            
            #2/ The card will have heads or tails. Whichever card the user receives will determine his next move
            print("Before going to flip the coin ")
            card_head_tail = int(input("Please choose 1 for head or 0 for tail of the card: "))
            if card_head_tail == 0 or card_head_tail == 1:
                #3/ The player will flip the coin after picking a card.
                input("press enter key to flip the coin: ")
                coin_flip = random.randint(0, 1)

                #4/ Once the player has flip his/her if it lands on the side that the cards says than the player moves 3 spaces.
                if coin_flip == card_head_tail:
                    player1_score = player1_score + moves[0]
                    print(player1_score)
                    break
                #5/ if the coin lands on the opposite side and not the same as the card they drew then the player will go back two spaces.

                else:
                    player1_score = player1_score - moves[1]
                    print(player1_score)
                    break
        except ValueError:
            print("please use numbers only.")
            
        else:
            print("please enter 0 or 1 only!")

    while True:
        print("Player-2's turn")
        
        try:
            card =  int(input("Pick a Card 1-50: "))
            print("Before going to flip the coin ")
            card_head_tail = int(input("Please choose 1 for head or 0 for tail of the card: "))

            if card_head_tail == 0 or card_head_tail == 1:
                input("press any key to flip the coin: ")
                coin_flip = random.randint(0, 1)

                if coin_flip == card_head_tail:
                    player2_score = player2_score + moves[0]
                    print(player2_score)
                    break
                else:
                    player2_score = player2_score - moves[1]
                    print(player2_score)
                    break
        except ValueError:
            print("please use numbers only.")
            
        else:
            print("please enter 0 or 1 only!")
        
#6/ when either player hits 30 points they will win
if player1_score == 30:
    print("Player-1 won")
elif player2_score == 30:
    print("Player-2 won")
else:
    print("Game draw!")