import random
from enum import IntEnum

class Computer(IntEnum):
    rock=0
    paper=1
    scissors=2
    
def playermove():
    x=input(f"{player_name} enter your move (rock[0],paper[1],scissors[2]) :  ")
    selection=int(x)
    action=Computer(selection)
    return action
    
         
def computermove():
    select=random.randint(0,len(Computer)-1)
    actions=Computer(select)
    return actions
     

print("ho welcome to rock-paper-scissors game ")
player_name=input(" please enter your name : ")
print(f"{player_name} lets start the game")

def starting():
    playerwin_score=0
    computerwin_score=0
    rounds=5
    while playerwin_score<rounds and computerwin_score<rounds:
        player_move=playermove()
        computer_move=computermove()
        if player_move==computer_move:
            print("this is tie")
        elif player_move==Computer.rock:
            if computer_move==Computer.paper:
                print("computer is winner")
                computerwin_score+=1
            else:
                print(f"{player_name} is winner")
                playerwin_score+=1
        elif player_move==Computer.paper:
            if computer_move==Computer.scissors:
                print("computer is winner")
                computerwin_score+=1
            else:
                print(f"{player_name} is winner")
                playerwin_score+=1
        elif player_move==Computer.scissors:
            if computer_move==Computer.rock:
                print("computer is winner")
                computerwin_score+=1
            else:
                print(f"{player_name} is winner")
                playerwin_score+=1
        else:
            print(f"something went wrong please try again {player_name}")
    print(f"{player_name}'s score is {playerwin_score} and computer's score is {computerwin_score}")
                        
starting() 
