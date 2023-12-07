import random
options=("rock","paper","scissors")
playing=True
while playing:
    player=None
    computer=random.choice(options)
    while player not in options:
        print("please type your choice")
        player=input("enter a choice (rock, paper, scissors): ")
    print(f"player: {player}")
    print(f"computer: {computer}")
    if player=='rock':
        if computer=="rock":
            print("Its a tie")
        elif computer=="paper":
            print("computer wins")
           
        else:
            print("You win!")
            
    elif player=="paper":
        if computer=="paper":
            print("Its a tie")
        elif computer=="rock":
            print("You win!")
        
        else:
            print("computer wins")
            
    else:
        if computer=="scissors":
            print("its a tie")
        elif computer=="paper":
            print("You win!")
    
        else:
            print("computer wins")
    print("please type y if you want to play again")
    
    if not input("Play again(y/n): ").lower()=='y':
        playing=False

print("THANKS FOR PLAYING")

