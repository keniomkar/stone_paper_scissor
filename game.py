import random

comp_win = 0
user_win = 0

options = ["rock", "paper", "scissor"]

while True:
    user_input = input("Enter Rock/ Paper/ Scissor or Press Q to Quit :").lower()
    
    if user_input == "q":
        print("You Quit the Game")
        break
    
    if user_input not in options:
        print("Invalid Text")
        continue
    
    random_num = random.randint(0,2)
    comp_pick = options[random_num]
    print("Computer picked :", comp_pick)
    
    if user_input == "stone" and comp_pick == "scissor":
        print("You won")
        user_win += 1
        
    elif user_input == "scissor" and comp_pick == "paper":
        print("You won")
        user_win += 1
        
    elif user_input == "paper" and comp_pick == "stone":
        print("You won")
        user_win += 1
        
    elif user_input == comp_pick:
        print("Draw")
        
    else:
        print("You Lost")
        comp_win += 1
        
print("You won", user_win, "times")
print("computer won", comp_win, "times")

print("Goodbyee!")




