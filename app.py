import random

def choose_random_word():
    words = ["python", "programming", "hangman", "computer", "algorithm", "developer", "game"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    print("Welcome to Hangman!")
    secret_word = choose_random_word()
    guessed_letters = []
    incorrect_attempts = 0
    max_attempts = 6

    while True:
        current_display = display_word(secret_word, guessed_letters)
        print(f"Word: {current_display}")
        print(f"Guessed Letters: {', '.join(guessed_letters)}")
        print(f"Incorrect Attempts: {incorrect_attempts}/{max_attempts}")

        if current_display == secret_word:
            print("Congratulations! You guessed the word!")
            break

        if incorrect_attempts == max_attempts:
            print(f"Sorry, you've run out of attempts. The correct word was '{secret_word}'.")
            break

        try:
            guess = input("Enter a letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                raise ValueError("Please enter a single letter.")

            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess in secret_word:
                print("Good guess!")
                guessed_letters.append(guess)
            else:
                print("Incorrect guess.")
                guessed_letters.append(guess)
                incorrect_attempts += 1

        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    hangman()
