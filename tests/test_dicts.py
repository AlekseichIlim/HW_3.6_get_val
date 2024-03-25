import pytest
from utils.dicts import get_val

coll = {'word1': 'dog', 'word2': 'cat'}
def test_1():
    assert get_val(coll, 'word1') == 'dog'

def test_2():
    assert get_val(coll, 'word2', 'fish') == 'cat'

def test_3():
    assert get_val(coll, '', 'fish') == 'fish'
