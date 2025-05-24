import random

print("===================")
print("Rock Paper Scissors")
print("===================")
print("1) ✊")
print("2) ✋")
print("3) ✌️")

player = int(input("Pick a number: "))

computer = random.randint(1,3)

gestures = {1: "✊ Rock", 2: "✋ Paper", 3: "✌️ Scissors"}

print("You chose:", gestures[player])
print("CPU chose:", gestures[computer])


if (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):

    print("The player won!")

elif player == computer:
    
    print("No winner!")

else:
    
    print("The computer won!")
