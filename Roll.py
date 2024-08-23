import random

def roll():
    min_value=1
    max_value=6
    roll=random.randint(min_value,max_value)
    
    return roll

value=roll()


while True:
    players=int(input("Enter number of players (2 - 4): "))

    if players>=2 and players<=4:
        break
    else:
        print("Must be between 2 - 4 players!")

print("Number of players: ",players)

max_Score=50
players_Score=[0 for i in range(players)]

while max(players_Score)<max_Score:

    for players_index in range(players):
        
        if max(players_Score) >= max_Score:
            break 
    
        print("\nPlayer",players_index+1,"turn has just started!\n")
        current_score=0


        while True:
            should_roll=input("Would you like to roll (y) ? ")
            if should_roll != 'y':
                break
            else:
                value=roll()

                if value==1:
                    print("You rolled a 1! You lost all the score you made!")
                    current_score=0
                    break
                else:
                    current_score=current_score+value
                    print("You rolled a : ",value)

            print("Your score for this turn is:" ,current_score)
        
        players_Score[players_index]+=current_score
        print("Your total score: ",players_Score[players_index])

winner_index = players_Score.index(max(players_Score))
print("\nPlayer", winner_index + 1,"wins with a score of",players_Score[winner_index],"!")