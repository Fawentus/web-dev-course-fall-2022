import pytest
from app.user import User
from app.router import register, add_fan_fiction, get_users, get_fan_fictions
from app.exceptions import AlreadyRegisteredError, UserNotFoundError

test_user = User(
    login="test",
    pswd="test",
    name="test",
)

wrong_user = User(
    id=1,
    login="wrong",
    pswd="wrong",
    name="wrong",
    fan_fictions_id=[]
)

right_user = User(
    id=0,
    login="test",
    pswd="test",
    name="test",
    fan_fictions_id=[],
)

right_user_whith_fan_fiction = User(
    id=0,
    login="test",
    pswd="test",
    name="test",
    fan_fictions_id=[0],
)


def test_registred():
    register(test_user)
    users = get_users()
    assert users == {0: right_user}

def test_add_fan_fiction():
    assert 0 == add_fan_fiction(right_user, "test")
    users = get_users()
    assert users == {0: right_user_whith_fan_fiction}
    assert (get_fan_fictions())[users[0].fan_fictions_id[0]] == "test"

def test_registred_err():
    with pytest.raises(AlreadyRegisteredError):
        register(test_user)
        users = get_users()
        assert users == {0: right_user}

def test_add_fan_fiction_err():
    with pytest.raises(UserNotFoundError):
        add_fan_fiction(wrong_user, "wrong")
        users = get_users()
        assert users == {0: right_user_whith_fan_fiction}
        assert (get_fan_fictions())[users[0].fan_fictions_id[0]] == "test"