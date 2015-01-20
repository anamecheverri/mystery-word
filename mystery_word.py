from random import randint


def print_greeting():
    print("------------------------------------------------------------")
    print("Welcome to Mystery Word - aka Hangman with three levels")
    print("Easy - (4-6 chars). Normal - (6-10 chars). Hard: >10 chars")
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


def select_random_word(level,words):
    if level == 'E':
        easy_words = [word for word in words
                      if len(word) >= 4 and len(word) <= 6]
        word = (easy_words[randint(0, len(easy_words)-1)])
    if level == 'N':
        normal_words = [word for word in words
                        if len(word) >= 6 and len(word) <= 10]
        word = (normal_words[randint(0, len(normal_words)-1)])
    if level == 'H':
        hard_words = [word for word in words if len(word) >= 10]
        word = (hard_words[randint(0, len(hard_words)-1)])
    return(word.upper())


def print_word_status(word, tries):
    print("-----------------------------------------------")
    print("Used Letters: {}".format(",".join(characters_read)))
    print("Your current word:", ''.join(word))
    print("-----------------------------------------------")
    print("You have {} guesses remaining".format(8 - tries))


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


def update_word(letter, word, wip):
    indexes = []
    counter = 0
    while counter < len(word):
        index_found = word.find(letter, counter)
        if index_found != -1:
            indexes.append(index_found)
            counter = index_found + 1
        else:
            counter += 1
    for index in indexes:
        if index != -1:
            wip[index] = letter
    return wip


if __name__ == '__main__':
    print_greeting()
    play = True
    file_location = open("/usr/share/dict/words")
    file_content = file_location.read()
    words = file_content.split()
    file_location.close()
    while play is True:
        tries = 0
        success = False
        characters_read = []
        word_in_process = []
        level = get_level()
        random_word = select_random_word(level,words)
        random_word_length = len(random_word)
        print("Your word has {} letters".format(random_word_length))
        word_in_process = ['-']*random_word_length
        while success is not True and tries < 8:
            print_word_status(word_in_process, tries)
            letter = get_letter(characters_read)
            if random_word.count(letter) > 0:
                word_in_process = update_word(letter,
                                              random_word,
                                              word_in_process)
                if ''.join(word_in_process) == random_word:
                    success = True
            else:
                tries += 1
        if success is True:
            print("CONGRATULATIONS. You win!")
        else:
            print("SORRY!!! Better luck next time")
        print("The word was {}".format(random_word))
        if input("Do you want to play again? (Y/N) ").upper() == "Y":
            continue
        else:
            play = False
