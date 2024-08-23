'''
STEPS:
    1.input from user(Rock,Paper,Scissor)
    2.computer choice(Random)-using random module
    3.print result
'''
'''
CASES:
    Case A-
     Rock-Rock=tie
     Rock-Paper= Paper win
     Rock-Scissor=Rock win

    Case B-
     Paper-Paper=tie
     Paper-Rock=Paper win
     Paper-Scissor=Scissor win

    Case c-
     Scissor-Scissor=tie
     Scissor-Rock=Rock win
     Scissor-Paper=Scissor win
'''

import random
item_list=["Rock","Paper","Scissor"]
user_choice=input("Enter your choice:[Rock,Paper,Scissor]")
comp_choice=random.choice(item_list)

print(f"Your choice={user_choice}, Computer's choice={comp_choice}")

if user_choice==comp_choice:
    print("Both chose the same. Its a tie!")
elif user_choice=="Rock":
    if comp_choice=="Paper":
        print("Paper covers Rock, Computer wins!")
    else:
        print("Rock crushes scissor, You win!")
elif user_choice=="Paper":
    if comp_choice=="Rock":
        print("Paper covers Rock, You win!")
    else:
        print("Scissor cuts Paper, Computer wins!")
elif user_choice=="Scissor":
    if comp_choice=="Rock":
        print("Rock crushes Scissor, Computer wins!")
    else:
        print("Scissor cuts Paper, You win!")
