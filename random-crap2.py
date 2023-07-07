import random

# List of words for the game
word_list = ["python", "hangman", "computer", "programming", "game", "openai"]

def play_hangman():
    # Select a random word from the list
    word = random.choice(word_list)

    # Initialize variables
    guessed_letters = []
    attempts = 6

    # Main game loop
    while True:
        # Display the current state of the word
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        print("\nWord:", display_word)

        # Prompt the player for a guess
        guess = input("Guess a letter: ").lower()

        # Check if the guessed letter is valid
        if not guess.isalpha() or len(guess) != 1:
            print("Invalid guess. Please enter a single letter.")
            continue

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        # Add the guessed letter to the list
        guessed_letters.append(guess)

        # Check if the letter is in the word
        if guess in word:
            print("Correct guess!")
        else:
            print("Wrong guess!")
            attempts -= 1

        # Check if the player has won or lost
        if "_" not in display_word:
            print("\nCongratulations! You guessed the word:", word)
            break
        elif attempts == 0:
            print("\nGame over! You ran out of attempts. The word was:", word)
            break

        # Display the remaining attempts
        print("Attempts left:", attempts)

# Start the game
print("Welcome to Hangman!")
play_hangman()
