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




"""(101 , "omkar" , 10 , "yellow" , 100 , "a", "mumbai" ),
(102 , "sai" , 9 , "red" , 55 , "c", "delhi" ),
(103 , "vaishnavi" , 8 , "black" , 98 , "a", "banglore" ),
(104 , "rupali" , 7 , "green" , 35 , "e", "chennai" ),
(105 , "sanjay" , 6 , "orange" , 45 , "d", "thane" ),
(106 , "parvati" , 5 , "grey" , 87 , "a", "mumbai" ),
(107 , "pushpalata" , 4 , "pink" , 72 , "b", "delhi" ),
(108 , "janardhan" , 3 , "pink" , 67 , "c", "banglore" ),
(109 , "mayur" , 2 , "grey" , 22 , "f", "chennai" ),
(110 , "reshma" , 1 , "red" , 77 , "b", "thane" ),
(111 , "shiv" , 10 , "orange" , 82 , "b", "mumbai" ),
(112 , "priyanka" , 8 , "brown" , 90 , "a", "delhi" ),
(113 , "paresh" , 6 , "red" , 70 , "b", "banglore" ),
(114 , "pranesh" , 10 , "blue" , 63 , "c", "chennai" ),
(115 , "ashok" , 1 , "green" , 45 , "d", "thane" ),
(116 , "meena" , 10 , "yellow" , 77 , "b", "mumbai" ),
(117 , "nikhil" , 3 , "green" , 100 , "a", "delhi" ),
(118 , "pranay" , 9 , "orange" , 16 , "f", "banglore" ),
(119 , "om" , 5 , "yellow" , 90 , "a", "chennai" ),
(120 , "bablu" , 4 , "blue" , 82 , "b", "thane" );"""