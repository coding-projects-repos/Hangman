# Hangman

1. [Description](#description)
2. [Prerequisites](#prerequisites)
3. [Prompt](#prompt)
4. [Testing](#testing)
5. [Extensions](#extensions)

## Description

Hangman is a fun but challenging game to implement in any language. This version will be a robust one which handles many corner cases and is very communicative to the player.

## Prerequisites

You should be familiar with the following topics:

- Loops
- String manipulation
- Functions
- Conditional statements
- Getting user input

## Prompt

At the beginning of the program, hidden to the user, you should have a list of single words or phrases, without spaces. This will serve as your "word bank", from which you will randomly select a word for the user's play. Once a word is selected, you should show the blank spaces `_` (one for each letter) and repeatedly ask the user for a letter until either they guess the word, or they run out of incorrect guesses. The user should have a set number of incorrect guesses (suggested is six - one head, one body, one for each limb), but correctly guessing a letter should not count as an incorrect guess.

After every guess, the user should be able to see:

- The blank letters in the word, with correctly-guessed letters filled in
- Their correctly guessed letters
- Their incorrectly guessed letters
- How many incorrect guesses they have left

## Testing

Once you think you have finished your program, you should play it extensively, testing every outcome that can happen. In the context of this game, for example, you'll want to play where:

- You guess the same letter multiple times in a row (you should not lose guesses)
- You guess the word correctly
- You guess the word incorrectly

You'll also want to pay special attention to:

- The game accurately displays the number of guesses remaining
- The game accurately displays the letters that have been guessed

Here's a sample output for what your program might look like:

```
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _
Guess a letter: a

Nope!
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _
Correct letters: []
Incorrect letters: ['a']
Chances: 1/6
Guess a letter: e

Good!
_ _ _ _ _ _ e _ _ _ _ e _ _ e
Correct letters: ['e']
Incorrect letters: ['a']
Chances: 1/6
Guess a letter: i

Good!
_ _ _ _ _ _ e _ _ _ i e _ _ e
Correct letters: ['e', 'i']
Incorrect letters: ['a']
Chances: 1/6
Guess a letter: o

Good!
_ o _ _ _ _ e _ _ _ i e _ _ e
Correct letters: ['e', 'i', 'o']
Incorrect letters: ['a']
Chances: 1/6
Guess a letter: u

Good!
_ o _ _ u _ e _ _ _ i e _ _ e
Correct letters: ['e', 'i', 'o', 'u']
Incorrect letters: ['a']
Chances: 1/6
Guess a letter: t

Good!
_ o _ _ u t e _ _ _ i e _ _ e
Correct letters: ['e', 'i', 'o', 'u', 't']
Incorrect letters: ['a']
Chances: 1/6
Guess a letter: m

Good!
_ o m _ u t e _ _ _ i e _ _ e
Correct letters: ['e', 'i', 'o', 'u', 't', 'm']
Incorrect letters: ['a']
Chances: 1/6
Guess a letter: h

Nope!
_ o m _ u t e _ _ _ i e _ _ e
Correct letters: ['e', 'i', 'o', 'u', 't', 'm']
Incorrect letters: ['a', 'h']
Chances: 2/6
Guess a letter: s

Good!
_ o m _ u t e _ s _ i e _ _ e
Correct letters: ['e', 'i', 'o', 'u', 't', 'm', 's']
Incorrect letters: ['a', 'h']
Chances: 2/6
Guess a letter: c

Good!
c o m _ u t e _ s c i e _ c e
Correct letters: ['e', 'i', 'o', 'u', 't', 'm', 's', 'c']
Incorrect letters: ['a', 'h']
Chances: 2/6
Guess a letter: p

Good!
c o m p u t e _ s c i e _ c e
Correct letters: ['e', 'i', 'o', 'u', 't', 'm', 's', 'c', 'p']
Incorrect letters: ['a', 'h']
Chances: 2/6
Guess a letter: r

Good!
c o m p u t e r s c i e _ c e
Correct letters: ['e', 'i', 'o', 'u', 't', 'm', 's', 'c', 'p', 'r']
Incorrect letters: ['a', 'h']
Chances: 2/6
Guess a letter: n

Good!
c o m p u t e r s c i e n c e
Correct letters: ['e', 'i', 'o', 'u', 't', 'm', 's', 'c', 'p', 'r', 'n']
Incorrect letters: ['a', 'h']
Chances: 2/6

You got it!  Great job!
```

## Extensions

### Support Spaces

Add functionality to allow spaces in words. Spaces are different in the sense that they aren't letters that have to be guessed, and they should not be printed as an "unguessed" character.

Adding space functionality to this project will change at least the following areas:

- How your game prints the word
- How your game knows if the word has been guessed or not
- How your guesses are handled (what if someone guesses a space?)

Adding this functionality would open your game words up to new possibilities, from short phrases to entire sentences!

### Simple ASCII Graphics

ASCII art can be fun sometimes, and in games like this, we can implement some very simple graphics to complement our game. For example, the hangman stand can look something like this:

```
_____
|/  |
|
|
|
|
+-----+
```

This would get printed with every guess. But when the user starts to guess the wrong letters...

```
_____
|/  |
|   O
|
|
|
+-----+
```

Until eventually we get to this point:

```
_____
|/  |
|   O
|  /|\
|  / \
|
+-----+
```

_(morbid? maybe a little bit)_

In any case, there are six characters to draw, hence six chances for the player.
