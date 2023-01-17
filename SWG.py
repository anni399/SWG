# Snake Water Gun

# Rules:

# Snake vs. Water: Snake drinks the water, hence wins.
# Water vs. Gun: The gun will drown in water, hence a point for water.
# Gun vs. Snake: Gun shoots the snake, hence wins a point.

import random
print('Snake - Water - Gun')

options = ['s', 'w', 'g']

rounds = 1
computerScore = 0
userScore = 0

print("\nLet's Play\nWe'll both get 8 chances!\n")

while rounds <= 8:

    print(f"Round :{rounds}")
    print("\nType 's' to choose Snake\n\t'w' for Water\n\t'g' for Gun\n")

    userChoice = input("Enter Your Choice: ")

    if userChoice != 's' and userChoice != 'w' and userChoice != 'g':
        print("\nInvalid Input, Try Again\n")
        continue

    computerChoice = random.choice(options)

    print(f"\nComputer's Choice is:{computerChoice}")

    if computerChoice == 's':
        if userChoice == 'w':
            computerScore += 1
            print(f"\nComputer Won Round {rounds}\n")
        elif userChoice == 'g':
            userScore += 1
            print(f"\nYou Won Round {rounds}\n")
        else:
            print("\nRound's a Tie!\n")

    elif computerChoice == 'w':
        if userChoice == 'g':
            computerScore += 1
            print(f"\nComputer Won Round {rounds}\n")
        elif userChoice == 's':
            userScore += 1
            print(f"\nYou Won Round {rounds}\n")
        else:
            print("\nRound's a Tie!\n")

    elif computerChoice == 'g':
        if userChoice == 's':
            computerScore += 1
            print(f"\nComputer Won Round {rounds}\n")
        elif userChoice == 'w':
            userScore += 1
            print(f"\nYou Won Round {rounds}\n")
        else:
            print("\nRound's a Tie!\n")

    else:
        print("Something Went Wrong! Try Again")

    rounds += 1

print("\nGame Over\n\n\tScoreBoard\n")
print(f"\t You: {userScore} | Computer: {computerScore}")

if userScore > computerScore:
    print("\nYou Win!\n")
elif computerScore > userScore:
    print("\nYou Lose!\n")
else:
    print("\nGame is Drawn!\n")
