# unit test add function use pytest
def add(x, y):
    return x + y


def test_add():
    assert add(2, 3) == 5
    assert add('space', 'ship') == 'spaceship'
