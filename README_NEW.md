There are 2 files:

1- mystery_word.py is the traditional hangman game including the hard version.
The game will ask the user for a letter giving them 8 tries and showing
the state of the game at every iteration (the word_in_process, the characters
that have been selected, and the number of tries left). If invalid characters
or previously selected characters are entered, the user is notified but they
don't miss a turn. They only miss a turn when the character entered
is not part of the word.

The game continues until the user guesses the word, or until the 8 tries
are used.  At the end of the game the user will be asked if they want to play again

2- evil_hangman.py is the implementation of the evil hangman algorithm.
The computer is basically tricking the user and selecting new possible
words at every iteration. The new possible words are selected out of the
match with more possible words.  The game ends when the user guesses the word
(which is practically impossible in 8 tries), or when the 8 tries are used.
At the end of the game the program will print "a" word telling the user
that was the word selected.  It will also ask if they want to play again.
