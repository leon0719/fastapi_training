# unit test add function use pytest
def add(x, y):
    return x + y


def test_add():
    assert add(2, 3) == 5
    assert add('space', 'ship') == 'spaceship'


def test_add_fail():
    assert add(2, 3) == 6
