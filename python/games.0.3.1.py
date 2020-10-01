
import random

print("Enter the Your name ")
player1 = input()
print('Press 1 to play rock-paper-scissor or press 2 to play guessing game')
x = int(input())
if x == 2:
    random_number = random.randint(1, 20)
    guess = None
    number_try = 1
    while True:
        guess = int(input("Pick a number from 1 to 20: "))
        if guess < random_number:
            print("your guess is LOW!")
            number_try += 1
        elif guess > random_number:
            print("your guess is HIGH!")
            number_try += 1
        else:
            print("YOU WON!!!!")
            print(f"You got your answer in {number_try} tries.")
            play_again = input("Do you want to play again? (y/n) ")
            if play_again == "y":
                random_number = random.randint(1, 20)
                guess = None
            else:
                print("Thank you for playing!")
                break


elif x == 1:
    player_score = 0
    computer_score = 0
    print("Enter the number of points you want play for: ")
    points = int(input())
    while player_score < points and computer_score < points:
        print(f"computer score = {computer_score}\t {player1} score = {player_score}")
        print("Rock 👊\n")
        print("Paper 🤚\n")
        print("Scissor ✌\n")
        input1 = input()
        lists = random.randint(0, 3)
        if lists == 0:
            inputc = 'rock'
        elif lists == 1:
            inputc = 'scissor'
        else:
            inputc = 'paper'

        if input1 == "Rock" or input1 == "rock":
            if inputc == "Paper" or inputc == "paper":
                print(f"Computer won the game.")
                computer_score += 1
            elif inputc == "Scissor" or inputc == "scissor":
                print(f"{player1} won the game.")
                player_score += 1
            else:
                print(f"Its a tie.")

        if input1 == "Paper" or input1 == "paper":
            if inputc == "Scissor" or inputc == "scissor":
                print(f"Computer won the game.")
                computer_score += 1
            elif inputc == "Rock" or inputc == "rock":
                print(f"{player1} won the game.")
                player_score += 1
            else:
                print(f"Its a tie.")

        if input1 == "Scissor" or input1 == "scissor":
            if inputc == "Rock" or inputc == "rock":
                print(f"Computer won the game.")
                computer_score += 1

            elif inputc == "Paper" or inputc == "paper":
                print(f"{player1} won the game.")
                player_score += 1
            else:
                print(f"Its a tie.")

    if player_score > computer_score:
        print("Congratulations you win....")
    else:
        print("Computer wins!!!")
        print("Better Luck next time..")

else:
    print(f'Hello {player1} invalid input please try again')
