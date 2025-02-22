import random

# List of words
words = ["python", "hangman", "coding", "program", "developer"]

# Choose a random word
word = random.choice(words)
guessed_word = ["_"] * len(word)
attempts = 6  # Number of allowed wrong guesses
guessed_letters = []

print("Welcome to Hangman!")
print(" ".join(guessed_word))

while attempts > 0 and "_" in guessed_word:
    guess = input("\nGuess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        print("Correct!")
    else:
        attempts -= 1
        print(f"Wrong! You have {attempts} attempts left.")

    print(" ".join(guessed_word))

# Check if the player won or lost
if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)

