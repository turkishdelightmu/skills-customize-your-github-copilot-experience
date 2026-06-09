# 📘 Assignment: Games in Python

## 🎯 Objective

Build a simple Hangman game in Python by using strings, loops, conditionals, and random selection. This assignment helps students practice user input, game state tracking, and basic program flow.

## 📝 Tasks

### 🛠️ Game Setup

#### Description
Create the core structure for the Hangman game using the provided starter code.

#### Requirements
Completed program should:

- Choose a random word from a predefined list
- Show the current word as underscores, such as `_ _ _ _ _`
- Store guessed letters and the number of remaining attempts
- Prompt the player to enter a letter on each turn

### 🛠️ Game Logic and End Conditions

#### Description
Add the logic that updates the board, checks guesses, and ends the game when the player wins or runs out of attempts.

#### Requirements
Completed program should:

- Reveal matching letters in the secret word
- Reduce remaining attempts for incorrect guesses
- Display a win message when the word is fully guessed
- Display a lose message when attempts are exhausted
- Handle repeated guesses without breaking the game
