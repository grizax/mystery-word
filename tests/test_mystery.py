'''Incomplete tests as I need more understanding on tests'''

import mystery_word as mw

def test_choose_word():
    word = mw.choose_word()
    assert word is not None

@pytest.fixture
def setup():
    secret_word = 'testing'
    mw.letters_guessed = []


def test_is_word_guessed(setup):
    assert mw.check_letter('t')
    assert not mw.check_letter('x')

'''def test_get_guessed_word(setup):
    assert

def test_get_available_letters(setup):
    assert 

@pytest.mark.parametrize("input,expected", [])
def test_mystery_word(setup):
    assert eval(input) == expected
    assert
'''
