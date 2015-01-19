import mystery_word as myt
import evil_hangman as evil


def test_validate_level():
    assert (myt.validate_level("E") is True or
            myt.validate_level("N") is True or
            myt.validate_level("H") is True)
    assert myt.validate_level("U") is False


def test_select_random_word():
    word = myt.select_random_word("E")
    assert len(word) >= 4 and len(word) <= 6
    word = myt.select_random_word("N")
    assert len(word) >= 6 and len(word) <= 10
    word = myt.select_random_word("H")
    assert len(word) >= 10


def test_valid_letter():
    assert myt.valid_letter('A', ['A']) is False
    assert myt.valid_letter('A', ['B', 'C']) is True
    assert myt.valid_letter('ANA', ['B', 'C']) is False


def test_update_word():
    assert (myt.update_word('A', 'BANANA', ['-', '-', '-', '-', '-', '-'])
            == ['-', 'A', '-', 'A', '-', 'A'])
    assert (myt.update_word('A', 'ACTION', ['-', '-', '-', '-', '-', '-'])
            == ['A', '-', '-', '-', '-', '-'])
    assert (myt.update_word('N', 'BANANA', ['B', 'A', '-', 'A', '-', 'A'])
            == ['B', 'A', 'N', 'A', 'N', 'A'])


def test_evil():
    assert (evil.evil_new_list('E',
            ['ALLY', 'BETA', 'COOL', 'DEAL', 'ELSE', 'FLEW'] +
            ['GOOD', 'HOPE', 'IBEX'], ['-', '-', '-', '-'])
            == ('----', ['ALLY', 'COOL', 'GOOD']))
    assert (evil.evil_new_list('O', ['ALLY', 'COOL', 'GOOD'],
            ['-', '-', '-', '-'])
            == ('-OO-', ["COOL", "GOOD"]))


def test_look_for_match():
    assert(evil.look_for_match('A', 'ANAMARIA')) == [0, 2, 4, 7]
    assert(evil.look_for_match('A', '')) == []
    assert(evil.look_for_match('E', 'ANAMARIA')) == []


def test_update_pattern_with_letter_match():
    assert(evil.update_pattern_with_letter_match('A', [0, 2], ['-', '-', '-'])
           == ['A', '-', 'A'])
    assert(evil.update_pattern_with_letter_match('F', [1], ['A', '-', '-'])
           == ['A', 'F', '-'])


def test_max_list():
    assert(evil.max_list({'A--': ['ANA'], '-A-': ['CAN', 'PAN']})
           == ('-A-', ['CAN', 'PAN']))
