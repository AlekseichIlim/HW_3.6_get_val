import pytest

from utils.dicts import get_val

coll = {'word1': 'dog', 'word2': 'cat'}

@pytest.fixture

def coll_fixture():
    return {'word1': 'dog', 'word2': 'cat'}
def test_1(coll_fixture):
    assert get_val(coll_fixture, 'word1') == 'dog'

def test_2(coll_fixture):
    assert get_val(coll_fixture, 'word2', 'fish') == 'cat'

def test_3(coll_fixture):
    assert get_val(coll_fixture, '', 'fish') == 'fish'
