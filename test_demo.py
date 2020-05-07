import demo
import pytest

def test_basics():
    assert True 
    assert 2 != 1
    #assert 4 == 2
    assert 'g' in return_hello()

def return_hello():
    return 'hello'

def test_add():
    assert demo.add(1, 2) == 3

def test_add_more():
    for i in range(10):
        assert demo.add(1, i) == i + 2
    assert demo.add(1, 100) == 101

def test_error():
    with pytest.raises(demo.MysteryError):
        assert demo.add(99, 1) == 100

@pytest.mark.parametrize('a, b, expected', [
    (1,1,2), (2,1,3), (3,1,4), (4,2,5), (5,1,6), (6,1,7), (7,1,8), (8,1,9), (9,1,10)]
)

def test_with_param(a, b, expected):
    assert demo.add(a, b) == expected
