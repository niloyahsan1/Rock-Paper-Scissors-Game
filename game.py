import random

game_list = ["Rock", "Paper", "Scissors"]
comp_score = 0
player_score = 0

while True:
    computer = random.choice(game_list)
    print("================")
    player = int(input(f"Rock -> 1\nPaper -> 2\Scissors -> 3\nQuit -> 4\nEnter Your Choice: "))
    print("================")

    if player == computer:
        print("Tie!")

    elif player == 1:
        if computer == "Scissors":
            print("Player Won!")
            player_score += 1
        else:
            print("Compuer Won!")
            comp_score += 1

    elif player == 2:
        if computer == "Rock":
            print("Player Won!")
            player_score += 1
        else:
            print("Compuer Won!")
            comp_score += 1

    elif player == 3:
        if computer == "Paper":
            print("Player Won!")
            player_score += 1
        else:
            print("Computer Won!")
            comp_score += 1

    elif player == 4:
        break

    else: 
        print("Wrong Command!")

print(f"Player Quitted")
print()
print(f"Score: Computer-> {comp_score} and Player-> {player_score}")
print()
