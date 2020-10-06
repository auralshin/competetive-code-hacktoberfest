import random

print("H A N G M A N")
words = ["python", "java", "kotlin", "javascript"]
random.seed()

while True:
    menu_selection = ""
    #while menu_selection not in ["play", "exit"]:
        #menu_selection = input('Type "play" to play the game, "exit" to quit: ')
    if menu_selection == "exit":
        break

    word = random.choice(words)
    word_length = len(word)
    hint = ["-"] * word_length
    lives = 8
    previous_guesses = []
    while lives > 0:
        print()
        print("".join(hint))
        guess = input("Input a letter: ")
        if len(guess) != 1:
            print("You should input a single letter")
            continue
        if not (guess.isascii() and guess.islower()):
            print("It is not an ASCII lowercase letter")
            continue
        if guess in previous_guesses:
            print("You already typed this letter")
            continue
        previous_guesses.append(guess)
        if guess in word:
            for i in range(word_length):
                if word[i] == guess:
                    hint[i] = guess
            if "".join(hint) == word:
                print("You guessed the word!")
                print("You survived!")
                break
        else:
            print("No such letter in the word")
            lives -= 1

    if lives == 0:
        print("You are hanged!")

    print()
    break
