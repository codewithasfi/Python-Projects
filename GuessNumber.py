import random as rd

number = rd.randint(1,50)
flag=False

chances=5
attempts=0

while chances>=1:
    guess=int(input("Guess a number between 1-50:"))
    attempts+=1
    if guess==number:
        flag=True
        break
    elif guess>number:
        print("Guess a little low!")
    else:
        print("Guess a little high!")

    chances-=1

if (flag):
    print(f"You won! You took {attempts} to win!")

else:
    print("You lost :(")
    print("The number was",number)
