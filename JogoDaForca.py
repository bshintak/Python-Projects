import random

def choose_word():
    words = ["hello" , "please", "knife" , "enjoy" , "map", "justice", "location" , "poison" , "photograph" , "flavor" , "guitar",
    "word" , "light" , "falling" , "flower" , "happy" , "beauty" , "beach" , "water" , "coffee" , "mirror" , "chill" , "music"]
    return random.choice(words)

def show_forca(error):
    forca = [
        """
           ------
           |    |
           |
           |
           |
           |
        ------
        """,
        """
           ------
           |    |
           |    O
           |
           |
           |
        ------
        """,
        """
           ------
           |    |
           |    O
           |    |
           |
           |
        ------
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        ------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |
           |
        ------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        ------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        ------
        """
    ]
    print(forca[error])

def show_hidden_word(word, correct_letters):
    for letter in word:
        if letter in correct_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()

def play_jogo_da_forca():
    word_secret = choose_word()
    correct_letters = set()
    incorrect_letters = set()
    maximum_attempts = 6
    error = 0

    print("Welcome to the Jogo da Forca!")

    while error < maximum_attempts:
        show_forca(error)
        show_hidden_word(word_secret, correct_letters)

        attempt = input("Choose a letter: ").lower()

        if len(attempt) != 1 or not attempt.isalpha():
            print("Please, enter a single valid letter.")
            continue

        if attempt in correct_letters or attempt in incorrect_letters:
            print("You've already tried this letter. Try another.")
            continue

        if attempt in word_secret:
            correct_letters.add(attempt)
        else:
            incorrect_letters.add(attempt)
            error += 1

        if set(correct_letters) == set(word_secret):
            print("Congratulations! You guessed the word:", word_secret)
            break

    if error == maximum_attempts:
        show_forca(error)
        print(f"Game over! The word was: {word_secret}")

if __name__ == "__main__":
    play_jogo_da_forca()
