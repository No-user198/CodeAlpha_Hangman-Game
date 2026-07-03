"""
A simple text-based Hangman game where the player guesses a word
one letter at a time.

Key Concepts Used: random, while loop, if-else, strings, lists.
"""

import random

# Small predefined list of words (no file/API needed)
WORDS = ["python", "hangman", "coding", "developer", "internship"]

MAX_ATTEMPTS = 6


def choose_word(word_list):
    """Randomly select a word from the word list."""
    return random.choice(word_list)


def display_word(word, guessed_letters):
    """Show the word with guessed letters revealed and others as underscores."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def play_hangman():
    word = choose_word(WORDS)
    guessed_letters = []
    wrong_guesses = 0

    print("=" * 40)
    print("       WELCOME TO HANGMAN GAME")
    print("=" * 40)
    print(f"You have {MAX_ATTEMPTS} incorrect guesses allowed.")
    print(f"The word has {len(word)} letters.\n")

    while wrong_guesses < MAX_ATTEMPTS:
        print("Word: ", display_word(word, guessed_letters))
        print(f"Wrong guesses: {wrong_guesses}/{MAX_ATTEMPTS}")
        print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")

        guess = input("\nGuess a letter: ").lower().strip()

        # Basic input validation
        if len(guess) != 1 or not guess.isalpha():
            print(">> Please enter a single valid letter.\n")
            continue

        if guess in guessed_letters:
            print(">> You already guessed that letter. Try another.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f">> Good guess! '{guess}' is in the word.\n")
        else:
            wrong_guesses += 1
            print(f">> Wrong guess! '{guess}' is not in the word.\n")

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print("=" * 40)
            print(f"🎉 Congratulations! You guessed the word: '{word}'")
            print("=" * 40)
            return

    # Player lost
    print("=" * 40)
    print("💀 Game Over! You've run out of attempts.")
    print(f"The correct word was: '{word}'")
    print("=" * 40)


def main():
    play_again = "y"
    while play_again == "y":
        play_hangman()
        play_again = input("\nPlay again? (y/n): ").lower().strip()
    print("\nThanks for playing Hangman! Goodbye 👋")

if __name__ == "__main__":
    main()
