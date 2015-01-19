from random import randint


def print_greeting():
    print("------------------------------------------------------------")
    print("Welcome to Mystery Word - aka Hangman")
    print()
    print("You will have 8 opportunities to enter a character")
    print("------------------------------------------------------------")


def validate_level(level):
    if level not in ["E", "N", "H"]:
        print("INVALID CHOICE! Valid Options are: E,e,N,n,H,h")
        return False
    else:
        return True


def get_level():
    while True:
        print("Enter the level desired")
        level_read = input("E/e for easy, N/n for normal, H/h for hard  ")
        level_read = level_read.upper()
        pass_level = validate_level(level_read)
        if pass_level is True:
            return level_read


def print_word_status(word, tries):
    print("-----------------------------------------------")
    print("You have {} guesses remaining".format(8 - tries))
    print("Used Letters: {}".format(",".join(characters_read)))
    print("Your current word:", ''.join(word))
    print("-----------------------------------------------")


def valid_letter(letter, chars_read):
    if len(letter) == 1:
        if letter not in chars_read:
            chars_read.append(letter)
            return True
        else:
            print("You already entered that character. Try again")
            return False
    else:
        return False


def get_letter(chars_read):
    while True:
        print("Enter your guess.")
        guess = input("A valid letter should be entered ").upper()
        pass_letter = valid_letter(guess, chars_read)
        if pass_letter is True:
            return guess


def look_for_match(letter, word):
    counter = 0
    indexes = []
    while counter < len(word):
        index_found = word.find(letter, counter)
        if index_found != -1:
            indexes.append(index_found)
            counter = index_found + 1
        else:
            counter += 1
    return indexes


def update_pattern_with_letter_match(letter, indexes, pattern):
    for index in indexes:
        pattern[index] = letter
    return pattern


def max_list(dict_options):
    maxvalue = 0
    for key, value in dict_options.items():
        if len(value) > maxvalue:
            maxvalue = len(value)
            maxlist = value
            maxindex = key
    return (maxindex, maxlist)


def evil_new_list(letter, currentlist, wip):
    # evil hangman calculates a new word list after each time
    # the player enters a character.  It classifies all words
    # looking for the match that provides the largest number of
    # possibilities. A directory called listoptions will store
    # the "match pattern" as the key, and the list of words that match
    # that pattern as the value.
    # Arguments:
    #  letter: character entered by the player
    #  currentlist: current list of words being processed (all words)
    #   of a specific length at the beginning. A new calculated list
    #  after each character entered
    #  wip: the word currently being built. Empty word of the type "---"
    #   at the beginning. As letters are matched, word is re-built
    dictoptions = {}
    # This for loop goes over all words in the current list and
    # classifies them according to the match pattern
    for word in currentlist:
        pattern = list(wip)
        # look_for_match will return a list with the indexes in which
        # letter is found in the word
        indexes = look_for_match(letter, word.upper())
        pattern = update_pattern_with_letter_match(letter, indexes, pattern)
        # convert the pattern stored on a list into a string to use as
        # key to the dictionary listoptions
        pattern_string = ''.join(pattern)
        if pattern_string in dictoptions:
                dictoptions[pattern_string].append(word)
        else:
            dictoptions[pattern_string] = [word]
    # In the unlikely scenario that there are no more new options
    # to create a new list of words, this function returns the
    # current word_in_process and the current list
    # But if there are more options to create new word lists, it returns
    # the list with the most words and the corresponding pattern to that list
    if len(dictoptions) == 0:
        return(currentlist, thelist)
    else:
        return max_list(dictoptions)


if __name__ == '__main__':
    print_greeting()
    print()
    play = True
    # Reads dictionary of words
    file_location = open("/usr/share/dict/words")
    file_content = file_location.read()
    words = file_content.split()
    file_location.close()
    # Checks to see what the longest word is so that a random length
    # can be selected without selecting a number larger than the
    # largest word
    max_word_length = 1
    for word in words:
        if len(word) > max_word_length:
            max_word_length = len(word)
    # Game Begins
    while play is True:
        random_length = randint(1, max_word_length)
    # Initializes global variables
        tries = 0
        success = False
        characters_read = []
        word_in_process = ['-']*random_length
    # Generates the initial word list made out of all words of the
    # word length generated
        word_list = [word for word in words if len(word) == random_length]
    # Tells the player how long the word is
        print("Your word has {} letters".format(random_length))
    # Game will ask for a letter giving the player 8 tries
        while success is not True and tries < 8:
            letter = get_letter(characters_read)
            evil_next_step = evil_new_list(letter, word_list, word_in_process)
            word_in_process = list(evil_next_step[0])
            word_list = list(evil_next_step[1])
            print_word_status(word_in_process, tries)
            if ''.join(word_in_process).count('-') == 0:
                print("wow! you won!!")
                success = True
            tries += 1
        if success is False:
            print("SORRY!!! Better luck next time")
        print("The word was {}".format(word_list[0]))
        if input("Do you want to play again? (Y/N) ").upper() == "Y":
            continue
        else:
            play = False
