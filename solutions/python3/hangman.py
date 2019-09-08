# name      letter_in_word
# args      guess: the letter the player is guessing
#            word: the correct word
#            correct_letters: list of correctly guessed letters
#            incorrect_letters: list of incorrectly guessed letters
# purpose   Check if guessed letter is in word, and then update each list of
#            correct/incorrect letters accordingly
# returns   TRUE if guess is in word
#            FALSE if guess is not in word
def letter_in_word(guess, word, correct_letters, incorrect_letters):
    if guess in word:
        correct_letters.append(guess)
        return True
    else:
        incorrect_letters.append(guess)
        return False

# name      get_guess
# args      word: the correct word
#            correct_letters: list of correctly guessed letters
#            incorrect_letters: list of incorrectly guessed letters
# purpose   get a valid guess from the user and make sure it is only
#            one character long and an alphabet letter
# returns   the user's guess, lowercase version
def get_guess(word, correct_letters, incorrect_letters):
    while 1:
        guess = input("Guess a letter: ")
        if not (guess.isalpha() and len(guess) == 1):
            print("Invalid input, try again")
        else:
            if has_letter_been_guessed(guess, correct_letters, incorrect_letters):
                print("Letter already guessed, try again")
            else:
                return guess

# name      has_letter_been_guessed
# args      guess: player's guess
#            correct_letters: list of correctly guessed letters
#            incorrect_letters: list of incorrectly guessed letters
# purpose   check if the letter has already been guessed or not, either correctly
#            or incorrectly
# returns   True if it has been guessed already
#            False if it has not
def has_letter_been_guessed(guess, correct_letters, incorrect_letters):
    if guess in correct_letters or guess in incorrect_letters:
        return True
    else:
        return False

# name      word_guessed
# args      word: the correct word
#            correct_letters: list of correctly guessed letters
# purpose   check if the user has won or not
# returns   True if all the letters in the word have been guessed correctly
#            False if not
def word_guessed(word, correct_letters):
    for letter in word:
        if letter not in correct_letters:
            return False
    return True

# name      get_word_string
# args      word: the correct word
#            correct_letters: list of correctly guessed letters
# purpose   creates a string representing each letter in a word, with
#            blank spaces ( "_" ) for letters that have not been correctly guessed
#               example: word = "hello", correct_letters = ['e','o']
#               would return: "_ e _ _ o "
# returns   The string described above
def get_word_string(word, correct_letters):
    result = ""
    for letter in word:
        if letter not in correct_letters:
            result = result + "_ "
        else:
            result = result + letter + " "
    return result

# name      is_game_over
# args      num_guesses: current number of incorrect guesses made by player
#            max_guesses: maximum number of incorrect guesses allowed
#            word: the correct word
#            correct_letters: list of correctly guessed letters
# purpose   check to see if the game is over, with three possibilities:
#               Player won - all the letters in word have been guessed (use word_guessed() )
#               Player lost - player has run out of guesses
#               Neither of the above is true - game is still going on
# returns   True if the game has ended
#            False if the game is still going on
def is_game_over(num_guesses, max_guesses, word, correct_letters):
    if num_guesses >= max_guesses or word_guessed(word, correct_letters):
        return True
    else:
        return False

# main function with game loop
def main():
    #words = []
    word = "computerscience"
    correct_letters = []
    incorrect_letters = []
    max_guesses = 5
    wrong_guesses = 0
    print(get_word_string(word, correct_letters))
    
    while not is_game_over(wrong_guesses, max_guesses, word, correct_letters):
        guess = get_guess(word, correct_letters, incorrect_letters)
        
        if letter_in_word(guess, word, correct_letters, incorrect_letters):
            print("Good!")
        else:
            print("Nope!")
            wrong_guesses = wrong_guesses + 1
        
        print(get_word_string(word, correct_letters))
        print("Correct letters: " + str(correct_letters))
        print("Incorrect letters: " + str(incorrect_letters))
        print("Chances: " + str(wrong_guesses) + "/" + str(max_guesses))

if __name__ == "__main__":
    main()