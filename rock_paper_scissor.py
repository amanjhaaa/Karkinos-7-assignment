from random import randint 
moves = ["rock" , "paper" ,"scissor"]

while True:
    computer = moves[randint(0,2)]
    player = input("rock paper or scissor? (or end the game)::").lower()
    if player == "end the game":
        print("YThe game has ended")
        break
    elif player == computer:
        print("computer choosen = " , computer )
        print("The match is tie!!!!")
    elif player == "rock":
        if computer == "paper":
            print("computer choosen = " , computer )
            print("You lose!")
        else:
            print("computer choosen = " , computer )
            print("You win") 

    elif player == "paper":
        if computer == "scissor":
            print("computer choosen = " , computer )
            print("you lose!") 
        else:
            print("computer choosen = " , computer )
            print("You win") 

    elif player =="scissor":
        if computer =="rock":
            print("computer choosen = " , computer )
            print("You lose!")
        else:
            print("computer choosen = " , computer )
            print("You win")
    else:
        print("GIve the valid input")