import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from models.model import User


def test_user_model():
    user = User(
        name='John',
        age=30,
        email='user@example.com',
        password='avc123456'
    )
    assert user.name
    assert user.age
    assert user.email
    assert user.password
