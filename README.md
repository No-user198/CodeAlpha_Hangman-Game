
# Hangman Game 🎮
A simple text-based Hangman game built in Python, where the player tries to guess a hidden word one letter at a time before running out of attempts.

## 📌 About the Project
This project is part of the **CodeAlpha Python Programming Internship**. It's a classic console-based Hangman game that demonstrates core Python fundamentals like loops, conditionals, string manipulation, and randomization.

## 🚀 Features
- Randomly selects a word from a predefined word list
- Displays word progress with guessed letters revealed and unguessed letters hidden
- Tracks and displays wrong guesses (out of a maximum of 6 attempts)
- Validates user input (rejects empty input, multiple characters, or repeated guesses)
- Play again option after each round
- Clean, beginner-friendly console interface

## 🛠️ Technologies Used
- Python 3
- Built-in `random` module (no external libraries required)

## 🧠 Concepts Applied
- Loops (`while`)
- Conditional statements (`if-else`)
- Functions
- Lists and strings
- Random module

## 📂 Project Structure
```
CodeAlpha_HangmanGame/
│
├── hangman.py       # Main game script
└── README.md         # Project documentation
```

## ▶️ How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/CodeAlpha_HangmanGame.git
   ```
2. Navigate to the project folder:
   ```bash
   cd CodeAlpha_HangmanGame
   ```
3. Run the script:
   ```bash
   python hangman.py
   ```

## 🎯 How to Play
1. The game randomly picks a word and shows blanks for each letter.
2. Enter one letter at a time when prompted.
3. Correct guesses reveal the letter's position(s) in the word.
4. Incorrect guesses reduce your remaining attempts (starts at 6).
5. Win by guessing the full word before running out of attempts!
6. After the game ends, choose to play again or exit.

## 📸 Sample Output
```
========================================
       WELCOME TO HANGMAN GAME
========================================
You have 6 incorrect guesses allowed.
The word has 6 letters.

Word:  _ _ _ _ _ _
Wrong guesses: 0/6
Guessed letters: None

Guess a letter: p
>> Good guess! 'p' is in the word.

Word:  p _ _ _ _ _
Wrong guesses: 0/6
Guessed letters: p
```

## 🔮 Future Improvements
- Add difficulty levels with larger word lists
- Add a hint system
- Display an ASCII hangman figure that updates with wrong guesses
- Load words from an external file or API

## 🏆 Internship
This project was completed as part of the **CodeAlpha Python Programming Internship**, which focuses on strengthening Python fundamentals through hands-on projects.

## 📞 Contact
Feel free to reach out or connect for feedback and suggestions!

---
⭐ If you found this project helpful, consider giving it a star on GitHub!
